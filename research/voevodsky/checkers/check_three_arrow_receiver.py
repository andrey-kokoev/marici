"""Three incoming primitive arrows and a cyclic-compatible pullback.
The primitive graph is distinct from its linear signal interpretation.
No return arrows, second K4, or spatial apex position are supplied.
"""
from itertools import permutations, product, combinations
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json
from check_geometric_cycle_reversal import geo, ONE, ZERO, conj
from check_reversed_coefficient_attachment import times, plus, div, rank, encode, sub

BASE=Path(__file__).resolve().parents[1]
PRIMITIVE_SOURCE=BASE.parent/'nima/checkers/check_triangle_half_phase.py'
OMEGA=geo.OMEGA
OMEGA2=times(OMEGA,OMEGA)
C=[[ZERO,ONE,ZERO],[ZERO,ZERO,ONE],[ONE,ZERO,ZERO]]

def cycle(x): return (x[1],x[2],x[0])
def scale(a,x): return tuple(times(a,z) for z in x)
def decode(z): return (z,times(OMEGA,z),times(OMEGA2,z))
WEIGHTS=(ONE,OMEGA2,OMEGA)
def images(x): return tuple(times(w,z) for w,z in zip(WEIGHTS,x))
def agrees(x,active=(0,1,2)):
    values=images(x)
    return len({values[i] for i in active})<=1

def equations(weights,active=(0,1,2)):
    if not active: return []
    first=active[0]; rows=[]
    for j in active[1:]:
        row=[ZERO]*3; row[first]=weights[first]; row[j]=(-weights[j][0],-weights[j][1]); rows.append(row)
    return rows

def simple_cycles(edges):
    vertices=sorted({x for e in edges for x in e}); found=set()
    for k in range(2,len(vertices)+1):
        for p in permutations(vertices,k):
            if all((p[i],p[(i+1)%k]) in edges for i in range(k)):
                found.add(min(p[i:]+p[:i] for i in range(k)))
    return found

def main():
    proton={(a,b) for a in 'ABCD' for b in 'ABCD' if a!=b}
    added={(a,'e') for a in 'ABC'}; network=proton|added
    cover=[]
    for a,b in sorted(network):
        path=[a,b]
        if b!='e': path+=['e'] if b in 'ABC' else ['A','e']
        cover.append(path)
    # Linear channels K at A,B,C and receiver K at e. The face action is
    # C(a,b,c)=(b,c,a). Retain its existing omega eigencharacter.
    eigen_constraints=[[sub(C[i][j],OMEGA if i==j else ZERO) for j in range(3)] for i in range(3)]
    matching=equations(WEIGHTS)
    # Equal nullspaces proven by exact rank of the stacked constraints.
    nullspace_same=rank(eigen_constraints)==rank(matching)==rank(eigen_constraints+matching)==2
    samples=[(Q(a,3),Q(b,5)) for a,b in product(range(-3,4),repeat=2)]
    covariance=all(cycle(decode(z))==decode(times(OMEGA,z)) for z in samples)
    inverses=all(agrees(decode(z)) and images(decode(z))==(z,z,z) for z in samples)
    deletions=[]
    for missing in range(3):
        active=tuple(i for i in range(3) if i!=missing)
        bad=list(decode(ONE)); bad[missing]=ZERO; bad=tuple(bad)
        deletions.append({'removed_arrow':'ABC'[missing]+'→e',
            'remaining_pullback_dimension':3-rank(equations(WEIGHTS,active)),
            'counterexample_inputs':encode(list(bad)),
            'incoming_images':encode(list(images(bad))),
            'remaining_agree':agrees(bad,active),'full_compatibility_fails':not agrees(bad)})
    # If f_i are nonzero scalars and their equal-output pullback must be the
    # omega eigenline, f_A=omega f_B=omega^2 f_C. Fix f_A=1.
    derived=(ONE,div(ONE,OMEGA),div(ONE,OMEGA2))
    unweighted=(ONE,ONE,ONE)
    nontrivial=decode(ONE)
    fixed_target_constraints=eigen_constraints+[
        [sub(ONE,OMEGA),ZERO,ZERO]]
    checks={
        'twelve_original_primitive_arrows_unchanged':len(proton)==12 and proton<=network,
        'exactly_three_new_incoming_arrows':network-proton==added and len(network)==15,
        'receiver_is_sink_without_return_arrows':not any(a=='e' for a,b in network),
        'new_four_vertex_subgraph_is_not_another_twelve_arrow_copy':len({(a,b) for a,b in network if a in 'ABCe' and b in 'ABCe'})==9,
        'all_closed_primitive_cycles_remain_old':simple_cycles(network)==simple_cycles(proton),
        'all_fifteen_arrows_have_terminal_path_witness':all(path[-1]=='e' and all((a,b) in network for a,b in zip(path,path[1:])) for path in cover)
            and set().union(*(set(zip(p,p[1:])) for p in cover))==network,
        'incoming_coefficients_follow_existing_character':derived==WEIGHTS,
        'pullback_is_exactly_existing_omega_eigenline':nullspace_same,
        'common_receiver_value_reconstructs_compatible_triple':inverses,
        'face_cycle_acts_covariantly_on_receiver_value':covariance,
        'each_incoming_arrow_is_deletion_essential_for_compatibility':all(r['remaining_agree'] and r['full_compatibility_fails'] and r['remaining_pullback_dimension']==2 for r in deletions),
        'three_unweighted_maps_fail_selected_mode':rank(equations(unweighted))==2 and len({times(w,x) for w,x in zip(unweighted,nontrivial)})>1,
        'strict_cycle_invariant_target_kills_nonzero_selected_mode':rank(fixed_target_constraints)==3,
        'reversing_cycle_reverses_incoming_phase_pattern':tuple(conj(x) for x in WEIGHTS)==(ONE,OMEGA,OMEGA2),
        'common_nonzero_rescaling_changes_no_compatibility':all(rank(equations(tuple(times(c,w) for w in WEIGHTS))+matching)==2 for c in (OMEGA,(Q(2),Q(0)),(Q(1),Q(1)))),
    }
    packet={'kind':'three-arrow-cyclic-receiver',
        'primitive_vertices':list('ABCD')+['e'],
        'proton_arrows':[list(e) for e in sorted(proton)],'incoming_arrows':[list(e) for e in sorted(added)],
        'channel_type':'K=Q(sqrt(-3)) at each of A,B,C,e',
        'cyclic_action':'C(a,b,c)=(b,c,a)',
        'selected_character':encode(OMEGA),
        'incoming_weights':{a:encode(w) for a,w in zip('ABC',WEIGHTS)},
        'pullback':'{(a,b,c): a=omega^2 b=omega c}',
        'decoder':'z -> (z,omega z,omega^2 z)',
        'receiver_action':'z -> omega z under the source face cycle',
        'terminal_path_cover':cover,
        'source_rule':'retain the existing omega character, permit nonzero scalar channel maps, and normalize the A leg to 1',
        'not_supplied':['an apex height','barycenter identification','a full coefficient protocol for the new receiver','particle charge or mass']}
    report={'verification_passed':all(checks.values()),'checks':checks,
        'primitive_arrow_count':len(network),'old_simple_cycle_count':len(simple_cycles(proton)),
        'pullback_complex_dimension':1,'deletion_tests':deletions,
        'outcome':'Three incoming maps realize the selected cyclic line as an exact compatibility pullback. Each is essential to that relation, although none enters a closed traversal. The new vertex is a receiving channel, not another complete four-state arrow network.',
        'qualification':'This derives the maps within the stated scalar-channel and fixed-character contract. The bare fifteen-arrow graph alone does not determine them.',
        'primitive_source_sha256':sha256(PRIMITIVE_SOURCE.read_bytes()).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/three_arrow_receiver_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/three_arrow_receiver.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
