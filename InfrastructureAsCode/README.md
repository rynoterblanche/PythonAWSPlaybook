# Infrastructure as code with AWS CDK

## CDK Installation 
```
# Configure credentials with access key (created on AWS Console)
aws configure

# Install AWS CDK
npm install aws-cdk -g
```

## CDK Sample App
```
mkdir SampleCDKApp
cd SampleCDKApp
cdk init sample-app --language python
cdk bootstrap
cdk synth
cdk deploy
```

## Common CDK Commands
```
# Check CDK version
cdk version

# Create a new CDK project (app)
cdk init TEMPLATE --language LANGUAGE

# Bootstrap the AWS environment
cdk bootstrap

# List the stacks in the CDK app
cdk list

# Deploy a CDK stack
cdk deploy

# Delete the stack
cdk destroy

# Launch CDK docs
cdk docs

# Compare local and deployed stack
cdk diff

# Generate CloudFormation templates
cdk synth

# Specifying AWS profiles
cdk deploy --profile PROFILE_NAME

# Specify a specific stack for an action
cdk deploy STACK_NAME

# Specify multiple stacks for an action
cdk deploy STACK_NAME_1 STACK_NAME_2

# Specify an action against all stacks in the app
cdk deploy "*"

# Check your app for problems
cdk doctor
```
