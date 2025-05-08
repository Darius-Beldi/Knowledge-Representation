# #inlocuiti fiecare comentariu TODO
#
# class NodArbore:
#     def __init__(self, _informatie, _parinte=None):
#         self.informatie = #TO DO
#         self.parinte = #TO DO
#
#     def drumRadacina(self):
#         nod=self
#         l=# TO DO lista vida
#         while nod:
#             #TO DO adaugam nod la finalul lui l
#             #TO DO urcam cu un nivel; variabila nod devine parintele sau
#         return l[::-1]
#
#     def inDrum(self,infoNod):
#         nod=self
#         while nod:
#             #TO DO verificam daca informatia nodului nod e egala cu infoNod
#                 return True
#             #TO DO urcam cu un nivel; variabila nod devine parintele sau
#         return False
#
#
#     def __str__(self):
#         return #TO DO conversia proprietatii informatie la string
#
#     #c (a->b->c)
#     def __repr__(self):
#         sirDrum=#TO DO se foloseste join cu separatorul "->" pe o lista cu informatiile nodurilor returnate de drumRadacina()
#         return f"{self.informatie}, ({sirDrum})"
#
# class Graf:
#     def __init__(self, _matr, _start, _scopuri):
#         self.matr=#TO DO
#         self.start=#TO DO
#         self.scopuri=#TO DO
#
#     def scop(self, informatieNod):
#         return #TO DO daca informatieNod se afla in lista self.scopuri
#
#     def succesori(self, nod):
#         lSuccesori=[]
#         for infoSuccesor in range(len(self.matr)):
#             conditieMuchie=#TO DO testam ca pe linia corespunzatoare informatiei nodului si pe coloana infoSuccesor avem 1 (muchie)
#             conditieNotInDrum=#TO DO testam ca infoSuccesor nu se afla in drumul nodului nod (cu metoda inDrum)
#             if conditieMuchie and conditieNotInDrum:
#                 nodNou=#TO DO obiect de tip NodArbore cu informatia infoSuccesor si parintele egal cu variabila nod
#                 lSuccesori.append(nodNou)
#         return lSuccesori
#
#
#
# m = [
#     [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# ]
#
# def BF(gr, nsol):
#     coada=#TO DO o lista cuprinzand un element de tip NodArbore cu informatia de start din graful gr
#     #TO DO nodul de start fiind radacina, nu va avea parinte
#     while coada:
#         nodCurent=#TO DO primul nod din coada care e sters si returnat in nodCurent (functia pop)
#         if gr.scop(nodCurent.informatie):
#             print("Solutie: ", end="")
#             print(repr(nodCurent))
#             #TO DO scadem cu 1 numarul de solutii nsol
#             #TO DO daca numarul de solutii nsol este 0
#                 return
#         coada+=#TO DO adaugam succesorii generati cu gr.succesori pentru nodCurent
#
#
#
# def depth_first(gr, nsol=1):
#     # vom simula o stiva prin relatia de parinte a nodului curent
#     DF(NodArbore(gr.start), nsol)
#
#
# def DF(nodCurent, nsol):
#     if nsol <= 0:
#         return nsol
#     #print("Stiva actuala: " + repr(nodCurent.drumRadacina()))
#
#     if gr.scop(nodCurent.info):
#         print("Solutie: ", end="")
#         print(repr(nodCurent))
#         print("\n----------------\n")
#
#         #TO DO scadem cu 1 numarul de solutii nsol
#         #TO DO daca numarul de solutii nsol este 0
#             return
#     lSuccesori = #TO DO lista cu succesorii generati cu gr.succesori pentru nodCurent
#     #TO DO  pentru fiecare succesor sc din lSuccesori
#         if nsol != 0:
#             nsol = DF(sc, nsol)
#
#     return nsol
#
#
# start = 0
# scopuri = [5, 9]
# gr=Graf(m,start,scopuri)
# BF(gr, 4)
