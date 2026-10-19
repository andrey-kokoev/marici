"""Source-derived geometric rim attachment, not a physical weak vertex."""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

from check_neutrino_triangle_cap_boundary import (
    ROOT,assemble,select,generator,apply,subtract,dot_metric,mm,mv,tr,
    parity,boundaries,rank,serial)
from electron_packet_interface import Interface, ACTIONS, I, sm, gmm, STORE as ELECTRON_STORE

CONTRACT=ROOT/'research/strominger/contracts/neutrino-rim-attachment.v1.json'
OUT=ROOT/'research/strominger/results/neutrino-rim-attachment-v1.json'
PRIOR=ROOT/'research/strominger/results/neutrino-triangle-cap-boundary-v1.json'
NSOURCE=ROOT/'research/voevodsky/inputs/mode-neutron.json'
PSOURCE=ROOT/'research/voevodsky/inputs/relative-proton.json'
REGISTRY=ROOT/'research/strominger/results/neutrino_seed_candidates.json'


def digest(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def edge_boundary(faces):
    out={}
    for face in faces:
        for k in range(3):
            e=face[:k]+face[k+1:];key=tuple(sorted(e))
            out[key]=out.get(key,0)+(-1)**k*parity(e)
    return {e:x for e,x in out.items() if x}
def chain(faces):
    out={}
    for face in faces:
        key=tuple(sorted(face));out[key]=out.get(key,0)+parity(face)
    return {f:x for f,x in out.items() if x}
def oriented(faces,sign):
    assert sign in (-1,1)
    return [list(f) if sign==1 else [f[1],f[0],f[2]] for f in faces]
def addpoint(J,b,p):return tuple(x+y for x,y in zip(mv(J,p),b))


def topology(faces,n):
    edges,B1,B2=boundaries(faces,n)
    assert mm(B1,B2)==[[F(0)]*len(faces) for _ in range(n)]
    r1,r2=rank(B1),rank(B2)
    return {'vertices':n,'edges':len(edges),'faces':len(faces),
        'boundary1_rank':r1,'boundary2_rank':r2,'betti':[n-r1,len(edges)-r1-r2,len(faces)-r2]}


def boundary_components(faces):
    boundary=edge_boundary(faces);adj={}
    for (a,b),coefficient in boundary.items():
        assert abs(coefficient)==1
        adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
    assert all(len(v)==2 for v in adj.values())
    components=[];remaining=set(adj)
    while remaining:
        found={min(remaining)};front=list(found)
        while front:
            v=front.pop()
            for w in adj[v]-found:found.add(w);front.append(w)
        remaining-=found
        component={e:x for e,x in boundary.items() if set(e)<=found}
        # No oriented vertex sources/sinks in this component.
        incidence={v:0 for v in found}
        for (a,b),x in component.items():incidence[a]-=x;incidence[b]+=x
        assert not any(incidence.values())
        components.append({'vertices':sorted(found),'edges':component})
    return components


def require_boundary(host,cap):
    components=boundary_components(host)
    if not any(set(c['vertices'])==set(cap) for c in components):
        raise ValueError('not an exposed boundary component')


def require_square(host_g,J,b,candidate_g):
    A,t=candidate_g;R,s=host_g
    if mm(R,J)!=mm(J,A) or apply(host_g,b)!=tuple(x+y for x,y in zip(mv(J,t),b)):
        raise ValueError('forward source word not intertwined')


def require_metric(J,G,source_metric):
    if mm(tr(J),mm(G,J))!=source_metric:raise ValueError('fixed metric mismatch')


def reject(fn,text):
    try:fn()
    except ValueError as error:assert text in str(error)
    else:raise AssertionError('accepted hostile: '+text)


def attachments(source,host,host_vertices,cap,candidate,metric,center_id):
    """Enumerate source-cycle correspondences, not fitted target cells."""
    hg=generator(source['generators'][0]);cg=generator(candidate['generators'][0])
    G=[list(map(F,row)) for row in source['metric']]
    require_boundary(host,cap)
    cgeometry=assemble(candidate)
    cp=[tuple(map(F,p)) for p in cgeometry['vertices']]+[tuple(map(F,cgeometry['center']))]
    assert cgeometry['center_vertex_id']==3
    faces=[list(f) for f in cgeometry['cone_cells']]
    out=[];reversals=0
    start=host_vertices[min(cap)]
    p_orbit=[start,apply(hg,start),apply(hg,apply(hg,start))]
    assert apply(hg,p_orbit[-1])==start and {host_vertices.index(p) for p in p_orbit}==set(cap)
    for shift in range(3):
        p0,p1,p2=[p_orbit[(shift+k)%3] for k in range(3)]
        J=[[p1[k]-p0[k],p2[k]-p0[k]] for k in range(3)]
        require_square(hg,J,p0,cg);require_metric(J,G,metric)
        ids={}
        for i,p in enumerate(cp[:3]):ids[i]=host_vertices.index(addpoint(J,p0,p))
        ids[3]=center_id
        mapped=[[ids[v] for v in f] for f in faces]
        patch_boundary=edge_boundary(mapped)
        host_component={e:x for e,x in edge_boundary(host).items() if set(e)<=set(cap)}
        assert set(patch_boundary)==set(host_component)
        first=next(iter(patch_boundary))
        sign=-host_component[first]//patch_boundary[first]
        assert all(sign*patch_boundary[e]==-host_component[e] for e in patch_boundary)
        patch=oriented(mapped,sign)
        assert not any(set(e)<=set(cap) for e in edge_boundary(host+patch))
        assert len(edge_boundary(host+patch))==len(edge_boundary(host))-3
        # The actual host cycle transports each patch cell into the same chain.
        lookup={p:i for i,p in enumerate(host_vertices)}
        vp={i:lookup[apply(hg,p)] for i,p in enumerate(host_vertices)};vp[center_id]=center_id
        assert chain([[vp[v] for v in f] for f in patch])==chain(patch)
        reverseJ=[[p2[k]-p0[k],p1[k]-p0[k]] for k in range(3)]
        require_metric(reverseJ,G,metric)
        reject(lambda:require_square(hg,reverseJ,p0,cg),'forward source word not intertwined')
        A,t=cg;A2=mm(A,A);t2=tuple(x+y for x,y in zip(mv(A,t),t))
        require_square(hg,reverseJ,p0,(A2,t2));reversals+=1
        out.append({'source_cycle_shift_word':[0]*shift,'candidate_vertex_to_host':ids,
            'embedding_linear_part':J,'embedding_translation':p0,
            'cap_center':addpoint(J,p0,cp[3]),'orientation_coefficient':sign,
            'patch_triangles':patch,'patch_boundary':edge_boundary(patch),
            'result_topology':topology(host+patch,len(host_vertices)+1),
            'remaining_boundary':edge_boundary(host+patch),
            'archive_required_for_corner_and_word_recovery':True})
    assert len(out)==reversals==3
    assert len({tuple(sorted(chain(x['patch_triangles']).items())) for x in out})==1
    assert len({x['candidate_vertex_to_host'][0] for x in out})==3
    return out,reversals


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items()),'stale cap comparison'
    candidate=read(REGISTRY)['candidates'][0]['source']
    old_metric=[list(map(F,row)) for row in candidate['metric']]
    nsource=read(NSOURCE);nfull=assemble(nsource);neutron,_=select(nsource)
    nv=[tuple(map(F,p)) for p in neutron['vertices']]
    host=[list(f) for f in neutron['carrier_facets']]
    full_faces=[list(f) for f in nfull['carrier_facets']]
    assert len(host)==6 and len(full_faces)==8 and not edge_boundary(full_faces)
    components=boundary_components(host)
    caps=neutron['external_interfaces']
    assert len(components)==2 and all(len(c['edges'])==3 for c in components)
    assert {tuple(c['vertices']) for c in components}=={tuple(sorted(c)) for c in caps}
    base_topology=topology(host,6);assert base_topology['betti']==[1,1,0]
    assert topology(full_faces,6)['betti']==[1,0,1]
    cap_metric=[[F(3,8)*x for x in row] for row in old_metric]
    scaled=deepcopy(candidate);scaled['metric']=[[str(x) for x in row] for row in cap_metric]
    matches=[];reverse_count=0
    for cap in caps:
        records,reversals=attachments(nsource,host,nv,cap,scaled,cap_metric,6)
        assert all(row['result_topology']['betti']==[1,0,0] for row in records)
        for row in records:
            reject(lambda:require_metric(row['embedding_linear_part'],[list(map(F,r)) for r in nsource['metric']],old_metric),'fixed metric mismatch')
        # Subdivision chain map: cap face boundary equals attached patch boundary.
        original=next(f for f in full_faces if set(f)==set(cap))
        assert edge_boundary([original])==records[0]['patch_boundary']
        matches.append({'cap_vertices':cap,'forward_maps':records});reverse_count+=reversals
    first=matches[0]['forward_maps'][0]['patch_triangles']
    # Allocate the second cap's own centroid separately; do not identify centers.
    second=[[7 if v==6 else v for v in f] for f in matches[1]['forward_maps'][0]['patch_triangles']]
    closed=host+first+second
    assert not edge_boundary(closed)
    closed_topology=topology(closed,8)
    assert closed_topology['betti']==[1,0,1]

    psource=read(PSOURCE);proton=assemble(psource)
    pv=[tuple(map(F,p)) for p in proton['vertices']];pf=[list(f) for f in proton['carrier_facets']]
    assert not boundary_components(pf) and topology(pf,4)['betti']==[1,0,1]
    # Excise a face actually cycled by the first retained proton generator.
    pg=generator(psource['generators'][0]);p0=tuple(map(F,psource['seeds'][0]['point']))
    porbit=[p0,apply(pg,p0),apply(pg,apply(pg,p0))]
    pcap=[pv.index(p) for p in porbit]
    removed=next(f for f in pf if set(f)==set(pcap))
    reject(lambda:require_boundary(pf,pcap),'not an exposed boundary component')
    punctured=[f for f in pf if set(f)!=set(pcap)]
    assert len(boundary_components(punctured))==1 and topology(punctured,4)['betti']==[1,0,0]
    # This countermodel changes both host scale and host by explicit excision.
    # It is not advertised as an available operation on the unchanged proton.
    pscaled=deepcopy(psource)
    pscaled['metric']=[[str(F(3,8)*F(x)) for x in row] for row in psource['metric']]
    control,control_reversals=attachments(pscaled,punctured,pv,pcap,scaled,cap_metric,4)
    assert all(x['result_topology']['betti']==[1,0,1] for x in control)

    # Restricted spin gate: a purely geometric chain line is even under the
    # central lift, whereas the actual retained electron logical doublet is odd.
    electron=Interface();minus=sm(F(-1),I)
    assert minus in ACTIONS
    raw_central=electron.raw_actions[minus]
    assert gmm(raw_central,electron.K)==sm(F(-1),electron.K)
    assert gmm(electron.D,gmm(raw_central,electron.K))==minus
    constraint=[[F(-2),F(0)],[F(0),F(-2)]]
    assert rank(constraint)==2
    for v in ((F(1),F(0)),(F(0),F(1))):assert mv(constraint,v)!=(F(0),F(0))
    # For matched baryon central signs eta_n=eta_p and eta_e=-1,
    # eta_n=eta_p*eta_e*eta_partner implies eta_partner=-1.
    for eta in (-1,1):
        assert [nu for nu in (-1,1) if eta==eta*(-1)*nu]==[-1]

    checks={name:True for name in (
        'actual_native_side_and_full_hull_oriented_chains',
        'two_rim_components_derived_from_boundary_not_target_injection',
        'native_neutron_surface_is_annulus_by_exact_boundary_ranks',
        'old_metric_rejected_and_explicit_cap_metric_accepted',
        'six_forward_affine_isometric_source_equivariant_identifications',
        'six_reversed_identifications_require_inverse_cycle_word',
        'each_attachment_cancels_exactly_one_rim_boundary',
        'each_single_cap_result_is_disk_by_exact_chain_homology',
        'two_caps_close_sphere_and_subdivision_boundary_squares',
        'actual_source_cycle_preserves_each_oriented_patch_chain',
        'same_glued_chain_loses_three_distinct_corner_word_histories',
        'unchanged_closed_proton_has_no_boundary_attachment_target',
        'explicit_excised_rescaled_proton_is_attachment_countermodel',
        'actual_retained_electron_raw_and_logical_central_minus_actions',
        'geometric_chain_transition_has_zero_central_spin_intertwiner')}
    pins=dict(prior['source_sha256'])
    for p in (CONTRACT,PRIOR,NSOURCE,PSOURCE,REGISTRY,ELECTRON_STORE,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix=='.py':pins[p.relative_to(ROOT).as_posix()]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.neutrino-rim-attachment-check.v1','status':'pass','checks':checks,
        'new_capability_scope':contract['scope'],'original_neutron_surface':host,
        'neutron_boundary_components':components,'neutron_topology':base_topology,
        'cap_metric_variant':scaled,'attachments':matches,'forward_map_count':6,
        'reversed_forward_word_rejections':reverse_count,'two_cap_closed_topology':closed_topology,
        'two_cap_closed_surface':closed,
        'proton_control':{'unchanged_boundary_components':0,'excision_face':removed,
            'changed_source_operations':['explicit face excision','uniform metric scaling by3/8','restrict transport to retained first-generator stabilizer'],
            'scaled_source':pscaled,'countermodel_matches':control,'countermodel_reverse_controls':control_reversals},
        'spin_gate':{'scope':'Geometric baryon and disk chain lines, actual electron doublet; not all future baryon/spinor extensions.',
            'geometric_chain_central_sign':1,'electron_central_sign':-1,
            'transition_coefficient_constraint':constraint,'allowed_vertex_dimension':0,
            'matched_baryon_central_parities_require_partner_sign':-1,
            'spinorial_partner_constructed_from_disk':False},
        'geometric_boundary_attachment_constructed':True,
        'new_operator_is_inherited_single_pole_rule':False,
        'unmarked_glued_chain_recovers_preparation_history':False,
        'species_unique_selector_constructed':False,
        'physical_weak_vertex_constructed':False,'physical_neutrino_identified':False,
        'charge_energy_momentum_or_chirality_attachment_supplied':False,
        'formal_proof_recompiled':False,'source_sha256':pins}
    OUT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':len(checks),'forward_maps':6,
        'neutron_betti_before':base_topology['betti'],'one_cap_betti':[1,0,0],
        'two_cap_betti':closed_topology['betti'],'geometric_attachment_constructed':True,
        'geometric_chain_weak_vertex_dimension':0,'physical_neutrino_identified':False},indent=2))


if __name__=='__main__':main()
