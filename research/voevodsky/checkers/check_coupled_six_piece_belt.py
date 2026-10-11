"""Source-rotation alignment with mode-only bridges between seed orbits.
An explicit extension of the original one-orbit construction. Keeps its exact
proton coefficients and positive fixed-weight deletion certificate. Does not
claim that geometry uniquely selects the inter-orbit bridging convention.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
from check_belt_operator_inputs import mode, mean
from check_geometric_cycle_reversal import SOURCE as PROTON, verify as verify_proton

BASE=Path(__file__).resolve().parents[1]

@dataclass(frozen=True,eq=False)
class R:
    a: Q=Q(0)
    b: Q=Q(0)
    def __post_init__(self):
        object.__setattr__(self,'a',Q(self.a));object.__setattr__(self,'b',Q(self.b))
    def __add__(self,x):
        x=cast(x);return R(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return R(-self.a,-self.b)
    def __sub__(self,x):return self+-cast(x)
    def __rsub__(self,x):return cast(x)+-self
    def __mul__(self,x):
        x=cast(x);return R(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=cast(x);d=x.a*x.a-2*x.b*x.b
        if not d:raise ZeroDivisionError()
        return self*R(x.a/d,-x.b/d)
    def __rtruediv__(self,x):return cast(x)/self
    def __eq__(self,x):
        if isinstance(x,(R,Q,int)):x=cast(x);return self.a==x.a and self.b==x.b
        return False
    def __hash__(self):return hash(self.a) if not self.b else hash((self.a,self.b))
    def __bool__(self):return bool(self.a or self.b)

def cast(x):return x if isinstance(x,R) else R(x)
Z=(R(),R()); ONE=(R(1),R())
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def scale(s,x):return (s*x[0],s*x[1])
def norm(x):return x[0]*x[0]+3*x[1]*x[1]
def total(xs):
    out=Z
    for x in xs:out=add(out,x)
    return out

def mv(r,v):return tuple(total(scale(a,z) for a,z in zip(row,v)) for row in r)
def mm(a,b):return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def transpose(a):return tuple(zip(*a))
def apply(a,v,n):
    out=[Z]*n
    for (i,j),z in a.items():out[i]=add(out[i],mul(z,v[j]))
    return tuple(out)
def encoded(z):return [str(z[0].a),str(z[0].b),str(z[1].a),str(z[1].b)]
def positive(x):
    if x.a>=0 and x.b>=0:return bool(x)
    if x.a<=0 and x.b<=0:return False
    return x.a*x.a>2*x.b*x.b if x.a>0 else 2*x.b*x.b>x.a*x.a

def construct(vectors,orbits,rotations):
    u=tuple(z for v in vectors for z in v); ns=[sum(norm(z) for z in v) for v in vectors]; nsum=sum(ns)
    N={(i,j):scale(1/nsum,mul(a,conj(b))) for i,a in enumerate(u) for j,b in enumerate(u) if a!=Z and b!=Z}
    L={(3*t+i,3*t+j):scale(1/ns[t],mul(a,conj(b))) for t,v in enumerate(vectors) for i,a in enumerate(v) for j,b in enumerate(v) if a!=Z and b!=Z}
    G={}
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if orbits[i]==orbits[j]:
                block=mm(rotations[i],transpose(rotations[j]))
                assert mv(block,vectors[j])==vectors[i]
                for a in range(3):
                    for b in range(3):
                        if block[a][b]:G[3*i+a,3*j+b]=(block[a][b]*ns[j]/nsum,R())
            else:
                for a in range(3):
                    for b in range(3):G[3*i+a,3*j+b]=N[3*i+a,3*j+b]
    return L,G,N,u,ns

def verify_operators(L,G,N,u):
    size=len(u); GL={}
    for (i,k),g in G.items():
        for j in range((k//3)*3,(k//3)*3+3):
            z=mul(g,L[k,j]);GL[i,j]=add(GL.get((i,j),Z),z)
    assert GL==N
    assert apply(N,u,size)==u and apply(L,u,size)==u and apply(G,u,size)==u
    assert all(L[j,i]==conj(z) for (i,j),z in L.items())
    assert all(N[j,i]==conj(z) for (i,j),z in N.items())
    assert all(G[j,i]==conj(z) for (i,j),z in G.items())
    # Exact closed-cycle trace certificate, factoring the three local source
    # choices. For every G[i,k], j runs over k's local triangle:
    # N[j,i] G[i,k] L[k,j] = q * |u[j]|²,
    # q = G[i,k] conj(u[i]) u[k] / (||u||² ||v_source||²).
    # Every such cycle is strictly positive, every arrow occurs in one, and
    # the sum of all cycles is trace(NGL)=trace(N)=1.
    nsum=sum(norm(z) for z in u); cycle_sum=R();usedL=set();usedG=set();usedN=set(); cycles=0
    for (i,k),g in G.items():
        js=range((k//3)*3,(k//3)*3+3); localnorm=sum(norm(u[j]) for j in js)
        q=scale(1/(nsum*localnorm),mul(g,mul(conj(u[i]),u[k])))
        assert q[1]==0 and positive(q[0])
        cycle_sum+=q[0]*localnorm
        for j in js:
            assert u[j]!=Z
            usedL.add((k,j));usedG.add((i,k));usedN.add((j,i));cycles+=1
    assert cycle_sum==1 and usedL==set(L) and usedG==set(G) and usedN==set(N)
    return {'L':len(L),'G':len(G),'N':len(N),'total':len(L)+len(G)+len(N),'typed_ports':3*size,
            'positive_closed_three_step_cycles':cycles,'cycle_trace_sum':'1','all_arrows_covered':True,
            'return':'NGL=GL=N; rank(N)=1','deletion_certificate':'Every proper fixed-weight edge deletion removes a strictly positive closed trace contribution.'}

def main():
    geo_path=BASE/'results/four_six_center_cones.json'; audit_path=BASE/'results/belt_operator_inputs.json'
    geo_raw=geo_path.read_bytes();audit_raw=audit_path.read_bytes();geometry=json.loads(geo_raw);audit=json.loads(audit_raw)
    if not geometry['verification_passed'] or not audit['verification_passed'] or audit['source_sha256']!=sha256(geo_raw).hexdigest():raise ValueError('source binding')
    points={k:tuple(map(Q,v)) for k,v in geometry['belt_scaled_coordinates'].items()};triangles=[];owners=[]
    for owner,f in enumerate(geometry['belt_faces']):
        center='F_'+'_'.join(sorted(f));points[center]=mean([points[k] for k in f])
        triangles.extend((center,f[i],f[(i+1)%3]) for i in range(3));owners.extend([owner]*3)
    def vector(t):
        re,im=mode(t,points)
        return tuple((R(*a),R(*b)) for a,b in zip(re,im))
    vectors=[vector(t) for t in triangles];orbit_of={tuple(t):i for i,o in enumerate(audit['orbits']) for t in o['triangles']}
    group=[tuple(tuple(Q(x) for x in row) for row in r) for r in audit['group_matrices']]
    orbit_ids=[orbit_of[t] for t in triangles];rotations=[]
    for t,v in zip(triangles,vectors):
        ref=vector(tuple(audit['orbits'][orbit_of[t]]['triangles'][0]))
        rotations.append(next(r for r in group if mv(r,ref)==v))
    L,G,N,u,ns=construct(vectors,orbit_ids,rotations)
    report=verify_operators(L,G,N,u)
    # Existing proton is a regression fixture for all weights, not just 1836.
    old_raw=PROTON.read_bytes();old=json.loads(old_raw);_,oldrows=verify_proton(old)
    obj=old['objects']; oldgeo=obj[obj[old['root']]['geometry']]['payload']
    oldpoints={'A':(1,1,1),'B':(1,-1,-1),'C':(-1,1,-1),'D':(-1,-1,1)}
    oldpoints={k:tuple(map(Q,v)) for k,v in oldpoints.items()}
    for face in ('ABC','ABD','ACD','BCD'):oldpoints['F_'+face]=mean([oldpoints[k] for k in face])
    records=oldgeo['triangles_and_transports']; oldv=[];oldR=[]; labels=[]
    c=(ONE,(R(-Q(1,2)),R(Q(1,2))),(R(-Q(1,2)),R(-Q(1,2))))
    for row in records:
        X=transpose(tuple(oldpoints[k] for k in row['triangle']))
        oldv.append(mv(X,c));oldR.append(tuple(tuple(Q(x) for x in r) for r in row['rotation']));labels.append(row['outer_arrow'])
    pL,pG,pN,pu,_=construct(oldv,[0]*12,oldR);proton_report=verify_operators(pL,pG,pN,pu)
    oldstages={r['source'][0] for r in oldrows}; assert oldstages=={'raw','local','aligned'}
    stage_names=[('raw','local'),('local','aligned'),('aligned','raw')]
    expected={}
    for matrix,(s,t) in zip((pL,pG,pN),stage_names):
        for (i,j),z in matrix.items():expected[((s,labels[j//3],'xyz'[j%3]),(t,labels[i//3],'xyz'[i%3]))]=z
    actual={(tuple(r['source']),tuple(r['target'])):(R(Q(r['weight_real'])),R(Q(r['weight_imag_sqrt3']))) for r in oldrows}
    assert expected==actual and proton_report['total']==1836
    # The shared-edge graph is connected. Mode bridges on those actual seams
    # are tau_ij=v_i v_j*/||v_j||², send v_j to v_i, and compose flatly:
    # tau_ik tau_kj = tau_ij. These identities follow exactly from each ns[k].
    adjacency={i:[j for j in range(18) if i!=j and len(set(triangles[i])&set(triangles[j]))==2] for i in range(18)}
    seen={0}; todo=[0]
    while todo:
        i=todo.pop()
        for j in adjacency[i]:
            if j not in seen:seen.add(j);todo.append(j)
    assert len(seen)==18 and all(positive(n) for n in ns)
    # Verify every shared-edge line bridge on its generated source vector.
    for i in adjacency:
        for j in adjacency[i]:
            bridge={(a,b):scale(1/ns[j],mul(vectors[i][a],conj(vectors[j][b]))) for a in range(3) for b in range(3)}
            assert apply(bridge,vectors[j],3)==vectors[i]
    arrows=[];piece_counts=Counter();pair_counts=Counter()
    for name,matrix,(s,t) in zip(('L','G','N'),(L,G,N),stage_names):
        for (i,j),z in sorted(matrix.items()):
            oi,oj=owners[i//3],owners[j//3]
            if oi==oj:piece_counts[oi]+=1
            else:pair_counts[tuple(sorted((oi,oj)))]+=1
            arrows.append({'source':[s,j//3,'xyz'[j%3]],'target':[t,i//3,'xyz'[i%3]],'stage':name,'coefficient':encoded(z)})
    assert len(arrows)==len({(tuple(a['source']),tuple(a['target'])) for a in arrows})==5346
    assert set(piece_counts.values())=={171} and len(piece_counts)==6
    assert set(pair_counts.values())=={288} and len(pair_counts)==15
    assert geo_path.read_bytes()==geo_raw and PROTON.read_bytes()==old_raw and audit_path.read_bytes()==audit_raw
    record={'schema':'marici.coupled-six-piece-belt.v1','geometry_sha256':sha256(geo_raw).hexdigest(),
        'orbit_audit_sha256':sha256(audit_raw).hexdigest(),'proton_root':old['root'],
        'rule':'Within a rotation orbit use the existing full spatial rotation. Across orbits use only the normalized selected-mode bridge. Average source blocks with weights ||v_j||²/sum ||v||². Materialize L,G,N in the original monomial Cartesian frame.',
        'coefficient_basis':['1','sqrt(2)','i*sqrt(3)','i*sqrt(6)'],
        'triangles':triangles,'face_owners':owners,'orbit_owners':orbit_ids,'shared_edge_adjacency':{str(k):v for k,v in adjacency.items()},
        'collective_vector':[encoded(z) for z in u],'arrows':arrows}
    root=sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    store={'root':root,'record':record}
    # Serialize and reconstruct every stage dictionary to avoid occurrence loss.
    replay=json.loads(json.dumps(store)); restored=[{} for _ in range(3)]
    assert sha256(json.dumps(replay['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==root
    for a in replay['record']['arrows']:
        s=a['source'];t=a['target'];z=list(map(Q,a['coefficient']))
        restored[('L','G','N').index(a['stage'])][3*t[1]+'xyz'.index(t[2]),3*s[1]+'xyz'.index(s[2])]=(R(*z[:2]),R(*z[2:]))
    assert tuple(restored)==(L,G,N)
    mutation_rejected=[]
    for stage in range(3):
        bad=[dict(m) for m in (L,G,N)];bad[stage].pop(next(iter(bad[stage])))
        try:verify_operators(*bad,u);mutation_rejected.append(False)
        except (AssertionError,KeyError):mutation_rejected.append(True)
    assert all(mutation_rejected)
    alpha=[sum(ns[j] for j in range(18) if orbit_ids[j]==k)/sum(ns) for k in range(3)]
    assert sum(alpha)==1 and all(positive(a) and positive(1-a) for a in alpha)
    # The six native off-line aligned directions acquire their orbit weights;
    # they are orthogonal to the one global selected mode.
    trace_G=sum(G.get((i,i),Z)[0] for i in range(54))
    trace_G2=sum(norm(z) for z in G.values())
    assert trace_G==3 and trace_G2==1+2*sum(a*a for a in alpha) and trace_G2!=trace_G
    output={'verification_passed':True,'root':root,'belt':report,'proton_regression':proton_report,
        'all_original_proton_coefficients_reproduced':True,'shared_edge_graph_connected':True,
        'missing_arrow_mutations_rejected_for_all_three_stages':all(mutation_rejected),
        'orbit_alignment_weights':[[str(a.a),str(a.b)] for a in alpha],
        'global_alignment_is_not_idempotent':trace_G2!=trace_G,
        'all_shared_edge_bridges_send_actual_mode_to_actual_mode':True,'serialized_arrow_replay_exact':True,
        'constituent_partition':'5346 = 6*171 + 15*288',
        'extra_over_independent_orbits':3888,
        'scope':'Certified count for the explicitly declared mode-only inter-orbit extension. Not a proof that geometry uniquely forces this extension, not a physical neutron mass.',
        'alignment_note':'For several seed orbits G is a self-adjoint positive contraction, not generally an idempotent projector; GL=LG=N and the original one-orbit G is reproduced exactly.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/coupled_six_piece_belt_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/coupled_six_piece_belt.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
