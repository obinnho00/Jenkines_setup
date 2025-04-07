pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p test-reports
                    python3 -m xmlrunner discover -s . -p "test_*.py" -o test-reports
                    ls -l test-reports
                '''
            }
        }
    }

    post {
        always {
            echo '✅ Build finished.'
            junit 'test-reports/*.xml'
        }
    }
}
