pipeline{
 agent any
 stages{
 stage('Deploy Application to AKS') 
	           {
			   agent { docker {image 'ubuntu'}}    
	             steps
	                  {
	                    sh 'python ./MultiComponentDeployment.yml'
	                  }             
	            }
	}}
