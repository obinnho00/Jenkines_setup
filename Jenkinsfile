pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/obinnho00/Jenkines_setup.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r Jenkines_Practice/requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    mkdir -p test-reports
                    python -m xmlrunner discover -s Jenkines_Practice -o test-reports
                '''
            }
        }
    }

    post {
        always {
            echo 'Build Finished.'
            junit 'test-reports/*.xml'
        }
    }
}
