pipeline {
    agent { label 'or_agent'
    }
    environment {
        dockerhub = credentials('dockerhub_or')
    }
    stages {
        stage('Build') {
            steps {
                sh 'sudo docker build . -t catalog'
                sh 'sudo docker run -p 5000:5000 --name catalog catalog &'
            }
        }
        stage('Test') {
            steps {
                sh 'sudo docker exec catalog bash -c "python3 tests.py"'
            }
        }
        stage('upload') {
            steps {
                sh 'echo $dockerhub_PSW | sudo docker login -u $dockerhub_USR --password-stdin'
                sh 'sudo docker image tag catalog:latest oratar333/catalog_shop:${BUILD_NUMBER}'
                sh 'sudo docker push oratar333/catalog_shop:${BUILD_NUMBER}'
            }
        }
       stage('deploy') {
           steps {
               sh 'kubectl apply -f deployment.yaml'
               
           }
       }
       
    }
        post {
	    always {
        sh 'sudo docker rm -f $(sudo docker ps -a -q)'
        sh 'sudo docker rmi -f $(sudo docker images -q )'
        

    }
  }
}
