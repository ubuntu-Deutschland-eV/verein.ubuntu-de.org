#!/usr/bin/env groovy

pipeline {
    agent {
        label 'master'
    }

    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                checkout scm
            }
        }
        stage('Build page') {
            steps {
                sh '''
                make install
                make publish
                '''
            }
        }
        stage ('pseudo deploy') {
            when {
                branch "master"
            }
            steps {
                sh 'rsync -av output/ /srv/local/verein --delete'
            }
        }
    }
}
