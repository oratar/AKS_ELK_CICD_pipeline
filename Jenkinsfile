podTemplate(yaml: '''
    apiVersion: v1
    kind: Pod
    spec:
      containers:
      - name: docker
        image: docker:dind 
        ''') {
    node('jenkins-slave') {
        stage('build docker image') {

        container('docker') {
                sh 'docker build -t catalog . '
        
       }
    }
  }
}
