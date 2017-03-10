#!/usr/bin/env groovy

node("master") {
    stage("Checkout") {
      deleteDir()
      checkout scm
    }
    
    stage("Build page") {
      sh '''
      make install
      make publish
      rsync -av output/ /srv/local/verein --delete
      '''
    }
}
