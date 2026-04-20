pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                checkout scm: [$class: 'GitSCM', 
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/Meddev28/devops-lab']],
                    extensions: [[$class: 'CleanCheckout']]
                ]
            }
        }
        
        stage('Build Docker') {
            steps {
                sh 'docker build -t webapp:latest .'
            }
        }
        
        stage('Deploy Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}