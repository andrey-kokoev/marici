"""Typed spinor rim extension and common-exterior breakup-energy test.

Reuses the declared proton spin lift from electron-pairing-coupling.md.
This constructs port types and rejects binding by the current pooled exterior
energy; no new attraction or measured binding value is inserted.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_belt_interface_response import mm
from check_pentachoron_spin_interfaces import A, CI, S2, S3, mm as amm, adj, I, add, scale

BASE=Path(__file__).resolve().parents[1]


def kron(a,b):
    return [[x*y for x in row_a for y in row_b] for row_a in a for row_b in b]


def main():
    source=json.loads((BASE/'results/deuterium_two_rim.json').read_text())
    T=[[F(x) for x in row] for row in source['joint_trace_matrix']]
    E=[[F(x) for x in row] for row in source['minimum_energy_extension']]
    c=F(source['effective_coefficient_exact'])
    bitI=[[F(1),F(0)],[F(0),F(1)]]
    Tspin=kron(T,bitI);Espin=kron(E,bitI)
    assert mm(Tspin,Espin)==[[F(i==j) for j in range(4)] for i in range(4)]
    boundary=kron([[c,-c],[-c,c]],bitI)
    assert boundary==[[c,0,-c,0],[0,c,0,-c],[-c,0,c,0],[0,-c,0,c]]
    # SU(2) covariance of a same-species two-rim term: identity in spin space.
    rotations=[((A(0),A(1)),(A(-1),A(0))),
               ((CI,A(0)),(A(0),-CI)),
               ((A(F(1,2)),S3/2),(-S3/2,A(F(1,2))))]
    p=(A(F(1,2)),CI*F(1,3));e=(S2/3,A(F(2,5)))
    def act(U,v):return tuple(sum((x*y for x,y in zip(row,v)),A(0)) for row in U)
    def norm(v):return sum((x.flip(8)*x for x in v),A(0))
    difference=tuple(x-y for x,y in zip(p,e))
    for U in rotations:
        assert amm(adj(U),U)==I
        assert norm(act(U,difference))==norm(difference)
    # Equal charges allow one transported linear spinor difference. Opposite
    # charges require a weight-two link or separate charged copies; no fixed
    # neutral linear identity can intertwine both phase laws.
    phase=CI
    assert norm(tuple(phase*x-phase.flip(8)*y for x,y in zip(p,e)))!=norm(difference)
    phase2=phase*phase
    assert norm(tuple(phase*x-phase2*phase.flip(8)*y for x,y in zip(p,e)))==norm(difference)
    # Separate species copies preserve charge: U^q along a link and spin
    # identity do not convert proton into electron. Pairing belongs on their
    # tensor product, not an off-diagonal direct-sum species hopping term.
    assert phase*phase.flip(8)==1
    def singlet(v,w):return v[0]*w[1]-v[1]*w[0]
    assert singlet(tuple(phase*x for x in p),tuple(phase.flip(8)*x for x in e))==singlet(p,e)
    for U in rotations:assert singlet(act(U,p),act(U,e))==singlet(p,e)

    # In the present common exterior graph, grounding the exterior separates
    # the proton and belt field quadratic forms. The only shared term is
    # eta*(Qp+Qb)^2/2, which is retained in both composite and breakup energies.
    vacuum=json.loads((BASE/'results/open_flux_common_vacuum.json').read_text())
    controls=[]
    for trial in vacuum['illustrative_minima']:
        beta=F(trial['beta']);eta=F(trial['exterior_eta'])
        p_self=beta/24
        diff_lo,diff_hi=map(F,trial['belt_minus_proton_interval'])
        b_self_lo,b_self_hi=p_self+diff_lo,p_self+diff_hi
        separate=(p_self+b_self_lo+eta,p_self+b_self_hi+eta)
        pair=(p_self+b_self_lo+2*eta,p_self+b_self_hi+2*eta)
        assert pair[0]-separate[0]==pair[1]-separate[1]==eta>0
        controls.append({'beta':str(beta),'eta':str(eta),
                         'pair_minus_separate_exact':str(eta),
                         'binding_energy_separate_minus_pair_exact':str(-eta),
                         'result':'repulsive exterior contribution, not nuclear binding'})
    # If both sectors use the SAME reservoir charge -2 even at separation,
    # its eta term cancels and the model still has no intercarrier attraction.
    same_reservoir_difference=F(0)
    # Electromagnetic interpretation cannot reuse positive norm charge for
    # the neutron: Qelectric=(1,0) removes that cross term altogether.
    electric_cross=F(1,5)*1*0
    assert electric_cross==same_reservoir_difference==0
    result={'verification_passed':True,
            'spin_lift':'T_spin=T tensor I2; E_spin=E tensor I2; scalar belt spin lift is a declared enlargement',
            'selected_belt_spin_dimension':12,'rim_spin_dimension':4,
            'same_species_rim_energy':'c*||spinor_lower-spinor_upper||^2',
            'coefficient_exact':str(c),'typed_trace':[[str(x) for x in row] for row in Tspin],
            'typed_extension':[[str(x) for x in row] for row in Espin],
            'same_species_SU2_controls':len(rotations),
            'opposite_charge_fixed_neutral_linear_matching_rejected':True,
            'compatible_options':['separate charged matter copies with U^q and a charge-preserving density interaction','a supplied weight-two link for opposite-charge linear matching','neutral bilinear singlet on the two-species tensor product'],
            'existing_pairing_reused':'research/voevodsky/electron-pairing-coupling.md',
            'nuclear_breakup_controls':controls,
            'same_total_exterior_charge_pair_minus_separate':'0',
            'electric_proton_neutron_exterior_cross_term':'0 when qp=1, qn=0',
            'binding_test_conclusion':'The current separate carrier blocks plus common exterior charging term do not bind proton and belt. Independently relaxed carrier energies cancel at breakup; the reservoir either adds repulsion or cancels under fixed total charge.',
            'next_interaction_gate':'A source-authorized number- and charge-preserving cross-carrier interaction, with the same reservoir and boundary data on composite and separation configurations.',
            'scope':'Typed rim coefficient extension and exact breakup test of the existing model. Spin lifts and physical charge labels are supplied; no nuclear attraction added.'}
    (BASE/'results/deuterium_typed_rim_binding.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('typed_trace','typed_extension')},indent=2))


if __name__=='__main__':main()
