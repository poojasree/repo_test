pipeline{
 agent any
 stages{
 stage('Deploy Application to AKS') 
	           {
	             agent any    
	             steps
	                  {
	                    sh 'python ./MultiComponentDeployment.yml'
	                  }             
	            }
	}}
