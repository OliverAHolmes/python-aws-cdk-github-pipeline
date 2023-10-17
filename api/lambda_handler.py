from mangum import Mangum
from main import app

print("Lambda handler initialized")


def lambda_handler(
    event, context
):  # make sure the function name matches what you've specified in the Lambda settings
    print("Lambda handler called")
    mangum_handler = Mangum(app, lifespan="off")
    return mangum_handler(event, context)
