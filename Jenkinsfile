podTemplate (containers: [
   containerTemplate(name: 'docker', image: 'docker:latest', command: 'sleep', args: '99d')
]) {
    node('jenkins-slave') {
       environment {
            dockerhub = credentials('dockerhub_or')
        }
        stage('build docker image') {

        container('docker') {
            stage('Build') {
                sh 'docker build -t catalog . '
        }
       }
    }
  }
}
