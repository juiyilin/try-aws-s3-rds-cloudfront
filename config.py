from dotenv import load_dotenv
import os

load_dotenv()


#rds
rds_host=os.environ.get('RDS_host')
rds_user=os.environ.get('RDS_user')
rds_password=os.environ.get('RDS_password')


#aws s3
bucket_name=os.environ.get('BUCKET_NAME')
AWSAccessKeyId=os.environ.get('AWSAccessKeyId')
AWSSecretKey=os.environ.get('AWSSecretKey')
cdn_domain=os.environ.get('cdn_domain')