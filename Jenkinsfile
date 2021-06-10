pipeline{
    agent any
    stages{
        stage("Test") {
            steps {
            // pytest 
            // run for each service
            // produce cov reports
            sh "bash jenkins/test.sh"   
        }   
    }
           
        stage("Build") {
            steps{
                script{
                    if (env.rollback == 'false'){
                        sh "docker-compose build --parallel --build-arg APP_VERSION=${app_version} && docker-compose push"
                        sh "docker system prune -af"
                        sh "bash jenkins/build_images.sh"
                    }    
                }
            }
        }
        stage("Config Management (Ansible)"){
            steps{
                // write out playbook, inventory
                // with roles
                // ssh keys generated from jenkins machine for jenkins user (ssh-keygen)
                // sudo su - jenkins, install ansible on this machine for jenkins
                // jenkins runs playbook
                sh "cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml"
            }
        }
        stage("Deploy"){
            steps{
                // copy docker-compose.yaml over ssh (scp command)
                // set env variables on swarm manager
                // ssh into swarm manager to deploy the stack
                sh "bash jenkins/deploy.sh"

            }
        }
    }
    post {
        always {
            junit '**/junit.xml'
            cobertura coberturaReportFile: '**/coverage.xml', failNoReports: false, failUnstable: false, onlyStable: false
        }    
    }
}