pipeline {
    agent {
        docker { image 'node:16.13.1-alpine' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'node --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}