import boto3
#from botocore.client import Config
import StringIO
import zipfile
import mimetypes

s3 = boto3.resource('s3') #, config=Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket('mehdi-portfolio')
build_bucket = s3.Bucket('mehdi-portfolio-build')

zip = StringIO.StringIO()
#build_bucket.download_fileobj('portfoliobuild.zip' , zip)
build_bucket.download_fileobj('portfoliobuild.zip' , zip)

with zipfile.ZipFile(zip) as myzip:
    for nm in myzip.namelist():
       obj = myzip.open(nm)
       print nm
       portfolio_bucket.upload_fileobj(obj, nm,
       ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
       portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
