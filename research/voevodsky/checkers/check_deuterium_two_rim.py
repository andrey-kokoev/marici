"""Actual two-rim coefficient attachment and static belt response.

This is the belt-side interface map; no scalar electron replacement, nuclear
binding energy, physical vacuum shift or measured mass is silently inserted.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_belt_interface_response import inverse, mm
from check_collective_carrier_spectrum import characteristic

BASE=Path(__file__).resolve().parents[1]


def main():
    coordinate_path=BASE/'results/belt_three_by_twelve_store.json'
    geometry_path=BASE/'results/coupled_six_piece_belt_store.json'
    energy_path=BASE/'results/collective_carrier_spectrum.json'
    coordinates=json.loads(coordinate_path.read_bytes())
    geometry=json.loads(geometry_path.read_bytes())['record']
    source=json.loads(energy_path.read_bytes())
    triangles=[geometry['triangles'][i] for i in coordinates['triangle_order']]
    lower=[];upper=[]
    for i,triangle in enumerate(triangles):
        vertices=triangle[1:]
        if all(v.startswith('L') for v in vertices):lower.append(i)
        if all(v.startswith('U') for v in vertices):upper.append(i)
    assert lower==[1,7,13] and upper==[4,10,16]
    # Each rim records all three source boundary edges; no bridge endpoint
    # trace is renamed as a rim trace.
    assert {frozenset(triangles[i][1:]) for i in lower}=={frozenset(('L0','L1')),frozenset(('L1','L2')),frozenset(('L2','L0'))}
    assert {frozenset(triangles[i][1:]) for i in upper}=={frozenset(('U0','U1')),frozenset(('U1','U2')),frozenset(('U2','U0'))}
    K=[[F(x) for x in row] for row in source['belt_reduced_matrix']]
    n=list(map(F,source['belt_modal_norms']))
    # Full aligned-state metric is 3*n, not one-sector n. Both physical rim
    # traces are the average over their three sector-related triangle modes.
    T=[[F(i==j) for j in range(6)] for i in (1,4)]
    B=[1,4];J=[0,2,3,5]
    stiffness=[[3*n[i]*K[i][j] for j in range(6)] for i in range(6)]
    D=[[stiffness[i][j] for j in J] for i in J]
    C=[[stiffness[i][j] for j in B] for i in J]
    extension=mm(inverse(D),C)
    extension=[[-x for x in row] for row in extension]
    E=[[F(0),F(0)] for _ in range(6)]
    for row,i in enumerate(B):E[i][row]=1
    for row,i in enumerate(J):E[i]=extension[row]
    assert mm(T,E)==[[F(1),F(0)],[F(0),F(1)]]
    residual=mm(stiffness,E)
    assert all(x==0 for i in J for x in residual[i])
    effective=mm([list(row) for row in zip(*E)],residual)
    c=effective[0][0]
    assert c>0 and effective==[[c,-c],[-c,c]]
    # Exact retained decomposition a=E*b+r with T*r=0. The energy cross
    # term vanishes for every retained residual, not just this example.
    assert all(residual[i]==[0,0] for i in J)
    test=[F(i-2,7) for i in range(6)]
    b=[test[i] for i in B]
    lifted=[sum(x*y for x,y in zip(row,b)) for row in E]
    r=[x-y for x,y in zip(test,lifted)]
    assert [r[i] for i in B]==[0,0]
    def energy(v):return sum(v[i]*sum(stiffness[i][j]*v[j] for j in range(6)) for i in range(6))
    assert energy(test)==c*(b[0]-b[1])**2+energy(r)
    # Two-component dynamic response: lower/upper equal and opposite traces
    # access the face-even and face-odd subspaces respectively.
    blocks={}
    for sign,label in ((1,'equal_rims'),(-1,'opposite_rims')):
        block=[[K[i][j]+sign*K[i][j+3] for j in range(3)] for i in range(3)]
        poles=characteristic(block)
        minor=[[block[i][j] for j in (0,2)] for i in (0,2)]
        numerator=[-x for x in characteristic(minor)]
        blocks[label]={'operator':[[str(x) for x in row] for row in block],
                       'normalized_response_numerator_descending':list(map(str,numerator)),
                       'normalized_response_denominator_descending':list(map(str,poles))}
        for t in (F(1,10),F(1),F(3)):
            shifted=[[block[i][j]+t*int(i==j) for j in range(3)] for i in range(3)]
            from check_belt_interface_response import evaluate
            assert inverse(shifted)[1][1]==evaluate(numerator,-t)/evaluate(poles,-t)
    # The native state has equal rim amplitudes and zero gluing energy;
    # opposite signs cost energy rather than producing a negative binding.
    equal_energy=c*(F(1)-F(1))**2
    opposite_energy=c*(F(1)-F(-1))**2
    assert equal_energy==0 and opposite_energy>0
    result={'verification_passed':True,
            'active_obligation':'attachment transport; belt-side joint maps before particle binding readout',
            'lower_rim_triangles':lower,'upper_rim_triangles':upper,
            'trace_rule':'Mean retained mode coefficient on each rim, in the C3-aligned sector; lower=a1, upper=a4',
            'joint_trace_matrix':[[str(x) for x in row] for row in T],
            'minimum_energy_extension':[[str(x) for x in row] for row in E],
            'aligned_metric':'diag(3*n), retaining three sectors',
            'effective_energy':'c*|lower-upper|^2',
            'effective_coefficient_exact':str(c),
            'effective_coefficient_decimal':float(c),
            'full_boundary_matrix':[[str(x) for x in row] for row in effective],
            'residual_retained_dimension':4,
            'retained_energy_decomposition':True,
            'dynamic_response_channels':blocks,
            'equal_rim_energy':str(equal_energy),'opposite_unit_rim_energy':str(opposite_energy),
            'binding_sign_result':'Positive source gluing is a compatibility penalty, not an attractive binding offset. With zero constituent constraint baselines it supplies no state below breakup.',
            'proton_rim_map_scope':'Geometric face matching does not select the proton coefficient adapter; none is fitted here.',
            'electron_rim_map_scope':'The electron boundary-cell source is rank-two spinorial; a scalar rim attachment requires a typed spinor channel or covariant pairing, not replacement by one scalar.',
            'nuclear_binding_derived':False,'atomic_binding_derived':False,
            'source_sha256':{str(p.relative_to(BASE.parent)):sha256(p.read_bytes()).hexdigest() for p in (coordinate_path,geometry_path,energy_path)}}
    (BASE/'results/deuterium_two_rim.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
