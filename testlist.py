#this is a test py

class FlightParameter(object):
    parameterDict={
        "aileron":10.0,
        "elevator":10.0,
        "rudder":10.0,
        "throttle0":10,
        "throttle1":10,
        "altitude_ft":200,
        ## 注意区分经纬这两个变量
        #"longtitude_deg":-20.5925,
        #"latitude":63.9850,
        #"airspeed_kt":10,

    }
    # parameterDict={
    #     "aileron":10.0,
    #     "elevator":10.0,
    #     "rudder":10.0,
    #     "throttle0":100.0,
    #     "throttle1":100.0,
    #     "latitude_deg":-20.5925,
    #     "longtitude_deg":63.985,
    #     "altitude_ft":100.0,
    # }
    def getKey(self):
        return tuple(self.parameterDict.keys())
    def getValue(self):
        return list(self.parameterDict.values())
    def getDict(self):
        return self.parameterDict
    def getValueStr(self):
        valuelist=[]
        for value in self.parameterDict.values():
            valuelist.append(str(value))
        return ",".join(valuelist)+"\n"
fptest=FlightParameter()

print(fptest.getKey())
print(fptest.getValue())
print(fptest.getDict())
print(fptest.getValueStr())




# print(parameterList)
# print(parameterValue)
# dict1=dict(zip(parameterList,parameterValue))
# print(dict1)
# string1=list


