"""Appendix B import, signed finite-cover lift and operator-valued chart bridge.
No Wolfram/NumPy dependency. Does not alter native geometry or scalar readers.
"""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import hashlib,json
from chamon_laurent import *
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
SOURCE=BASE/'references/chamon-gauge-map-source'
BITS=list(product(range(2),repeat=3))
SLOTS=[BITS[i] for i in (7,3,5,1,6,2,4,0)]
GAUGE_SLOTS=[(-1,0,0),(0,-1,0),(0,0,-1),(0,-1,-1),(-1,0,-1),(-1,-1,0),(-1,-1,-1),(0,0,0)]
CHART_RECEIPT=BASE/'results/eight-sector-interface/verification.json'
CHART_DATA=json.loads(CHART_RECEIPT.read_text(encoding='utf8'))
CHARTS={k:[[F(x) for x in row] for row in M] for k,M in CHART_DATA['unnormalizedCharts'].items()}
assert CHART_DATA['sectorSigns']==[[2*b-1 for b in s] for s in BITS]
def physical(u):return (u[1]+u[2],u[0]+u[2],u[0]+u[1])
def honeycomb_incidence(A):
    o=(0,0,0);x=(1,0,0);y=(0,1,0);z=(0,0,1)
    edges=[(o,x),(o,y),(o,z),(y,z),(z,x),(x,y)]
    opposite=[(1,1,1),(0,1,1),(1,0,1),(1,1,0)]
    octa=[x,y,z,(0,1,1),(1,0,1),(1,1,0)]
    for j,vertices in enumerate(([o,x,y,z],opposite,octa)):
        actual=set()
        for i,edge in enumerate(edges):
            for shift in A[i][j]:actual.add(tuple(sorted(tuple(a+b for a,b in zip(p,shift)) for p in edge)))
        expected=set()
        for a,b in combinations(vertices,2):
            delta=[u-v for u,v in zip(a,b)]
            if sum(d*d for d in delta)+sum(delta)**2==2:expected.add(tuple(sorted((a,b))))
        assert actual==expected
        assert len(actual)==(6 if j<2 else 12)
    assert GAUGE_SLOTS[:6]==[tuple(-a-b for a,b in zip(u,v)) for u,v in edges]

def site_map(period,cells,slots):
    sites={}
    for ci,c in enumerate(cells):
        for i,b in enumerate(slots):
            q=tuple((a+d)%L for a,d,L in zip(c,physical(b),period))
            assert q not in sites;sites[q]=8*ci+i
    assert len(sites)==8*len(cells)
    return sites

def coarse_column():
    # C1 -> B1: macro translations -2 primitive steps; X->Y,Y->Z,Z->X.
    M=zero(16,8)
    for j,b in enumerate(SLOTS):
        for axis,terms in enumerate((poly('1/y+1/z+1/xy+1/xz'),poly('1/x+1/z+1/xy+1/yz'))):
            for shift in terms:
                u=tuple(v+w for v,w in zip(b,shift));i=SLOTS.index(tuple(v%2 for v in u))
                q=frozenset({tuple(-(v//2) for v in u)})
                M[i][j]^=q
                if axis==0:M[i+8][j]^=q
    return M

def finite_cells(period):
    assert all(v%4==0 for v in period),'untwisted eight-slot quotient requires periods divisible by four'
    wrap=lambda p:tuple(x%L for x,L in zip(p,period))
    steps=[physical(tuple(-2*int(i==j) for i in range(3))) for j in range(3)]
    cells=[(0,0,0)];seen=set(cells)
    for c in cells:
        for s in steps:
            d=wrap(tuple(x+y for x,y in zip(c,s)))
            if d not in seen:seen.add(d);cells.append(d)
    return sorted(cells)
def finite(A,period,cells,pauli=False):
    # Polynomial columns expand in (cell, internal slot) order; X rows precede Z.
    q=len(A)//2;k=len(A[0]);n=q*len(cells);ci={c:i for i,c in enumerate(cells)}
    columns=[]
    for cell in cells:
        for j in range(k):
            word=0
            for r in range(2*q):
                for e in A[r][j]:
                    d=physical(tuple(-2*v for v in e));target=tuple((a+b)%L for a,b,L in zip(cell,d,period))
                    bit=(r//q)*n+ci[target]*q+r%q;word^=1<<bit
            columns.append((word&((1<<n)-1),word>>n))
    if pauli:
        assert k==2*q
        columns=[columns[c*k+a*q+j] for a in range(2) for c in range(len(cells)) for j in range(q)]
    return columns

def times(a,b):
    x,z,p=a;y,w,q=b
    return x^y,z^w,(p+q+2*(z&y).bit_count())%4

def hermitian(v):
    x,z=v;return x,z,(x&z).bit_count()%4

def act(word,images):
    x,z,p=word;n=len(images)//2;out=(0,0,p)
    for bits,offset in ((x,0),(z,n)):
        while bits:
            bit=bits&-bits;out=times(out,images[offset+bit.bit_length()-1]);bits^=bit
    return out

def rank(words):
    basis={}
    for w in words:
        while w:
            b=w.bit_length()-1
            if b in basis:w^=basis[b]
            else:basis[b]=w;break
    return len(basis)

def signed_rank(words,n):
    basis={};dependencies=0
    for word in words:
        w=word
        while w[0] or w[1]:
            pivot=(w[0]|(w[1]<<n)).bit_length()-1
            if pivot in basis:w=times(w,basis[pivot])
            else:basis[pivot]=w;break
        else:
            assert w[2]==0,'minus identity dependency'
            dependencies+=1
    return len(basis),dependencies

def qmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def addword(out,w,coefficient=(F(1),F(0))):
    x,z,p=w;phase=(p-(x&z).bit_count())%4
    factor=((1,0),(0,1),(-1,0),(0,-1))[phase]
    a=qmul(coefficient,factor);old=out.get((x,z),(F(0),F(0)));value=(old[0]+a[0],old[1]+a[1])
    if value!=(0,0):out[x,z]=value
    else:out.pop((x,z),None)
def singleton(w):
    out={};addword(out,w);return out

def opmul(A,B):
    out={}
    for a,c in A.items():
        for b,d in B.items():addword(out,times(hermitian(a),hermitian(b)),qmul(c,d))
    return out

def opact(A,images):
    out={}
    for a,c in A.items():addword(out,act(hermitian(a),images),c)
    return out

def linear(M,A):
    result=[]
    for row in M:
        out={}
        for scale,values in zip(row,A):
            for w,c in values.items():addword(out,hermitian(w),(scale*c[0],scale*c[1]))
        result.append(out)
    return result

def chart(A,name,inverse=False):
    H=CHARTS[name]
    M=[[x/2 for x in row] for row in zip(*H)] if inverse else H
    return linear(M,A)

def norm(A):return sum(a*a+b*b for v in A for a,b in v.values())

def bridge(period,cells,images,inverse_images):
    n=len(images)//2;sites=site_map(period,cells,SLOTS)
    centre=(1,1,1);families=[]
    for axes in ('XYZ','ZXY'):
        operators=[]
        for sector in BITS:
            w=(0,0,0)
            for axis,bit in enumerate(sector):
                q=list(centre);q[axis]+=1 if bit else -1;site=sites[tuple(v%L for v,L in zip(q,period))]
                pauli=axes[axis];local=(1<<site if pauli in 'XY' else 0,1<<site if pauli in 'YZ' else 0,1 if pauli=='Y' else 0)
                w=times(w,local)
            operators.append(w)
        families.append(operators)
    A,B=families
    # Actual octahedron: opposite triangular faces multiply to its signed stabilizer.
    H=times(A[0],A[7]);assert all(times(A[i],A[7-i])==H for i in range(8))
    target=[[singleton(w) for w in family] for family in families]
    source=[[opact(a,inverse_images) for a in family] for family in target]
    assert [[opact(a,images) for a in family] for family in source]==target
    checks=0
    for selected in CHARTS:
        for target_family,source_family in zip(target,source):
            assert chart(chart(source_family,selected),selected,inverse=True)==source_family
            assert norm(chart(source_family,selected))==2*norm(source_family)
            assert [opact(a,images) for a in chart(source_family,selected)]==chart(target_family,selected)
        # Products are taken after exact reconstruction, not coordinatewise on averages.
        left=chart(chart(source[0],selected),selected,inverse=True)
        right=chart(chart(source[1],selected),selected,inverse=True)
        for i in range(8):
            for j in range(8):assert opact(opmul(left[i],right[j]),images)==opmul(target[0][i],target[1][j]);checks+=1
        for i in range(4):assert opact(opmul(left[i],left[7-i]),images)==singleton(H)
    for transition in CHART_DATA['transitions']:
        i,j=transition['source'],transition['target'];M=[[F(x) for x in row] for row in transition['matrix']]
        assert linear(M,chart(source[0],i))==chart(source[0],j)
    anti=sum(times(a,b)!=times(b,a) for a in A for b in B)
    assert anti==32
    # Averages lose the ability to recover individual face operators.
    averaged=chart(source[0],'0');averaged[4:]=[{} for _ in range(4)]
    assert chart(averaged,'0',inverse=True)!=source[0]
    # A site belongs to four sectors; it must not become four independent qubits.
    assert sum(bool(w[0]&(1<<sites[(2,1,1)])) for w in A)==4
    duplicated_B=(B[3][0]<<(3*n),B[3][1]<<(3*n),B[3][2])
    assert times(A[0],B[3])!=times(B[3],A[0])
    assert times(A[0],duplicated_B)==times(duplicated_B,A[0])
    naive=chart([opmul(a,b) for a,b in zip(chart(source[0],'0'),chart(source[1],'0'))],'0',inverse=True)
    assert naive!=[opmul(a,b) for a,b in zip(source[0],source[1])]
    return {'duplicatedSharedVertexRejected':True,'naiveChartMultiplicationRejected':True,'charts':4,'chartTransitions':16,'normalizedOperatorNormsPreserved':True,'crossFamilyProducts':checks,'anticommutingPairs':anti,'oppositeFaceProducts':4,'sharedPhysicalSites':6,'averageOnlyRejected':True}

def signed_gate_lift(gates,period,cells):
    n=8*len(cells);images=[(1<<i,0,0) for i in range(n)]+[(0,1<<i,0) for i in range(n)]
    for kind,args in reversed(gates):
        E=gate_matrix(kind,args);Einv=mm(mm(omega(8),dag(E)),omega(8))
        gate_images=[hermitian(v) for v in finite(Einv,period,cells,pauli=True)]
        if kind=='cPhase':
            assert poly(args[1])==ONE
            # The reduction uses S; its inverse is S-dagger, not S.
            for cell in range(len(cells)):
                i=8*cell+int(args[0])-1;x,z,p=gate_images[i];gate_images[i]=(x,z,(p+2)%4)
        images=[act(w,gate_images) for w in images]
    return images

def verify_cover(period,V,G,H,R,Vinv,gates):
    cells=finite_cells(period);n=8*len(cells)
    vf=finite(V,period,cells,pauli=True);images=signed_gate_lift(gates,period,cells)
    assert [w[:2] for w in images]==vf
    # Align ancillary +Z with the target generator products; bulk phases are pulled back.
    hf=finite(H,period,cells);target_generators=[hermitian(w) for w in hf]
    sites=site_map(period,cells,SLOTS);assert set(site_map(period,cells,GAUGE_SLOTS))==set(sites)
    for ci,c in enumerate(cells):
        for j,b in enumerate(SLOTS):
            centre=tuple(a+d-1 for a,d in zip(c,physical(b)));word=(0,0,0)
            for axis in range(3):
                for sign in (-1,1):
                    q=list(centre);q[axis]+=sign;site=sites[tuple(v%L for v,L in zip(q,period))]
                    word=times(word,(1<<site if axis<2 else 0,1<<site if axis>0 else 0,int(axis==1)))
            assert word==target_generators[8*ci+j]

    # R is a generator map, not a Pauli map: expand as X-only rows.
    rf=finite(R+zero(8,8),period,cells)
    targets=[act((v[0],0,0),target_generators+[(0,0,0)]*n) for v in rf]
    ancillary_sign_corrections=[]
    for cell in range(len(cells)):
        for a in (6,7):
            index=8*cell+a;current=images[n+index];target=targets[index]
            if current!=target:ancillary_sign_corrections.append(index)
            assert current[:2]==target[:2]
            images[n+index]=target
    for i,a in enumerate(images):
        assert times(a,a)==(0,0,0)
        for j,b in enumerate(images):
            parity=((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
            assert parity==int((i+n)%(2*n)==j)
    inverse_images=[]
    for i,v in enumerate(finite(Vinv,period,cells,pauli=True)):
        w=hermitian(v);out=act(w,images);desired=(1<<i,0,0) if i<n else (0,1<<(i-n),0)
        assert out[:2]==desired[:2];inverse_images.append((w[0],w[1],(w[2]-out[2])%4))
        assert act(inverse_images[-1],images)==desired
    gf=finite(G,period,cells);source_signs=[]
    # Source gauge syndrome = V2^T times native Chamon syndrome.
    syndrome_checks=0
    for i,error in enumerate(inverse_images):
        target_error=(1<<i,0) if i<n else (0,1<<(i-n))
        syndrome=sum((((x&target_error[1]).bit_count()+(z&target_error[0]).bit_count())%2)<<j for j,(x,z) in enumerate(hf))
        for (x,z),mix in zip(gf,rf):
            assert ((x&error[1]).bit_count()+(z&error[0]).bit_count())%2==(syndrome&mix[0]).bit_count()%2
            syndrome_checks+=1
    signed_source=[]
    for v,target in zip(gf,targets):
        w=hermitian(v);out=act(w,images);assert out[:2]==target[:2]
        delta=(target[2]-out[2])%4;assert delta in (0,2);source_signs.append(delta)
        signed=(w[0],w[1],(w[2]+delta)%4)
        assert act(signed,images)==target
        signed_source.append(signed)
    assert all(source_signs[8*c+a]==0 for c in range(len(cells)) for a in (6,7))
    rH=rank([x|(z<<n) for x,z in hf]);rG=rank([x|(z<<n) for x,z in gf]);assert rG==rH
    assert signed_rank(target_generators,n)==signed_rank(signed_source,n)==(rH,n-rH)
    return {'period':period,'coarseCells':len(cells),'gaugeEdgeQubits':6*len(cells),'ancillaQubits':2*len(cells),'spins':n,'rank':rH,'minusIdentityAbsent':True,'logicalQubits':n-rH,'sourceGaugeSignExponents':source_signs,'notebookLiftAncillaryXCorrections':ancillary_sign_corrections,'ancillasPositiveZ':True,'signedGeneratorImages':2*n,'nativeOctahedraCompared':n,'syndromePairings':syndrome_checks,'operatorBridge':bridge(period,cells,images,inverse_images)}

def main():
    prerequisites=(CHART_RECEIPT,BASE/'results/chamon-fcc-benchmark/verification.json')
    for prerequisite in prerequisites:
        data=json.loads(prerequisite.read_text(encoding='utf8'));assert data['status']=='pass'
        for path,digest in data['sourceHashes'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,('stale prerequisite',path)
    text=(SOURCE/'main.tex').read_text(encoding='utf8');nb=(SOURCE/'supplementary.nb').read_text(encoding='utf8')
    A,B,W,T,H,C,R=import_matrices(text);w,t=shear(W,T);V=mm(mm(C,w),t);O=omega(8);Vinv=mm(mm(O,dag(V)),O)
    assert coarse_column()==H
    honeycomb_incidence(A)
    assert mm(mm(dag(V),O),V)==O and mm(V,Vinv)==eye(16)
    assert mm(R,inv(R))==eye(8) and mm(inv(R),R)==eye(8)
    S=zero(16,8)
    for i in range(6):
        for j in range(3):S[i][j]=A[i][j];S[i+8][3+j]=B[i][j]
    G=mm(mm(t,w),S);G[14][6]=ONE;G[15][7]=ONE
    assert mm(V,G)==mm(H,R)
    assert mm(mm(dag(G),O),G)==zero(8,8)
    assert mm(mm(dag(H),O),H)==zero(8,8)
    wp,tp=shear(W,T,True);Vp=mm(mm(C,wp),tp);Gp=[r[:] for r in G];Gp[6][6]=ONE;Gp[7][7]=ONE
    assert mm(mm(dag(Vp),O),Vp)==O and mm(Vp,Gp)==mm(H,R)
    assert mm(Vp,G)!=mm(H,R) # Mixing the two ancilla conventions is rejected.
    gates=notebook_gates(nb);reduced=V
    for kind,args in gates:
        E=gate_matrix(kind,args);assert mm(mm(dag(E),O),E)==O;reduced=mm(E,reduced)
    assert reduced==eye(16)
    broken=[r[:] for r in V];broken[0][0]^=ONE
    assert mm(mm(dag(broken),O),broken)!=O
    assert mm(mm(C,t),w)!=V
    for bad in ((2,2,2),(6,6,6),(4,6,8)):
        try:finite_cells(bad)
        except AssertionError:pass
        else:raise AssertionError('incompatible quotient admitted')
    covers=[verify_cover(p,V,G,H,R,Vinv,gates) for p in ((4,4,4),(4,4,8),(8,8,8))]
    receipt={'schema':'marici.chamon-gauge-map.v1','status':'pass','formalIdentities':['VdagOmegaV=Omega','VinvV=I','V2 invertible over Laurent ring','V SigmaGauge=SigmaChamon V2','blocked C1=B1','printed map with Y ancillas = notebook map with Z ancillas'], 'notebookReductionSteps':len(gates),'retainedSublatticeTranslations':[args for kind,args in gates if kind=='rowMul'],'targetQubitAndCheckSlots':SLOTS,'sourceGaugeEdgeAndAncillaSlots':GAUGE_SLOTS,'macroTranslation':'-2 times FCC primitive basis','covers':covers,'mutationControlsRejected':['matrix_entry','wrong_WT_order','mixed_ancilla_frames','incompatible_unit_cell_quotients','average_only','duplicated_shared_vertex','naive_chart_multiplication'],'phaseScope':'Replay inverse notebook reduction with standard H, S, CNOT, CZ, SWAP and retained wire translation; any ancillary input X corrections are explicit. Source bulk signs are pulled back from positive native Chamon stabilizers; polynomial equations alone do not specify signs.','nativeGrammarChanged':False,'readerFieldsChanged':False,'sourceHashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in (SOURCE/'main.tex',SOURCE/'supplementary.nb',Path(__file__).resolve(),Path(__file__).with_name('chamon_laurent.py'),SOURCE/'README.md',*prerequisites)}}
    out=BASE/'results/chamon-gauge-map';out.mkdir(parents=True,exist_ok=True)
    (out/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
    matrices_out={name:[[sorted(p) for p in row] for row in M] for name,M in {'V':V,'VInverse':Vinv,'V2':R,'V2Inverse':inv(R),'SigmaGauge':G,'SigmaChamon':H}.items()}
    (out/'matrices.json').write_text(json.dumps(matrices_out,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':'pass','formalIdentities':len(receipt['formalIdentities']),'notebookReductionSteps':len(gates),'covers':[{k:c[k] for k in ('period','spins','rank','logicalQubits','operatorBridge')} for c in covers]},indent=2))
if __name__=='__main__':main()
