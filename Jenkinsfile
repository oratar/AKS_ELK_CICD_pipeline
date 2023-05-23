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
''' 
    }
  }
  stages {
    stage('idk'){
   container('dind-daemon') {
    stage('build') {
      steps {
                sh ' docker build -t catalog ./src/'
        }
    }
    stage('test') {
                sh 'docker run -p 5000:5000 catalog' 
      } 
   }}
  }
}

