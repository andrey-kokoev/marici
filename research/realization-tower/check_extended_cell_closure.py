"""Exact oriented cellular chain audit of the four-step FCC interval."""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json


def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def rank(m):
    a=[[F(x) for x in row] for row in m];r=0
    for col in range(len(a[0]) if a else 0):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];scale=a[r][col];a[r]=[x/scale for x in a[r]]
        for i in range(r+1,len(a)):
            if a[i][col]:
                scale=a[i][col];a[i]=[x-scale*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def main():
    home=Path(__file__).parent
    receipt=json.loads((home/'results/extended-probe-diagonal-v1.json').read_text())
    points={tuple(p) for p in receipt['extended'][1]['shortest_walk_union']}
    cells=[]
    for c in product(range(-1,5),range(-3,3),range(-3,3)):
        tet=tuple(sorted(p for d in product((0,1),repeat=3) if sum(p:=tuple(x+y for x,y in zip(c,d)))%2==0))
        if set(tet)<=points:cells.append(tet)
        if sum(c)%2:
            octa=tuple(sorted(tuple(c[i]+(s if i==axis else 0) for i in range(3)) for axis in range(3) for s in (-1,1)))
            if set(octa)<=points:cells.append(octa)
    assert Counter(map(len,cells))=={4:8,6:6}
    boundaries=[]
    for cell in cells:
        facets={}
        for face in combinations(cell,3):
            a,b,c=face;n=cross(sub(b,a),sub(c,a));signs=[dot(n,sub(p,a)) for p in cell if p not in face]
            if all(x>0 for x in signs):facets[face]=-1
            elif all(x<0 for x in signs):facets[face]=1
        assert len(facets)==(4 if len(cell)==4 else 8)
        boundaries.append(facets)
    faces=sorted({face for b in boundaries for face in b})
    edges=sorted({edge for face in faces for edge in combinations(face,2)})
    verts=sorted(points);vi={p:i for i,p in enumerate(verts)};ei={e:i for i,e in enumerate(edges)};fi={f:i for i,f in enumerate(faces)}
    d1=[[0]*len(edges) for _ in verts];d2=[[0]*len(faces) for _ in edges];d3=[[0]*len(cells) for _ in faces]
    for j,(a,b) in enumerate(edges):d1[vi[a]][j]=-1;d1[vi[b]][j]=1
    for j,(a,b,c) in enumerate(faces):
        for edge,sign in [((a,b),1),((b,c),1),((a,c),-1)]:d2[ei[edge]][j]=sign
    for j,b in enumerate(boundaries):
        for f,sign in b.items():d3[fi[f]][j]=sign
    for i in range(len(verts)):
        for j in range(len(faces)):assert sum(d1[i][k]*d2[k][j] for k in range(len(edges)))==0
    for i in range(len(edges)):
        for j in range(len(cells)):assert sum(d2[i][k]*d3[k][j] for k in range(len(faces)))==0
    counts=Counter(f for b in boundaries for f in b);assert max(counts.values())==2
    outer=[]
    for f in faces:
        coefficient=sum(d3[fi[f]])
        assert abs(coefficient)==(1 if counts[f]==1 else 0)
        if coefficient:outer.append(f)
    be=sorted({e for f in outer for e in combinations(f,2)});bv=sorted({p for f in outer for p in f})
    r1,r2,r3=rank(d1),rank(d2),rank(d3)
    betti=[len(verts)-r1,len(edges)-r1-r2,len(faces)-r2-r3,len(cells)-r3]
    bd1=[[d1[vi[v]][ei[e]] for e in be] for v in bv];bd2=[[d2[ei[e]][fi[f]] for f in outer] for e in be]
    br1,br2=rank(bd1),rank(bd2);boundary_betti=[len(bv)-br1,len(be)-br1-br2,len(outer)-br2]
    assert betti==[1,0,0,0] and boundary_betti==[1,0,1]
    report={'status':'pass','cell_counts':[len(verts),len(edges),len(faces),len(cells)],
            'boundary_counts':[len(bv),len(be),len(outer)],'chain_ranks':[r1,r2,r3],
            'rational_betti':betti,'boundary_rational_betti':boundary_betti,
            'checks':['d1*d2=0','d2*d3=0','internal faces cancel with opposite orientations','face incidence at most two'],
            'scope':'Ordinary cellular incidence coherence; not a native WG phase/metric/reader filler certificate.'}
    (home/'results/extended-cell-closure-v1.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':main()
