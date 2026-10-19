"""Charge completion and conditional rest gap for the existing seam-register law.

The transported source dynamics determines how a conserved label extends to
its bank. It does not select the supplied register energy parameters or units.
The rest Hamiltonian tested here is the prior seam law, not a sum of pulses.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,difference,rank,scale,mv,encoded
from check_neutron_rest_energy_preflight import nullspace
from check_seam_occupation_energy import local_certificate
from check_pentachoron_spin_interfaces import A,S2,S5


def psd_rank(M):
    a=[list(r) for r in M];count=0
    assert a==transpose(a)
    while a:
        pivot=a[0][0];assert pivot>=0
        if pivot==0:
            assert all(x==0 for x in a[0]);a=[r[1:] for r in a[1:]];continue
        count+=1
        a=[[a[i][j]-a[i][0]*a[0][j]/pivot for j in range(1,len(a))] for i in range(1,len(a))]
    return count


def main():
    paths={k:ROOT/p for k,p in {
        'transport':'research/strominger/results/neutron-seam-control-transport.json',
        'charge_prior':'research/voevodsky/charge-compatible-internal-contact.md',
        'seam_checker':'research/voevodsky/checkers/check_seam_occupation_energy.py'}.items()}
    packet=json.loads(paths['transport'].read_text());assert packet['status']=='passed';checks={}
    for p,h in packet['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_full_seam_transport_receipt']=True
    M=[list(map(F,r)) for r in packet['metric']];n=len(M);assert n==24
    native=[list(map(F,r)) for r in packet['native_energy']]
    seams=[[list(map(F,r)) for r in row['projector']] for row in packet['seam_controls']]
    pulses={(row['label'],row['frame']):[list(map(F,r)) for r in row['projector']] for row in packet['source_pulses']}
    rotation=[list(map(F,r)) for r in packet['native_rotation']]
    generators={'rotation':rotation,'native_energy':native}
    generators.update({'pulse:'+label:difference(eye(n),scale(2,P)) for (label,t),P in pulses.items() if t==0})
    generators.update({f'seam:{row["ordered_triangle_positions"][0]}-{row["ordered_triangle_positions"][1]}':P for row,P in zip(packet['seam_controls'],seams)})
    B=[list(map(F,r)) for r in packet['closure_generation']['basis_columns']]
    witnesses=packet['closure_generation']['witnesses'];x0=list(map(F,packet['initial_coordinates']))
    assert rank(B)==n and [r[0] for r in B]==x0
    for j,w in enumerate(witnesses[1:],1):
        assert w['parent']<j
        assert mv(generators[w['operator']],[r[w['parent']] for r in B])==[r[j] for r in B]
    # Algebraic implication: if Q x0=q x0 and Q commutes with every generator,
    # every verified word vector B_j has charge q. Since B is invertible,
    # Q B=q B implies Q=q I, without a diagonal/block ansatz for Q.
    checks['charge_uniqueness_from_replayed_cyclic_basis']=True
    C=eye(n);cold=[[F(i==j and i<18) for j in range(n)] for i in range(n)]
    assert all(mm(C,T)==mm(T,C) for T in generators.values())
    assert all(rank(difference(mm(cold,P),mm(P,cold)))==2 for P in pulses.values())
    checks['bank_must_share_the_declared_occupied_particle_label']=True
    # Explicit empty-vacuum completion, following the prior supplied sector
    # convention. No vacuum/particle transition is introduced by this model.
    Cv=[[F(0)]*(n+1)]+[[F(0)]+r for r in C]
    for name,T in generators.items():
        Tv=[[F(0)]*(n+1)]+[[F(0)]+r for r in T]
        # Unitary exchanges/rotation fix the vacuum; energy and seam
        # projectors annihilate it.
        Tv[0][0]=F(name=='rotation' or name.startswith('pulse:'))
        assert mm(Cv,Tv)==mm(Tv,Cv)
    checks['empty_vacuum_and_occupied_bank_sector_separated']=True
    native_rank=psd_rank(mm(M,native))
    for P in seams:
        assert mm(P,P)==P and psd_rank(mm(M,P))==1
        S=difference(C,P);assert mm(S,S)==S
    ground=nullspace(native+[r for P in seams for r in P],n)
    assert len(ground)==7
    checks['actual_native_and_seam_positivity_and_joint_kernel']=True
    # Freshly invoke the exact local spectral calculation. It supplies
    # h_e >= e_b I - delta P_e in the occupied sector. Hence
    # Hrest >= 21 e_b I + Hnative +(kappa-delta) sum P_e.
    # A common carrier zero vector times 21 matched-register ground vectors
    # saturates the bound; vacuum energy is 21 e_v.
    epsilon,J,kappa=F(1,4),F(1,2),F(1)
    trials=[(F(0),A(F(3,4)),A(F(1,4))),
            (F(1,8),S2*S5/4,S2/4),
            (F(3,8),3*S2/4,S2*S5/4)]
    reports=[]
    for g,rplus,rminus in trials:
        cert=local_certificate(epsilon,J,g,rplus,rminus)
        assert epsilon>0 and J>epsilon and kappa>epsilon and g>=0
        delta=cert['relative_seam_energy']
        assert delta*(rplus+rminus)==A(2*epsilon*J)
        # For these positive roots, the triangle inequality on vectors
        # (J+epsilon,2g) and (J-epsilon,-2g) gives rplus+rminus>=2J.
        # Therefore 0<delta<=epsilon<kappa, independent of decimal rounding.
        assert cert['matched_ground']-cert['inactive_ground']==delta
        reports.append({'epsilon':str(epsilon),'J':str(J),'kappa':str(kappa),'g':str(g),
                        'vacuum_ground':(21*cert['inactive_ground']).record(),
                        'occupied_ground':(21*cert['matched_ground']).record(),
                        'vacuum_subtracted_gap':(21*delta).record(),
                        'occupied_ground_multiplicity':len(ground)})
    assert reports[0]['vacuum_subtracted_gap']=={'0':'21/4'}
    checks['prior_local_spectral_certificates_freshly_recomputed']=True
    checks['many_register_ground_bound_has_actual_saturating_carrier_states']=True
    # Two legal supplied parameter completions on the exact same charge and
    # operator binding. This records nonselection, not a new fitted mechanism.
    alternatives=[]
    for e in (F(1,4),F(1,2)):
        j=2*e;k=4*e;cert=local_certificate(e,j,F(0),A(j+e),A(j-e))
        assert cert['relative_seam_energy']==A(e) and k>e
        alternatives.append({'epsilon':str(e),'J':str(j),'kappa':str(k),'g':'0','gap':str(21*e)})
    assert alternatives[0]['gap']!=alternatives[1]['gap']
    checks['source_binding_and_charge_do_not_select_the_register_gap']=True
    result={'status':'passed','checks':checks,
            'charge_completion':{'uniqueness':'Any conserved linear Q with Q x0=q x0 equals q I on the verified cyclic 24D closure.',
                'conditional_physical_labels':{'neutron_and_bank':{'electric_charge':0,'baryon_label':1},'empty_vacuum':{'electric_charge':0,'baryon_label':0}},
                'physical_label_origin':'Supplied identification as in prior charge-compatible internal-channel construction; only the extension to the bank is forced by commutation.'},
            'conditional_rest_model':{'occupied_projector':'C=I24, zero on appended vacuum',
                'seam_control':'S_e=C-P_e',
                'Hamiltonian':'H_native+kappa sum_e P_e+sum_e [epsilon n_e+J(n_e-S_e)^2-g X_e]',
                'new_neutral_registers':21,'dynamic_bank_is_not_these_registers':True,
                'vacuum_subtracted_gap':'21/2*(sqrt((J+epsilon)^2+4g^2)-sqrt((J-epsilon)^2+4g^2))',
                'conditions':'J>epsilon>0, kappa>epsilon, g>=0; zero bare occupied baseline in this model',
                'native_constraint_rank':native_rank,'occupied_ground_multiplicity':len(ground),
                'pulse_role':'Bound pulses remain charge-conserving driven interactions; they are not included as an autonomous summed rest Hamiltonian.',
                'trials':reports,'distinct_admissible_parameter_completions':alternatives},
            'scope':'A consistent conditional neutron-plus-bank rest-gap calculation under the existing supplied seam-register law. Not a source-selected neutron mass or physical-unit prediction.',
            'next_gate':'Identify epsilon, J, g and the energy/time normalization from source operations, or certify that the searched source packet leaves them independent.'}
    bound=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-charge-completed-rest-gap.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'conserved_occupied_label':'same on all 24 neutron/bank modes',
                      'conditional_rest_gap_at_prior_parameters':'21/4','ground_multiplicity':len(ground),
                      'alternative_admissible_gaps':[r['gap'] for r in alternatives],
                      'physical_neutron_mass_predicted':False},indent=2))

if __name__=='__main__':main()
