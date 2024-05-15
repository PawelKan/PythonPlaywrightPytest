//Created with chatgpt for training
pipeline {
    agent any

    environment {
        // Definiowanie zmiennej środowiskowej dla wirtualnego środowiska
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Debug') {
    steps {
        bat 'echo %PATH%'
        bat 'dir'
        bat 'where python'
    }
}
        stage('Checkout') {
            steps {
                // Pobranie kodu źródłowego z repozytorium
                git 'https://github.com/PawelKan/PythonPlaywrightPytest'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Utworzenie wirtualnego środowiska
                    bat 'python -m venv %PYTHON_ENV%'
                    // Aktywacja wirtualnego środowiska i instalacja zależności
                    bat """
                    call %PYTHON_ENV%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Playwright Install') {
            steps {
                script {
                    // Instalacja przeglądarek Playwright
                    bat """
                    call %PYTHON_ENV%\\Scripts\\activate
                    playwright install
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Aktywacja wirtualnego środowiska i uruchomienie testów
                    bat """
                    call %PYTHON_ENV%\\Scripts\\activate
                    pytest --disable-warnings
                    """
                }
            }
        }
    }
}
