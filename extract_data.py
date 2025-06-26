import os
import requests
import base64
import json
from convert_base64 import convertobase64
from schema_file import schema1

# schema = schema1
schema ={

    "fields":{
        "scopeOfWork":[{
                "group" : "which group this position belongs,just above the table in bold letters with group and its number number in alpha numeric also check in next line",
                "serialnumber": "name of positions",
                "post": "name of positions",
                "experienceYears": "experience in numeric",
                "numberOfResources": "number of resource in numeric",
            }] 
    }
}

# schema = {}

def extract_data(filePath):

    file = convertobase64(filePath)

    sample = {
            "file": file,
            "settings": {
                "pages": "1-500",
                "dpi": 300,
                "ocr": {
                    "extract": True,
                    "multilingual": False,
                    "fields": {
                        "extract": True,
                        "filter": False,
                        "model": "engine7"
                    },
                    "table": {
                        "extract": True,
                        "include": True,
                        "validate": False,
                        "json": True
                    },
                    "paragraphs": {
                        "json": True
                    },
                    "localization": {
                        "translate":False,
                        "language": "english",
                        "model": "engine7"
                    }
                },
                "barcode": {
                    "extract": False
                },
                "signature": {
                    "extract": False,
                    "crop": True
                }
            },
            "schema":schema,
            "version": "3.0.0",
            "key": "0f0e453f-58fc-4c34-8ef0-901340cf46ba"
        }

    ############# To make a json file for payload ############
    # payloadPath = os.path.join(os.path.dirname(__file__),"payload.json")
    # with open(payloadPath, 'w+') as fl:
    #     json.dump(sample, fl, indent=4)
    
    json_data = json.dumps(sample)
    
    try:
        url = "https://sequeldocapi-dev.azurewebsites.net/api/sequelDoc?code=OgRpEZ37XUhD1qwr7_w6sHxkfx0nka5hD990mhhsYZt1AzFuy1RWLw=="
        response = requests.post(url, data=json_data, headers={"Content-type":"application/json"})
        
        print(response,"Response generated")
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the POST request:", e)
        return None
    except json.JSONDecodeError as e:
        print("An error occurred while parsing the JSON response:", e)
        return None  
    except IOError as e:
        print("An error occurred while writing the JSON response to a file:", e)
        return None