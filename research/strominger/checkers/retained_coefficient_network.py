"""Dimension-independent exact staged coefficient networks over Q(sqrt(3),i).

A coefficient is (a,b,c,d)=a+b sqrt(3)+i(c+d sqrt(3)). Ports and
operator matrices are supplied retained data, not inferred from a shape.
"""
from fractions import Fraction as F

ZERO=(F(0),)*4
ONE=(F(1),F(0),F(0),F(0))


def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def realmul(x,y): return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def mul(x,y):
    ac=realmul(x[:2],y[:2]);bd=realmul(x[2:],y[2:])
    ad=realmul(x[:2],y[2:]);bc=realmul(x[2:],y[:2])
    return (ac[0]-bd[0],ac[1]-bd[1],ad[0]+bc[0],ad[1]+bc[1])
def conj(x): return x[:2]+tuple(-a for a in x[2:])
def rinv(x):
    d=x[0]**2-3*x[1]**2
    if not d: raise ValueError('Zero field element')
    return (x[0]/d,-x[1]/d)
def inv(x):
    n=add(mul(x,conj(x)),ZERO)
    r=rinv(n[:2]);return mul(conj(x),r+(F(0),F(0)))
def encode(x):return list(map(str,x))
def positive(x):
    if x[2:]!=(0,0):return False
    a,b=x[:2]
    if a>=0 and b>=0:return a+b>0
    if a<=0 and b<=0:return False
    return a*a>3*b*b if a>0 else 3*b*b>a*a


def product(A,B):
    """A after B; sparse keys are (target,source)."""
    rows={}
    for (i,j),x in A.items():rows.setdefault(j,[]).append((i,x))
    out={}
    for (j,k),y in B.items():
        for i,x in rows.get(j,[]):out[i,k]=add(out.get((i,k),ZERO),mul(x,y))
    return {k:v for k,v in out.items() if v!=ZERO}


def rank(A,n):
    rows=[[A.get((i,j),ZERO) for j in range(n)] for i in range(n)]
    r=0
    for j in range(n):
        p=next((i for i in range(r,n) if rows[i][j]!=ZERO),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r]
        z=inv(rows[r][j]); rows[r]=[mul(v,z) for v in rows[r]]
        for i in range(n):
            if i==r or rows[i][j]==ZERO:continue
            z=rows[i][j];rows[i]=[add(x,neg(mul(z,y))) for x,y in zip(rows[i],rows[r])]
        r+=1
    return r


def assemble(ports,operators):
    """Each stage maps ports[s] to ports[(s+1)%m]. Preserve every port/edge.

    Matrices use local integer indices and exact four-component coefficients.
    Counts concern this supplied staged realization, not a minimum.
    """
    if len(ports)<1 or len(ports)!=len(operators):raise ValueError('Stage/port mismatch')
    for stage,p in enumerate(ports):
        if len(set(p))!=len(p):raise ValueError('Duplicate port label')
        for (i,j),v in operators[stage].items():
            if not 0<=j<len(p) or not 0<=i<len(ports[(stage+1)%len(ports)]):raise ValueError('Operator endpoint outside stage')
            if len(v)!=4 or v==ZERO:raise ValueError('Expected nonzero four-component coefficient')
    R={(i,i):ONE for i in range(len(ports[0]))}
    for M in operators:R=product(M,R)
    trace=ZERO
    for (i,j),v in R.items():
        if i==j:trace=add(trace,v)
    used=set();count=0;weight_sum=ZERO;all_positive=True
    outgoing=[]
    for M in operators:
        d={}
        for (i,j),v in M.items():d.setdefault(j,[]).append((i,v))
        outgoing.append(d)
    def walk(stage,start,current,weight,history):
        nonlocal count,weight_sum,all_positive
        if stage==len(operators):
            if current==start:
                count+=1;weight_sum=add(weight_sum,weight);all_positive &= positive(weight);used.update(history)
            return
        for target,v in outgoing[stage].get(current,[]):
            walk(stage+1,start,target,mul(v,weight),history+[(stage,target,current)])
    for i in range(len(ports[0])):walk(0,i,i,ONE,[])
    if weight_sum!=trace:raise AssertionError('Cycle sum disagrees with operator trace')
    arrows=[{'stage':s,'source':ports[s][j],'target':ports[(s+1)%len(ports)][i],'weight':encode(v)}
            for s,M in enumerate(operators) for (i,j),v in sorted(M.items())]
    return {'ports':ports,'arrows':arrows,'measures':{'stage_supports':list(map(len,operators)),
        'transfers':len(arrows),'port_nodes':sum(map(len,ports)),
        'return_rank':rank(R,len(ports[0])),'return_idempotent':product(R,R)==R,
        'return_hermitian':{(j,i):conj(v) for (i,j),v in R.items()}==R,
        'closed_cycles':count,'cycle_union_transfers':len(used),'all_transfers_on_cycles':len(used)==len(arrows),
        'positive_cycle_weights':all_positive,'cycle_trace':encode(trace)},
        'return_operator':[{'target':i,'source':j,'weight':encode(v)} for (i,j),v in sorted(R.items())]}


def recover(packet):
    ports=packet['ports'];ops=[{} for _ in ports]
    for row in packet['arrows']:
        s=row['stage'];j=ports[s].index(row['source']);i=ports[(s+1)%len(ports)].index(row['target'])
        if (i,j) in ops[s]:raise ValueError('Duplicate transfer record')
        ops[s][i,j]=tuple(F(x) for x in row['weight'])
    return ports,ops
