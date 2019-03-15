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
        requests.get('http://168.62.52.51:8080/job/'+name+'/build')
        time.sleep(60)

deployMultiRelease()
