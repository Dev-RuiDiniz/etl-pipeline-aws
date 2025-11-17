from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
)
from constructs import Construct

class EtlStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        fn = _lambda.Function(
            self, "EtlLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="src.main.run_pipeline",
            timeout=Duration.minutes(15),
            memory_size=512,
            code=_lambda.Code.from_asset("../../"),
        )

        fn.add_to_role_policy(iam.PolicyStatement(
            actions=["s3:PutObject"],
            resources=["*"]
        ))

        rule = events.Rule(
            self, "DailyTrigger",
            schedule=events.Schedule.cron(minute="0", hour="2")
        )
        rule.add_target(targets.LambdaFunction(fn))
