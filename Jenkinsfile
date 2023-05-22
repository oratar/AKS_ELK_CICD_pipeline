podTemplate (containers: [
   containerTemplate(name: 'docker', image: 'docker:dind')
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
