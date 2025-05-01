pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'arumi21/airline-system'
        DOCKER_USER = 'ARUMI21'
        DOCKER_PASS = 'iA!906200'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Application Code') {
            steps {
                sh 'python3 legacy_airline_system_refactored.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $DOCKER_IMAGE
                '''
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
    }
}
