pipeline {
  agent { label 'linux' }

  environment {
    PATH="/var/jenkins_home/miniconda3/bin:$PATH"
  }

  stages {
      stage('build') {
        steps {
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/obviousrebel/python-jenkins-xml.git']]])
          sh 'conda info'
          sh 'conda install -c bioconda junit-xml'
          sh "python pyxml.py"
        }
      }
      stage('test') {
        steps {
          junit 'convert_test_report.xml'
          junit 'check_test_report.xml'
        }
      }
      stage('archive') {
        steps {
          archiveArtifacts artifacts: '*.xml', onlyIfSuccessful: false, allowEmptyArchive: true
          cleanWs()
        }
      }
  }
}
