"""Gauge-preserving selector factorization and exact success/reject accounting."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_cross_lead_selection import audit as cross_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,S5,mm,adj,rank,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import S2,S3,CI
from check_native_intrinsic_spinor_adapter import native_decode
from check_electron_charge_spin_frontier import spin,qm

DEST=BASE/'results/retained-selector-controls.v1.json'


def permute(xs,p):
    out=[0]*4
    for i in range(4):out[p[i]]=xs[i]
    return tuple(out)

def swaps(p):
    current=list(range(4));out=[]
    for i in range(4):
        if current[i]!=p[i]:
            a,b=current[i],p[i];out.append((a,b));current=[b if x==a else a if x==b else x for x in current]
    assert current==list(p)
    return out

def gauss(s):
    k,n,ell=s;return tuple(n[i]+ell[i]+int(i==k) for i in range(4))

def field(s,p):
    k,n,ell=s;newell=permute(ell,p)
    return (k,tuple(n[i]+ell[i]-newell[i] for i in range(4)),newell)

def matter(s,p):
    k,n,ell=s;newk=p[k]
    return (newk,tuple(n[i]+int(i==k)-int(i==newk) for i in range(4)),ell)

def lifted(s,p):return matter(field(s,p),p)

def inverse(p):return [p.index(i) for i in range(4)]


def audit():
    previous=cross_audit()
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    n0=A(F(1,2))+S3/6;anchor=tuple(face[0][i][0] for i in range(2));w=[anchor]
    for i in range(1,4):w.append(tuple(row[0]/Q[i][0] for row in mm(face[i],tuple((x,) for x in anchor))))
    V=tuple(tuple(w[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8));D=scale(n0.inverse(),adj(V))
    assert mm(adj(V),V)==scale(n0,eye(4))
    actions={};control_rows=[]
    for item in previous['joint_symmetry']['source_group_maps']:
        q=tuple(F(x) for x in item['quaternion']);p=item['permutation']
        U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(q))
        assert [face.index(mm(mm(U,x),adj(U))) for x in face]==p
        raw=tuple(tuple(U[i%2][j%2] if i//2==p[j//2] else ZERO for j in range(8)) for i in range(8))
        T=mm(mm(D,raw),V);assert mm(adj(T),T)==eye(4) and mm(T,K)==mm(K,T)
        assert all(T[i][j]==ZERO for j in range(4) for i in range(4) if i!=p[j])
        actions[q]=(p,T)
        control_rows.append({'quaternion':list(map(str,q)),'permutation':p,'swap_sequence':swaps(p),
                             'input_matter_phases':[T[p[k]][k].record() for k in range(4)],
                             'selector_coefficient':str(q[0]/6)})
    fluxes=[ell for ell in product(range(-2,3),repeat=4) if sum(ell)==-1]
    tests=0;off_kernel_tests=0;max_intermediate=F(0);witness=None
    beta=F(load('research/strominger/contracts/common-endpoint-charging.json')['beta'])
    for ell in fluxes:
        for k in range(4):
            n=tuple(-ell[i]-int(i==k) for i in range(4));s=(k,n,ell)
            for p,T in actions.values():
                mid=field(s,p);out=matter(mid,p)
                assert gauss(mid)==gauss(out)==gauss(s)==(0,0,0,0)
                assert out==(p[k],permute(n,p),permute(ell,p))
                assert field(matter(s,p),p)==out
                assert field(mid,inverse(p))==s and matter(matter(s,p),inverse(p))==s
                step=s
                for a,b in swaps(p):
                    trans=list(range(4));trans[a],trans[b]=b,a;step=field(step,trans)
                assert step==mid
                step=mid
                for a,b in swaps(p):
                    trans=list(range(4));trans[a],trans[b]=b,a;step=matter(step,trans)
                assert step==out
                work=beta*F(sum(x*x for x in mid[1])-sum(x*x for x in n),8)
                final_work=beta*F(sum(x*x for x in out[1])-sum(x*x for x in mid[1]),8)
                assert work+final_work==0
                max_intermediate=max(max_intermediate,abs(work))
                if work and witness is None:witness={'state':[k,list(n),list(ell)],'permutation':p,'field_stage_charging_change':str(work),'matter_stage_charging_change':str(final_work)}
                tests+=1
                # Gauge-invariant lift is stronger than coordinate permutation:
                # even off the physical kernel it fixes every G_i individually.
                off=(k,tuple(n[i]+i-1 for i in range(4)),ell)
                assert gauss(field(off,p))==gauss(matter(off,p))==gauss(lifted(off,p))==gauss(off)
                off_kernel_tests+=1
    s=(2,(3,-1,4,-2),(-3,1,0,1));compositions=0
    for q,(p,T) in actions.items():
        for r,(pr,S) in actions.items():
            pt,TT=actions[qm(q,r)]
            assert mm(T,S)==TT and lifted(lifted(s,pr),p)==lifted(s,pt)
            compositions+=1
    # Linear combination of unitaries, keeping the orthogonal controller
    # branches. Norm sum is 5/3; preparation weights are 1/10 or 1/20.
    normalization=sum(abs(q[0]/6) for q in actions);assert normalization==F(5,3)
    W=[];Reject=[];success=tuple(tuple(ZERO for _ in range(4)) for _ in range(4));lcu=[]
    for q,(p,T) in actions.items():
        alpha=q[0]/6
        if not alpha:continue
        probability=abs(alpha)/normalization;sign=1 if alpha>0 else -1
        amplitude=S2*S5/10 if probability==F(1,10) else S5/10
        assert amplitude*amplitude==A(probability)
        signed=scale(A(sign),T);W.extend(scale(amplitude,signed))
        success=add(success,scale(A(probability),signed))
        lcu.append({'quaternion':list(map(str,q)),'preparation_probability':str(probability),'controlled_sign':sign})
    W=tuple(W);assert len(lcu)==18 and mm(adj(W),W)==eye(4)
    assert success==scale(A(F(3,5)),P)
    for row in lcu:
        q=tuple(F(x) for x in row['quaternion']);T=actions[q][1]
        amplitude=S2*S5/10 if F(row['preparation_probability'])==F(1,10) else S5/10
        Reject.extend(scale(amplitude,add(scale(A(row['controlled_sign']),T),scale(A(-1),success))))
    Reject=tuple(Reject)
    success_effect=mm(adj(success),success);reject_effect=mm(adj(Reject),Reject)
    assert success_effect==scale(A(F(9,25)),P)
    assert reject_effect==add(Pm,scale(A(F(16,25)),P))
    assert add(success_effect,reject_effect)==eye(4) and rank(Reject)==4
    # Reading the group branch instead of coherently recombining does not
    # select a summand: every signed T is a unitary preserving both projectors.
    assert all(mm(T,P)==mm(P,T) for _,T in actions.values())
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_retained_selector_controls.py'}
    return {
        'schema':'marici.scattering.retained-selector-controls.v1',
        'status':'explicit_gauge_preserving_control_factorization_and_conditional_selector_with_retained_reject',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'factorization':{'field':'F_pi: (k,n,ell)->(k,n+ell-pi(ell),pi(ell))',
                         'matter':'M_g: (k,n,ell)->t_k*(pi(k),n+e_k-e_pi(k),ell)',
                         'joint':'U_hat_g=M_g F_pi=F_pi M_g',
                         'field_primitive':'lead momentum swap with compensating endpoint translation controlled by the two lead momenta',
                         'matter_primitive':'assisted matter swap plus diagonal native input phases',
                         'coincides_with_previous_joint_symmetry_on_G_zero':True,
                         'off_kernel_commutes_with_each_G_i':True,
                         'off_kernel_commutes_with_full_H':False,
                         'basis_tests':tests,'off_kernel_G_tests':off_kernel_tests,'group_compositions':compositions,
                         'controls':control_rows},
        'work_accounting':{'net_physical_charging_change':0,
                            'individual_stages_need_not_preserve_energy_or_ground':True,
                            'max_absolute_intermediate_charging_change_in_fixture':str(max_intermediate),
                            'nonzero_work_witness':witness,
                            'control_work_or_supply_not_derived':True},
        'coherent_selector':{'method':'prepare signed group control, controlled U_hat, unprepare, retain success and orthogonal reject',
                              'absolute_coefficient_norm':'5/3','nonzero_controller_branches':18,
                              'controller_preparation':lcu,'success_amplitude':'(3/5)*P_plus',
                              'success_effect':'(9/25)*P_plus','reject_effect':'P_minus+(16/25)*P_plus',
                              'completeness_verified':True,'reject_rank_on_ground':4,
                              'retained_reject_map':record(Reject),
                              'measuring_group_history_before_recombination_selects_doublet':False},
        'boundary':{'new_field_controls_required':True,'new_coherent_controller_required':True,
                    'addressable_assisted_swaps_and_native_phases_required':True,
                    'native_H_implements_protocol':False,'postselection_is_deterministic_preparation':False,
                    'failure_or_nonselected_records_erased':False,'physical_spin_or_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Test whether failure-conditioned retries of this retained selector converge to the plus doublet without erasing minus-sector or controller history; distinguish unconditional instruments from postselected preparation and quantify the flux-reader disturbance.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale retained-selector receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact matter/field swap factorization preserves each Gauss generator, with retained intermediate work.')
    print('PASS: coherent selector success=(3/5)P_plus, reject completeness exact; new controls remain explicit inputs.')


if __name__=='__main__':main()
