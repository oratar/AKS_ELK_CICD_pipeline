pipeline {
  agent {
    kubernetes {
      yamlFile 'builder.yaml' 
    }
  }
   environment {
    dockerhub = credentials('dockerhub_or')
  }
  stages {
    stage('build') {
      steps {
           container('dind-daemon') {
                sh ' docker build -t catalog ./src/'

        }
      } 
    }
    stage('test') {
      steps {
         container('dind-daemon') {
                sh 'docker run -d -p 5000:5000 --name catalog-container catalog && docker exec catalog-container bash -c "python3 tests.py"'
         }
      }
  }
    stage('upload') {
      steps {
        container('dind-daemon') {
                sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
                sh 'docker image tag catalog:latest oratar333/catalog_shop:${BUILD_NUMBER}'
                sh 'docker push oratar333/catalog_shop:${BUILD_NUMBER}'
        }
      }
    }  
    stage('deploy') {
      steps {
       container('kubectl') {
         withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
           sh 'sed -i "s/<TAG>/${BUILD_NUMBER}/" ./manifests/deployment.yaml'
           sh 'kubectl apply -f ./manifests/deployment.yaml'
           sh 'kubectl apply -f ./manifests/service.yaml'
           sh 'kubectl apply -f ./manifests/filebeat-kubernetes.yaml'
         }
       }
      }
    }
}
}
