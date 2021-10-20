from storages.backends.s3boto3 import S3Boto3Storage  # noqa E402
from django.conf import settings

AWS_S3_REGION_NAME = settings.AWS_S3_REGION_NAME
AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME


class StaticRootS3Boto3Storage(S3Boto3Storage):
    default_acl = "public-read"
    custom_domain = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    location = "static/"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    file_overwrite = False
    default_acl = "public-read"
    custom_domain = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
