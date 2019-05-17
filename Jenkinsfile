pipeline {
    agent {
        docker { label 'docker-python' }
    }

    stages {
        stage('Build Information') {
            steps {
                echo 'Printing build information...'
                echo "Build ID: ${BUILD_ID}"
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'python -m pytest tests/'
            }
        }

        stage('Run Tests') {
            steps {
              echo 'Aggregating test result information...'
            }
        }
    }
}
