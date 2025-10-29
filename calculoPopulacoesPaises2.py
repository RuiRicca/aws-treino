import sys

paisA=int(sys.argv[1])
taxaA=float(sys.argv[2])
paisB=int(sys.argv[3])
taxaB=float(sys.argv[4])
anos=0
while paisA==paisB:
    print("Países com populações iguais não permitem o funcionamento deste programa.\nPor favor indique os dados de outros países")
    paisA=int(sys.argv[1])
    taxaA=float(sys.argv[2])
    paisB=int(sys.argv[3])
    taxaB=float(sys.argv[4])
if paisA<paisB:
    while paisA<paisB:
        paisA+=paisA*(taxaA/100)
        paisB+=paisB*(taxaB/100)
        anos+=1
    print(f"A população do país A ultrapassará a do país B dentro de {anos} anos.")
else:
    while paisB<paisA:
        paisB+=paisB*(taxaB/100)
        paisA+=paisA*(taxaA/100)
        anos+=1
    print(f"A população do país B ultrapassará a do país A dentro de {anos} anos.")
