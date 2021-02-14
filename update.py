import json
import boto3


client = boto3.client('s3')

# this is the policy template which is applied to all new buckets created by this script
dict_policy = client.get_bucket_policy(Bucket = 'ZZZZZZZZZZZZZZ') 
print(dict_policy)

json_str = json.dumps(dict_policy)
resp = json.loads(json_str)
resp = resp["Policy"]
resp = json.loads(resp)

json_formatted_str = json.dumps(resp, indent=2)
print(json_formatted_str)
print(resp["Statement"][0]['Resource'])
resource = resp["Statement"][0]['Resource']
new_resource = 'arn:aws:s3:::' + 'XXXXXXXXXXXXXX'

str_policy = json.loads(json.dumps(json_str).replace(resource, new_resource))
str_policy = json.loads(str_policy)

print(str_policy)
str_policy = str_policy["Policy"]
str_policy = str_policy.replace('"Policy": ','')
print(str_policy)

response = client.put_bucket_policy(Bucket = 'XXXXXXXXXXXXXX', Policy = str_policy)
print(response)

