from aws_cdk import (
    Stack,
    pipelines,

)
from constructs import Construct


class CodePipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection(
                    connection_arn="arn:aws:codestar-connections:ap-southeast-2:208792096778:connection/e712612a-93a5-4260-a350-cd3215f19475",
                    branch="main",
                    repo_string="OliverAHolmes/python-aws-cdk-github-pipeline"
				),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "cd cdk",
                    "npx cdk synth",
                ]
            ),
        )
