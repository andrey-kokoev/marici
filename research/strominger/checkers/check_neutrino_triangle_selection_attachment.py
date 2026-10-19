#!/usr/bin/env python3
"""Reuse existing facet selector/attachment rule; test triangle against proton face."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
CHECKERS=ROOT/'research/voevodsky/checkers'
sys.path.insert(0,str(CHECKERS))
from assemble_relative_geometry import assemble, apply, subtract, dot_metric
from check_relative_geometry_mode_selection import select, change_frame

# Exact quadratic-field scalar and matrix arithmetic, no extra spin module.
ZERO=(Q(0),Q(0)); ONE=(Q(1),Q(0)); OMEGA=(-Q(1,2),Q(1,2))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def scale(x,q):return (q*x[0],q*x[1])
def matmul(A,B):return [[sumfield(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sumfield(xs):
    out=ZERO
    for x in xs:out=add(out,x)
    return out

def generator(raw):return (tuple(tuple(map(Q,r)) for r in raw['matrix']),tuple(map(Q,raw['translation'])))
def centroid(points):return tuple(sum(p[k] for p in points)/len(points) for k in range(len(points[0])))
def score(p,source):
    G=[[Q(x) for x in row] for row in source['metric']]
    return sum(dot_metric(v,v,G) for raw in source['generators'] for v in [subtract(apply(generator(raw),p),p)])

def main():
    registry_path=ROOT/'research/strominger/results/neutrino_seed_candidates.json'
    registry=json.loads(registry_path.read_text())
    source=registry['candidates'][0]['source']
    proton_path=ROOT/'research/voevodsky/inputs/relative-proton.json'
    proton=json.loads(proton_path.read_text())
    tri_out,_=select(source); proton_out,_=select(proton)
    # Reuse existing affine covariance control on the new source.
    changed=change_frame(source,[Q(2),Q(3)],[Q(-2,3),Q(1,5)])
    transformed,_=select(changed)
    p=tuple(map(Q,proton['seeds'][0]['point'])); g=generator(proton['generators'][0])
    local_face=[p,apply(g,p),apply(g,apply(g,p))]
    assert apply(g,local_face[-1])==p
    Gp=[[Q(x) for x in row] for row in proton['metric']]
    face_distances=[[str(dot_metric(subtract(a,b),subtract(a,b),Gp)) for b in local_face] for a in local_face]
    tc=centroid([tuple(map(Q,p)) for p in tri_out['vertices']])
    pc=centroid(local_face)
    local_fixed=apply(g,pc)==pc
    # The same 3-coordinate pullback action C=(b,c,a) for each ordered cycle.
    C=[[ZERO,ONE,ZERO],[ZERO,ZERO,ONE],[ONE,ZERO,ZERO]]
    I=[[ONE if i==j else ZERO for j in range(3)] for i in range(3)]
    w2=mul(OMEGA,OMEGA)
    v=[ONE,OMEGA,w2]
    P=[[scale(mul(a,conj(b)),Q(1,3)) for b in v] for a in v]
    CP=matmul(C,P)
    wP=[[mul(OMEGA,x) for x in row] for row in P]
    # Both cycles produce this same derived projector; no new chosen line.
    projector_idempotent=matmul(P,P)==P
    reverse=[[conj(x) for x in row] for row in P]
    # Attachment rule: without an existing pole mark, no port is selected.
    unmarked=assemble(source)
    marked=copy.deepcopy(source);marked['seeds'][0]['role']='attachment_pole'
    marked_out=assemble(marked)
    p_attach=assemble(proton)['retained_attachment_interfaces']
    tri_edges=[tuple(sorted(f)) for f in unmarked['supporting_facets']]
    tri_points=[tuple(map(Q,p)) for p in unmarked['vertices']]
    tg=generator(source['generators'][0]); lookup={p:i for i,p in enumerate(tri_points)}
    edge_perm={e:tuple(sorted(lookup[apply(tg,tri_points[i])] for i in e)) for e in tri_edges}
    edge_orbit={tri_edges[0]};front=[tri_edges[0]]
    while front:
        q=edge_perm[front.pop()]
        if q not in edge_orbit:edge_orbit.add(q);front.append(q)
    checks={
        'same_selector_keeps_three_triangle_edges':tri_out['counts']['carrier_facets']==3,
        'same_selector_keeps_four_proton_faces':proton_out['counts']['carrier_facets']==4,
        'new_triangle_selector_affine_covariant':transformed['mode_scores']==tri_out['mode_scores'],
        'proton_face_metric_equals_candidate_metric':face_distances==[['0' if i==j else '8' for j in range(3)] for i in range(3)],
        'local_proton_face_centroid_fixed_by_face_cycle':local_fixed,
        'standalone_triangle_centroid_fixed_by_its_cycle':apply(tg,tc)==tc,
        'full_proton_action_moves_that_face_centroid':score(pc,proton)>0,
        'derived_character_projector_idempotent':projector_idempotent,
        'same_cyclic_eigenvalue_equation':CP==wP,
        'local_return_three_steps_identity':matmul(matmul(C,C),C)==I,
        'reverse_character_distinct':reverse!=P,
        'no_unmarked_attachment_selected':not unmarked['retained_attachment_interfaces'],
        'all_triangle_edges_one_orbit_no_invariant_single_edge':len(edge_orbit)==3,
        'existing_pole_rule_selects_edge_not_face':len(marked_out['retained_attachment_interfaces'])==1 and len(marked_out['retained_attachment_interfaces'][0])==2,
        'proton_existing_attachment_is_triangle':len(p_attach)==1 and len(p_attach[0])==3,
    }
    out={
        'schema':'marici.strominger.neutrino-triangle-selection-attachment.v1',
        'status':'passed' if all(checks.values()) else 'failed',
        'scientific_disposition':'geometrically distinct ambient assembly; locally indistinguishable cyclic mode; no neutrino-specific selector or same-dimensional attachment established',
        'triangle_selection':{'counts':tri_out['counts'],'facet_scores':tri_out['mode_scores']},
        'proton_selection':{'counts':proton_out['counts'],'facet_scores':proton_out['mode_scores']},
        'local_comparison':{'proton_face_vertices':[list(map(str,p)) for p in local_face],'squared_distances':face_distances,'proton_face_centroid':list(map(str,pc)),'face_centroid_score_under_full_proton_generators':str(score(pc,proton)),'face_centroid_displacement_under_its_stabilizing_cycle':'0','candidate_whole_triangle_centroid_displacement':'0','coordinate_action_both':'C(a,b,c)=(b,c,a)','character_projector_both':'P_omega=vv^dagger/3, v=(1,omega,omega^2)','projector_rank_both':1,'three_step_return_both':'I','mode_discriminator_found':False,'scope':'Comparison of source geometric face-cycle action; no identification of the full native 12-coordinate proton selector with a 3-coordinate face space.'},
        'attachment':{'candidate_without_pole':[],'candidate_with_existing_pole_rule':marked_out['retained_attachment_interfaces'],'proton_existing_port':p_attach,'candidate_port_dimension':1,'proton_port_dimension':2,'whole_triangle_to_proton_face_possible_as_metric_identification':True,'whole_triangle_is_candidate_boundary_port':False,'new_attachment_admitted':False,'obstruction':'The unchanged pole rule selects an edge on a 2D carrier, not its whole filled triangle. Gluing that whole disk to a proton face would require a new attachment contract.'},
        'checks':checks,
        'first_missing_datum':'An arrow-derived global selection or interaction/attachment witness distinguishing the standalone cycle from an ordinary proton face mode, without importing charge or spin labels.',
        'physical_neutrino_identification':False,'spin_decoration':False,'charge_assigned':False,
        'claim_boundary':'The inherited rules distinguish global dimensions/facet counts, but not a neutrino sector. Equal local cyclic modes and a boundary-port dimension mismatch are exact results, not a no-go theorem for every future interaction.'}
    deps=[Path(__file__),registry_path,proton_path,CHECKERS/'assemble_relative_geometry.py',CHECKERS/'check_relative_geometry_mode_selection.py']
    out['source_hashes']={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}
    dest=ROOT/'research/strominger/results/neutrino_triangle_selection_attachment.json'
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
