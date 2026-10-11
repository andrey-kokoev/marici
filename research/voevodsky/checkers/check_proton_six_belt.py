"""Exhaustive six-triangle test and explicit six-panel vertex-link belts.
A combinatorial annulus is an interface candidate, not a charge assignment
or an already constructed electron/proton pullback.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json

from check_proton_merkle_reassembly import verify as verify_focus, POINTS
from check_proton_face_extension import geometry, mean, sub, cross, dot

BASE=Path(__file__).resolve().parents[1]
FOCUS=BASE/'results/proton_merkle_store.json'

def components(nodes,adj):
    left=set(nodes); result=[]
    while left:
        seen=set(); todo=[min(left)]
        while todo:
            v=todo.pop()
            if v not in seen: seen.add(v); todo.extend(adj[v]-seen)
        result.append(sorted(seen)); left-=seen
    return result

def topology(faces):
    vertices=set(); edges=Counter(); signs=Counter(); adjacency=defaultdict(set); links=defaultdict(list)
    for face in faces:
        if len(face)<3 or len(set(face))!=len(face): raise ValueError('simple polygon required')
        vertices.update(face)
        for i,u in enumerate(face):
            v=face[(i+1)%len(face)]; e=tuple(sorted((u,v))); edges[e]+=1; signs[e]+=1 if u<v else -1
            adjacency[u].add(v); adjacency[v].add(u)
            links[u].append((face[i-1],v))
    boundary=[e for e,n in edges.items() if n==1]; badj=defaultdict(set)
    for u,v in boundary: badj[u].add(v); badj[v].add(u)
    cycles=bool(boundary) and all(len(ns)==2 for ns in badj.values())
    loops=components(set(badj),badj) if cycles else []
    manifold=all(n in (1,2) for n in edges.values())
    for vertex,pairs in links.items():
        counts=Counter(); adj=defaultdict(set)
        for a,b in pairs: counts[a]+=1; counts[b]+=1; adj[a].add(b); adj[b].add(a)
        degrees=sorted(counts.values())
        shape=(degrees.count(1)==2 and all(d in (1,2) for d in degrees)) if vertex in badj else all(d==2 for d in degrees)
        manifold &= shape and len(components(set(counts),adj))==1
    connected=len(components(vertices,adjacency))==1
    oriented=all(signs[e]==0 for e,n in edges.items() if n==2)
    chi=len(vertices)-len(edges)+len(faces)
    return {'vertices':len(vertices),'edges':len(edges),'faces':len(faces),'euler_characteristic':chi,
            'connected':connected,'manifold_with_boundary':manifold,'supplied_orientation_consistent':oriented,
            'boundary_loops':len(loops),'boundary_lengths':sorted(len(c) for c in loops),
            'annulus':manifold and connected and oriented and cycles and len(loops)==2 and chi==0,
            'disk':manifold and connected and oriented and cycles and len(loops)==1 and chi==1}

def geometry_points(triangles):
    points={k:tuple(map(Q,v)) for k,v in POINTS.items()}
    for tri in triangles: points[tri[0]]=mean([points[k] for k in tri[0][2:]])
    return points

def belt(triangles,vertex,fraction=Q(1,2)):
    if not 0<fraction<1: raise ValueError('cut fraction must lie strictly between 0 and 1')
    points=geometry_points(triangles); star=[t for t in triangles if vertex in t]; quads=[]
    for tri in star:
        i=tri.index(vertex); a,b=tri[(i+1)%3],tri[(i+2)%3]
        for w in (a,b):
            points[f'cut_{vertex}_{w}']=tuple((1-fraction)*x+fraction*y for x,y in zip(points[vertex],points[w]))
        quads.append([f'cut_{vertex}_{a}',a,b,f'cut_{vertex}_{b}'])
    used={v for q in quads for v in q}
    return {'kind':'vertex-link-belt','center_vertex':vertex,'cut_fraction':str(fraction),'source_triangles':star,
            'points':{v:list(map(str,points[v])) for v in sorted(used)},'quadrilaterals':quads,
            'removed_corner_triangles':[[vertex,q[0],q[-1]] for q in quads],
            'retained_area_fraction_of_star':str(1-fraction*fraction)}

def digest(record): return sha256(b'marici.proton-six-belt.v1\0'+json.dumps(record,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def verify_packet(packet):
    if set(packet)!={'schema','focus','record','root'} or packet['schema']!='marici.proton-six-belt-store.v1': raise ValueError('packet schema')
    verify_focus(packet['focus']); record=packet['record']
    if digest(record)!=packet['root'] or set(record)!={'kind','focus','belts'} or record['kind']!='four-vertex-belts' or record['focus']!=packet['focus']['root']: raise ValueError('root binding')
    triangles=[r['triangle'] for r in geometry(packet['focus'])['triangles_and_transports']]
    if len(record['belts'])!=4: raise ValueError('expected four original-corner belts')
    for v,b in zip('ABCD',record['belts']):
        if b!=belt(triangles,v,Q(b['cut_fraction'])) or not topology(b['quadrilaterals'])['annulus']: raise ValueError('invalid belt geometry or topology')
    return True

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    focus=json.loads(FOCUS.read_text(encoding='utf-8')); verify_focus(focus)
    records=geometry(focus)['triangles_and_transports']; triangles=[r['triangle'] for r in records]
    census=Counter(); annuli=[]
    for indices in combinations(range(12),6):
        report=topology([triangles[i] for i in indices])
        category='annulus' if report['annulus'] else 'disk' if report['disk'] else 'other'
        census[category]+=1
        if report['annulus']: annuli.append(list(indices))
    # Enumerate simple six-cycles of the dual graph, modulo cyclic rotation/reversal.
    dual={i:{j for j in range(12) if i!=j and len(set(triangles[i])&set(triangles[j]))==2} for i in range(12)}
    cycles=set()
    def walk(path):
        if len(path)==6:
            if path[0] in dual[path[-1]]:
                variants=[]
                for row in (path,list(reversed(path))):
                    variants.extend(tuple(row[i:]+row[:i]) for i in range(6))
                cycles.add(min(variants))
            return
        for j in sorted(dual[path[-1]]):
            if j not in path: walk(path+[j])
    for i in range(12): walk([i])
    belts=[belt(triangles,v) for v in 'ABCD']; reports=[topology(b['quadrilaterals']) for b in belts]
    checks={'all_924_six_triangle_subsets_examined':sum(census.values())==924,
            'no_six_whole_triangle_subset_is_an_annulus':len(annuli)==0,
            'four_simple_dual_six_cycles':len(cycles)==4,
            'dual_six_cycles_bound_disks_not_annuli':all(topology([triangles[i] for i in c])['disk'] for c in cycles),
            'dual_six_cycles_are_original_vertex_stars':{frozenset(c) for c in cycles}=={frozenset(i for i,t in enumerate(triangles) if v in t) for v in 'ABCD'},
            'four_truncated_stars_are_actual_six_panel_annuli':all(r['annulus'] and r['faces']==6 for r in reports),
            'two_six_edge_boundary_loops':all(r['boundary_lengths']==[6,6] for r in reports),
            'belt_counts_12_vertices_18_edges_6_panels':all((r['vertices'],r['edges'],r['faces'])==(12,18,6) for r in reports),
            'midpoint_belt_retains_three_quarters_of_star':all(b['retained_area_fraction_of_star']=='3/4' for b in belts),
            'face_center_has_three_panel_belt_not_six':len(belt(triangles,'F_ABC')['quadrilaterals'])==3 and topology(belt(triangles,'F_ABC')['quadrilaterals'])['annulus'],
            'collapsed_inner_loop_rejected':rejected(lambda:belt(triangles,'A',Q(0))),
            'zero_width_band_rejected':rejected(lambda:belt(triangles,'A',Q(1))),
            'different_cut_radius_still_annular':topology(belt(triangles,'A',Q(1,3))['quadrilaterals'])['annulus']}
    points=geometry_points(triangles)
    squared_areas=[]
    for tri in triangles:
        a,b,c=[points[v] for v in tri]; normal=cross(sub(b,a),sub(c,a))
        squared_areas.append(dot(normal,normal)/4)
    checks['equal_source_triangle_areas_justify_three_eighths_shell_fraction']=len(set(squared_areas))==1 and Q(6,12)*(1-Q(1,2)**2)==Q(3,8)
    # Diagonal subdivision turns six quadrilaterals into twelve genuine triangles.
    split=[[q[0],q[1],q[2]] for q in belts[0]['quadrilaterals']]+[[q[0],q[2],q[3]] for q in belts[0]['quadrilaterals']]
    checks['triangulated_belt_has_twelve_triangles']=topology(split)['annulus'] and topology(split)['faces']==12
    # Two abstract copies can be glued with cancelling shared-boundary orientation.
    # This is not an independently derived electron sector.
    first=belts[0]['quadrilaterals']; second=[]
    for q in first:
        second.append([v if v.startswith('cut_') else 'other_'+v for v in reversed(q)])
    joined=topology(first+second)
    checks['abstract_opposite_orientation_seam_glues_two_bands']=joined['annulus'] and joined['boundary_lengths']==[6,6]
    wrong=[[v if v.startswith('cut_') else 'other_'+v for v in q] for q in first]
    checks['same_orientation_seam_does_not_cancel']=not topology(first+wrong)['supplied_orientation_consistent']
    record={'kind':'four-vertex-belts','focus':focus['root'],'belts':belts}
    packet={'schema':'marici.proton-six-belt-store.v1','focus':focus,'record':record,'root':digest(record)}
    checks['merkle_geometry_and_annuli_reverify']=verify_packet(packet)
    bad=deepcopy(packet); bad['record']['belts'][0]['points'][next(iter(bad['record']['belts'][0]['points']))][0]='999'; bad['root']=digest(bad['record'])
    checks['honestly_rehashed_wrong_fold_geometry_rejected']=rejected(lambda:verify_packet(bad))
    checks['serialized_belt_packet_reverifies']=verify_packet(json.loads(json.dumps(packet)))
    result={'schema':'marici.proton-six-belt-check.v1','passed':all(checks.values()),'checks':checks,
            'six_triangle_subset_census':dict(census),'dual_six_cycles':[[records[i]['outer_arrow'] for i in c] for c in sorted(cycles)],
            'belt_reports':dict(zip('ABCD',reports)),'halfway_belt_area_fraction_of_whole_shell':'3/8',
            'abstract_two_band_gluing':joined,'root':packet['root'],
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact geometry and combinatorial topology only. No electric charge law, independent electron complex, or pullback interface maps supplied.'}
    out=BASE/'results'
    (out/'proton_six_belt.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (out/'proton_six_belt_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    b=belts[0]; names=list(b['points']); index={v:i+1 for i,v in enumerate(names)}
    obj=['# Six-panel annulus around vertex A; visualization coordinates only']
    obj+=['v '+' '.join(str(float(Q(x))) for x in b['points'][v]) for v in names]
    obj+=['f '+' '.join(str(index[v]) for v in q) for q in b['quadrilaterals']]
    (out/'proton_six_belt.obj').write_text('\n'.join(obj)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
