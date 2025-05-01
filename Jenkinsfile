pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'arumi21/airline-system'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Application Code') {
            steps {
                sh 'python3 legacy_airline_system_refactored.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p test-reports
                    python3 -m xmlrunner discover -s . -p "test_*.py" -o test-reports
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub-creds', url: '') {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
            junit 'test-reports/*.xml'
        }
    }
}
