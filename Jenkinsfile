pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'arumi21/airline-system'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                // Install required dependencies from requirements.txt
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
                // Run the application code (your assignment system)
                sh 'python legacy_airline_system_refactored.py'  // This will run the assignment code
            }
        }

        stage('Run Tests') {
            steps {
                // Ensure the directory for test reports exists
                sh 'mkdir -p test-reports'

                // Run tests using xmlrunner and generate the XML reports
                sh '''
                    python3 -m xmlrunner discover -s . -p "test_*.py" -o test-reports
                    ls -l test-reports  // List the reports for debugging purposes
                '''
            }
        }
    }

    post {
        always {
            // Always echo a message when the build finishes
            echo 'Build finished.'
            
            // Publish the test reports as JUnit results to Jenkins
            junit '**/test-reports/*.xml'
        }
    }
}
