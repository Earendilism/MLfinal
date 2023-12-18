STR = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39\
 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15\
 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"
L_STR = STR.split(" ")
L_STR_M = []
D_STR = {}
SS = [j[0] for i, j in enumerate(L_STR)]
NN = [int(j[1:]) for i, j in enumerate(L_STR)]
D_STR = dict(zip(NN, SS))
a = dict(sorted(D_STR.items()))
print("".join(a.values()))
