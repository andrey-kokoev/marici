"""Derive phase attachment on all 1836 typed arrows, not just N.

Contract: corresponding ports differ only by unit scalar phases; every
coefficient arrow must intertwine. The electron coefficients come from
reversed local cycles with the fixed source character.
"""
from collections import defaultdict, deque
from hashlib import sha256
from pathlib import Path
import json

from check_geometric_cycle_reversal import geo, SOURCE, verify, ONE, conj, encode
from check_reversed_coefficient_attachment import weight, times, div, ZERO

BASE=Path(__file__).resolve().parents[1]

def solve(edges,root):
    """d_target = ratio * d_source. Reverse edges are equation-solving
    steps, not new physical arrows or free inverse traversals."""
    adjacent=defaultdict(list)
    for i,(s,t,r) in enumerate(edges):
        adjacent[s].append((t,r,i))
        adjacent[t].append((s,div(ONE,r),i))
    values={root:ONE}; queue=deque([root]); tree=[]
    while queue:
        s=queue.popleft()
        for t,r,i in adjacent[s]:
            expected=times(r,values[s])
            if t not in values:
                values[t]=expected; queue.append(t); tree.append(i)
    defects=[i for i,(s,t,r) in enumerate(edges) if times(r,values[s])!=values[t]]
    return values,tree,defects


def main():
    original=SOURCE.read_bytes(); source=json.loads(original)
    evidence,rows=verify(source)
    objects=source['objects']; geometry=objects[objects[source['root']]['geometry']]['payload']
    triangles=geometry['triangles_and_transports']
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):
        points['F_'+face]=geo.mean([points[v] for v in face])
    coeff=(ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA))
    vectors={}; rotations={}
    for row in triangles:
        X=geo.transpose(tuple(points[k] for k in row['triangle']))
        vectors[row['outer_arrow']]=geo.zmv(X,coeff)
        rotations[row['outer_arrow']]=tuple(tuple(geo.F(x) for x in r) for r in row['rotation'])
    ports=sorted({tuple(p) for r in rows for p in (r['source'],r['target'])})
    root=('raw','AB','x')
    primitive_phase={p:div(vectors[p[1]]['xyz'.index(p[2])],conj(vectors[p[1]]['xyz'.index(p[2])])) for p in ports}
    calibration=primitive_phase[root]
    geometric_phase={p:div(d,calibration) for p,d in primitive_phase.items()}
    # Host coefficient h, reversed-cycle coefficient conjugate(h):
    # h d_source = d_target conjugate(h).
    edges=[(tuple(r['source']),tuple(r['target']),div(weight(r),conj(weight(r)))) for r in rows]
    phases,tree,defects=solve(edges,root)
    all_ports_reached=set(phases)==set(ports)
    # Transport the seed phase operator rather than fitting an assembled N.
    seed=vectors['AB']; seed_D=tuple(tuple(div(seed[i],conj(seed[i])) if i==j else ZERO for j in range(3)) for i in range(3))
    transported=True
    for edge,R in rotations.items():
        expected=tuple(tuple(primitive_phase[('raw',edge,'xyz'[i])] if i==j else ZERO for j in range(3)) for i in range(3))
        actual=geo.zmm(geo.zmm(geo.zreal(R),seed_D),geo.zreal(geo.transpose(R)))
        transported &= actual==expected
    # One altered relative phase is an exact negative control: its mismatch
    # cannot be absorbed into consistent port phases on this same graph.
    broken=list(edges)
    s,t,r=broken[0]; broken[0]=(s,t,times(r,geo.OMEGA))
    _,_,bad_defects=solve(broken,root)
    reroot=('local','CD','z')
    other,_,other_defects=solve(edges,reroot)
    common=div(ONE,phases[reroot])
    # A global seed phase changes all primitive attachment phases by one
    # common factor; canonical root normalization removes it.
    seed_phase=geo.OMEGA
    rephased={p:div(times(seed_phase,vectors[p[1]]['xyz'.index(p[2])]),
                      conj(times(seed_phase,vectors[p[1]]['xyz'.index(p[2])]))) for p in ports}
    same_normalized=all(div(rephased[p],rephased[root])==geometric_phase[p] for p in ports)
    changed_by_stage=defaultdict(int)
    mismatch_without=[]
    for i,r in enumerate(rows):
        if weight(r)!=conj(weight(r)):
            changed_by_stage[r['source'][0]]+=1; mismatch_without.append(i)
    checks={
        'source_freshly_verified':evidence['verified'],
        'all_108_ports_connected':all_ports_reached and len(ports)==108,
        'all_1836_arrow_constraints_satisfied':not defects and len(edges)==1836,
        'spanning_tree_has_107_constraints':len(tree)==107 and len(set(tree))==107,
        'all_1729_remaining_constraints_close':len(edges)-len(tree)==1729 and not defects,
        'geometric_local_modes_reconstruct_all_port_phases':phases==geometric_phase,
        'seed_phase_operator_transports_consistently':transported,
        'all_port_phases_are_unit_norm':all(times(d,conj(d))==ONE for d in phases.values()),
        'same_coordinate_phase_on_all_three_stages':all(phases[('raw',e,a)]==phases[('local',e,a)]==phases[('aligned',e,a)] for e,a in {(p[1],p[2]) for p in ports}),
        'phase_map_matches_each_arrow_not_just_return':all(
            times(weight(r),phases[tuple(r['source'])])==times(phases[tuple(r['target'])],conj(weight(r))) for r in rows),
        'removing_alignment_breaks_fixed_frame_arrows':bool(mismatch_without),
        'changing_one_relative_phase_is_rejected':bool(bad_defects),
        'rerooting_changes_only_one_global_factor':not other_defects and all(other[p]==times(common,phases[p]) for p in ports),
        'global_seed_phase_does_not_change_normalized_attachment':same_normalized,
        'intermediate_phase_factor_can_be_absorbed_without_deleting_source_arrows':all(
            times(times(phases[tuple(r['target'])],conj(weight(r))),conj(phases[tuple(r['source'])]))==weight(r) for r in rows),
        'source_unchanged':SOURCE.read_bytes()==original,
    }
    report={
        'verification_passed':all(checks.values()),'checks':checks,
        'contract':{
            'electron_rule':'reverse the local triangle cycles, holding their character fixed',
            'port_matching':'same typed stage/triangle/axis labels',
            'attachment_class':'invertible unit scalar at each corresponding port; no mixing of coordinate channels',
            'compatibility':'h_arrow d_source = d_target conjugate(h_arrow), for every original arrow',
            'root':list(root),'root_phase':encode(ONE),
            'status':'explicit frame-registration law, not generated by an undecorated spatial point'},
        'solution':{
            'ports':len(ports),'arrows':len(edges),'spanning_tree_edges':len(tree),
            'independent_cycles':len(edges)-len(ports)+1,
            'phase_classes_modulo_global_factor':1,
            'basis':'connected constraint graph fixes every phase relative to the root; all cycle constraints agree',
            'nontrivial_cycle_obstructions':len(defects),
            'port_phases':[{'port':list(p),'value':encode(phases[p])} for p in ports],
            'spanning_tree_arrow_indices':tree},
        'fixed_frame_mismatches_without_alignment':dict(changed_by_stage),
        'negative_control_defect_count':len(bad_defects),
        'retention':{
            'sufficient':'oriented seed triangle frame, selected character, real tetrahedral transports, typed port correspondence',
            'phase_table':'reconstructible from that retained data; need not be an independent stored complex',
            'bare_barycenter':'does not supply the oriented frame or character',
            'path_identity':'the phase change preserves every original arrow label; phases telescope along each path'},
        'conclusion':'One normalized phase attachment exists and is reconstructed from the local generated modes and transports. '
            'Its connection has no cycle obstruction. The frozen scalar-frame contract supplies no second inequivalent phase class or indispensable extra carrier.',
        'source_root':source['root'],'source_sha256':sha256(original).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (BASE/'results/retained_phase_attachment.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='solution'},indent=2))
    print(json.dumps({k:v for k,v in report['solution'].items() if k not in ('port_phases','spanning_tree_arrow_indices')},indent=2))
    if not report['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
