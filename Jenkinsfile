pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Starting CI pipeline'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
                sh 'pytest'
            }
        }

        stage('Docker') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t minhaaj1/devops-app:latest .'
            }
        }
    }
}
