pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo "${WORKSPACE}"
                sh 'php -v'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
                echo 'Deploying....'
            }
        }
    }
}
