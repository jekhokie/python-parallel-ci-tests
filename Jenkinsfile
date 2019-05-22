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
                stage('Suite 1') {
                    agent { label 'docker-python' }

                    stages {
                        stage('Initialize Database...') {
                            steps {
                                currentBuild.result = 'FAILURE'
                                return
                            }
                        }
                        stage("Set up directory...") {
                            steps {
                                echo 'Running tests for Test Suite 1...'
                                echo 'Running tests on:'
                                sh 'hostname -f'
                                sh 'virtualenv .env'
                                sh '. .env/bin/activate'
                                sh 'pip install -r requirements.txt'
                                sh 'mkdir build'
                            }
                        }
                        stage('Run Tests'...) {
                            steps {
                                sh 'python -m pytest --junitxml build/suite-results-1.xml tests/test_app_job_id1.py'
                            }
                            post {
                                always {
                                    stash includes: 'build/**', name: 'test-suite-1'
                                }
                            }
                        }
                    }
                }

/*
                stage('Suite 2') {
                    agent { label 'docker-python' }

                    stages {
                        stage("Set up directory...") {
                            steps {
                                echo 'Running tests for Test Suite 2...'
                                echo 'Running tests on:'
                                sh 'hostname -f'
                                sh 'virtualenv .env'
                                sh '. .env/bin/activate'
                                sh 'pip install -r requirements.txt'
                                sh 'mkdir build'
                            }
                        }
                        stage('Run Tests...') {
                            steps {
                                sh 'python -m pytest --junitxml build/suite-results-2.xml tests/test_app_job_id2.py'
                            }
                            post {
                                always {
                                    stash includes: 'build/**', name: 'test-suite-2'
                                }
                            }
                        }
                    }
                }

                stage('Suite 3') {
                    agent { label 'docker-python' }

                    stages {
                        stage("Set up directory...") {
                            steps {
                                echo 'Running tests for Test Suite 3...'
                                echo 'Running tests on:'
                                sh 'hostname -f'
                                sh 'virtualenv .env'
                                sh '. .env/bin/activate'
                                sh 'pip install -r requirements.txt'
                                sh 'mkdir build'
                            }
                        }
                        stage('Run Tests...') {
                            steps {
                                sh 'python -m pytest --junitxml build/suite-results-3.xml tests/test_app_no_jobid.py'
                            }
                            post {
                                always {
                                    stash includes: 'build/**', name: 'test-suite-3'
                                }
                            }
                        }
                    }
                }
*/
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
