pipeline {
    agent { label 'docker-python' }

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

                // TODO: These should be baked into the base image - takes too long
                //       to do this on every Jenkins run
                echo 'Install pip...'
                sh 'apt-get -y install software-properties-common'
                sh 'apt-get update'
                sh 'apt-get -y install python-pip'
                sh 'pip install virtualenv'

                // run tests
                sh 'virtualenv .env'
                sh '. .env/bin/activate'
                sh 'pip install -r requirements.txt'
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
