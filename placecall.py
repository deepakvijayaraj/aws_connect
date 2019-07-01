import boto3

client = boto3.client('connect')

response = client.start_outbound_voice_contact(
    DestinationPhoneNumber='+61xxxxxxxxx',
    ContactFlowId='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    InstanceId='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    SourcePhoneNumber='+61yyyyyyyyy',
    Attributes={
        'message': 'Company Name here'
    }
)
