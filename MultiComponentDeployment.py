import json
import requests
import time

def deployMultiRelease():
        with open("release.json", "r") as f:
                manifestobj = json.load(f)
        for microservice_details in manifestobj["release"]["artifacts"]["microservices"]:
                        print(microservice_details["name"])
                        deploy(microservice_details["name"])


def deploy(name):
        # requests.post('http://168.62.62.128:8080/job/'+name+'/build')
        requests.post('http://devops:11551700c23df7a3119430044a9048dc9f@168.62.62.128:8080/job/'+name+'/build')
        #curl -X POST http://devops:devops12345@168.62.62.128:8080/job/'+name+'/build
        time.sleep(60)

deployMultiRelease()
