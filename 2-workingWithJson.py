import json

def readJSON(filename):
    with open(filename,'rb') as f:
        data = json.load(f)
    return data

def writeDictToJson(data,filename):
    try:
        reqString = json.dumps(data, indent=2)
        with open(filename,'w') as f:
            f.write(reqString)
    except Exception as e:
        raise e

a = {
    "a" : 1,
    "b" : 100,
    "c" : True
}
writeDictToJson(a,'randomJsonWrite.json')
