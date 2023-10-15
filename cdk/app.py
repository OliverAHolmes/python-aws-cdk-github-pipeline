#!/usr/bin/env python3

import aws_cdk as cdk

from cdk.pipeline_stack import CodePipelineStack


app = cdk.App()
CodePipelineStack(app, "CDKPythonCodePipelineStack")

app.synth()
