pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'PYTHONPATH=src pytest'
            }
        }

        stage('Build Simulation') {
            steps {
                echo 'Build completed successfully.'
            }
        }

        stage('Deploy Simulation') {
            steps {
                echo 'Simulating deployment of traffic analyzer application...'
            }
        }
    }
}
