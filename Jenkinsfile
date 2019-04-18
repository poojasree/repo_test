pipeline{
 agent any
 stages{
 stage('Deploy Application to AKS') 
	           {
			   agent { docker {image 'ubuntu:latest'}}   
	             steps
	                  {
	                    sh 'python ./MultiComponentDeployment.yml'
	                  }             
	            }
	}}
