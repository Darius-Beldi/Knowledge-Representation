#inlocuiti fiecare comentariu TODO

class NodArbore:
    #parinte e un nod, nu doar informatia parintelui
    def __init__(self, _informatie, _parinte=None):
        self.informatie = _informatie
        self.parinte = _parinte

    def drumRadacina(self):
        nod=self
        l = []
        while nod:
            l.append(nod)
            nod = nod.parinte
        return l[::-1]

    def inDrum(self,infoNod):
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
        return f"{self.informatie}, ({sirDrum})"

class Graf:
    def __init__(self, _matr, _start, _scopuri):
        self.matr= _matr
        self.start= _start
        self.scopuri= _scopuri

    def scop(self, informatieNod):
        return informatieNod in self.scopuri

    def succesori(self, nod):
        lSuccesori=[]
        for infoSuccesor in range(len(self.matr)):
            conditieMuchie = self.matr[nod.informatie][infoSuccesor]
            #TO DO testam ca pe linia corespunzatoare informatiei nodului si pe coloana infoSuccesor avem 1 (muchie)
            conditieNotInDrum = not nod.inDrum(infoSuccesor)
            #TO DO testam ca infoSuccesor nu se afla in drumul nodului nod (cu metoda inDrum)
            if conditieMuchie and conditieNotInDrum:
                nodNou = NodArbore(infoSuccesor, nod)
                #TO DO obiect de tip NodArbore cu informatia infoSuccesor si parintele egal cu variabila nod
                lSuccesori.append(nodNou)
        return lSuccesori



m = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

#nsol = numarul de solutii
def BF(gr, nsol):
    coada=[NodArbore(gr.start)]
    #TO DO o lista cuprinzand un element de tip NodArbore cu informatia de start din graful gr

    #TO DO nodul de start fiind radacina, nu va avea parinte
    while coada:
        nodCurent = coada.pop(0)
        #TO DO primul nod din coada care e sters si returnat in nodCurent (functia pop)

        #verific cand sterg din coada, pentru ex 6 tre sa verific cand il pun in coada
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            nsol -= 1
            if not nsol:
                return
        coada+= gr.succesori(nodCurent)



def depth_first(gr, nsol=1):
    # vom simula o stiva prin relatia de parinte a nodului curent
    print("DF")
    DF(NodArbore(gr.start), nsol)
    DF_non_recursive(NodArbore(gr.start), nsol)


def DF(nodCurent, nsol):
    if nsol <= 0:
        return nsol
    #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))

    if gr.scop(nodCurent.informatie):
        print("Solutie: ", end="")
        print(repr(nodCurent))
        print("\n----------------\n")
        nsol -= 1
        if not nsol:
            return 0
    lSuccesori = gr.succesori(nodCurent)
    #TO DO lista cu succesorii generati cu gr.succesori pentru nodCurent
    #TO DO  pentru fiecare succesor sc din lSuccesori
    for sc in lSuccesori:
        if nsol != 0:
            nsol = DF(sc, nsol)

    return nsol

#ex 5
def DF_non_recursive(nodInitial, nsol):
    if nsol <= 0:
        return nsol
    stack = [nodInitial]
    while stack and nsol > 0:
        nodCurent = stack.pop()
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            print("\n----------------\n")
            nsol -= 1
            if nsol == 0:
                return 0
        lSuccesori = gr.succesori(nodCurent)
        for sc in reversed(lSuccesori):
            stack.append(sc)
    return nsol

#EX 6
def BF6(gr, nsol):
    coada=[NodArbore(gr.start)]
    while coada:
        nodCurent = coada.pop(0)
        coada += gr.succesori(nodCurent)
        if gr.scop(nodCurent.informatie):
            print("Solutie: ", end="")
            print(repr(nodCurent))
            nsol -= 1
            if not nsol:
                return



start = 0
scopuri = [5, 9]
gr=Graf(m,start,scopuri)
BF(gr, 4)
BF6(gr, 4)
depth_first(gr,4)