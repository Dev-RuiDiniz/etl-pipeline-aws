#!/usr/bin/env python3
from aws_cdk import App
from etl_stack import EtlStack

app = App()
EtlStack(app, "EtlPipelineStack")
app.synth()
