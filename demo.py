import yaml


class Dictionary():
    def __init__(self,yaml_file):
        self.dictionary = {}       
        self.file = yaml_file

    def yaml_reader(self):
        content = open(self.file,"r")
        self.dictionary = yaml.safe_load(content)
        

class Information_yaml(Dictionary):
    def info(self):
        self.list = []
        for i in self.dictionary:
            self.list.append(i)
        print(self.list)


    def Api(self):
        data = self.dictionary[self.list[1]]
        title = data['title']
        print(title)

    def Description(self):
        data1 = self.dictionary[self.list[1]]
        description = data1['description']
        print(description)


    def Version(self):
        data2 = self.dictionary[self.list[1]]
        version = data2['version']
        print(version)

class Servers_yaml(Information_yaml):
    def info(self):
        self.list = []
        for i in self.dictionary:
            self.list.append(i)
        return(self.list)

    def data(self):
        self.data = self.dictionary[self.list[2]]
        return self.data
    
    def server_url(self):
        self.data = self.dictionary[self.list[2]][0]
        self.url = self.data['url']
        return self.url
    
    def server_description(self):
        self.data = self.dictionary[self.list[2]][0]
        self.description = self.data['description']
        return self.description

class Paths(Dictionary):
    def info(self):
        self.list = []
        for i in self.dictionary:
            self.list.append(i)
        self.data = self.dictionary[self.list[3]]
        return(self.data) 

class Accounts_get(Dictionary):
    def info(self):
        self.list = []
        for i in self.dictionary:
            self.list.append(i)
        self.data = self.dictionary[self.list[3]]
        self.accounts = self.data['/accounts']['get']
        return self.accounts





Data = Dictionary("banking.yml")
Data.yaml_reader()
Data2 = Information_yaml("banking.yml")
Data2.yaml_reader()
Data2.info()
Data2.Api()
Data2.Description()
Data2.Version()
Data3 = Servers_yaml("banking.yml")
Data3.yaml_reader()
Data3.info()
print(Data3.server_url())
print(Data3.server_description())
Data4 = Accounts_get("banking.yml")
Data4.yaml_reader()
Data4.info()