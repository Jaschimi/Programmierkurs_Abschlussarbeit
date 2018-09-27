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
                for i in x0:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of x0 need to be real numbers! x0[0] was of type '" +
                        "{}', x0[1] was of type '{}', ".format(type(x0[0]).__name__, type(x0[1]).__name__) +
                        "and x0[2] was of type '{}'.".format(type(x0[2]).__name__))
                self._x0 = x0

                for i in vector1:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of vector1 need to be real numbers! vector1[0] was of type '" +
                        "{}', vector1[1] was of type '{}', ".format(type(vector1[0]).__name__, type(vector1[1]).__name__) +
                        "and vector1[2] was of type '{}'.".format(type(vector1[2]).__name__))
                self._vector1 = vector1

                for i in vector2:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of vector2 need to be real numbers! vector2[0] was of type '" +
                        "{}', vector2[1] was of type '{}', ".format(type(vector2[0]).__name__, type(vector2[1]).__name__) +
                        "and vector2[2] was of type '{}'.".format(type(vector2[2]).__name__))
                self._vector2 = vector2
            else:
                raise IndexError("x0, vector1, and vector2 need to be of length 3! x0 was of length '" +
            "{}', vector1 was of length '{}', ".format(len(x0), len(vector1)) +
            "and vector2 was of length '{}'.".format(len(vector2)))

        else:
            raise TypeError("x0, vector1, and vector2 need to be lists! x0 was of type '" +
            "{}', vector1 was of type '{}', ".format(type(x0).__name__, type(vector1).__name__) +
            "and vector2 was of type '{}'.".format(type(vector2).__name__))

    def move(self, vec):
        if(type(vec)==list):
            if(len(vec)==3):
                for i in range(len(vec)):
                    if(not(type(vec[i])==float or type(vec[i])==int)):
                        raise TypeError("The entries of vec need to be real numbers! vec[0] was of type '" +
                        "{}', vec[1] was of type '{}', ".format(type(vec[0]).__name__, type(vec[1]).__name__) +
                        "and vec[2] was of type '{}'.".format(type(vec[2]).__name__))
                    else:
                        self._x0[i]+=vec[i]

            else:
                raise IndexError("vec needs to be of length 3! vec was of length '{}'.".format(len(vec)))
        else:
            raise TypeError("vec needs to be a list! vec was of type '{}'.".format(type(vec).__name__))

    def getX0(self):
        return self._x0

    def getVector1(self):
        return self._vector1

    def getVector2(self):
        return self._vector2

    def setX0(self, x0):
        if(type(x0)==list):
            if(len(x0)==3):
                for i in x0:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of x0 need to be real numbers! x0[0] was of type '" +
                        "{}', x0[1] was of type '{}', ".format(type(x0[0]).__name__, type(x0[1]).__name__) +
                        "and x0[2] was of type '{}'.".format(type(x0[2]).__name__))
                self._x0 = x0

            else:
                raise IndexError("x0 needs to be of length 3! x0 was of length '{}'.".format(len(x0)))
        else:
            raise TypeError("x0 needs to be a list! x0 was of type '{}'.".format(type(x0).__name__))

    def setVector1(self, vector1):
        if(type(vector1)==list):
            if(len(vector1)==3):
                for i in vector1:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of vector1 need to be real numbers! vector1[0] was of type '" +
                        "{}', vector1[1] was of type '{}', ".format(type(vector1[0]).__name__, type(vector1[1]).__name__) +
                        "and vector1[2] was of type '{}'.".format(type(vector1[2]).__name__))
                self._vector1 = vector1

            else:
                raise IndexError("vector1 needs to be of length 3! vector1 was of length '{}'.".format(len(vector1)))
        else:
            raise TypeError("vector1 needs to be a list! vector1 was of type '{}'.".format(type(vector1).__name__))

    def setVector2(self, vector2):
        if(type(vector2)==list):
            if(len(vector2)==3):
                for i in vector2:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of vector2 need to be real numbers! vector2[0] was of type '" +
                        "{}', vector2[1] was of type '{}', ".format(type(vector2[0]).__name__, type(vector2[1]).__name__) +
                        "and vector2[2] was of type '{}'.".format(type(vector2[2]).__name__))
                self._vector2 = vector2

            else:
                raise IndexError("vector2 needs to be of length 3! vector2 was of length '{}'.".format(len(vector2)))
        else:
            raise TypeError("vector2 needs to be a list! vector2 was of type '{}'.".format(type(vector2).__name__))
            
          
    def getnormal(self):
        v1 = self._vector1
        v2 = self._vector2
        vecpr =[ v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0] ]
        return vecpr

    def toHess(self):
        vecpr = self.getnormal()
        vecprLength = (vecpr[0]**2+vecpr[1]**2+vecpr[2]**2)**0.5
        vecpr[0] /= vecprLength
        vecpr[1] /= vecprLength
        vecpr[2] /= vecprLength
        p0 = 0
        for i in range(3):
            p0 += self._x0[i]*vecpr[i]
        if p0 < 0:
            for i in range(3):
                vecpr[i] = vecpr[i]*(-1)
                
        hesse_d = 0
        for i in range(3):
            hesse_d += self._x0[i]*vecpr[i]
        return EbeneHess(hesse_d,vecpr)

    def ison(self,y):
        check = toHess
        d = check.getD
        n0 = check.getNormal0
        for i in range(3):
            k = 0
            k += n0[i]*y[i]
        if k-d = 0 :
            print("The point {} does lay in the plain".format(y))
        else:
            print("The point {} doesn't lay in the plain".format(y))

    def __str__(self):
        print()
        #Easy access for the length of the entries in x0
        lengthOfX00 = len(str(self._x0[0]))
        lengthOfX01 = len(str(self._x0[1]))
        lengthOfX02 = len(str(self._x0[2]))
        
        #Easy access for the length of the entries in vector1
        lengthOfV10 = len(str(self._vector1[0])) - (1 if self._vector1[0]<0 else 0)
        lengthOfV11 = len(str(self._vector1[1])) - (1 if self._vector1[1]<0 else 0)
        lengthOfV12 = len(str(self._vector1[2])) - (1 if self._vector1[2]<0 else 0)

        #Easy access for the length of the entries in vector2
        lengthOfV20 = len(str(self._vector2[0])) - (1 if self._vector2[0]<0 else 0)
        lengthOfV21 = len(str(self._vector2[1])) - (1 if self._vector2[1]<0 else 0)
        lengthOfV22 = len(str(self._vector2[2])) - (1 if self._vector2[2]<0 else 0)


        #Calculating the amount of spaces needed in front of the three entries of x0
        mostDigitsX0 = lengthOfX00 if (lengthOfX00>lengthOfX01) else (lengthOfX01 if (lengthOfX01>lengthOfX02) else lengthOfX02)
        
        spacesX00 = mostDigitsX0 - lengthOfX00
        spacesX01 = mostDigitsX0 - lengthOfX01
        spacesX02 = mostDigitsX0 - lengthOfX02
        
        spacesX00 = " " * spacesX00
        spacesX01 = " " * spacesX01
        spacesX02 = " " * spacesX02

        #Calculating the amount of spaces needed in front of the three entries of vector1
        mostDigitsV1 =  lengthOfV10 if (lengthOfV10>lengthOfV11) else (lengthOfV11 if (lengthOfV11>lengthOfV12) else lengthOfV12)
        
        spacesV10 = mostDigitsV1 - lengthOfV10
        spacesV11 = mostDigitsV1 - lengthOfV11
        spacesV12 = mostDigitsV1 - lengthOfV12

        spacesV10 = " " * spacesV10
        spacesV11 = " " * spacesV11
        spacesV12 = " " * spacesV12

        #Calculating the amount of spaces needed in front of the three entries of vector1
        mostDigitsV2 =  lengthOfV20 if (lengthOfV20>lengthOfV21) else (lengthOfV21 if (lengthOfV21>lengthOfV22) else lengthOfV22)
        
        spacesV20 = mostDigitsV2 - lengthOfV20
        spacesV21 = mostDigitsV2 - lengthOfV21
        spacesV22 = mostDigitsV2 - lengthOfV22

        spacesV20 = " " * spacesV20
        spacesV21 = " " * spacesV21
        spacesV22 = " " * spacesV22

        return ("    {}{} {} {}{} * s {} {}{} * t\n".format(spacesX00, self._x0[0], "+" if (self._vector1[0]>=0) else "-", spacesV10, self._vector1[0] if self._vector1[0]>=0 else -self._vector1[0], "+" if (self._vector2[0]>=0) else "-", spacesV20, self._vector2[0] if self._vector2[0]>=0 else -self._vector2[0]) + 

                "E = {}{} {} {}{} * s {} {}{} * t\n".format(spacesX01, self._x0[1], "+" if (self._vector1[1]>=0) else "-", spacesV11, self._vector1[1] if self._vector1[1]>=0 else -self._vector1[1], "+" if (self._vector2[1]>=0) else "-", spacesV21, self._vector2[1] if self._vector2[1]>=0 else -self._vector2[1]) +
                
                "    {}{} {} {}{} * s {} {}{} * t\n".format(spacesX02, self._x0[2], "+" if (self._vector1[2]>=0) else "-", spacesV12, self._vector1[2] if self._vector1[2]>=0 else -self._vector1[2], "+" if (self._vector2[2]>=0) else "-", spacesV22, self._vector2[2] if self._vector2[2]>=0 else -self._vector2[2]))


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
                for i in x0:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of x0 need to be real numbers! x0[0] was of type '" +
                        "{}', x0[1] was of type '{}', ".format(type(x0[0]).__name__, type(x0[1]).__name__) +
                        "and x0[2] was of type '{}'.".format(type(x0[2]).__name__))
                self._x0 = x0

                for i in vector1:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of vector1 need to be real numbers! vector1[0] was of type '" +
                        "{}', vector1[1] was of type '{}', ".format(type(vector1[0]).__name__, type(vector1[1]).__name__) +
                        "and vector1[2] was of type '{}'.".format(type(vector1[2]).__name__))
                self._vector1 = vector1
            else:
                raise IndexError("x0 and vector1 need to be of length 3! x0 was of length '" +
            "{}' and vector1 was of length '{}'.".format(len(x0), len(vector1)))

        else:
            raise TypeError("x0 and vector1 need to be lists! x0 was of type '"
            + "{}' and vector1 was of type '{}'.".format(type(x0).__name__, type(vector1).__name__))
  
    def move(self, vec):
        if(type(vec)==list):
            if(len(vec)==3):
                for i in range(len(vec)):
                    if(not(type(vec[i])==float or type(vec[i])==int)):
                        raise TypeError("The entries of vec need to be real numbers! vec[0] was of type '" +
                        "{}', vec[1] was of type '{}', ".format(type(vec[0]).__name__, type(vec[1]).__name__) +
                        "and vec[2] was of type '{}'.".format(type(vec[2]).__name__))
                    else:
                        self._x0[i]+=vec[i]

            else:
                raise IndexError("vec needs to be of length 3! vec was of length '{}'.".format(len(vec)))
        else:
            raise TypeError("vec needs to be a list! vec was of type '{}'.".format(type(vec).__name__))


    def isOn(self,point):
        if(type(point)==list or type(point)==tuple):
            if(len(point)==3):
                
                print("der zu untersuchende punkt ist ",point)
                for i in range(3):
                    if( not(type(point[i])==float or type(point[i])==int) ):
                        raise TypeError("The entries of point need to be real numbers! point[0] was of type '" +
                        "{}', point[1] was of type '{}', ".format(type(point[0]).__name__, type(point[1]).__name__) +
                        "and point[2] was of type '{}'.".format(type(point[2]).__name__))
                
                aufpunkt = self.getX0()
                print("der stützpunkt ist ",aufpunkt)
                richtungsvektor = self.getVector1()
                print("der richtungsvektor ist ", richtungsvektor)
                diff = [ point[0]-aufpunkt[0] , point[1]-aufpunkt[1] , point[2]-aufpunkt[2] ]
                r = [0,0,0]  #lösung der geradengleichung
                
                for i in range(3):
                    if(diff[i]!=0 and richtungsvektor[i]!=0):
                        r[i] =diff[i]/richtungsvektor[i]
                        

                    elif(diff[i]!=0 and richtungsvektor[i]==0):
                        return print("nope, nicht auf gerade.")

                    elif(diff[i]==0 and richtungsvektor[i]!=0):
                        #jetzt muss r=0 sein, damit man chance auf erfolg hat
                        
                        if(r!=0):
                            return print("nope, nicht auf gerade.")
                        
                    else:
                    #also if(diff[i]==0 and richtungsvektor[i]==0):
                        r[i] = "beliebig wählbar" 
                print(r)
                answers = []
                for k in range(3):
                    if(type(r[k])==str):
                        continue
                    else:
                        answers.append(r[k])
                if(len(answers)<2):
                    return print("jo, liegt auf der gerade")
                else:
                    return print("nope, nicht auf gerade.")

            else:
                raise IndexError("your input needs to be of length 3! it was of length '{}'.".format(len(point)))
        else:
            raise TypeError("your input needs to be a list! it was of type '{}'.".format(type(point).__name__)) 

    def getX0(self):
        return self._x0

    def getVector1(self):
        return self._vector1

    def setX0(self, x0):
        if(type(x0)==list):
            if(len(x0)==3):
                for i in x0:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of x0 need to be real numbers! x0[0] was of type '" +
                        "{}', x0[1] was of type '{}', ".format(type(x0[0]).__name__, type(x0[1]).__name__) +
                        "and x0[2] was of type '{}'.".format(type(x0[2]).__name__))
                self._x0 = x0

            else:
                raise IndexError("x0 needs to be of length 3! x0 was of length '{}'.".format(len(x0)))
        else:
            raise TypeError("x0 needs to be a list! x0 was of type '{}'.".format(type(x0).__name__))

    def setVector1(self, vector1):
        if(type(vector1)==list):
            if(len(vector1)==3):
                for i in vector1:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of vector1 need to be real numbers! vector1[0] was of type '" +
                        "{}', vector1[1] was of type '{}', ".format(type(vector1[0]).__name__, type(vector1[1]).__name__) +
                        "and vector1[2] was of type '{}'.".format(type(vector1[2]).__name__))
                self._vector1 = vector1

            else:
                raise IndexError("vector1 needs to be of length 3! vector1 was of length '{}'.".format(len(vector1)))
        else:
            raise TypeError("vector1 needs to be a list! vector1 was of type '{}'.".format(type(vector1).__name__))
        
    def __str__(self):
        print()
        #Easy access for the length of the entries in x0
        lengthOfX00 = len(str(self._x0[0]))
        lengthOfX01 = len(str(self._x0[1]))
        lengthOfX02 = len(str(self._x0[2]))

        #Easy access for the length of the entries in vector1
        lengthOfV10 = len(str(self._vector1[0])) - (1 if self._vector1[0]<0 else 0)
        lengthOfV11 = len(str(self._vector1[1])) - (1 if self._vector1[1]<0 else 0)
        lengthOfV12 = len(str(self._vector1[2])) - (1 if self._vector1[2]<0 else 0)


        #Calculating the amount of spaces needed in front of the three entries of x0
        mostDigitsX0 = lengthOfX00 if (lengthOfX00>lengthOfX01) else (lengthOfX01 if (lengthOfX01>lengthOfX02) else lengthOfX02)
        
        spacesX00 = mostDigitsX0 - lengthOfX00
        spacesX01 = mostDigitsX0 - lengthOfX01
        spacesX02 = mostDigitsX0 - lengthOfX02
        
        spacesX00 = " " * spacesX00
        spacesX01 = " " * spacesX01
        spacesX02 = " " * spacesX02


        #Calculating the amount of spaces needed in front of the three entries of vector1
        mostDigitsV1 =  lengthOfV10 if (lengthOfV10>lengthOfV11) else (lengthOfV11 if (lengthOfV11>lengthOfV12) else lengthOfV12)
        
        spacesV10 = mostDigitsV1 - lengthOfV10
        spacesV11 = mostDigitsV1 - lengthOfV11
        spacesV12 = mostDigitsV1 - lengthOfV12

        spacesV10 = " " * spacesV10
        spacesV11 = " " * spacesV11
        spacesV12 = " " * spacesV12

        return ("    {}{} {} {}{} * r\n".format(spacesX00, self._x0[0], "+" if (self._vector1[0]>=0)
                else "-", spacesV10, self._vector1[0] if self._vector1[0]>=0 else -self._vector1[0]) + 

                "G = {}{} {} {}{} * r\n".format(spacesX01, self._x0[1], "+" if (self._vector1[1]>=0)
                else "-", spacesV11, self._vector1[1] if self._vector1[1]>=0 else -self._vector1[1]) +
                
                "    {}{} {} {}{} * r\n".format(spacesX02, self._x0[2], "+" if (self._vector1[2]>=0)
                else "-", spacesV12, self._vector1[2] if self._vector1[2]>=0 else -self._vector1[2]))

    def __repr__(self):
        return "Gerade({}, {})".format(self._x0, self._vector1)


class EbeneHess:
    def __init__(self, d, normal0):
        if(type(d)==float or type(d)==int):
            if(d>=0):
                self._d = d
            else:
                raise ArithmeticError("d needs to be greater than/equal to 0.")
        else:
            raise TypeError("d needs to be a real number! d was of type '{}'.".format(type(d).__name__))
            
        if(type(normal0)==list):
            if(len(normal0)==3):
                for i in normal0:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of normal0 need to be real numbers! normal0[0] was of type '" +
                        "{}', normal0[1] was of type '{}', ".format(type(normal0[0]).__name__, type(normal0[1]).__name__) +
                        "and normal0[2] was of type '{}'.".format(type(normal0[2]).__name__))
                normal0Length = (normal0[0]**2+normal0[1]**2+normal0[2]**2)**0.5
                normal0[0] /= normal0Length
                normal0[1] /= normal0Length
                normal0[2] /= normal0Length
                self._normal0 = normal0

            else:
                raise IndexError("normal0 needs to be of length 3! normal0 was of length '{}'.".format(len(normal0)))
        else:
            raise TypeError("normal0 needs to be a list! normal0 was of type '{}'.".format(type(normal0).__name__))

    def getD(self):
        return self._d

    def getNormal0(self):
        return self._normal0

    def setD(self, d):
        if(type(d)==float or type(d)==int):
            if(d>=0):
                self._d = d
            else:
                raise ArithmeticError("d needs to be greater than/equal to 0.")
        else:
            raise TypeError("d needs to be a real number! d was of type '{}'.".format(type(d).__name__))

    def setNormal0(self, normal0):
        if(type(normal0)==list):
            if(len(normal0)==3):
                for i in normal0:
                    if(not(type(i)==float or type(i)==int)):
                        raise TypeError("The entries of normal0 need to be real numbers! normal0[0] was of type '" +
                        "{}', normal0[1] was of type '{}', ".format(type(normal0[0]).__name__, type(normal0[1]).__name__) +
                        "and normal0[2] was of type '{}'.".format(type(normal0[2]).__name__))
                normal0Length = (normal0[0]**2+normal0[1]**2+normal0[2]**2)**0.5
                normal0[0] /= normal0Length
                normal0[1] /= normal0Length
                normal0[2] /= normal0Length
                self._normal0 = normal0

            else:
                raise IndexError("normal0 needs to be of length 3! normal0 was of length '{}'.".format(len(normal0)))
        else:
            raise TypeError("normal0 needs to be a list! normal0 was of type '{}'.".format(type(normal0).__name__))
            
    def __str__(self):
        print()
        #Easy access for the length of the entries in vector1
        lengthOfN00 = len(str(self._normal0[0]))
        lengthOfN01 = len(str(self._normal0[1]))
        lengthOfN02 = len(str(self._normal0[2]))

        #Calculating the amount of spaces needed in front of the three entries of vector1
        mostDigitsN0 =  lengthOfN00 if (lengthOfN00>lengthOfN01) else (lengthOfN01 if (lengthOfN01>lengthOfN02) else lengthOfN02)
        
        spacesN00 = mostDigitsN0 - lengthOfN00
        spacesN01 = mostDigitsN0 - lengthOfN01
        spacesN02 = mostDigitsN0 - lengthOfN02

        spacesN00 = " " * spacesN00
        spacesN01 = " " * spacesN01
        spacesN02 = " " * spacesN02

        return ("     |x1|   |{}{}|\n".format(spacesN00, self._normal0[0]) + 

                "E := |x2| * |{}{}| - {} = 0\n".format(spacesN01, self._normal0[1], self._d) +
                
                "     |x3|   |{}{}|\n".format(spacesN02, self._normal0[2]))
        
    def __repr__(self):
        return "EbeneHess({}, {})".format(self._d, self._normal0)
    
    def toPara(self):
        n0 = self.getNormal0()
        d = self.getD()
        
        line = [[], [], []]
        if(n0[0]!=0):
            line[0] = [d/-n0[0], n0[1]/-n0[0], n0[2]/-n0[0]]
            line[1] = [0, 1, 0]
            line[2] = [0, 0, 1]
        elif(n0[1]!=0):
            line[0] = [0, 1, 0]
            line[1] = [d/-n0[1], n0[0]/-n0[1], n0[2]/-n0[1]]
            line[2] = [0, 0, 1]
        elif(n0[2]!=0):
            line[0] = [0, 1, 0]
            line[1] = [0, 0, 1]
            line[2] = [d/-n0[2], n0[0]/-n0[2], n0[1]/-n0[2]]


        stützvektor = [line[0][0], line[1][0], line[2][0]]
        richtungsvektor1 = [line[0][1], line[1][1], line[2][1]]
        richtungsvektor2 = [line[0][2], line[1][2], line[2][2]]
        
        #c.f.: https://de.serlo.org/entity/view/1899
        return Ebene(stützvektor, richtungsvektor1, richtungsvektor2)

                

testGerade = Gerade([-200, 662, 3], [-991, 2, 33])
# print(testGerade)

# testEbeneHess = EbeneHess(1, [4, 4, 4])
# print(testEbeneHess)

# testEbeneHessToPara = testEbeneHess.toPara()
# print(testEbeneHessToPara)

# testEbeneHessToParaToHess = testEbeneHessToPara.toHess()
# print(testEbeneHessToParaToHess)


testEbene = Ebene([0, 0, 0], [0, 25, 0], [1, 0, 0])
print(testEbene)

testEbeneHess = testEbene.toHess()
print(testEbeneHess)

testEbeneHessToPara = testEbeneHess.toPara()
print(testEbeneHessToPara)