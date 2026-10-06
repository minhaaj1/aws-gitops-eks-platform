pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python3 -m pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t minhaaj1/devops-app:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Docker Login & Push') {
            steps {
                echo 'Pushing Docker image...'
                sh '''
                    docker push minhaaj1/devops-app:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo '======================================'
            echo 'PIPELINE COMPLETED SUCCESSFULLY!'
            echo '======================================'
        }

        failure {
            echo '======================================'
            echo 'PIPELINE FAILED!'
            echo 'Check the console output.'
            echo '======================================'
        }
    }
}
