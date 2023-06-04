"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    with open('data.csv') as csv_file:

      suma = 0
      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for column in range(len(row)):
          if column == 1:
            # print(row[column])
            suma += int(row[column])


    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    with open('data.csv') as csv_file:

      dicti = {"A":0,
               "B":0,
               "C":0,
               "D":0,
               "E":0}

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        match row[0]:
          case "A":
            dicti["A"] += 1
          case "B":
            dicti["B"] += 1
          case "C":
            dicti["C"] += 1
          case "D":
            dicti["D"] += 1
          case "E":
            dicti["E"] += 1

    return list(dicti.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    with open('data.csv') as csv_file:

      dicti = {"A":0,
               "B":0,
               "C":0,
               "D":0,
               "E":0}

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for column in range(len(row)):
          if column == 1:
            match row[0]:
              case "A":
                dicti["A"] += int(row[1])
              case "B":
                dicti["B"] += int(row[1])
              case "C":
                dicti["C"] += int(row[1])
              case "D":
                dicti["D"] += int(row[1])
              case "E":
                dicti["E"] += int(row[1])

    return list(dicti.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dicti = {"01":0,
             "02":0,
             "03":0,
             "04":0,
             "05":0,
             "06":0,
             "07":0,
             "08":0,
             "09":0,
             "10":0,
             "11":0,
             "12":0}

    import csv
    with open('data.csv') as csv_file:

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for column in range(len(row)):
          if column == 1:
            match row[2].split("-")[1]:
              case "01":
                dicti["01"] += 1
              case "02":
                dicti["02"] += 1
              case "03":
                dicti["03"] += 1
              case "04":
                dicti["04"] += 1
              case "05":
                dicti["05"] += 1
              case "06":
                dicti["06"] += 1
              case "07":
                dicti["07"] += 1
              case "08":
                dicti["08"] += 1
              case "09":
                dicti["09"] += 1
              case "10":
                dicti["10"] += 1
              case "11":
                dicti["11"] += 1
              case "12":
                dicti["12"] += 1

    return list(dicti.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """ 
    A = []
    B = []
    C = []
    D = []
    E = []
    
    import csv
    with open('data.csv') as csv_file:

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for column in range(len(row)):
          if column == 1:
              match row[0]:
                case "A":
                  A.append(row[1])
                case "B":
                  B.append(row[1])
                case "C":
                  C.append(row[1])
                case "D":
                  D.append(row[1])
                case "E":
                  E.append(row[1])
            
    
        
    return [("A",max(A),min(A)),
            ("B",max(B),min(B)),
            ("C",max(C),min(C)),
            ("D",max(D),min(D)),
            ("E",max(E),min(E))]



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    aaa = []
    bbb = []
    ccc = []
    ddd = []
    eee = []
    fff = []
    ggg = []
    hhh = []
    iii = []
    jjj = []

    import csv
    with open('data.csv') as csv_file:

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for column in row[4].split(","):
          # print(column)
          match column.split(":")[0]:
            case "aaa":
              aaa.append(int(column.split(":")[1]))
            case "bbb":
              bbb.append(int(column.split(":")[1]))
            case "ccc":
              ccc.append(int(column.split(":")[1]))
            case "ddd":
              ddd.append(int(column.split(":")[1]))
            case "eee":
              eee.append(int(column.split(":")[1]))
            case "fff":
              fff.append(int(column.split(":")[1]))
            case "ggg":
              ggg.append(int(column.split(":")[1]))
            case "hhh":
              hhh.append(int(column.split(":")[1]))
            case "iii":
              iii.append(int(column.split(":")[1]))
            case "jjj":
              jjj.append(int(column.split(":")[1]))
          

    return [("aaa",min(aaa),max(aaa)),
    ("bbb",min(bbb),max(bbb)),
    ("ccc",min(ccc),max(ccc)),
    ("ddd",min(ddd),max(ddd)),
    ("eee",min(eee),max(eee)),
    ("fff",min(fff),max(fff)),
    ("ggg",min(ggg),max(ggg)),
    ("hhh",min(hhh),max(hhh)),
    ("iii",min(iii),max(iii)),
    ("jjj",min(jjj),max(jjj))]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dicti = {"0":list(),
             "1":list(),
             "2":list(),
             "3":list(),
             "4":list(),
             "5":list(),
             "6":list(),
             "7":list(),
             "8":list(),
             "9":list()}


    import csv
    with open('data.csv') as csv_file:

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for column in row[1]:
          match column:
            case "0":
              dicti["0"].append(row[0]) 
            case "1":
              dicti["1"].append(row[0]) 
            case "2":
              dicti["2"].append(row[0])
            case "3":
              dicti["3"].append(row[0])
            case "4":
              dicti["4"].append(row[0])
            case "5":
              dicti["5"].append(row[0])
            case "6":
              dicti["6"].append(row[0])
            case "7":
              dicti["7"].append(row[0])
            case "8":
              dicti["8"].append(row[0])
            case "9":
              dicti["9"].append(row[0])
        

    return list(dicti.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    res = pregunta_07()

    listTuples = []
    for row in res:
      index = row[0]
      sinRep = set(row[1])
      listTuples.append((index,sorted(sinRep)))

    
    return listTuples


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    import re

    dictio = {"aaa":0,
              "bbb":0,
              "ccc":0,
              "ddd":0,
              "eee":0,
              "fff":0,
              "ggg":0,
              "hhh":0,
              "iii":0,
              "jjj":0}

    delimiters = r':|,'

    with open('data.csv') as csv_file:

      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        a = re.split(delimiters, row[4])
        for item in a:
          if item in dictio:
            dictio[item] += 1
 
    return dictio


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    import csv

    list10 = []

    with open('data.csv') as csv_file:
      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        # print(row)
        list10.append((row[0],len(row[3].split(',')),len(row[4].split(','))))


    return list10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv

    dicto11={}

    with open('data.csv') as csv_file:
      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for col in row[3].split(","):
            dicto11[str(i)] = dicto11.get(str(col),0) + int(row[1])
    return dict(sorted(dicto11.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dicto12={}
    import csv
    with open('data.csv') as csv_file:
      reader_variable = csv.reader(csv_file, delimiter="	")
      for row in reader_variable:
        for col in row[4].split(","):
            dicto12[row[0]] = dicto12.get(row[0],0) + int(col[4:])
    return dict(sorted(dicto12.items()))
