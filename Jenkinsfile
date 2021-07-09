pipeline {
  agent any

  stages {
    stage('Install sam-cli') {
      steps {
        sh 'python3 -m venv venv && venv/bin/pip install aws-sam-cli'
        stash includes: '**/venv/**/*', name: 'venv'
      }
    }
    stage('Build') {
      steps {
        withAWS(credentials: 'sam-jenkins-demo-credentials', region: 'eu-central-1'){
        unstash 'venv'
        sh 'ls'
        sh 'venv/bin/sam package -t template.yml --s3-bucket bohdan-solianyk-app --output-template-file ./cft.yml'
        //stash includes: '**/.aws-sam/**/*', name: 'aws-sam'
        }
      }
    }
    stage('beta') {
      environment {
        STACK_NAME = 'JenkinsTest'
        S3_BUCKET = 'bohdan-solianyk-app'
      }
      steps {
        withAWS(credentials: 'sam-jenkins-demo-credentials', region: 'eu-central-1') {
          unstash 'venv'
          //unstash 'aws-sam'
          sh 'venv/bin/sam deploy --template-file cft.yml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM'
        }
      }
    }
  }
}