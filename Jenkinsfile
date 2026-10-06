pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting CI pipeline'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing application dependencies'
                sh '''
                    cd app
                    python3 -m pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
                sh '''
                    cd app
                    pytest
                '''
            }
        }

        stage('Docker') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t minhaaj1/devops-app:latest ./app'
            }
        }
    }
}
