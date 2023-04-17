pipeline {
    agent { label 'or_agent' }

    stages {
        stage('Build') {
            steps {
                sh 'sudo docker build . -t catalog'
                sh 'docker run -p 5000:5000 --name catalog catalog
            }
        }
        stage('Test') {
            steps {
                sh 'sudo docker exec -it python3 tests.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
