"""Test directed-incidence-induced cycle orientation on the actual source.

The orientation coupling is an explicit conjectured rule, not a consequence
of un-oriented flag incidence. A competing fixed-boundary rule is tested too.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from fractions import Fraction as Q
from collections import defaultdict, deque
import json

from check_geometric_cycle_reversal import geo, SOURCE, verify, ONE, conj, encode
BASE=Path(__file__).resolve().parents[1]

def edge_chain(tri):
    result={}
    for a,b in zip(tri,tri[1:]+tri[:1]):
        key=tuple(sorted((a,b))); result[key]=1 if (a,b)==key else -1
    return result

def boundary(triangles):
    result=defaultdict(int)
    for tri in triangles:
        for edge,sign in edge_chain(tri).items(): result[edge]+=sign
    return {e:s for e,s in result.items() if s}

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(s,v): return tuple(s*x for x in v)
def induced_pairing(direction,tri,points,chi):
    a,b,c=(points[v] for v in tri)
    return chi*dot(direction,geo.cross(sub(b,a),sub(c,a)))

def main():
    original=SOURCE.read_bytes(); source=json.loads(original)
    evidence,_=verify(source)
    objects=source['objects']; geometry=objects[objects[source['root']]['geometry']]['payload']
    rows=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    tris=[tuple(r['triangle']) for r in rows]
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):
        points['F_'+face]=geo.mean([points[v] for v in face])
    center=(Q(0),)*3
    # Calibration is explicit: the source triangles have OUTWARD geometric
    # normals. Calling the source's hypothetical radial traversal 'inward'
    # therefore fixes chi=-1 in chi * contraction(direction, volume_form).
    chi=-1
    reversed_tris=[(a,c,b) for a,b,c in tris]
    selected=(ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA))
    incidence_reports=[]; cycles=True; modes=True; actual_outward=True
    for tri,rev in zip(tris,reversed_tris):
        outward=sub(points[tri[0]],center); inward=scale(-1,outward)
        incoming=induced_pairing(inward,tri,points,chi)
        outgoing_old=induced_pairing(outward,tri,points,chi)
        outgoing_new=induced_pairing(outward,rev,points,chi)
        actual_outward &= induced_pairing(outward,tri,points,1)>0
        X=geo.transpose(tuple(points[k] for k in tri))
        Xr=geo.transpose(tuple(points[k] for k in rev))
        A=geo.mm(geo.mm(X,geo.C),geo.inv(X))
        Ar=geo.mm(geo.mm(Xr,geo.C),geo.inv(Xr))
        v=geo.zmv(X,selected); vr=geo.zmv(Xr,selected)
        cycles &= Ar==geo.mm(A,A)
        modes &= vr==tuple(conj(z) for z in v)
        incidence_reports.append({'triangle':list(tri),'incoming_pairing':str(incoming),
            'outgoing_old_orientation_pairing':str(outgoing_old),
            'outgoing_reversed_orientation_pairing':str(outgoing_new)})
    # Exhaust the parent mesh's orientation choices, not merely one sample.
    coherent=[]
    for signs in product((-1,1),repeat=len(tris)):
        oriented=[t if s==1 else (t[0],t[2],t[1]) for t,s in zip(tris,signs)]
        if not boundary(oriented): coherent.append(signs)
    # Source triangles split along outer-edge midpoints into the 24 flags.
    refined=[]
    for f,a,b in tris:
        mid='M_'+''.join(sorted((a,b)))
        points[mid]=geo.mean([points[a],points[b]])
        refined.extend([(f,a,mid),(f,mid,b)])
    edge_owners=defaultdict(list)
    for i,tri in enumerate(refined):
        for edge,sign in edge_chain(tri).items(): edge_owners[edge].append((i,sign))
    graph=defaultdict(set)
    for owners in edge_owners.values():
        assert len(owners)==2
        (i,a),(j,b)=owners
        assert a==-b
        graph[i].add(j); graph[j].add(i)
    seen={0}; queue=deque([0])
    while queue:
        for j in graph[queue.popleft()]:
            if j not in seen: seen.add(j); queue.append(j)
    bad=list(tris); bad[0]=reversed_tris[0]
    mixed=boundary(bad)
    # Alternative law: use the body's fixed outward normal, independently
    # of traversal direction. It keeps the source cycles for both directions.
    fixed_boundary_law_ok=all(induced_pairing(points[t[0]],t,points,1)>0 for t in tris)
    checks={
        'source_reverified':evidence['verified'],
        'source_cycle_orientations_are_geometrically_outward':actual_outward,
        'single_global_calibration_matches_source_on_incoming_arrows':all(Q(r['incoming_pairing'])>0 for r in incidence_reports),
        'outgoing_arrows_reject_old_and_select_reversed_orientation':all(
            Q(r['outgoing_old_orientation_pairing'])<0 and Q(r['outgoing_reversed_orientation_pairing'])>0 for r in incidence_reports),
        'selected_cycle_is_inverse_in_same_spatial_coordinates':cycles,
        'same_character_derives_conjugated_vectors':modes,
        'source_boundary_has_no_seam':not boundary(tris),
        'globally_reversed_boundary_has_no_seam':not boundary(reversed_tris),
        'exhaustive_twelve_triangle_orientations_have_only_two_coherent_choices':
            set(coherent)=={(-1,)*12,(1,)*12},
        'single_triangle_orientation_error_creates_three_edge_defects':len(mixed)==3 and all(abs(v)==2 for v in mixed.values()),
        'refined_surface_has_twenty_four_distinct_triangles':len(refined)==len(set(refined))==24,
        'refined_surface_has_no_seam_in_either_orientation':not boundary(refined)
            and not boundary([(a,c,b) for a,b,c in refined]),
        'refined_orientation_constraints_are_connected':len(seen)==24,
        'outward_incidence_alone_also_allows_unchanged_boundary_orientation':fixed_boundary_law_ok,
        'source_unchanged':SOURCE.read_bytes()==original,
    }
    report={
        'verification_passed':all(checks.values()),'checks':checks,
        'contract':{
            'orientation_rule':'beta_d(u,v) = chi * Omega(d,u,v), with fixed ambient volume form Omega',
            'direction':'d is the directed body-center/face-center displacement',
            'calibration':chi,
            'calibration_reason':'source triangles have outward normals; matching them to a proposed incoming traversal requires chi=-1',
            'character':'omega is held fixed on both constructions',
            'status':'explicit conjectured coupling of traversal to cycle orientation'},
        'orientation_choices_tested':2**12,'coherent_choices':len(coherent),
        'refined_vertices':len({x for t in refined for x in t}),
        'refined_edges':len(edge_owners),'refined_triangles':len(refined),
        'incidence_pairings':incidence_reports,
        'single_flip_edge_defects':[[list(e),v] for e,v in sorted(mixed.items())],
        'conclusion':'Under the directed-incidence orientation rule, reversal forces all cycles to invert coherently and derives conjugated modes. '
            'A fixed-boundary orientation rule is also coherent and does not invert cycles. Thus the coupling is consistent but is not forced by outward growth alone.',
        'source_root':source['root'],'source_sha256':sha256(original).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (BASE/'results/directed_incidence_orientation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
