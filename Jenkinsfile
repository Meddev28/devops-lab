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
                bat 'docker build -t webapp:latest .'
            }
        }
        
        stage('Deploy Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}