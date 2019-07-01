# aws_connect
Application for AWS Connect


# Pre-requisite
1. AWS Account 
2. AWS Connect - Phone number claimed and setup for use
3. Contact Flow created to accept Dynamic attribute
4. Use `aws configure` to setup the AWS credentials for the account having access to AWS Connect

# Run
1. To run the application, replace the parameters with your Connect details 
    DestinationPhoneNumber='xxxxxxxx'  # Number to be called
    ContactFlowId='xxxxxxx' # Contact flow ID to be used when the outbound call is being made
    InstanceId='xxxxx' # Instance ID of the Connect to be used for placing the call
    SourcePhoneNumber='+61xxxxxxxx' # AWS Connect phone number to be used for placing the call
2. Run the program as 
`python3 placecall.py`

This should place a call now to the number specified.
