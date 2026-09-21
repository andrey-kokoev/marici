"""Identify degree-two diamond Tor with the terminal marked-path kernel.

Compare the compressed two-feature fixture with independent chamber features,
and separate ambient-memory from source-generated module homology.
"""
from pathlib import Path
from itertools import product
import sympy as s
import json

def analyze(d,features):
    vertices=(2,4,6,12);height={2:0,4:1,6:1,12:2}
    words=lambda n:[w for r in range(n+1) for w in product(range(d),repeat=r)]
    a,b,c=features;add=lambda x,y:tuple(u+v for u,v in zip(x,y))
    raw=[(2,4,a),(4,12,add(b,c)),(2,6,add(a,b)),(6,12,c)]
    edges=[(x,y,m,g) for x,y,g in raw for m in (0,1)]
    emit=lambda ei:{():s.Integer(1)} if not edges[ei][2] else {(j,):v for j,v in enumerate(edges[ei][3]) if v!=0}
    B0=[(x,k,u,v) for x in vertices for k in range(3) for u in words(k) for v in words(2-k)]
    B1=[(ei,k,u,v) for ei in range(8) for k in range(2) for u in words(k) for v in words(1-k)]
    i0={v:i for i,v in enumerate(B0)};i1={v:i for i,v in enumerate(B1)}
    out=words(2);oi={w:i for i,w in enumerate(out)}
    D=s.zeros(len(B0),len(B1));mu=s.zeros(len(out),len(B0))
    for j,(ei,k,u,v) in enumerate(B1):
        x,y,_,_=edges[ei]
        for w,z in emit(ei).items():
            D[i0[y,k+1,u+w,v],j]+=z;D[i0[x,k,u,w+v],j]-=z
    for j,(_,_,u,v) in enumerate(B0):mu[oi[u+v],j]=1
    terminal=s.zeros(len(out),8);derivative=s.zeros(len(B1),8)
    j=0
    for first,second in ((0,2),(4,6)):
        for m,n in product((0,1),repeat=2):
            e,f=first+m,second+n
            for u,x in emit(e).items():
                derivative[i1[f,1,u,()],j]+=x
                for v,y in emit(f).items():terminal[oi[u+v],j]+=x*y
            for v,y in emit(f).items():derivative[i1[e,0,(),v],j]+=y
            j+=1
    endpoints=s.zeros(len(B0),len(out))
    for j,w in enumerate(out):endpoints[i0[12,2,w,()],j]=1;endpoints[i0[2,0,(),w],j]=-1
    clean=lambda m:m.applyfunc(s.simplify)
    assert clean(D*derivative-endpoints*terminal)==s.zeros(len(B0),8)
    assert derivative.rank()==8
    kernels=terminal.nullspace();K=s.Matrix.hstack(*kernels)
    assert clean(D*derivative*K)==s.zeros(len(B0),len(kernels))
    rank=D.rank()
    assert (derivative*K).rank()==len(B1)-rank
    grades=[]
    for r in range(3):
        rows=[i for i,(_,_,u,v) in enumerate(B0) if len(u)+len(v)==r]
        cols=[i for i,(ei,_,u,v) in enumerate(B1) if len(u)+len(v)+edges[ei][2]==r]
        rankr=D.extract(rows,cols).rank()
        grades.append({'record_degree':r,'C_minus_one':len(cols),'C_zero':len(rows),
                       'H_minus_one':len(cols)-rankr,'H_zero':len(rows)-rankr})
    if d==2:
        extra=s.Matrix([0,-s.I,-1,0,0,1+s.I,0,0])
        assert clean(terminal*extra)==s.zeros(len(out),1)
    # Actual source-generated prefix/suffix images, NOT arbitrary memories.
    one={():s.Integer(1)}
    terminal_basis=[{w:v[i] for i,w in enumerate(out) if v[i]!=0} for v in terminal.columnspace()]
    M={2:[one],4:[emit(0),emit(1)],6:[emit(4),emit(5)],12:terminal_basis}
    N={12:[one],4:[emit(2),emit(3)],6:[emit(6),emit(7)],2:terminal_basis}
    def inclusion(degree):
        cols=[]
        if degree==0:
            for x in vertices:
                for u in M[x]:
                    for v in N[x]:
                        z=s.zeros(len(B0),1)
                        for uw,uc in u.items():
                            for vw,vc in v.items():z[i0[x,height[x],uw,vw]]=uc*vc
                        cols.append(z)
        else:
            for ei,(x,y,_,_) in enumerate(edges):
                for u in M[x]:
                    for v in N[y]:
                        z=s.zeros(len(B1),1)
                        for uw,uc in u.items():
                            for vw,vc in v.items():z[i1[ei,height[x],uw,vw]]=uc*vc
                        cols.append(z)
        return s.Matrix.hstack(*cols)
    inc0,inc1=inclusion(0),inclusion(1)
    pivots=list(inc0.T.rref()[1]);cols=list(range(inc0.cols))
    left=inc0.extract(pivots,cols).inv()
    small=clean(left*(D*inc1).extract(pivots,list(range(inc1.cols))))
    assert clean(inc0*small-D*inc1)==s.zeros(len(B0),inc1.cols)
    smallrank=small.rank()
    source_h0=inc0.cols-smallrank
    assert source_h0==terminal.rank()==(mu*inc0).rank()
    assert inc1.cols-smallrank==len(kernels)
    return {'feature_dimension':d,'terminal_marked_rank':terminal.rank(),
            'ambient':{'C_minus_one':len(B1),'C_zero':len(B0),'H_minus_one':len(B1)-rank,'H_zero':len(B0)-rank},
            'retained_degree_split':grades,'path_kernel_derivative_equals_entire_H_minus_one':True,
            'source_generated_modules':{'C_minus_one':inc1.cols,'C_zero':inc0.cols,
                                        'H_minus_one':inc1.cols-smallrank,'H_zero':source_h0},
            'interpretation':'Extra two-coordinate chamber relation' if d==2 else 'Three independent chamber features'}

results=[analyze(2,((1,0),(0,1),(1,s.I))),
         analyze(3,((1,0,0),(0,1,0),(0,0,1)))]
result={'schema':'marici.grothendieck.bar-homology-prior-clues.v1','passed':True,'fixtures':results,
        'scope':'Exact identification for the two-prime source and these feature models. Not an identification of arbitrary ambient bar classes with a Green radical.'}
p=Path(__file__).resolve().parents[1]/'results/bar-homology-prior-clues.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
