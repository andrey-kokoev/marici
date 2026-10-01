"""Exact primitive rectangle->triangle chain map with retained metric residual.

Target-family anchors choose a concrete map; the chain boundary and source
closure constraints determine what complementary cell data must be retained.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from biclique_complex import apply, biclique, dowker, rank


def transpose(a): return [list(row) for row in zip(*a)]
def multiply(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def identity(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def subtract(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def norm(x): return sum(row[0]**2 for row in x)


def inverse(a):
    n=len(a); rows=[list(row)+unit for row,unit in zip(a,identity(n))]
    for col in range(n):
        pivot=next(i for i in range(col,n) if rows[i][col])
        rows[col],rows[pivot]=rows[pivot],rows[col]
        scale=rows[col][col]; rows[col]=[v/scale for v in rows[col]]
        for i in range(n):
            if i!=col:
                scale=rows[i][col]
                rows[i]=[x-scale*y for x,y in zip(rows[i],rows[col])]
    return [row[n:] for row in rows]


def dense(columns,rows):
    return [[column.get(i,F(0)) for column in columns] for i in range(rows)]


ends=[(('s',a),('t',b)) for a,b in product(range(4),repeat=2) if a!=b]
bdims,bdiffs,bcells,_=biclique(ends)
ddims,ddiffs,dcells=dowker(ends,include_cells=True)
bvertices=sorted({v for pair in ends for v in pair},key=repr)
dlabels={d:{face:i for i,face in enumerate(rows)} for d,rows in dcells.items()}
anchor={('t',t):('s',(t+1)%4) for t in range(4)}


def oriented(face):
    if len(set(face))!=len(face): return {}
    ordered=tuple(sorted(face,key=repr))
    order=[ordered.index(v) for v in face]
    sign=(-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
    return {dlabels[len(face)-1][ordered]:F(sign)}


T0=dense([{dlabels[0][(v if v[0]=='s' else anchor[v],)]:F(1)} for v in bvertices],4)
T1=dense([oriented((anchor[t],s)) for s,t in ends],6)
columns=[]
for left,right in bcells[2]:
    u,w=left; v,z=right
    col=oriented((anchor[v],u,w))
    for j,value in oriented((anchor[z],u,w)).items(): col[j]=col.get(j,F(0))-value
    columns.append({j:v for j,v in col.items() if v})
T2=dense(columns,4)
B1=dense(bdiffs[1],8); B2=dense(bdiffs[2],12)
D1=dense(ddiffs[1],4); D2=dense(ddiffs[2],6)
assert multiply(T0,B1)==multiply(D1,T1)
assert multiply(T1,B2)==multiply(D2,T2)
assert rank(columns)==4
# Source has a primitive integral sphere cycle with first coordinate+1.
cycles=[]
for tail in product((-1,1),repeat=5):
    z=[[F(v)] for v in (1,)+tail]
    if not any(row[0] for row in multiply(B2,z)): cycles.append(z)
assert len(cycles)==1
z=cycles[0]; image=multiply(T2,z)
assert norm(z)==6 and norm(image)==4
assert all(abs(row[0])==1 for row in image)
assert not any(row[0] for row in multiply(D2,image))

# Quotient metric on ALL target2-chains and the retained orthogonal residual.
G=inverse(multiply(T2,transpose(T2)))
L=multiply(transpose(T2),G)
P=subtract(identity(6),multiply(L,T2))
assert multiply(T2,L)==identity(4)
assert multiply(P,P)==P and transpose(P)==P
for entries in product(map(F,(-1,0,1)),repeat=6):
    x=[[v] for v in entries]; y=multiply(T2,x)
    lifted=multiply(L,y); residual=multiply(P,x)
    assert [[a[0]+b[0]] for a,b in zip(lifted,residual)]==x
    assert not any(row[0] for row in multiply(T2,residual))
    target_cost=multiply(transpose(y),multiply(G,y))[0][0]
    assert norm(x)==target_cost+norm(residual)

lift=multiply(L,image); residual=multiply(P,z)
quotient_cost=multiply(transpose(image),multiply(G,image))[0][0]
assert not any(row[0] for row in multiply(B2,[[a[0]+b[0]] for a,b in zip(lift,residual)]))
# Closure must be imposed in the retained source, not just after mapping.
assert any(row[0] for row in multiply(B2,lift))
assert norm(residual)>0
assert quotient_cost+norm(residual)==6
# No nonzero residual is both invisible to T2 and a closed source cycle.
augmented=[dict(enumerate(column)) for column in zip(*(T2+B2))]
assert rank(augmented)==6
# Scale the cycle to check exact closed-class returns and their budget.
for value in (F(-2),F(0),F(3,7)):
    scaled=[[value*v[0]] for v in z]
    target=multiply(T2,scaled)
    assert norm(scaled)==6*value**2
    assert norm(target)==4*value**2
    assert not any(row[0] for row in multiply(B2,scaled))
# Audit all3^4 choices of a source anchor in each target neighborhood.
# Target image dimension can vary, but the retained closed-class cost must not.
anchor_ranks=Counter()
for choices in product(*(tuple(a for a in range(4) if a!=t) for t in range(4))):
    anchors={('t',t):('s',a) for t,a in enumerate(choices)}
    cols=[]
    for left,right in bcells[2]:
        u,w=left; v,t=right
        col=oriented((anchors[v],u,w))
        for j,value in oriented((anchors[t],u,w)).items(): col[j]=col.get(j,F(0))-value
        cols.append({j:value for j,value in col.items() if value})
    matrix=dense(cols,4)
    edge_map=dense([oriented((anchors[t],s)) for s,t in ends],6)
    vertex_map=dense([{dlabels[0][(v if v[0]=='s' else anchors[v],)]:F(1)} for v in bvertices],4)
    assert multiply(vertex_map,B1)==multiply(D1,edge_map)
    assert multiply(edge_map,B2)==multiply(D2,matrix)
    assert multiply(matrix,z)==image
    # Nonzero columns have disjoint supports. The unconstrained minimum lift
    # keeps precisely their source coordinates and zeroes the invisible ones.
    supports=[set(c) for c in cols if c]
    assert sum(map(len,supports))==len(set().union(*supports))
    minimal=[row if cols[i] else [F(0)] for i,row in enumerate(z)]
    rest=subtract(z,minimal)
    r=rank(cols); anchor_ranks[r]+=1
    assert multiply(matrix,minimal)==image
    assert norm(minimal)==r and norm(rest)==6-r
    assert norm(minimal)+norm(rest)==6
assert anchor_ranks==Counter({4:30,3:48,2:3})
print(f'All81 anchor choices preserve the same oriented class and closed cost6; map-rank counts={dict(sorted(anchor_ranks.items()))}.')
print('Explicit rectangle->triangle chain map passes both boundary squares and maps the primitive integral class with degree +/-1.')
print(f'T2 rank4; retained kernel dimension2; target quotient Gram={G}.')
print('729 exact source-cell states reconstruct from target cells plus orthogonal residual, preserving total cost.')
print(f'Sphere: source cost6 = target unconstrained quotient cost {quotient_cost} + retained residual cost {norm(residual)}.')
print('Unconstrained minimum lift has nonzero source boundary; closure plus retained residual recovers the exact class cost6.')
print('On the target cycle line the closure-constrained cost equals(3/2)*its unit-triangle norm; off-cycle metric extension is separate.')
