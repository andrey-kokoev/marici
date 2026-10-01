"""Free DG path realization on the actual shared-leg assembly.

Leg witnesses compare against declared base legs; independent base-path
witnesses compare each block with the direct reference. No endpoint
identification or factorization of the direct reference is assumed.
"""
from fractions import Fraction as F
from itertools import product
from biclique_complex import rank, add_scaled


def plus(*chains):
    result={}
    for chain in chains: add_scaled(result,chain,F(1))
    return result


def minus(chain): return {p:-c for p,c in chain.items()}
def word(*names): return {tuple(names):F(1)}


def build(roots):
    arrows={}; differentials={}
    def arrow(name,s,t,degree=0,boundary=None):
        arrows[name]=(s,t,degree); differentials[name]=boundary or {}
    arrow('d','A','B')
    for tag,size,mid in (('a',11,'U'),('s',4,'V')):
        r,c=roots[tag]
        for i in range(size): arrow(f'{tag}x{i}','A',mid)
        for j in range(size): arrow(f'{tag}y{j}',mid,'B')
        for i in range(size):
            if i!=r: arrow(f'{tag}h{i}','A',mid,1,plus(word(f'{tag}x{i}'),minus(word(f'{tag}x{r}'))))
        for j in range(size):
            if j!=c: arrow(f'{tag}k{j}',mid,'B',1,plus(word(f'{tag}y{j}'),minus(word(f'{tag}y{c}'))))
        arrow(f'{tag}base','A','B',1,plus(word(f'{tag}x{r}',f'{tag}y{c}'),minus(word('d'))))

    def degree(path): return sum(arrows[a][2] for a in path)
    def signature(path):
        assert path
        assert all(arrows[a][1]==arrows[b][0] for a,b in zip(path,path[1:]))
        return arrows[path[0]][0],arrows[path[-1]][1],degree(path)
    def delta(chain):
        result={}
        for path,coefficient in chain.items():
            signature(path)
            for i,a in enumerate(path):
                sign=(-1)**degree(path[i+1:])  # chronological path order
                for replacement,c in differentials[a].items():
                    term=path[:i]+replacement+path[i+1:]
                    assert signature(term)==(arrows[path[0]][0],arrows[path[-1]][1],degree(path)-1)
                    add_scaled(result,{term:c},coefficient*sign)
        return result
    paths=[]
    def walk(at,path=()):
        if at=='B': paths.append(path); return
        for a,(s,t,_) in arrows.items():
            if s==at: walk(t,path+(a,))
    walk('A')
    bases={k:[p for p in paths if degree(p)==k] for k in range(4)}
    assert list(map(len,bases.values()))==[138,246,109,0]
    indexes={k:{p:i for i,p in enumerate(ps)} for k,ps in bases.items()}
    matrices={k:[{indexes[k-1][p]:v for p,v in delta(word(*path)).items()} for path in bases[k]] for k in (1,2,3)}
    assert rank(matrices[1])==137 and rank(matrices[2])==109
    assert all(not delta(delta(word(*path))) for path in paths)
    rectangles=[]
    def routes(tag,i,j):
        r,c=roots[tag]
        base=word(f'{tag}base')
        first=plus(base,word(f'{tag}x{i}',f'{tag}k{j}') if j!=c else {},
                   word(f'{tag}h{i}',f'{tag}y{c}') if i!=r else {})
        second=plus(base,word(f'{tag}h{i}',f'{tag}y{j}') if i!=r else {},
                    word(f'{tag}x{r}',f'{tag}k{j}') if j!=c else {})
        filler=word(f'{tag}h{i}',f'{tag}k{j}') if i!=r and j!=c else {}
        boundary=plus(word(f'{tag}x{i}',f'{tag}y{j}'),minus(word('d')))
        assert delta(first)==delta(second)==boundary
        assert delta(filler)==plus(second,minus(first))
        return first,second,filler
    for tag,size in (('a',11),('s',4)):
        r,c=roots[tag]
        for i,j in product(range(size),repeat=2):
            first,second,filler=routes(tag,i,j)
            if not filler: continue
            rectangle=plus(first,minus(routes(tag,i,c)[0]),minus(routes(tag,r,j)[0]),routes(tag,r,c)[0])
            mixed_boundary=plus(word(f'{tag}x{i}',f'{tag}y{j}'),minus(word(f'{tag}x{i}',f'{tag}y{c}')),
                                minus(word(f'{tag}x{r}',f'{tag}y{j}')),word(f'{tag}x{r}',f'{tag}y{c}'))
            assert delta(rectangle)==mixed_boundary and mixed_boundary
            rectangles.append((tag,i,j,filler,rectangle))
    assert len(rectangles)==109
    return arrows,delta,bases,rectangles,routes


Z=((F(0),F(0)),(F(0),F(0)))
I=((F(1),F(0)),(F(0),F(1)))
H=((F(0),F(1)),(F(0),F(0)))
K=((F(0),F(0)),(F(1),F(0)))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(c,a): return tuple(tuple(c*x for x in row) for row in a)
def mul(a,b): return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)),F(0)) for j in range(2)) for i in range(2))

# The direct reference is independent of either base-path product.
values={'d':scale(2,I)}
for tag,size in (('a',11),('s',4)):
    for i in range(size): values[f'{tag}x{i}']=add(I,scale(F(i,3),H))
    for j in range(size): values[f'{tag}y{j}']=add(I,scale(F(j,5),K))


def evaluate(chain,assigned):
    out=Z
    for path,c in chain.items():
        value=I
        for a in path: value=mul(assigned[a],value)
        out=add(out,scale(c,value))
    return out


for roots in ({'a':(0,0),'s':(0,0)},{'a':(3,7),'s':(2,1)}):
    arrows,delta,bases,rectangles,routes=build(roots)
    assigned=dict(values)
    # A witness's response is the evaluated difference of its two maps.
    for a,(_,_,degree) in arrows.items():
        if degree==1: assigned[a]=evaluate(delta(word(a)),values)
    total=Z
    for tag,size in (('a',11),('s',4)):
        for i,j in product(range(size),repeat=2):
            first,second,_=routes(tag,i,j)
            expected=add(mul(values[f'{tag}y{j}'],values[f'{tag}x{i}']),scale(-1,values['d']))
            assert evaluate(first,assigned)==evaluate(second,assigned)==expected
            total=add(total,scale(F(1,137),expected))
    for tag,i,j,filler,rectangle in rectangles:
        r,c=roots[tag]
        dx=add(values[f'{tag}x{i}'],scale(-1,values[f'{tag}x{r}']))
        dy=add(values[f'{tag}y{j}'],scale(-1,values[f'{tag}y{c}']))
        assert evaluate(filler,assigned)==evaluate(rectangle,assigned)==mul(dy,dx)
        assert evaluate(delta(filler),assigned)==Z
    assert any(evaluate(filler,assigned)!=Z for _,_,_,filler,_ in rectangles)
    if roots['a']==(0,0):
        baseline_total=total
        # Change the base from(0,0) to(1,1), then back, using the same
        # first-route convention. New h_0=-old h_1 and new k_0=-old k_1.
        for tag in ('a','s'):
            first,_,filler=routes(tag,1,1)
            returned=plus(first,minus(word(f'{tag}x0',f'{tag}k1')),
                          minus(word(f'{tag}h1',f'{tag}y1')))
            base=word(f'{tag}base')
            assert plus(returned,minus(base))==minus(delta(filler))
            assert delta(returned)==delta(base)
            assert evaluate(returned,assigned)==evaluate(base,assigned)
            assert evaluate(filler,assigned)!=Z
    else: assert total==baseline_total
print('Actual shared-leg DG model:31 degree0 and28 degree1 generators; Hom(A,B) dimensions138,246,109,0.')
print('All137 path/reference comparisons have two exact witness routes;109 degree2 products fill their discrepancies.')
print('Both routes recover the finite matrix residual; each higher product reads the same mixed rectangle response.')
print('An independent direct reference is retained via two base-path witnesses; changing base legs preserves the total response.')
print('Base-leg change and return preserves the reference response; its witness-history shift is filled by the same rectangle product.')
print('Degree2 boundary is injective and there are no degree3 paths: this original network supports squares, but no nontrivial next cube.')
print('Free leg/base-path witnesses and contextual roots are declared choices; no metric, gauge action or new network is inferred.')
