pipeline {
  agent {
    kubernetes {
      yaml '''
apiVersion: v1
kind: Pod
metadata:
  name: dind
spec:
  containers:
    - name: kubectl
      image: bitnami/kubectl:latest
      volumeMounts:
        - name: kubeconfig
          mountPath: /.kube/config
      command: [""]
    - name: docker-cmds
      image: docker:latest
      env:
        - name: DOCKER_HOST
          value: tcp://localhost:2375
    - name: dind-daemon
      image: docker:dind
      securityContext:
        privileged: true
      volumeMounts:
        - name: docker-graph-storage
          mountPath: /var/lib/docker
  volumes:
    - name: docker-graph-storage
      emptyDir: {}
    - name: kubeconfig
      mountPath: $kubeconfig

''' 
    }
  }
   environment {
    dockerhub = credentials('dockerhub_or')
    kubeconfig = credentials('kubeconfig')
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
    stage('deploy') {
      steps {
       container('kubectl') {
         sh 'kubectl'
       }
      }
    }
}
}
