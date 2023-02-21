pipeline {
    agent {
        docker { image 'php:8.1.16-apache' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
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
                echo 'Deploying....'
            }
        }
    }
}
