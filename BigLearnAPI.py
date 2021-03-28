import json
import requests
from Log import log


def big_learn_api():
    URL = "http://45.40.234.190:8080/API/Class/DXXJson/"
    log.update("(BigLearnAPI): GET {}".format(URL[-19:]))
    try:
        r = requests.get(URL)
        r.raise_for_status()
        log.update('(BigLearnAPI): GET {} <SUCCESS>'.format(URL[-19:]))
        infoDict = json.loads(r.text)
        # print(infoDict)
        return infoDict
    except:
        log.update("(BigLearnAPI): Data request failed <ERROR>")
        return False

# big_learn_api()