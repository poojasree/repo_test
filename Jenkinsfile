pipeline{
 agent any
 stages{
 stage('Deploy Application to AKS') 
	           {
			   agent { docker {image 'python:latest'}}   
	             steps
	                  {
	                    sh 'python ./MultiComponentDeployment.py'
	                  }             
	            }
	}}
