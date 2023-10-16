from aws_cdk import (
    Stack,
    pipelines,
)
from constructs import Construct

from cdk.FastAPI_stack import FastAPIAppStage


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
                    repo_string="OliverAHolmes/python-aws-cdk-github-pipeline",
                ),
                commands=[
                    "cd cdk",
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "npx cdk synth",
                ],
                primary_output_directory="cdk/cdk.out",
            ),
            docker_enabled_for_synth=True,
            docker_enabled_for_self_mutation=True,
        )

        # Add a new stage to the pipeline
        app_stage = pipeline.add_stage(FastAPIAppStage(self, "FastAPIAppDev", stage_name="dev"))

        app_stage.add_post(
            pipelines.ManualApprovalStep("ManualApproval")
        )

        app_stage = pipeline.add_stage(FastAPIAppStage(self, "FastAPIAppTest", stage_name="test"))

        app_stage.add_post(
            pipelines.ManualApprovalStep("ManualApproval")
        )

        app_stage = pipeline.add_stage(FastAPIAppStage(self, "FastAPIAppProd", stage_name="prod"))
