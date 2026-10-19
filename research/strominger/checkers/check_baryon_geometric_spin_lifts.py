"""Actual affine-generator -> metric Clifford spin lifts, with both signs retained."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_pentachoron_spin_interfaces import A,ZERO,ONE,S2,S3,CI,mm,adj,add,scale

def digest(p):return sha256(p.read_bytes()).hexdigest()
def identity(n):return tuple(tuple(ONE if i==j else ZERO for j in range(n)) for i in range(n))
def transpose(M):return tuple(zip(*M))
def key(M):return tuple(tuple(x.c for x in row) for row in M)
def record(M):return [[x.record() for x in row] for row in M]
def matrix(rows):return tuple(tuple(A(F(x)) for x in row) for row in rows)
def inverse(M):
    n=len(M);aug=[list(row)+list(identity(n)[i]) for i,row in enumerate(M)]
    for j in range(n):
        k=next(k for k in range(j,n) if aug[k][j]!=ZERO)
        aug[j],aug[k]=aug[k],aug[j];d=aug[j][j]
        aug[j]=[x/d for x in aug[j]]
        for i in range(n):
            if i!=j:
                d=aug[i][j];aug[i]=[x-d*y for x,y in zip(aug[i],aug[j])]
    return tuple(tuple(row[n:]) for row in aug)
def act(M,v):return tuple(sum((a*b for a,b in zip(row,v)),ZERO) for row in M)
def power(M,n):
    out=identity(len(M))
    for _ in range(n):out=mm(M,out)
    return out
I2=identity(2);I3=identity(3)
E=(((CI,ZERO),(ZERO,-CI)),((ZERO,ONE),(-ONE,ZERO)),((ZERO,CI),(CI,ZERO)))
def clifford(v):
    out=scale(ZERO,I2)
    for x,e in zip(v,E):out=add(out,scale(x,e))
    return out

def lift_order3(R):
    # Every inspected source generator has trace0/order3. Positive scalar part
    # fixes one algebraic representative; its opposite remains equally valid.
    assert sum((R[i][i] for i in range(3)),ZERO)==ZERO
    q0=A(F(1,2))
    q=((R[2][1]-R[1][2])/(A(4)*q0),(R[0][2]-R[2][0])/(A(4)*q0),(R[1][0]-R[0][1])/(A(4)*q0))
    U=add(scale(q0,I2),clifford(q))
    assert mm(adj(U),U)==I2
    for j in range(3):
        col=tuple(R[i][j] for i in range(3))
        assert mm(mm(U,E[j]),adj(U))==clifford(col)
    return U

def closure(gens,dimension,bound):
    seed=identity(dimension);seen={key(seed):seed};todo=[seed]
    while todo:
        a=todo.pop()
        for g in gens:
            b=mm(g,a);k=key(b)
            if k not in seen:
                seen[k]=b;todo.append(b)
                assert len(seen)<=bound,'declared finite closure bound exceeded'
    return tuple(seen.values())

def main():
    prerequisite=ROOT/'research/strominger/results/baryon-doublet-extension-v1.json'
    prior=json.loads(prerequisite.read_text(encoding='utf-8'));assert prior['status']=='pass'
    pins=dict(prior['source_sha256'])
    pins[prerequisite.relative_to(ROOT).as_posix()]=digest(prerequisite)
    pins[Path(__file__).resolve().relative_to(ROOT).as_posix()]=digest(Path(__file__))
    choices={
      'proton':('research/voevodsky/inputs/relative-proton.json',
                ((2*S2,S2,S2),(ZERO,S2*S3,S2*S3/A(3)),(ZERO,ZERO,A(4)*S3/A(3))),
                (A(F(1,4)),)*3),
      'neutron':('research/voevodsky/inputs/mode-neutron.json',
                 ((S3,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE)),(ZERO,)*3)}
    for rel,_,_ in choices.values():pins[rel]=digest(ROOT/rel)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale prerequisite'
    from electron_packet_interface import ACTIONS
    def native_field(U):
        rows=[]
        for row in U:
            converted=[]
            for z in row:
                coeff=[F(0)]*16;coeff[0]=F(z[0]);coeff[8]=F(z[1]);converted.append(A(tuple(coeff)))
            rows.append(tuple(converted))
        return tuple(rows)
    electron_native={key(native_field(U)) for U in ACTIONS}
    result={};checks={}
    for name,(rel,B,center) in choices.items():
        source=json.loads((ROOT/rel).read_text(encoding='utf-8'))
        M=matrix(source['metric']);Binv=inverse(B)
        assert mm(transpose(B),B)==M and mm(B,Binv)==I3
        rows=[];rotations=[];lifts=[]
        for index,g in enumerate(source['generators']):
            T=matrix(g['matrix']);translation=tuple(A(F(x)) for x in g['translation'])
            assert tuple(x+y for x,y in zip(act(T,center),translation))==center
            assert mm(mm(transpose(T),M),T)==M and power(T,3)==I3
            R=mm(mm(B,T),Binv)
            assert mm(transpose(R),R)==I3 and power(R,3)==I3
            U=lift_order3(R)
            assert key(U) not in electron_native and key(scale(-ONE,U)) not in electron_native
            assert power(U,3)==scale(-ONE,I2) and power(scale(-ONE,U),3)==I2
            # Source-metric Clifford square, not an identity action for coefficients.
            for j in range(3):
                v=tuple(ONE if i==j else ZERO for i in range(3))
                assert mm(mm(U,clifford(act(B,v))),adj(U))==clifford(act(B,act(T,v)))
            for sign in (ONE,-ONE):
                V=scale(sign,U)
                for j in range(3):assert mm(mm(V,E[j]),adj(V))==clifford(tuple(R[i][j] for i in range(3)))
            rotations.append(R);lifts.append(U)
            rows.append({'source_generator':index,'whitened_rotation':record(R),'positive_scalar_spin_lift':record(U),
                         'opposite_lift':record(scale(-ONE,U)),'geometric_order':3,'positive_lift_cube':'-I','opposite_lift_cube':'+I','in_electron_native24_in_declared_frame':False})
        G=closure(rotations,3,12 if name=='proton' else 3)
        H=closure(lifts,2,24 if name=='proton' else 6)
        assert len(G)==(12 if name=='proton' else 3) and len(H)==2*len(G)
        projected={}
        for U in H:
            # Read SO(3) action from Clifford coefficients using -tr(Ea X)/2.
            columns=[]
            for e in E:
                X=mm(mm(U,e),adj(U))
                columns.append(tuple(-sum((mm(a,X)[i][i] for i in range(2)),ZERO)/A(2) for a in E))
            R=tuple(zip(*columns));k=key(R)
            assert k in {key(g) for g in G}
            projected[k]=projected.get(k,0)+1
        assert len(projected)==len(G) and set(projected.values())=={2}
        checks[name+'_actual_metric_whitening_and_affine_center']=True
        checks[name+'_source_generator_clifford_covariance_both_signs']=True
        checks[name+'_three_step_amplitude_sign_not_fixed_by_geometric_return']=True
        checks[name+'_finite_double_cover_two_lifts_per_rotation']=True
        result[name]={'source':rel,'center':[x.record() for x in center],'whitening':record(B),
          'generators':rows,'geometric_group_size':len(G),'positive_branch_spin_group_size':len(H),
          'spin_lifts_per_geometric_rotation':2,
          'frame_convention':'Chosen exact positive-diagonal Cholesky whitening; a different orthonormal frame conjugates the spin presentation.',
          'not_bound':'Actual coefficient action T_g on native36 modes, its line phase, physical lift selection and coupling law.'}
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    checks['chosen_frame_lifts_not_silently_imported_as_electron_native_actions']=True
    checks['native_inputs_receipts_and_previous_pins_unchanged']=True
    report={'schema':'marici.baryon-geometric-spin-lifts.v1','status':'pass','checks':checks,'carriers':result,
      'filled_square':'U_g Clifford(Bv) U_g*=Clifford(B T_g_vector v)',
      'remaining_square':'(T_g_coefficient tensor U_g) K_tilde = K_tilde V_g, with T_g_coefficient and any induced native line phase still unbound',
      'guard':'Affine action is centered before Clifford encoding; translation is not treated as a linear spin rotation.',
      'source_sha256':pins,'source_lift_selected':False,'coefficient_action_assigned_identity':False,
      'physical_coupling_or_cost_claim':False,'formal_proof_recompiled':False,'native_producers_executed':False}
    (ROOT/'research/strominger/results/baryon-geometric-spin-lifts-v1.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('carriers','source_sha256')},indent=2))
if __name__=='__main__':main()
