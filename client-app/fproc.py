import codecs

from sentence import addSentences

def makeSentences(path):
    """Crea oraciones desde el texto del archivo especificado por path"""
    try:
        with codecs.open(path) as f:
            txt = f.read()
            startIdx = 0
            idx = txt.find(".", 0, len(txt))
            print(len(txt))
            while idx != -1:
                addSentences(txt[startIdx:idx+1].strip())
                # actualiza los valores de los indices
                startIdx = idx+2
                # determina dónde está el próximo punto
                idx = txt.find(".", startIdx, len(txt))
            if idx != len(txt.strip()):
                # añade cualquier texto que hay quedado
                # que no termine en un punto
                addSentences(txt[startIdx:].strip())
    except:
        print(" > Ocurrió un error al crear oraciones\n")
