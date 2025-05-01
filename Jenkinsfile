pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'arumi21/airline-system'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    try {
                        sh 'pip install -r requirements.txt'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Run Application Code') {
            steps {
                // Run your main Python app
                sh 'python legacy_airline_system_refactored.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p test-reports
                    python -m xmlrunner discover -s . -p "test_*.py" -o test-reports
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub-creds', url: '') {
                        sh "docker push $DOCKER_IMAGE"
                    }
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
