pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r Jenkins_Practice/requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p Jenkins_Practice/test-reports
                    python -m xmlrunner discover -s Jenkins_Practice -p "test_*.py" -o Jenkins_Practice/test-reports
                    ls -l Jenkins_Practice/test-reports
                '''
            }
        }
    }

    post {
        always {
            echo '✅ Build finished.'
            junit 'Jenkins_Practice/test-reports/*.xml'
        }
    }
}
