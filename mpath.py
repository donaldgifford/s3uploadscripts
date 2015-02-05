#!/usr/bin/python

import math, os
import boto
from filechunkio import FileChunkIO
from boto.s3.connection import S3Connection


conn = S3Connection('id', 'key')
bucket = conn.get_bucket('bucket')

source_path = '/path/to/file'
source_size = os.stat(source_path).st_size

mp = bucket.initiate_multipart_upload(os.path.basename(source_path))

chunk_size = 52438800
chunk_count = int(math.ceil(source_size / chunk_size))

for i in range(chunk_count +1):
	offset = chunk_size * i 
	bytes = min(chunk_size, source_size - offset)
	with FileChunkIO(source_path, 'r', offset=offset, bytes=bytes) as fp:
		mp.upload_part_from_file(fp, part_num=i +1)

mp.complete_upload()
