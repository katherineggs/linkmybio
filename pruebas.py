import yaml

with open("links.yaml") as yml:
    personal = yaml.load(yml,Loader=yaml.FullLoader)

for categorie,char in personal.items():
    print(char)
    # for page,value in char.it:
