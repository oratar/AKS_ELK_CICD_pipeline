pipeline {
  agent {
    kubernetes {
      yamlFile 'manifests/builder.yaml' 
    }
  }
   environment {
    MAJ = '3'
    DOCKERHUB = credentials('dockerhub_or')
    DOCKERHUB_REGISTERY = 'oratar333/catalog_shop'
    IMG_TAG = "python-$MAJ.${BUILD_NUMBER}"
    
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
          script {
            sh '''
                 echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin
                 docker image tag catalog:latest $DOCKERHUB_REGISTERY:$IMG_TAG
                 docker push $DOCKERHUB_REGISTERY:$IMG_TAG
               '''
          }
        }
      }
    }  
    stage('deploy') {
      steps {
        container('kubectl') {
         withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
           script {
             sh '''
               sed -i "s/<TAG>/${BUILD_NUMBER}/" ./manifests/deployment.yaml
               kubectl apply -f ./manifests/deployment.yaml
               kubectl apply -f ./manifests/service.yaml
               kubectl apply -f ./manifests/filebeat-kubernetes.yaml
                '''
         }
       }
      }
    }
  }
 }
}
