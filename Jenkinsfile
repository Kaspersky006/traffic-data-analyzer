pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    environment {
        PYTHONPATH = 'src'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Simulation') {
            steps {
                echo 'Build simulated: no package is built yet.'
            }
        }

        stage('Deploy Simulation') {
            steps {
                echo 'Deploy simulated: no server to deploy to yet.'
            }
        }
    }
}
