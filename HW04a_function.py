import requests
import json

def no_of_commit_in_repository(ID, REPO, username, token ):
    response = requests.get('https://api.github.com/repos/'+ID+'/'+REPO+'/commits', auth=(username, token))
    repo = response.json()
    length = len(repo)
    output="Repo: "+REPO+" Number of commits: "+str(length)
    return output

