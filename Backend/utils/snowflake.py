from toollib.guid import SnowFlake
from django.conf import settings

snowflake = SnowFlake(worker_id=settings.SNOWFLAKE.get('WORKER_ID'), datacenter_id=settings.SNOWFLAKE.get('DATACENTER_ID'))

def generate_uid():
    return snowflake.gen_uid()
