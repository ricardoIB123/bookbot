

def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"


def count_caracter(text):
    texto = text.lower()
    conteo = {}
    for letra in texto:
        if letra.isalpha(): #solo cuenta letras e ignora espacio y simbolos
            if letra not in conteo:
                conteo[letra] = 1
            else:
                conteo[letra] +=1
    #for letra, cantidad in conteo.items():
    #    print(f"sd {letra} y {cantidad}")
    return conteo

def informe(text, book_path, num_words, caracter_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for clave, valor in sorted(caracter_words.items(), key=lambda x:x[1], reverse=True):
        print(f"{clave}: {valor}")
    print("============= END ===============")



