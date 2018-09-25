#Themengebiet 2: Projekt I
#In diesem Projekt sollen einfache geometrische Objekte, wie Geraden und Ebenen im 3-dimensionalen Raum
#betrachtet werden. Hierzu schreibe man zuerst die zwei Klassen Gerade und Ebene mit den nicht-öffentlichen
#Attributen x_0,vec_1,vec_2 im Falle von Ebenen. x_0,vec_1 im Falle von Geraden.
#Hierbei sollen die Ebenen bzw. Geraden in Parameterform dargestellt sein. Man schreibe Konstruktoren
#um die Objekte aus vorgegebenen x_0,vec_1,vec_2 bzw. x_0,vec_1 zu erzeugen. Die Parameter sollen hier
#Listen sein.
#Zusätzlich soll für beide Klassen eine Methode move(vec)geschrieben werden, die die Gerade/Ebene um vec
#verschiebt und eine Methode ison(x), die ausgibt, ob der Punkt x(Liste/Tupel) auf der Gerade/Ebene liegt.
#Für alle in diesem Themengebiet geschriebenen Klassen stelle man vernünftige (passende) Konstruktoren,
#und set, get-Methoden und geeignete Ausgaben, __str__ und __repr__, zur Verfügung.
#Man überprüfe stets die Funkltionalität der implementierten Methoden.

#Projekt I: Man schreibe eine Methode getnormal(), die einen Vektor(Liste) zurückliefert, der senkrecht
#auf der Ebene steht. Anschließend schreibe man eine weitere Klasse EbeneHess, die die nichtöffentlichen
#Attribute d,normal_0 enthält und die Ebene in der Hesseschen Normalenform (Wikipedia) darstellt.
#Jetzt schreibe man für die Klassen EbeneHess und Ebene Methoden, die die Darstellung in das jeweils
#andere Format überführen, also die gleiche Ebene im jeweils anderen Format zurück liefern.



class Ebene:
    def __init__(self, x0, vector1, vector2):
        if(type(x0)==list and type(vector1)==list and type(vector2)==list):
            if(len(x0)==3 and len(vector1)==3 and len(vector2)==3):
                self._x0 = x0
                self._vector1 = vector1
                self._vector2 = vector2
            else:
                raise IndexError("x0, vector1, and vector2 need to be of length 3! x0 was of length '" +
            "{}', vector1 was of type '{}', ".format(len(x0), len(vector1)) +
            "and vector2 was of type '{}'.".format(len(vector2)))

        else:
            raise TypeError("x0, vector1, and vector2 need to be lists! x0 was of type '" +
            "{}', vector1 was of type '{}', ".format(type(x0).__name__, type(vector1).__name__) +
            "and vector2 was of type '{}'.".format(type(vector2).__name__))

    def __str__(self):
        return ("    {} + {} * s + {} * t\n".format(self._x0[0], self._vector1[0], self._vector2[0]) + 
                "E = {} + {} * s + {} * t\n".format(self._x0[1], self._vector1[1], self._vector2[1]) +
                "    {} + {} * s + {} * t\n".format(self._x0[2], self._vector1[2], self._vector2[2]))


        # result = "["
        # for i in range(len(self._x0)):
        #     result += "[{} + {}*s + {}*t],".format(self._x0[i], self._vector1[i], self._vector2[i])
        # result += "]"
        # return result

    def __repr__(self):
        return "Ebene({}, {}, {})".format(self._x0, self._vector1, self._vector2)

class Gerade:
    def __init__(self, x0, vector1):
        if(type(x0)==list and type(vector1)==list):
            if(len(x0)==3 and len(vector1)==3):
                self._x0 = x0
                self._vector1 = vector1
            else:
                raise IndexError("x0 and vector1 need to be of length 3! x0 was of length '" +
            "{}' and vector1 was of length '{}'.".format(len(x0), len(vector1)))

        else:
            raise TypeError("x0 and vector1 need to be lists! x0 was of type '"
            + "{}' and vector1 was of type '{}'.".format(type(x0).__name__, type(vector1).__name__))
  
    def __str__(self):
        return ("    {} + {} * r\n".format(self._x0[0], self._vector1[0]) + 
                "G = {} + {} * r\n".format(self._x0[1], self._vector1[1]) +
                "    {} + {} * r\n".format(self._x0[2], self._vector1[2]))

    def __repr__(self):
        return "Gerade({}, {})".format(self._x0, self._vector1)

testEbene = Ebene([1, 6662, 3], [1, 2, 3], [1, 2, 3])
testGerade = Gerade([1, 2, 3], [1, 2, 3])

print(testEbene)
print(testGerade)