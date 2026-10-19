"""Pointed unitary lift of source local cycle inversions; exact field algebra."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from check_opposite_branch_canonical import (ROOT,BASE,R,Z,ONE,decode,encoded,add,mul,conj,scale,norm,total,identity,plus,times,compose,adjoint,entries,diag,dump,apply,transported)
hashes={}
def read(p):
    b=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(b).hexdigest();return json.loads(b)
def inv(z):assert z!=Z;return scale(1/norm(z),conj(z))
def sub(a,b):return add(a,scale(-1,b))
def inner(a,b,d):return total(scale(1/q,mul(conj(x),y)) for x,y,q in zip(a,b,d))

def main():
    read('research/strominger/inputs/opposite-branch-cycle-lift-protocol-v1.json')
    prior=read('research/strominger/results/opposite-branch-canonical/verification.json');assert prior['status']=='pass'
    for p,h in prior['sourceHashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    packet=read('research/strominger/results/opposite-branch-canonical/operators.json')
    old=read('research/voevodsky/results/belt_three_by_twelve_store.json')
    new=read('research/voevodsky/results/opposite_branch_belt_store.json')
    ambient=read('research/voevodsky/results/coupled_six_piece_belt_store.json')['record']
    rotation=read('research/strominger/results/neutron-canonical-rotation-frame.json')
    energy=read('research/voevodsky/results/native_operation_energy_lift_store.json')['carriers']['belt']
    coords=old['coordinates'];d=[F(c['d']) for c in coords]
    z=[decode(c['selected_numerator']) for c in coords];zz=list(map(decode,new['selected_numerators']))
    signs=[new['face_signs'][ambient['face_owners'][c['triangle']]] for c in coords]
    def lift(v):
        J={};phases=[]
        for t in range(18):
            if signs[2*t]==1:
                J[2*t,2*t]=J[2*t+1,2*t+1]=ONE;continue
            w=v[2*t:2*t+2];bar=list(map(conj,w));c=inner(w,bar,d[2*t:2*t+2]);assert c!=Z
            q=mul(c,inv(conj(c)));assert norm(q)==1
            determinant=sub(mul(w[0],bar[1]),mul(bar[0],w[1]));assert determinant!=Z
            vi=[[bar[1],scale(-1,bar[0])],[scale(-1,w[1]),w[0]]]
            vi=[[mul(x,inv(determinant)) for x in row] for row in vi]
            target=[[bar[i],mul(q,w[i])] for i in range(2)]
            for i in range(2):
                for j in range(2):
                    x=total(mul(target[i][k],vi[k][j]) for k in range(2))
                    if x!=Z:J[2*t+i,2*t+j]=x
            phases.append({'triangle':coords[2*t]['triangle'],'squaredForwardLiftPhase':encoded(q),'crossGram':encoded(c)})
        return J,phases
    J,phases=lift(z);Backward,_=lift(zz);Js=adjoint(J,d)
    assert compose(Js,J)==identity(36) and compose(J,Js)==identity(36)
    assert Backward==Js and compose(Backward,J)==identity(36)
    assert apply(J,z,36)==tuple(zz)
    C=entries(packet['sameGeometryCycle']);C2=compose(C,C)
    Csign={e:v for e,v in C.items() if signs[e[0]]==1}
    Csign.update({e:v for e,v in C2.items() if signs[e[0]]==-1})
    assert compose(compose(C,C),C)==identity(36)
    assert compose(J,C)==compose(Csign,J)
    assert compose(compose(Csign,Csign),Csign)==identity(36)
    assert compose(J,C)!=compose(C,J)
    ops=[]
    for store in (old,new):
        ops.append({s:{(a['target'],a['source']):scale(1/d[a['source']],decode(a['numerator'])) for a in store['arrows'] if a['stage']==s} for s in ('L','G','N')})
    for s in ('L','G','N'):assert compose(ops[1][s],J)==compose(J,ops[0][s])
    T={(j,i):ONE for i,j in enumerate(rotation['native_coordinate_permutation'])}
    assert compose(J,T)==compose(T,J)
    H_old=entries(energy['entries']);H_new=entries(packet['signedCharacterHamiltonianIn4HOverPiUnits'])
    assert compose(H_new,J)==compose(J,H_old)
    # On a negative face C^-1-omega=-(C-conjugate(omega)). Thus native
    # cycle inversion gives exactly the independently rebuilt signed energy.
    omega=(R(F(-1,2)),R(F(1,2)))
    defneg=plus(C2,times(-1,diag([omega]*36)))
    defsigned=plus(C,times(-1,diag([conj(omega)]*36)))
    negative=lambda A:{e:v for e,v in A.items() if signs[e[0]]==-1}
    assert negative(defneg)==times(-1,negative(defsigned))
    J52={**J,**{(i,i):ONE for i in range(36,52)}}
    U=diag(tuple(map(decode,packet['nativeDiagonalAdapter']))+(ONE,)*16)
    Ui=diag(tuple(conj(v) for _,v in sorted(U.items())))
    for data in packet['canonicalProjectors'].values():
        Pnew=entries(data);Pold=compose(compose(Ui,Pnew),U)
        assert compose(Pnew,J52)==compose(J52,Pold)
    square=compose(J,J);assert square!=identity(36)
    residual=plus(square,times(-1,identity(36)))
    # The two lifts agree on every selected mode and bank feature, hence on
    # the already verified 21D joint generated carrier; their distinction is
    # on the remaining native plane direction, not a hidden field deletion.
    joint=read('research/strominger/results/opposite-branch-joint-closure/verification.json');assert joint['status']=='pass'
    jointops=read('research/strominger/results/opposite-branch-joint-closure/operators.json')
    Fullnew=entries(jointops['full52DNativeBankEmbedding']);Fullold=compose(Ui,Fullnew)
    assert compose(J52,Fullold)==Fullnew
    checks={'all_nine_negative_triangle_Gram_lifts_unitary':True,'source_cycle_inversion_and_L_G_N_C3_intertwined':True,'independent_signed_energy_and_all18_pulses_intertwined':True,'independent_backward_lift_is_metric_adjoint':True,'forward_lift_not_silently_treated_as_involution':True,'same_21D_joint_carrier_as_diagonal_adapter':True}
    hashes[Path(__file__).relative_to(ROOT).as_posix()]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out=BASE/'results/opposite-branch-cycle-lift';out.mkdir(parents=True,exist_ok=True)
    (out/'operators.json').write_text(json.dumps({'forwardLift':dump(J),'backwardLift':dump(Backward),'signedInverseCycle':dump(Csign),'squaredForwardLiftResidual':dump(residual),'localPhases':phases},indent=2)+'\n')
    result={'schema':'marici.opposite-branch-cycle-lift.v1','status':'pass','checks':checks,'sourceHashes':hashes,'negativeTriangles':len(phases),'forwardLiftSquaredIdentity':False,'backwardTimesForwardIdentity':True,'jointClosureComplexDimension':joint['dimensions']['jointMinimalClosureComplex'],'disposition':'A pointed metric-unitary lift exists for explicit source cycle inversion on opposite faces. It does not commute with the unchanged cycle and is not one involution: backward transport is the independently based adjoint, with source-determined phases retained. No physical branch or time-reversal selection is derived.'}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'negativeTriangles':len(phases),'squaredForwardIdentity':False,'backwardTimesForwardIdentity':True,'jointClosureComplexDimension':result['jointClosureComplexDimension']}))

if __name__=='__main__':main()
