"""Reconstruct proton coefficients from their generating geometry, then
reverse the primitive triangle cycle while keeping its selected character.
No isotope assignment or attachment repair is made.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from itertools import permutations
import json
import sys

from check_reversed_coefficient_attachment import (
    SOURCE, verify, weight, ZERO, ONE, transpose, adjoint, multiply, conj,
    encode, trace)
BASE=Path(__file__).resolve().parents[1]
GENERATOR=BASE.parent/'nima/checkers/check_twelve_triangle_positive_geometry.py'
PRIMITIVES=GENERATOR.with_name('check_triangle_half_phase.py')
sys.path.insert(0,str(GENERATOR.parent))
import check_twelve_triangle_positive_geometry as geo

def lists(a): return [list(row) for row in a]
def conjugate(a): return [[conj(z) for z in row] for row in a]
def scaled_vector(z,v): return tuple(geo.zmul(z,x) for x in v)

def main():
    source_bytes=SOURCE.read_bytes(); source=json.loads(source_bytes)
    verified,rows=verify(source)
    store=source['objects']; root=store[source['root']]
    geometry=store[root['geometry']]['payload']
    triangles=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    labels=sorted({tuple(r['source'][1:]) for r in rows}); index={p:i for i,p in enumerate(labels)}
    original={s:[[ZERO]*36 for _ in range(36)] for s in ('raw','local','aligned')}
    for r in rows:
        original[r['source'][0]][index[tuple(r['target'][1:])]][index[tuple(r['source'][1:])]]=weight(r)
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):
        points['F_'+face]=geo.mean([points[v] for v in face])
    c=(ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA))
    c_reverse=tuple(conj(z) for z in c)
    C=geo.C; C_reverse=geo.mm(C,C)
    forward_vectors={}; reverse_vectors={}; projectors={}; reverse_projectors={}; rotations={}
    flags=[]; eigen_tests=[]; transport_tests=[]; double_reversal_tests=[]
    reference=geo.zmv(geo.transpose(tuple(points[k] for k in ('F_ABC','A','B'))),c)
    for row in triangles:
        edge=row['outer_arrow']; tri=row['triangle']
        X=geo.transpose(tuple(points[k] for k in tri))
        A=geo.mm(geo.mm(X,C),geo.inv(X))
        A_reverse=geo.mm(geo.mm(X,C_reverse),geo.inv(X))
        v=geo.zmv(X,c); vr=geo.zmv(X,c_reverse)
        R=tuple(tuple(Q(x) for x in r) for r in row['rotation'])
        forward_vectors[edge]=v; reverse_vectors[edge]=vr
        projectors[edge]=geo.projector(v); reverse_projectors[edge]=geo.projector(vr)
        rotations[edge]=R
        eigen_tests.append(geo.zmv(A,v)==scaled_vector(geo.OMEGA,v)
                           and geo.zmv(A_reverse,vr)==scaled_vector(geo.OMEGA,vr)
                           and geo.mm(A,A_reverse)==geo.I)
        transport_tests.append(geo.zmv(geo.transpose(R),v)==reference
            and geo.zmv(geo.transpose(R),vr)==tuple(conj(z) for z in reference))
        double_reversal_tests.append(geo.zmv(A_reverse,v)==scaled_vector(conj(geo.OMEGA),v))
        face=tuple(sorted(tri[0][2:])); outer=tuple(sorted(tri[1:]))
        for vertex in tri[1:]:
            flags.append((tuple('ABCD'),face,outer,(vertex,)))
    local=[[projectors[e]['xyz'.index(a)]['xyz'.index(b)] if e==f else ZERO
            for f,b in labels] for e,a in labels]
    local_reverse=[[reverse_projectors[e]['xyz'.index(a)]['xyz'.index(b)] if e==f else ZERO
            for f,b in labels] for e,a in labels]
    G=[[(geo.mm(rotations[e],geo.transpose(rotations[f]))['xyz'.index(a)]['xyz'.index(b)]/12,Q(0))
         for f,b in labels] for e,a in labels]
    assembled=tuple(forward_vectors[e]['xyz'.index(a)] for e,a in labels)
    assembled_reverse=tuple(reverse_vectors[e]['xyz'.index(a)] for e,a in labels)
    N=lists(geo.projector(assembled)); Nr=lists(geo.projector(assembled_reverse))
    reversed_return=multiply(Nr,multiply(G,local_reverse))
    outward_flags=set(flags)
    complete_flags={tuple(tuple(sorted(p[:k])) for k in (4,3,2,1)) for p in permutations('ABCD')}
    checks={
        'source_freshly_verified':verified['verified'],
        'twelve_triangles_reconstructed':len(triangles)==len(projectors)==12,
        'geometric_local_selection_reproduces_every_L_entry':local==original['raw'],
        'rotation_averaging_reproduces_every_G_entry':G==original['local'],
        'assembled_geometric_mode_reproduces_every_N_entry':N==original['aligned'],
        'all_primitive_cycles_and_inverse_cycles_have_declared_eigenvectors':all(eigen_tests),
        'forward_and_reverse_modes_transport_to_their_respective_seed':all(transport_tests),
        'primitive_cycle_inversion_conjugates_local_selection':local_reverse==conjugate(local),
        'primitive_cycle_inversion_leaves_real_averaging_unchanged':G==conjugate(G),
        'primitive_cycle_inversion_conjugates_assembled_mode':Nr==conjugate(N),
        'derived_reverse_is_not_original_mode':Nr!=N,
        'derived_reverse_matches_transpose_not_adjoint_of_return':Nr==transpose(N) and Nr!=adjoint(N),
        'reverse_generation_closes_its_own_protocol':multiply(G,local_reverse)==Nr and reversed_return==Nr,
        'reversing_cycle_and_character_together_restores_original_line':all(double_reversal_tests),
        'twelve_source_triangles_split_into_all_twenty_four_flags':len(flags)==24 and outward_flags==complete_flags,
        'reversing_flag_order_preserves_its_geometric_cells':all(set(f)==set(reversed(f)) for f in flags),
        'geometry_and_coefficient_source_unchanged':SOURCE.read_bytes()==source_bytes,
    }
    result={
        'verification_passed':all(checks.values()),'checks':checks,
        'source_root':source['root'],'source_sha256':sha256(source_bytes).hexdigest(),
        'generator_sha256':sha256(GENERATOR.read_bytes()).hexdigest(),
        'primitives_sha256':sha256(PRIMITIVES.read_bytes()).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'construction':{
            'seed_triangle':['F_ABC','A','B'],
            'cyclic_character':encode(geo.OMEGA),
            'coefficient_vector':encode(list(c)),
            'reversed_cycle_coefficient_vector':encode(list(c_reverse)),
            'forward':'v=X(1,omega,omega^2); P=v v*/(v*v); G=rotation average; N=assembled projector',
            'reverse':'C becomes C^-1 with omega held fixed; v becomes conjugate(v); L and N conjugate; G unchanged',
            'radial_flag_reversal':'changes body/face/edge/vertex traversal, not the cyclic operator by itself'},
        'mode_overlap_trace':encode(trace(multiply(Nr,N))),
        'conclusion':'Reversing the generating triangle cycle with a fixed character derives conjugated modes, '
            'rather than guessing a reversed coefficient matrix. Outward radial incidence alone does not '
            'specify this cycle reversal. No isotope closure or neutron complex has been constructed.'}
    output=BASE/'results/geometric_cycle_reversal.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
