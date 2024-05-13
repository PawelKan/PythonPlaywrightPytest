pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                //get data from repository
                git 'https://github.com/PawelKan/PythonPlaywrightPytest'
            }
        }
        stage('Install dependencies') {
            steps {
                // install dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // run tests (simple run)
                sh 'pytest'
            }
        }
    }
}