import subprocess

#result = subprocess.run(["speedtest-cli"], stdout=subprocess.PIPE)
#output = result.stdout.decode("utf-8")
#output=output.replace("..","")
#element = []
#element = output.split("\r\n")
#print(output)
#print (element)
#print(element[0])
cuenta= 2+2

class Red:
    def __init__(self):
        self.testing = ""
        self.host=""
        self.dowload = ""
        self.upload = ""    
    def update(self):
        result = subprocess.run(["speedtest-cli"], stdout=subprocess.PIPE)
        output = result.stdout.decode("utf-8")
        output=output.replace("..","")
        element = []
        element = output.split("\r\n")
        self.testing = element[1]
        self.host=element[4]
        self.dowload = element[6]
        self.upload = element[8]
    

