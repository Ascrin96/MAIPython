import requests
from bs4 import BeautifulSoup


url = "https://www.nordstar.ru/about/park"

r = requests.get(url)
planes_dict = {}
if r.status_code == 200:
    content = r.text
    bs = BeautifulSoup(content, "lxml")
    models = bs.find_all("div", attrs={"class": "col-sm-6 col-xs-12 vs"})
    models_image = bs.find_all("div", attrs={"class": "col-sm-6 col-xs-12 vsi"})


    for model in models:
        plane_dict = {}
        plane_dict["number"] = model.find("img", attrs={"alt":"Количество в парке"}).parent.find("b").text
        plane_dict["speed"] = model.find("img", attrs={"alt": "Крейсерская скорость"}).parent.find("b").text
        plane_dict["chairs"] = model.find("img", attrs={"alt": "Количество мест"}).parent.find("b").text
        plane_dict["distance"] = model.find("img", attrs={"alt": "Дальность полета"}).parent.find("b").text
        planes_dict[model.find("h2").text] = plane_dict

    for image in models_image:
        name = image.previous_sibling.previous_sibling.find("h2").text
        planes_dict[name] = image.find("img")["src"]
    print(planes_dict)

