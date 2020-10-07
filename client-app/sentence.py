from random import randint
from json import dumps
from requests import post

"""lista de oraciones"""
_sentences = []

"""lista de autores"""
_authors = ["Otis Galloway",
            "Lydia Landry",
            "Jaylan Rubio",
            "Connie Holt",
            "Beauden Cunningham",
            "Arianna Hayden",
            "Edna Begum",
            "Oran Whittaker",
            "Rehan Mclean",
            "Fox Bean",
            "Mariah Garza",
            "Eddison Hutton",
            "Gethin Mayo",
            "Chenai Smith",
            "Fionn Lowry",
            "Gavin Bevan",
            "Ryley Garner",
            "Shanon Davenport",
            "Giselle Henderson",
            "Chester Watkins",
            "Peyton Marquez",
            "Saim Olsen",
            "Cherie Paine",
            "Marco Derrick",
            "Presley Boyd",
            "Fahad Rose",
            "Jasleen Chester",
            "Kamron Kirkland",
            "Denzel Horner",
            "Timur Hulme",
            "Mccauley Jacobson",
            "Meadow May",
            "Mehreen Mccullough",
            "Izzie Workman",
            "Aden Cruz",
            "Joao Acosta",
            "Kajal Carr",
            "Natalie Chambers",
            "Macsen Key",
            "Sidra Greenaway",
            "Karishma Talbot",
            "Jovan Brown",
            "Amna Underwood",
            "Conah Stott",
            "Roshan Stein",
            "Sunil Morris",
            "Wallace Oakley",
            "Jun Richard",
            "Maia Denton",
            "Mared Mcmanus",
            "Yvette Sparks",
            "Louie Mccarthy",
            "Jayden O'Reilly",
            "Leila Mccall",
            "Lance Allison",
            "Shiv Mcmahon",
            "Penny Fields",
            "Ella-Mae Mills",
            "Betsy Ashton",
            "Beverley Rossi",
            "Selina Mckenzie",
            "Lillie-Mae Crosby",
            "Harrison Busby",
            "Lamar Bender",
            "Olivia-Rose England,"
            "Dora Farrell",
            "Taylah Dodd",
            "Griff Millar",
            "Matthias Miller",
            "Ocean Lara",
            "Zunairah Wainwright,"
            "Miranda Mack",
            "Imaad Nairn",
            "Margaret Heath",
            "Jordan Friedman",
            "Sadie Dean",
            "Leja Sanford",
            "Charmaine Carroll",
            "Elize Sims",
            "Reyansh Powell",
            "Aj Silva",
            "Luther Quintero",
            "Noel Brennan",
            "Margaux Burton",
            "Agatha Allman",
            "Arwen Dawe",
            "Chelsey Burt",
            "Dominykas Valdez",
            "Loretta Fitzgerald",
            "Danielle Finney",
            "Jeremy Hutchinson",
            "Euan Bowler",
            "Philippa Kelley",
            "Zachariah Rhodes",
            "Anushka Thomson",
            "Amanpreet Barrett",
            "Makenzie Rangel",
            "Leigh Jackson",
            "Armani Wooten",
            "Zeshan Rooney"]

def getAuthor():
    """Recupera el nombre de un autor"""
    n = randint(0,99)
    return _authors[n]

def addSentences(sentence):
    """Agrega una nueva oración"""
    _sentences.append({"autor": getAuthor(), "oracion":sentence})

def printSentences():
    """Imprimir oraciones"""
    for stc in _sentences:
        print(dumps(stc))

def sendSenteces(url):
    """Envía las oraciones al servidor 1"""
    for stc in _sentences:
        res = post(url, json=dumps(stc))
        if res.status_code != 200:
            print(" > Ocurrió un error al enviar una oración", res.status_code)
        else:
            print(res.json())
