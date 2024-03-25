import argparse


def get_cmd_args():

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument(
        "-r",
        "--region",
        required=False,
        choices=["us-east-1", "eu-central-1", "ap-southeast-2"],
        default="us-east-1",
        help="AWS Region (us-east-1 | eu-central-1 | ap-southeast-2)",
        type=str.lower,
    )

    PARSER.add_argument(
        "-p",
        "--profile",
        required=False,
        default="default",
        help="AWS Profile (default | cch-prd | cch-int)",
        type=str,
    )

    args = PARSER.parse_args()
    aws_region = args.region
    aws_profile = args.profile

    return aws_profile, aws_region


if __name__ == "__main__":
    pass
