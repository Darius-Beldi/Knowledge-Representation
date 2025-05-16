#inlocuiti fiecare comentariu TODO

class NodArbore:
    #parinte e un nod, nu doar informatia parintelui
    #h = euristica cat estimam de la un nod la nod scop (cat estimez)
    #g = cost de la un nod la altul (cat am parcurs)
    #f = suma dintre g si h (cat am parcurs + cat estimez)
    def __init__(self, _informatie, _parinte=None, _g = 0, _h = 0):
        '''
        :param _informatie:
        :param _parinte:
        :param _g: cat am parcurs
        :param _h: cat estimez
        '''
        self.informatie = _informatie
        self.parinte = _parinte
        self.g = _g
        self.h = _h
        self.f = _g + _h

    def drumRadacina(self):
        '''
        drumul de la nod la radacina
        :return:
        '''
        nod=self
        l = []
        while nod:
            l.append(nod)
            nod = nod.parinte
        return l[::-1]

    def inDrum(self,infoNod):
        '''
        verifica daca nodul dat ca parametru e in drumul de la nodul self la radacina
        :param infoNod:
        :return:
        '''
        nod=self
        while nod:
            if nod.informatie == infoNod:
                return True
            nod = nod.parinte
        return False

    #str de consola
    def __str__(self):
        return str(self.informatie)
    #repr de debugger
    #c (a->b->c)
    def __repr__(self):
        sirDrum = "->".join(map(str,self.drumRadacina()))
        return f"{self.informatie}, cost: {self.g}, ({sirDrum})"

    def __lt__(self, other):
        '''
        ordonam dupa suma dintre cost curent + estimare pana la final scop
        daca sunt egale, ordonam dupa drumul unde stim mai multa informatie
        :param other:
        :return:
        '''
        return (self.f < other.f) or (self.f == other.f and self.h < other.h)


class Graf:
    def __init__(self, _matr, _start, _scopuri, _h):
        '''

        :param _matr: matricea de adiacenta cu costuri
        :param _start: radacina
        :param _scopuri: nodurile finale
        :param _h: vectorul de estimatii (euristica)
        '''
        self.matr= _matr
        self.start= _start
        self.scopuri= _scopuri
        self.h= _h

    def scop(self, informatieNod):
        '''
        verifica daca nodul este in scop
        :param informatieNod:
        :return:
        '''
        return informatieNod in self.scopuri

    def estimeaza_h(self, infoNod):
        '''
        :param infoNod: nodul pentru care se estimeaza
        :return: estimarea nodului
        '''
        return self.h[infoNod]

    def succesori(self, nod):
        lSuccesori=[]
        for infoSuccesor in range(len(self.matr)):
            conditieMuchie = self.matr[nod.informatie][infoSuccesor] > 0 #verifica daca exista o muchie intre noduri
            conditieNotInDrum = not nod.inDrum(infoSuccesor) # verifica daca nu a mai fost vizitat deja
            if conditieMuchie and conditieNotInDrum:
                __g = (nod.g + #costul pana aici
                + self.matr[nod.informatie][infoSuccesor] )#costul de la nod parinte la nod actual)
                __h = self.estimeaza_h(infoSuccesor)
                nodNou = NodArbore(infoSuccesor, nod, __g, __h)
                lSuccesori.append(nodNou)
        return lSuccesori


def aStarSolMultiple(gr, nsol):
    '''
    solutiile vor fi ordonate dupa cost (nodurile scop au estimat 0, deci f = g)
    :param gr: graful
    :param nsol: numar de solutii
    :return: void
    '''
    coada=[NodArbore(gr.start)]
    while coada:
        #iau primul nod din coada si verific daca e nod scop
        nodCurent = coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            nsol -= 1
            if not nsol:
                return

        coada+= gr.succesori(nodCurent)
        # coada este o coada de prioritati, deci o sortam
        coada.sort()

def a_Star(gr):
    '''
    face drumul de cost minim
    :param gr: graful
    :return: void
    '''
    CLOSED=[]
    OPEN=[NodArbore(gr.start)]
    while OPEN:
        #iau primul nod din OPEN si verific daca e nod scop
        nodCurent = OPEN.pop(0)
        CLOSED.append(nodCurent)

        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            return

        lSuccesori = gr.succesori(nodCurent)
        for sc in lSuccesori:
            gasitOPEN = False
            for nod in OPEN: # cauta in cele care nu au fost vizitate
                if nod.informatie == sc.informatie:
                    gasitOPEN = True
                    if nod < sc:
                        lSuccesori.remove(sc)
                    else:
                        OPEN.remove(nod)
                    break

            if not gasitOPEN: #daca nu l am gasit in OPEN
                for nod in CLOSED: #il cautam in CLOSED (cele deja parcurse)
                    if nod.informatie == sc.informatie:
                        if nod < sc:
                            lSuccesori.remove(sc)
                        else:
                            CLOSED.remove(nod)
                            #cand il scot din CLOSED il las sa se expandeze adica il las sa isi reevalueze succesorii
                        break

        OPEN += lSuccesori
        OPEN.sort()

    print("Nu avem solutii")
    return

m = [ #matrice de adiacenta
[0, 3, 5, 10, 0, 0, 100],
[0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 4, 9, 3, 0],
[0, 3, 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 4, 0, 5],
[0, 0, 3, 0, 0, 0, 0],
]

start = 0 #nodul radacina
scopuri = [4,6] #noduri finale
h=[0,1,6,2,0,3,0] # vectorul de estimatii

gr=Graf(m,start,scopuri,h)
nsol = 5
print("aStarSolMultiple: ")
aStarSolMultiple(gr, nsol)
print("a_Star: ")
a_Star(gr)