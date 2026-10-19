"""Exact complex-plane encoding audit of the existing neutron geometry."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble, apply, dot_metric, subtract
from evolve_relative_geometry_modes import evolve


def mul(z,w):
    a,b=z; c,d=w
    return (a*c-3*b*d,a*d+b*c)


def cube(z):
    return mul(mul(z,z),z)


def mean(points):
    return tuple(sum(p[i] for p in points)/len(points) for i in range(len(points[0])))


def main():
    path=ROOT/'research/voevodsky/inputs/mode-neutron.json'
    source=json.loads(path.read_text())
    full=assemble(source)
    motion=evolve(source)
    points=[tuple(map(Q,p)) for p in full['vertices']]
    G=[[Q(x) for x in row] for row in source['metric']]
    heights=sorted(set(p[1] for p in points))
    h=heights[-1]
    assert heights==[-h,h]
    encode=lambda p:(p[2],p[0]) # u=a+i sqrt(3)b
    def decode_vertex(z):
        c=cube(z)
        if c[1] or c[0] not in (-1,1):
            raise ValueError('Vertex decoder requires u^3=+1 or -1')
        return (z[1],h*c[0],z[0])
    zs=[encode(p) for p in points]
    root=(-Q(1,2),-Q(1,2))
    g=source['generators'][0]
    generator=(tuple(tuple(map(Q,row)) for row in g['matrix']),tuple(map(Q,g['translation'])))
    checks={
        'six_distinct_planar_points':len(set(zs))==6,
        'sixth_roots':all(mul(cube(z),cube(z))==(1,0) for z in zs),
        'vertex_decoder_exact':all(decode_vertex(encode(p))==p for p in points),
        'rotation_intertwines':all(encode(apply(generator,p))==mul(root,encode(p)) for p in points),
        'height_character_preserved':all(cube(mul(root,z))==cube(z) for z in zs),
    }
    # Full vertex metric is not the flat complex-plane metric.
    mismatches=[]
    for i,p in enumerate(points):
        for j,q in enumerate(points):
            dz=subtract(zs[i],zs[j]); flat=dz[0]**2+3*dz[1]**2
            correction=h*h*(cube(zs[i])[0]-cube(zs[j])[0])**2
            actual=dot_metric(subtract(p,q),subtract(p,q),G)
            assert actual==flat+correction
            if actual!=flat:
                mismatches.append({'vertices':[i,j],'flat':str(flat),'lifted':str(actual),'correction':str(correction)})
    checks['flat_metric_loses_cross_rim_distances']=len(mismatches)==18
    checks['all_vertex_distances_recovered_with_height_character']=True
    # Reconstruct the original source via decoding its two seed points, then
    # call the unchanged assembler. This explicitly keeps metric and action.
    reconstructed=json.loads(json.dumps(source))
    for seed in reconstructed['seeds']:
        seed['point']=list(map(str,decode_vertex(encode(tuple(map(Q,seed['point']))))))
    checks['decoded_source_assembly_exact']=assemble(reconstructed)==full
    checks['decoded_source_full_cycle_exact']=evolve(reconstructed)==motion
    # Flat-plane rival, using the actual induced action and both source orbits.
    flat_source={'metric':[[1,0],[0,3]],'generators':[
        {'matrix':[['-1/2','3/2'],['-1/2','-1/2']],'translation':[0,0]}],
        'seeds':[{'point':list(map(str,encode(tuple(map(Q,s['point']))))),'role':'carrier'} for s in source['seeds']]}
    planar=assemble(flat_source)
    planar_motion=evolve(flat_source)
    checks['flat_assembly_is_hexagon_not_belt']=planar['dimension']==2 and planar['counts']['supporting_facets']==6 and full['dimension']==3 and full['counts']['supporting_facets']==8
    # Averaging does not commute with the cubic vertex lift. Retain h-moment
    # eta=sum lambda_i*u_i^3 for affine cells, rather than cube(sum lambda_i*u_i).
    faces=[]; fixed=[]
    for f in full['supporting_facets']:
        c=mean([points[i] for i in f]); z=mean([zs[i] for i in f])
        eta=sum(cube(zs[i])[0] for i in f)/len(f)
        lifted=(z[1],h*eta,z[0])
        assert lifted==c
        entry={'vertices':f,'u':list(map(str,z)),'retained_height_moment':str(eta),
               'cube_of_mean':list(map(str,cube(z))),'centroid':list(map(str,c))}
        faces.append(entry)
        if z==(0,0):fixed.append(entry)
    checks['cap_centroids_collide_in_plane']=len(fixed)==2 and fixed[0]['centroid']!=fixed[1]['centroid']
    checks['cubic_lift_fails_cap_centroids']=all(row['cube_of_mean']==['0','0'] and row['retained_height_moment']!='0' for row in fixed)
    checks['all_facet_centroids_recovered_with_moment']=True
    # Check affine identity on vertices/center and sample points of every cone.
    # General identity follows by linearity of the three retained coordinates.
    center=tuple(map(Q,full['center']))
    for cell in full['cone_cells']:
        corners=[center if i==full['center_vertex_id'] else points[i] for i in cell]
        for weights in [(Q(1,4),)*4,(Q(1,10),Q(2,10),Q(3,10),Q(4,10))]:
            p=tuple(sum(w*c[k] for w,c in zip(weights,corners)) for k in range(3))
            z=tuple(sum(w*encode(c)[k] for w,c in zip(weights,corners)) for k in range(2))
            eta=sum(w*c[1]/h for w,c in zip(weights,corners))
            assert (z[1],h*eta,z[0])==p
            moved=apply(generator,p)
            assert encode(moved)==mul(root,z) and moved[1]/h==eta
    checks['retained_affine_cell_decoder_and_action']=True
    checks['full_mode_selection_six_moving_two_fixed']=sum(s['moving_centroid'] for s in motion['facet_states'])==6 and len(motion['facet_states'])==8
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,
        'encoding':'u=Z+i sqrt(3)X; vertices satisfy Y=h*u^3', 'h':str(h),
        'vertices':[{'point':list(map(str,p)),'u':list(map(str,z)),'u_cubed':list(map(str,cube(z)))} for p,z in zip(points,zs)],
        'vertex_metric':'|u-v|^2+h^2*(u^3-v^3)^2 on the six vertex values',
        'cross_rim_distance_counterexamples':mismatches[:2], 'facet_centroids':faces,
        'flat_source':flat_source,'flat_geometry_counts':planar['counts'],
        'flat_cycle_steps':planar_motion['scheduled_atomic_steps_to_word_return'],
        'original_geometry_counts':full['counts'],
        'disposition':'Vertex-level encoding and lifted assembly are exact. Bare flat complex plane loses height metric and full-cell information. Retaining eta=Y/h (or barycentric provenance) recovers cells and actions, but keeps a third real degree of freedom for interiors.',
        'not_derived':['height scale h','particle identity','photon decomposition'],
        'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [path,Path(__file__).resolve(),ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py']}}
    dest=ROOT/'research/strominger/results/neutron_complex_plane_encoding.json'
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'checks':checks,'disposition':report['disposition']},indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
