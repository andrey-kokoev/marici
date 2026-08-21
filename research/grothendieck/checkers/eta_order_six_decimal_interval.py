"""Directed-rounding enclosure of eta derivatives through order six."""
import json
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from pathlib import Path

PREC, N, M, J = 80, 10_000, 15, 6
down = Context(prec=PREC, rounding=ROUND_FLOOR)
up = Context(prec=PREC, rounding=ROUND_CEILING)
near = Context(prec=PREC)

def add(x,y): return down.add(x[0],y[0]), up.add(x[1],y[1])
def neg(x): return x[1].copy_negate(), x[0].copy_negate()
def sub(x,y): return add(x,neg(y))
def divp(x,d): return down.divide(x[0],d), up.divide(x[1],d)
def logbox(n):
    with localcontext(near) as ctx:
        v=ctx.ln(Decimal(n)); return ctx.next_minus(v),ctx.next_plus(v)
def power(x,j):
    if j==0:return Decimal(1),Decimal(1)
    return down.power(x[0],j),up.power(x[1],j)
def term(n,j): return divp(power(logbox(n),j),Decimal(n))

def eta(j):
    total=(Decimal(0),Decimal(0))
    for n in range(1,N):
        x=term(n,j);total=add(total,x if n%2 else neg(x))
    row=[term(n,j) for n in range(N,N+M+1)]
    transformed=(Decimal(0),Decimal(0));two=Decimal(2)
    for _ in range(M):
        transformed=add(transformed,divp(row[0],two))
        row=[sub(row[i],row[i+1]) for i in range(len(row)-1)]
        two*=2
    total=sub(total,transformed) # N even
    total=add(total,(Decimal('-2e-52'),Decimal('2e-52')))
    return neg(total) if j%2 else total

intervals=[eta(j) for j in range(J+1)]
assert all(lo<hi for lo,hi in intervals)
assert max(hi-lo for lo,hi in intervals)<Decimal('5e-52')
result={
    'precision_decimal_digits':PREC,'tail_start':N,'euler_transforms':M,
    'eta_derivative_intervals':[[str(a),str(b)] for a,b in intervals],
    'maximum_interval_width':str(max(b-a for a,b in intervals)),
    'eta_jet_through_order_six_certified':True,'zero_locations_used':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'eta-order-six-decimal-interval.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
