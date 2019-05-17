pipeline {
    agent {
        docker { label 'docker-python' }
    }

    stages {
        stage('Build Information') {
            echo 'Printing build information...'
            echo "Build ID: ${BUILD_ID}"
        }

        stage('Run Tests') {
            echo 'Running tests...'
        }

        stage('Run Tests') {
            echo 'Aggregating test result information...'
        }
    }
}
