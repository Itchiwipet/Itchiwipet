meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Cara graciosa",
            "CREEPY": "Algo aterrador",
            "BOOMER": "Persona que se aferra mucho al pasado",
            "PA": "para",
            "TROLIAR": "Hacer una broma"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No se encontro la palabra")