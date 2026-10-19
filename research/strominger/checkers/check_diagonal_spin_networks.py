"""Extend prior intrinsic spin frames to actual diagonal-source generators.

Declared global protocol: L=direct sum of face projectors; G=N=J P J*.
P is each prior admitted low projector, not selected by a fitted support count.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_pentachoron_spin_interfaces import A,S2,S3,S5,CI,ZERO,ONE,I,dot,sub,wedge,chiral,pauli,add,scale,mm,adj,rank,constraints
from check_pentachoron_cycle_transport import eye,power,trace,act,record
OUT=ROOT/'research/strominger/results/diagonal-spin-networks'


def sparse(M):return {(i,j):x for i,row in enumerate(M) for j,x in enumerate(row) if x!=ZERO}
def smul(a,b):
    rows={};out={}
    for (i,j),x in a.items():rows.setdefault(j,[]).append((i,x))
    for (j,k),y in b.items():
        for i,x in rows.get(j,[]):out[i,k]=out.get((i,k),ZERO)+x*y
    return {k:v for k,v in out.items() if v!=ZERO}
def sadj(a):return {(j,i):x.flip(8) for (i,j),x in a.items()}
def srecord(a):return [{'target':i,'source':j,'coefficient':x.record()} for (i,j),x in sorted(a.items())]
def decode(x):return A(tuple(F(x.get(str(i),'0')) for i in range(16)))
def recover(entries):return {(r['target'],r['source']):decode(r['coefficient']) for r in entries}


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    receipt=ROOT/'research/strominger/results/electron_diagonal_seeds.json'
    prior=ROOT/'research/voevodsky/results/pentachoron_cycle_transport.json'
    sources=json.loads(receipt.read_text());previous=json.loads(prior.read_text())
    for data in (sources,previous):
        for p,h in data['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    vertices=[tuple(A(x) for x in v)+(ZERO,) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]+[(ZERO,ZERO,ZERO,S5)]
    center=(ZERO,ZERO,ZERO,S5/5)
    basis=tuple(zip(*(sub(vertices[j],vertices[4]) for j in range(4))))
    normals=[tuple(-S5*x/4 for x in sub(v,center)) for v in vertices]
    triangles={}
    for c in range(5):
        facet=[i for i in range(5) if i!=c]
        for j,d in enumerate(facet):
            f=[i for i in facet if i!=d]
            triangles[c,d]=scale(A((-1)**(c+j+1)),wedge(sub(vertices[f[1]],vertices[f[0]]),sub(vertices[f[2]],vertices[f[0]])))
    edges=list(combinations(range(5),2));rows=[];packets=[]
    # The retained source labels are pole A and basis B,C,D,E. Prior
    # geometric labels put this pole at E and the basis at A,B,C,D.
    label_to_cell=dict(zip('ABCDE',[4,0,1,2,3]))
    for chirality in (1,-1):
        projectors={k:scale(A(F(1,2)),add(I,scale(A(-1),pauli(tuple(x/(4*S3) for x in chiral(b,chirality)))))) for k,b in triangles.items()}
        folds={};cosine=S2*S3/4
        for c,d in edges:
            k=tuple(x/(2*cosine) for x in chiral(wedge(normals[c],normals[d]),chirality))
            folds[c,d]=add(scale(cosine,I),scale(-CI,pauli(k)));folds[d,c]=adj(folds[c,d])
        full=constraints({(c,d):(folds[c,d],I) for c,d in edges})
        lap=mm(adj(full),full);hi=A(4)+2*S2*S3/3;lo=A(4)-S2*S3
        Q=scale((hi-lo).inverse(),add(scale(hi,eye(10)),scale(A(-1),lap)))
        C=tuple(tuple(A(F(1,5)) if i%2==j%2 else ZERO for j in range(10)) for i in range(10))
        B=add(Q,scale(A(-1),C));spaces={'low':Q,'constant':C,'complementary':B}
        facekeys=sorted(projectors)
        J={(2*k+i,2*c+j):x/S2 for k,(c,d) in enumerate(facekeys) for i,row in enumerate(projectors[c,d]) for j,x in enumerate(row) if x!=ZERO}
        L={(2*k+i,2*k+j):x for k,key in enumerate(facekeys) for i,row in enumerate(projectors[key]) for j,x in enumerate(row) if x!=ZERO}
        assert smul(sadj(J),J)==sparse(eye(10));assert smul(L,J)==J
        measures={}
        for name,P in spaces.items():
            dimension=rank(P);assert mm(P,P)==P and adj(P)==P
            W=tuple(tuple(S5*row[8+j] for j in range(2)) for row in P)
            if name!='low':
                assert mm(adj(W),W)==I and mm(W,adj(W))==P
                prior_chiral=next(r for r in previous['chirality_results'] if r['chirality']==chirality)
                selected_name='constant' if chirality==1 else 'complementary'
                export_key='attachment_encoding' if name==selected_name else 'opposite_lift_attachment_encoding'
                exported=prior_chiral['conditional_cycle_defect_extension'][export_key]
                assert exported['cell_isometry']==record(W)
                assert exported['face_order']==[list(key) for key in facekeys]
                encoded=smul(J,sparse(W))
                assert exported['face_isometry']==[[encoded.get((i,j),ZERO).record() for j in range(2)] for i in range(40)]
            N=smul(smul(J,sparse(P)),sadj(J))
            # N^2=N and NL=N follow from the checked isometry,
            # projector and LJ=J identities. Check NL sparsely as a control.
            assert smul(N,L)==N
            measures[name]={'stage_supports':[len(L),len(N),len(N)],'transfers':len(L)+2*len(N),'return_rank':dimension,'raw_coordinates':40,'stage_ports':120}
            packet={'chirality':chirality,'carrier':name,'face_order':facekeys,'field':'Q(sqrt(2),sqrt(3),sqrt(5),i); mask bits 1,2,4,8',
                    'protocol':'L block face projectors; G=N=J P J*; return N G L=N',
                    'logical_projector':record(P),'encoding':srecord(J),'operators':{'L':srecord(L),'G':srecord(N),'N':srecord(N)},'measures':measures[name]}
            assert recover(packet['operators']['L'])==L
            assert recover(packet['operators']['G'])==recover(packet['operators']['N'])==N
            dest=OUT/f'chirality-{chirality}-{name}.json';dest.write_text(json.dumps(packet,indent=2)+'\n');packets.append(dest)
        for case_name in ('plus_DB','plus_AD','plus_CA','plus_EC','plus_BE'):
            case=sources['cases'][case_name];actions=[];Ts=[]
            for word,g in zip(case['cycles'],case['source']['generators']):
                cycle=[label_to_cell[x] for x in word[:-1]]
                permutation=list(range(5))
                for a,b in zip(cycle,cycle[1:]+cycle[:1]):permutation[a]=b
                ns=[tuple(x/(2*S2) for x in sub(vertices[cycle[0]],vertices[j])) for j in cycle[1:]]
                assert len(ns)%2==0
                rotation=eye(4);spin=I
                for n in ns:
                    h=tuple(tuple(A(i==j)-2*n[i]*n[j] for j in range(4)) for i in range(4));rotation=mm(h,rotation)
                for k in range(0,len(ns),2):
                    a,b=ns[k+1],ns[k]
                    pair=add(scale(dot(a,b),I),scale(CI,pauli(chiral(wedge(a,b),chirality))))
                    spin=mm(pair,spin)
                assert all(act(rotation,sub(v,center))==sub(vertices[permutation[c]],center) for c,v in enumerate(vertices))
                M=tuple(tuple(A(x) for x in row) for row in g['matrix']);t=tuple(A(x) for x in g['translation'])
                assert mm(rotation,basis)==mm(basis,M)
                assert act(basis,t)==sub(vertices[permutation[4]],vertices[4])
                assert mm(adj(spin),spin)==I
                for c,d in projectors:
                    assert mm(mm(spin,projectors[c,d]),adj(spin))==projectors[permutation[c],permutation[d]]
                    assert mm(mm(spin,folds[c,d]),adj(spin))==folds[permutation[c],permutation[d]]
                T=tuple(tuple(spin[i%2][j%2] if i//2==permutation[j//2] else ZERO for j in range(10)) for i in range(10));Ts.append(T)
                assert mm(adj(T),T)==eye(10);assert mm(T,lap)==mm(lap,T)
                preserved={name:mm(T,P)==mm(P,T) for name,P in spaces.items()}
                assert all(preserved.values())
                assert power(spin,len(cycle))==scale(A(-1),I)
                if len(cycle)==3:
                    defect_energy=add(scale(A(2),eye(10)),scale(A(-1),add(T,adj(T))))
                    assert all(mm(defect_energy,P)==P for P in spaces.values())
                actions.append({'cycle':word,'geometric_cell_permutation':permutation,'spin_lift':record(spin),'logical_transport':record(T),
                                'preserved':preserved,'restricted_traces':{name:trace(mm(T,P)).record() for name,P in spaces.items()},
                                'lift_cycle_power':record(power(spin,len(cycle)))})
            forward=eye(10)
            for step in range(10):
                forward=mm(Ts[step%2],forward)
                assert mm(adj(forward),mm(forward,Q))==Q
            rows.append({'case':case_name,'chirality':chirality,'actions':actions,'reverse_prefixes_checked':10,'network_measures':measures,'added_triangle_defect_on_low_space':'identity; shifts both doublets equally, no further selection'})
    result={'status':'passed','cases':rows,'scope':'Intrinsic geometric lifts preserve both prior doublets and the rank-four low space. Global protocol is a declared extension; lift signs and carrier selection remain explicit. Transport steps are not included in protocol support counts.',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),receipt,prior,ROOT/'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py',ROOT/'research/voevodsky/checkers/check_pentachoron_cycle_transport.py']},
            'network_packets':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in packets}}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','cases':len(rows),'measures_by_chirality':{str(s):next(r['network_measures'] for r in rows if r['chirality']==s) for s in (1,-1)}},indent=2))

if __name__=='__main__':main()
