"""Exact finite Gaussian boundary responses; no third-party dependencies.
Run: python research/strominger/checkers/check_fcc_gaussian_boundary.py
K = sum_cell (I_vertices/14 + L_edges/4), m^2=kappa=1.
An infinite FCC vertex meets 14 cells, an edge 4 cells. Thus the assembled
infinite action is I+Delta. On a finite region this is a specified free-boundary
cell-additive restriction, NOT the induced graph with one full mass per vertex.
"""
from fractions import Fraction as Q
from itertools import product, combinations, permutations
from collections import Counter
from math import lcm
from pathlib import Path
import hashlib
import json
import time

BASE = Path(__file__).resolve().parents[1]
OUT = BASE/'results/fcc-gaussian-boundary-direct'
NN = tuple(v for v in product((-1,0,1), repeat=3) if sum(x*x for x in v)==2)
add = lambda a,b: tuple(x+y for x,y in zip(a,b))
sub = lambda a,b: tuple(x-y for x,y in zip(a,b))
distance = lambda a,b: sum((x-y)**2 for x,y in zip(a,b))
TTRIPLES = tuple(v for v in combinations(NN,3) if all(distance(a,b)==2 for a,b in combinations(v,2)))

def inside(p,n,kind):
    x,y,z=p
    if kind=='T': return min(x+y-z,x+z-y,y+z-x)>=0 and x+y+z<=2*n
    return sum(abs(x-n) for x in p)<=n

def mesh(n,kind):
    lo,hi=(-1,2*n+1)
    pts={p for p in product(range(lo,hi+1),repeat=3) if sum(p)%2==0 and inside(p,n,kind)}
    cells=set()
    for p in pts:
        for triple in TTRIPLES:
            c=tuple(sorted((p,*(add(p,v) for v in triple))))
            if set(c)<=pts: cells.add(c)
    for c in product(range(lo,hi+1),repeat=3):
        if sum(c)%2==0: continue
        verts=tuple(sorted(add(c,tuple(s if j==i else 0 for j in range(3))) for i in range(3) for s in (-1,1)))
        if set(verts)<=pts: cells.add(verts)
    assert set().union(*map(set,cells))==pts
    return tuple(sorted(cells))

def vertices(cells): return sorted(set().union(*map(set,cells)))

def boundary(cells):
    faces=Counter()
    for c in cells:
        for f in combinations(c,3):
            if all(distance(a,b)==2 for a,b in combinations(f,2)): faces[f]+=1
    assert max(faces.values())<=2
    return sorted({p for f,count in faces.items() if count==1 for p in f})

def action(cells,pts):
    index={p:i for i,p in enumerate(pts)}
    a=[[0]*len(pts) for _ in pts]
    for c in cells:
        for p in c: a[index[p]][index[p]]+=2
        for p,q in combinations(c,2):
            if distance(p,q)!=2: continue
            i,j=index[p],index[q]
            a[i][i]+=7; a[j][j]+=7; a[i][j]-=7; a[j][i]-=7
    return [[Q(x,28) for x in row] for row in a]

def reduce_kernel(a,keep):
    """Partial symmetric Bareiss elimination, exact rational input/output.
    Returns Schur kernel, determinant of eliminated block, eliminated count.
    Strict SPD follows from positive mass in every incident cell.
    """
    total=len(a); keep=list(keep); eliminated=[j for j in range(total) if j not in set(keep)]
    order=eliminated+keep; count=len(eliminated)
    if not count: return [[a[i][j] for j in keep] for i in keep],Q(1),0
    denominator=lcm(*(x.denominator for row in a for x in row))
    b=[[int(a[i][j]*denominator) for j in order] for i in order]
    previous=1
    for k in range(count):
        pivot=b[k][k]; assert pivot>0
        for i in range(k+1,total):
            left=b[i][k]
            for j in range(i,total):
                num=pivot*b[i][j]-left*b[k][j]
                value,remainder=divmod(num,previous); assert remainder==0
                b[i][j]=value; b[j][i]=value
        previous=pivot
    # previous is det of eliminated block of the integer-scaled matrix.
    schur=[[Q(b[i][j],previous*denominator) for j in range(count,total)] for i in range(count,total)]
    return schur,Q(previous,denominator**count),count

def encode(s):
    values=sorted({x for row in s for x in row}); lookup={x:i for i,x in enumerate(values)}
    return {'values':[str(v) for v in values], 'matrix':[[lookup[x] for x in row] for row in s]}

def stats(s,det,count):
    b=len(s); values={x for row in s for x in row}
    return {'boundaryDOF':b,'symmetricSlots':b*(b+1)//2,
            'nonzeroUpperEntries':sum(s[i][j]!=0 for i in range(b) for j in range(i,b)),
            'distinctRationalEntries':len(values),
            'dictionaryBitCost':sum(abs(x.numerator).bit_length()+x.denominator.bit_length() for x in values),
            'maxEntryBitCost':max(abs(x.numerator).bit_length()+x.denominator.bit_length() for x in values),
            'indexBitsUpperBound':b*(b+1)//2*max(1,(len(values)-1).bit_length()),
            'normalization':{'twoPiPower':count,'inverseSquareRootDeterminant':str(det)},
            'determinantBitCost':abs(det.numerator).bit_length()+det.denominator.bit_length()}

def covariance(pts,s,n,kind):
    """T: all 24 vertex permutations (including improper isometries).
    O: all 48 signed coordinate permutations. No A4-specific effect claimed.
    """
    index={p:i for i,p in enumerate(pts)}; checked=0
    transformations=[]
    if kind=='T':
        for perm in permutations(range(4)):
            def transform(p,perm=perm):
                x,y,z=p
                w=(2*n-x-y-z,x+y-z,x+z-y,y+z-x)
                ww=[w[j] for j in perm]
                return ((ww[1]+ww[2])//2,(ww[1]+ww[3])//2,(ww[2]+ww[3])//2)
            transformations.append(transform)
    else:
        for perm in permutations(range(3)):
            for signs in product((-1,1),repeat=3):
                transformations.append(lambda p,perm=perm,signs=signs:tuple(n+signs[j]*(p[perm[j]]-n) for j in range(3)))
    for transform in transformations:
        pp=[index[transform(p)] for p in pts]
        assert all(s[i][j]==s[pp[i]][pp[j]] for i in range(len(pts)) for j in range(i,len(pts)))
        checked+=1
    return checked

def glue_test(n,c1,c2):
    pts=vertices(c1+c2); outer=boundary(c1+c2); interface=set(vertices(c1))&set(vertices(c2))
    direct,dd,nd=reduce_kernel(action(c1+c2,pts),[pts.index(p) for p in outer])
    ports=sorted(set(outer)|interface); index={p:i for i,p in enumerate(ports)}
    sewn=[[Q(0) for _ in ports] for _ in ports]; determinant=Q(1); eliminated=0
    for cells in (c1,c2):
        local=vertices(cells); retained=[p for p in local if p in index]
        s,d,e=reduce_kernel(action(cells,local),[local.index(p) for p in retained])
        determinant*=d; eliminated+=e
        for i,p in enumerate(retained):
            for j,q in enumerate(retained): sewn[index[p]][index[q]]+=s[i][j]
    staged,di,ni=reduce_kernel(sewn,[index[p] for p in outer])
    assert staged==direct and determinant*di==dd and eliminated+ni==nd
    # Deliberately count shared interface action twice: result must differ.
    bad=[row[:] for row in sewn]
    for p in interface: bad[index[p]][index[p]]+=1
    bad_s,bad_d,_=reduce_kernel(bad,[index[p] for p in outer])
    assert bad_s!=direct or determinant*bad_d!=dd
    return {'scale':n,'interfaceVertices':len(interface),'interfaceIntegrated':ni,
            'externalBoundary':outer,'kernel':encode(direct),
            'normalization':stats(direct,dd,nd)['normalization'],
            'kernelRouteEquality':True,'normalizationRouteEquality':True,
            'doubleCountedInterfaceRejected':True,
            'scope':'same fine-scale action, independently reduced pieces versus assembled region; not a coarse-response refinement map'}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    results=[]; meshes={}
    for kind in ('T','O'):
        for level in range(4):
            start=time.monotonic(); n=2**level; cells=mesh(n,kind); meshes[kind,n]=cells
            counts=Counter(len(c) for c in cells)
            t,o=(1,0) if kind=='T' else (0,1)
            for _ in range(level):t,o=4*t+8*o,t+6*o
            assert counts[4]==t and counts[6]==o
            pts=vertices(cells); ports=boundary(cells); a=action(cells,pts)
            s,d,e=reduce_kernel(a,[pts.index(p) for p in ports])
            symmetries=covariance(ports,s,n,kind)
            # Fixed old-vertex response is a different port type from full boundary.
            old=[tuple(n*x for x in p) for p in vertices(mesh(1,kind))]
            # Eliminate from the original integer-scaled action, not from a
            # dense rational Schur matrix: the latter introduces an enormous
            # avoidable common-denominator power in fraction-free arithmetic.
            old_s,total_d,total_e=reduce_kernel(a,[pts.index(p) for p in old])
            old_d,old_e=total_d/d,total_e-e
            base_a=action(mesh(1,kind),vertices(mesh(1,kind)))
            record={'grain':kind,'level':level,'scale':n,'cells':{'T':t,'O':o},'vertices':len(pts),
                    **stats(s,d,e),'symmetryMapsChecked':symmetries,
                    'fullBoundary':{'vertices':ports,'kernel':encode(s)},
                    'inheritedPorts':{'vertices':old,'kernel':encode(old_s),
                                      'normalization':{'twoPiPower':e+old_e,'inverseSquareRootDeterminant':str(d*old_d)},
                                      'equalsOriginalAtUnchangedCouplings':old_s==base_a,
                                      'sameFullAmplitudeAtUnchangedCouplings':old_s==base_a and d*old_d==1 and e+old_e==0}}
            path=OUT/f'{kind}-level-{level}.json';path.write_text(json.dumps(record,indent=2)+'\n')
            results.append({k:v for k,v in record.items() if k not in ('fullBoundary','inheritedPorts') }|
                           {'inheritedPorts':{k:v for k,v in record['inheritedPorts'].items() if k not in ('vertices','kernel')},
                            'artifact':str(path.relative_to(BASE.parents[1]))})
            print(kind,level,'vertices',len(pts),'boundary',len(ports),'unique',record['distinctRationalEntries'],
                  'seconds',round(time.monotonic()-start,2),flush=True)
    gluing=[glue_test(n,meshes['T',n],meshes['O',n]) for n in (1,2,4)]
    for record in gluing:
        (OUT/f"pair-scale-{record['scale']}.json").write_text(json.dumps(record,indent=2)+'\n')
    receipt={'schema':'marici.fcc-gaussian-boundary.v1','status':'pass','arithmetic':'exact rational symmetric Bareiss',
             'sourceHash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'ownership':'Each elementary cell contributes mass 1/14 per incident vertex and spring 1/4 per edge. Sum cells, never induced-graph patch masses.',
             'normalizationConvention':'N=(2*pi)^(twoPiPower/2)/sqrt(inverseSquareRootDeterminant), Lebesgue integration; source-free centered Gaussian',
             'coherenceObligation':'route/coherencer compatibility on a fixed fine mesh, constant labelled external ports; refinement dynamics not supplied by boundary response alone',
             'grains':results,'gluing':[{k:v for k,v in r.items() if k not in ('externalBoundary','kernel')} for r in gluing],
             'residuals':['No map from a coarse boundary response alone to a specified refined microscopic theory is constructed.',
                          'Three refinement levels do not prove an unbounded complexity law or minimal representation.',
                          'No coupling/field rescaling fixed-point search performed.',
                          'No non-Gaussian, Chamon or HoTT claim.',
                          'S4 rotational octahedral symmetry and S4 full tetrahedral symmetry are different spatial actions.']}
    (OUT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'pass','grainCases':len(results),'gluingCases':len(gluing)}))

if __name__=='__main__': main()
