#!/usr/bin/env python3

import aws_cdk as cdk

from sample_cdk_app.sample_cdk_app_stack import SampleCdkAppStack


app = cdk.App()
SampleCdkAppStack(app, "sample-cdk-app")

app.synth()
