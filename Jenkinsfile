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
            parallel {
                stage('Test Suite 1') {
                    agent { label 'docker-python' }

                    stages {
                        stage("Set up directory...") {
                            steps {
                                echo 'Running tests for Test Suite 1...'
                                echo 'Running tests on:'
                                sh 'hostname -f'
                                sh 'virtualenv .env'
                                sh '. .env/bin/activate'
                                sh 'pip install -r requirements.txt'
                            }
                        }
                        stage('Run Tests') {
                            steps {
                                sh 'python -m pytest tests/test_app_job_id1.py'
                            }
                            post {
                                always {
                                    stash includes: '**', name: 'test-suite-1'
                                }
                            }
                        }
                    }
                }
                //sh 'python -m pytest tests/test_app_job_id2.py'
                //sh 'python -m pytest tests/test_app_no_jobid.py'
            }
        }

        stage('Aggregate Results') {
            steps {
              echo 'Aggregating test result information...'
              unstash 'test-suite-1'
              unstash 'test-suite-2'
              unstash 'test-suite-3'
            }
            post {
                always {
                    junit 'build/*.xml'
                }
            }
        }
    }
}
