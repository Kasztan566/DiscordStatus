import json

class Config:
    """ Class used for operations on config file """
    def __init__(self, path_to_config: str):
        self.path = path_to_config

    def read(self):
        with open(self.path) as f:
            j = json.load(f)
        return j
    
    def save(self, j: object):
        with open(self.path, 'w') as f:
            json.dump(j, f, indent=4)

    def edit(self, key: str, value: any):
        j = self.read()
        j[key] = value
        self.save(j)
