import sys

paisA=sys.argv[1]
paisB=sys.argv[2]
anos=0
while paisA<paisB:
    paisA+=paisA*0.03
    paisB+=paisB*0.015
    anos+=1
print(f"A população do país A ultrapassará a do país B dentro de {anos} anos.")
