from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam
)
from constructs import Construct

class EtlStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        fn = _lambda.Function(
            self, "EtlLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="src.main.run_pipeline",
            code=_lambda.Code.from_asset("."),
            timeout=core.Duration.minutes(15),
            memory_size=512,
        )

        # Policy to write to S3 (replace bucket arn as needed)
        fn.add_to_role_policy(iam.PolicyStatement(
            actions=["s3:PutObject", "s3:PutObjectAcl"],
            resources=["arn:aws:s3:::your-bucket-name/*"]
        ))

        rule = events.Rule(self, "ScheduleRule",
            schedule=events.Schedule.cron(minute="0", hour="2")  # daily @02:00 UTC
        )
        rule.add_target(targets.LambdaFunction(fn))
