podTemplate(yaml: '''
    apiVersion: v1
    kind: Pod
    spec:
      containers:
      - name: docker
        image: docker:latest
''') {
    node('jenkins-slave') {
        environment {
            dockerhub = credentials('dockerhub_or')
        }
            stage('Build') {
                    container('docker') {
                        sh 'sudo docker build . -t catalog'
                        sh 'sudo docker run -p 5000:5000 --name catalog catalog &'
                    
                
            }
        }
    }
}
