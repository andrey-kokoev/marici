"""Countermodels for selection of the seed exchange kernel, exact rationals.
Same event law, ambient dimension, labels and initial state. No physical fit.
"""
from fractions import Fraction as F
from check_natural_tower_return import PACKETS
from check_triangle_half_phase import mm, transpose

labels=tuple(p[0] for p in PACKETS); index={label:i for i,label in enumerate(labels)}
carrier=7; n=6; dim=carrier+n
I=tuple(tuple(F(i==j) for j in range(dim)) for i in range(dim))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c): return tuple(tuple(c*x for x in row) for row in a)
def mv(a,x): return tuple(sum(v*w for v,w in zip(row,x)) for row in a)
def sub(a,b): return add(a,scale(b,-1))
Z=scale(I,0)
words=(('AD','DB','BC','CA'),('AD','DB','BA'),('AB','BC','CA'),('AB','BA'))
signs=(1,-1,-1,1)
initial=tuple(F(i==carrier+index['AB']) for i in range(dim))

results=[]
for a,b in ((F(0),F(1)),(F(3,5),F(4,5))):
    # u_i=a*e_shared+b*e_i. Both families have six independent features:
    # the six unique coordinates have nonzero coefficient b.
    U=tuple((a,)+tuple(b*F(i==j) for j in range(n)) for i in range(n))
    assert a*a+b*b==1 and b!=0
    G=mm(U,transpose(U))
    assert all(G[i][j]==(1 if i==j else a*a) for i in range(n) for j in range(n))
    H={}
    for label,i in index.items():
        u=U[i]; matrix=[list(row) for row in I]
        for j in range(carrier):
            for k in range(carrier): matrix[j][k]-=u[j]*u[k]
            matrix[j][carrier+i]=u[j]
            matrix[carrier+i][j]=u[j]
        matrix[carrier+i][carrier+i]=F(0)
        event=tuple(tuple(row) for row in matrix)
        assert mm(event,event)==I and mm(transpose(event),event)==I
        H[label]=event
    def execute(word):
        out=I
        for label in word: out=mm(H[label],out)
        return out
    rectangle=Z
    outputs=[]
    for word,sign in zip(words,signs):
        action=execute(word); out=mv(action,initial);outputs.append(out)
        assert sum(v*v for v in out)==1
        assert mv(execute(tuple(reversed(word))),out)==initial
        rectangle=add(rectangle,scale(action,sign))
    X0=execute(('AB',)); X1=execute(('AD','DB'))
    Y0=execute(('BA',)); Y1=execute(('BC','CA'))
    assert rectangle==mm(sub(Y1,Y0),sub(X1,X0))
    response=mv(rectangle,initial)
    # Actual seed automorphism swaps AB/BA, BC/AD, CA/DB. Transport both
    # carrier-feature coordinates and labelled records; shared coordinate fixed.
    vertex_swap=dict(zip('ABCD','BADC'))
    ends_to_label={(s,t):label for label,s,t in PACKETS}
    ep=tuple(index[ends_to_label[(vertex_swap[s],vertex_swap[t])]] for _,s,t in PACKETS)
    p=(0,)+tuple(1+j for j in ep)+tuple(carrier+j for j in ep)
    T=tuple(tuple(F(i==p[j]) for j in range(dim)) for i in range(dim))
    for label,i in index.items():
        assert mm(T,H[label])==mm(H[labels[ep[i]]],T)
    results.append((rectangle,response))
    print('Overlap',a*a,'mixed operator zero?',rectangle==Z,
          'same prepared-state mixed response zero?',not any(response))
assert results[0][0]==Z and not any(results[0][1])
assert results[1][0]!=Z and any(results[1][1])
print('PASS: both kernels are unit, full feature-rank and seed-equivariant; all events preserve budget and invert exactly.')
print('RESULT: structural incidence, retained records and reversible exchange do not select a nonzero seam response.')
print('Scope: countermodels to kernel selection, not a physical model or calibrated measurement.')
