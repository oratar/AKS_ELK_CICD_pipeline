podTemplate(yaml: '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: jnlp
            image: docker:latest
            command:
            - cat
            tty: true
            volumeMounts:
             - mountPath: /var/run/docker.sock
               name: docker-sock
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock    
''') {  

node('jenkins-slave') {
        stage('build docker image') {
           container('jnlp') {
                sh 'docker build -t catalog . '
        
           }
        }
  }
}
