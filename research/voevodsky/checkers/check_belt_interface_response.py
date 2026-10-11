"""Exact source-derived response of the bridge between paired belt faces.

Reuses prior minimal-interface-record and Schur-response methods; introduces
no rotor factors, record gaps, external coupling strengths or mass readout.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_collective_carrier_spectrum import characteristic, polynomial_product

BASE=Path(__file__).resolve().parents[1]


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def inverse(a):
    n=len(a);rows=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[pivot]=rows[pivot],rows[j]
        q=rows[j][j];rows[j]=[x/q for x in rows[j]]
        for i in range(n):
            if i!=j:
                q=rows[i][j];rows[i]=[x-q*y for x,y in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]


def determinant3(a):
    return (
        a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def evaluate(p,x):
    out=F(0)
    for c in p:out=out*x+c
    return out


def main():
    path=BASE/'results/collective_carrier_spectrum.json'
    raw=path.read_bytes();source=json.loads(raw)
    assert source['verification_passed'] and source['belt_aligned_sector_exactly_closed']
    K=[[F(x) for x in row] for row in source['belt_reduced_matrix']]
    n=list(map(F,source['belt_modal_norms']))
    odd=[[K[i][j]-K[i][j+3] for j in range(3)] for i in range(3)]
    p=characteristic(odd)
    assert p==list(map(F,source['belt_face_odd_characteristic_descending']))
    # The source bridge's unit mismatch vector has support on vertices 0,3.
    # Its resolvent is S(z)=[(K_odd-zI)^(-1)]_00, in the weighted metric.
    minor=[[odd[i][j] for j in (1,2)] for i in (1,2)]
    numerator=[-x for x in characteristic(minor)]
    inv=inverse(odd);inv2=mm(inv,inv)
    assert [row[0] for row in inv]==[F(1)]*3
    assert inv[0]==[x/n[0] for x in n[:3]]
    assert inv[0][0]==1 and inv2[0][0]==F(4485,1193)
    assert evaluate(numerator,F(0))/evaluate(p,F(0))==1
    # Exact resolvent checks at distinct negative probe energies (no poles).
    for z in map(F,(-1,-2,-3,-7)):
        shifted=[[odd[i][j]-z*int(i==j) for j in range(3)] for i in range(3)]
        assert inverse(shifted)[0][0]==evaluate(numerator,z)/evaluate(p,z)
    # Both controllability and observability are needed for minimality.
    e=[[F(1)],[F(0)],[F(0)]]
    v1=mm(odd,e);v2=mm(odd,v1)
    control=[[e[i][0],v1[i][0],v2[i][0]] for i in range(3)]
    observe=[[F(1),F(0),F(0)],odd[0],mm(odd,odd)[0]]
    dc,do=determinant3(control),determinant3(observe)
    assert dc!=0 and do!=0
    # Same interface value, different next Hamiltonian response.
    assert e[1][0]==0 and odd[0][1]!=0
    # Static Schur reduction of the actual stiffness M K, keeping the
    # bridge endpoints. Interior variables are retained in the full model.
    stiffness=[[n[i]*K[i][j] for j in range(6)] for i in range(6)]
    boundary=[0,3];interior=[1,2,4,5]
    A=[[stiffness[i][j] for j in boundary] for i in boundary]
    B=[[stiffness[i][j] for j in interior] for i in boundary]
    C=[[stiffness[i][j] for j in boundary] for i in interior]
    D=[[stiffness[i][j] for j in interior] for i in interior]
    correction=mm(mm(B,inverse(D)),C)
    schur=[[A[i][j]-correction[i][j] for j in range(2)] for i in range(2)]
    conductance=n[0]/2
    assert schur==[[conductance,-conductance],[-conductance,conductance]]
    assert conductance==F(1193,675)
    report={
        'verification_passed':True,
        'prior_methods_reused':['interface-required-record.md','mass-rotor-action-and-external-charge.md','collective-mechanics-prior-clues.md'],
        'boundary':'relative amplitude of the two triangles touching the actual shared-face bridge, indices 0 and 3',
        'new_independent_registers':0,
        'odd_sector_matrix':[[str(x) for x in row] for row in odd],
        'normalized_response':'S(z)=<(unit bridge mismatch),(K-zI)^(-1)(unit bridge mismatch)>',
        'response_numerator_descending':list(map(str,numerator)),
        'response_denominator_descending':list(map(str,p)),
        'static_normalized_response':'1',
        'response_derivative_at_zero':str(inv2[0][0]),
        'static_boundary_stiffness':str(conductance),
        'minimal_linear_response_state_dimension':3,
        'additional_coordinates_beyond_boundary_scalar':2,
        'controllability_determinant':str(dc),'observability_determinant':str(do),
        'scalar_closure_counterexample':'x=(0,0,0) and x=(0,1,0) have identical observed x0 but different (K_odd*x)0',
        'counterexample_response_difference':str(odd[0][1]),
        'coherent_return_bridge_overlap':'0',
        'external_coupling_formula':'A supplied neutral reference level epsilon with coupling g to this normalized bridge has Schur denominator epsilon-z-g^2*S(z). Neither epsilon nor g is selected here.',
        'zero_loading_result':'Equal boundary amplitudes have zero minimum energy; the bridge operator annihilates the coherent return, so coupling only through this mismatch leaves that state dark.',
        'rest_mass_generated':False,
        'scope':'Actual source-derived interface response and minimal retained coordinates, not physical vacuum identification or a relativistic self-energy calculation.',
        'source_sha256':sha256(raw).hexdigest()}
    (BASE/'results/belt_interface_response.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
