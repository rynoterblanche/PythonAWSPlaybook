# Infrastructure as code with AWS CDK

## Requirements
- AWS CLI
- node.js
- npm

## Install the CDK
```
# Configure credentials with your access key (created on AWS Console)
aws configure

# Install AWS CDK
npm install aws-cdk -g
```

## Launch a CDK Sample App
```
# Create sample project folder 
mkdir sample_app
cd sample_app

# Create project
cdk init sample-app --language python

# Create needed AWS resources for CDK environment
cdk bootstrap

# Generate CloudFormation templates from code
cdk synth

# Launch templates with CloudFormation
cdk deploy
```

## Python CDK Samples
[aws-samples / aws-cdk-examples](https://github.com/aws-samples/aws-cdk-examples/tree/master/python)

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
