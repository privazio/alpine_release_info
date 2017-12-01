pipeline {
  agent {
    docker {
      image 'centos:7'
    }
    
  }
  stages {
    stage('Test') {
      steps {
        sh 'uname -a'
      }
    }
  }
}