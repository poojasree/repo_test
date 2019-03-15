stage('Deploy Application to AKS') 
	           {
	              agent any    
	             steps
	                  {
	                    withCredentials([azureServicePrincipal('azurelogin')])
	                       {
	                         sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID'
	                         sh 'az aks get-credentials --resource-group $resourcegroup --name $aksname'
	                         sh 'kubectl apply -f apache_deployment.yml'
	                         echo 'Waiting for external IP to be genarated'
	                         sleep 120 // seconds
	                         sh 'kubectl get svc'
	                        }
	                  }             
	            }
