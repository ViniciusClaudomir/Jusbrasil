import re
import json
from typing import Any

def restructure_json(string) -> json:
    s = re.sub('(\w+)', '"\g<1>"', string)
    return json.loads(s.replace('""','"').replace('"."','.'))

def restructure_droplet_config(string) -> dict:
    
    s1 = re.sub(',(link_text.*)}', '}',string)
    s2 = re.sub('{(\w+):', '{"\g<1>":', s1)
    s3 = re.sub(',(\w+):', ',"\g<1>":', s2)
    s3 = s3.replace('"$".','')
    s3 = s3.replace('null','None')
    
    return eval(s3)
    
def concat(func):
    return func
def Vt(droplet, id_, tipo, tipo_id) -> Any:
    return id_