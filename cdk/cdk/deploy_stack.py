from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_cdk as cdk,

)
from constructs import Construct


class PipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the Lambda function
        api_lambda = _lambda.Function(self, 'ApiLambda',
            code=_lambda.Code.from_asset('../api', bundling={
                # pylint: disable=no-member
                'image': _lambda.Runtime.PYTHON_3_11.bundling_image,
                'command': [
                    'bash',
                    '-c',
                    'pip install -r requirements.txt -t /asset-output && cp -au . /asset-output'
                ],
            }),
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler='lambda_handler.lambda_handler',
            timeout=Duration.seconds(15)
        )

        # Create the API Gateway
        api = apigateway.LambdaRestApi(self, 'ApiGateway',
            handler=api_lambda,
            deploy_options={
                "stage_name": "prod"
            }
        )

        # Export the URL of the API Gateway endpoint
        cdk.CfnOutput(self, 'ApiGatewayUrl', value=api.url)