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

# class Servers_yaml(Information_yaml):
#     def servers(self):
#         self.list = []
#         for i in self.dictionary:
#             self.list.append(i)
#         print(self.list)

#     def Server(self):
#         data3 = self.dictionary[self.list[1]]
#         servers = data3['servers']
#         print(servers)



Data = Dictionary("banking.yml")
Data.yaml_reader()
Data2 = Information_yaml("banking.yml")
Data2.yaml_reader()
Data2.info()
Data2.Api()
Data2.Description()
Data2.Version()
# Data3 = Servers_yaml("banking.yml")
# Data3.yaml_reader()
# Data3.Server()