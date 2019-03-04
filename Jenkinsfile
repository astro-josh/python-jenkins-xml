pipeline {
  agent { label 'linux' }

  environment {

  }

  stages {
      stage('build') {
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/obviousrebel/python-jenkins-xml.git']]])
          sh "python pyxml.py"
      }
      stage('test') {
          junit 'test-report.xml'
      }
  }
}
