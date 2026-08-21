"""One-pass directed-rounding eta jet through derivative order eight."""
import json
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING,localcontext
from pathlib import Path

PREC,N,M,J=80,100_000,8,8
down=Context(prec=PREC,rounding=ROUND_FLOOR);up=Context(prec=PREC,rounding=ROUND_CEILING);near=Context(prec=PREC)
def add(x,y):return down.add(x[0],y[0]),up.add(x[1],y[1])
def neg(x):return x[1].copy_negate(),x[0].copy_negate()
def sub(x,y):return add(x,neg(y))
def divp(x,d):return down.divide(x[0],d),up.divide(x[1],d)
def logbox(n):
    with localcontext(near) as c:
        v=c.ln(Decimal(n));return c.next_minus(v),c.next_plus(v)
def powers_at(n):
    l=logbox(n);return [(Decimal(1),Decimal(1))]+[(down.power(l[0],j),up.power(l[1],j)) for j in range(1,J+1)]

totals=[(Decimal(0),Decimal(0)) for _ in range(J+1)]
for n in range(1,N):
    for j,p in enumerate(powers_at(n)):
        x=divp(p,Decimal(n));totals[j]=add(totals[j],x if n%2 else neg(x))

for j in range(J+1):
    row=[]
    for n in range(N,N+M+1):row.append(divp(powers_at(n)[j],Decimal(n)))
    transformed=(Decimal(0),Decimal(0));two=Decimal(2)
    for _ in range(M):
        transformed=add(transformed,divp(row[0],two))
        row=[sub(row[i],row[i+1]) for i in range(len(row)-1)];two*=2
    totals[j]=sub(totals[j],transformed) # N even
    totals[j]=add(totals[j],(Decimal('-4e-36'),Decimal('4e-36')))
    if j%2:totals[j]=neg(totals[j])

assert all(a<b for a,b in totals)
assert max(b-a for a,b in totals)<Decimal('9e-36')
result={'precision_decimal_digits':PREC,'tail_start':N,'euler_transforms':M,
        'eta_derivative_intervals':[[str(a),str(b)] for a,b in totals],
        'maximum_interval_width':str(max(b-a for a,b in totals)),
        'eta_jet_through_order_eight_certified':True,'zero_locations_used':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'eta-order-eight-decimal-interval.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
