import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        # print(data)
        record = json.loads(data)
        print("record")
        print(record)
        for k, v in record.items():
            mapper(k,v)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        #jenc = json.JSONEncoder(encoding='latin-1')
        jenc = json.JSONEncoder()
        banana = {}
        for item in self.result:
            print(jenc.encode(item))
            #romeo = {item[0] : item[1]}
            #banana.update(romeo)
        #print json.dumps(banana)    
