pipeline {
    agent {
        docker {
            image 'jenkins/ssh-slave'
            label 'docker-python'
        }
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

        stage('Aggregate Results') {
            steps {
              echo 'Aggregating test result information...'
            }
        }
    }
}
