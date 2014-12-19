import math, os
import boto
from filechunkio import FileChunkIO
from boto.s3.connection import S3Connection


conn = S3Connection('id', 'key')
bucket = conn.get_bucket('bucket')

source_path = '/path/to/file'

mp = bucket.initiate_multipart_upload(os.path.basename(source_path))

mp.cancel_upload()
