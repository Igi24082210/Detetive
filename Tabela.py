import ttg
                        #Pistas da cozinha 
# Definindo proposições
                            #Pista 1
x = ttg.Truths(bases=['A'], phrases=['A'], ints=False)
print(x)
print(x.valuation())

                            #Pista 2
x = ttg.Truths(bases=['B','C'], phrases=['(B=C)'], ints=False)
print(x)
print(x.valuation())

                            #Pista 3
x = ttg.Truths(bases=['B','D'], phrases=['(B or D) = (B or D)'], ints=False)
print(x)
print(x.valuation())

                            #Pista 4
x = ttg.Truths(bases=['G','E','F'], phrases=['(G and (E and F))'], ints=False)
print(x)
print(x.valuation())

                            #Pista 5
x = ttg.Truths(bases=['H','I'], phrases=[' (H = I)=(H = I)'], ints=False)
print(x)
print(x.valuation())

                            #Pista 6
x = ttg.Truths(bases=['J'], phrases=['J'], ints=False)
print(x)
print(x.valuation())

                            #Pista 7
x = ttg.Truths(bases=['K'], phrases=['K'], ints=False)
print(x)
print(x.valuation())

                            #Pista 8
x = ttg.Truths(bases=['L','S'], phrases=['(L and S)=>L'], ints=False)
print(x)
print(x.valuation())

                            #Pista 9
x = ttg.Truths(bases=['M'], phrases=['M'], ints=False)
print(x)
print(x.valuation())

                            #Pista 10
x = ttg.Truths(bases=['N'], phrases=['N'], ints=False)
print(x)
print(x.valuation())

                            #Pista 11
x = ttg.Truths(bases=['O'], phrases=['~O'], ints=False)
print(x)
print(x.valuation())

                            #Pista 12
x = ttg.Truths(bases=['T','U'], phrases=['T and U'], ints=False)
print(x)
print(x.valuation())

                            #Pista 13
x = ttg.Truths(bases=['D','C'], phrases=['(D = ~C) and (D and C )'], ints=False)
print(x)
print(x.valuation())

                            #Pista 14 
x = ttg.Truths(bases=['Q','P'], phrases=['(Q and ~(P or Q)) '], ints=False)
print(x)
print(x.valuation())

                            #Pista 15 
x = ttg.Truths(bases=['R'], phrases=['(R and ~R)'], ints=False)
print(x)
print(x.valuation())
