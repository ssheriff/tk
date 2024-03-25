import boto3
import botocore
import sys

boto_session = boto3.Session(region_name="us-east-1")


def get_session(profile, region):
    try:
        this_session = boto3.Session(profile_name=profile, region_name=region)
    except:
        print("Error creating boto3 Session.")
        raise
    else:
        return this_session


def get_client(session, client_type: str):
    try:
        this_client = session.client(client_type)
    except:
        print("Error creating boto3 client")
        raise
    else:
        return this_client
