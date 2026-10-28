"""Transport existing local phase references, refusing a whole-sector phase claim."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import subprocess
import sys
from check_octahedron_esd7_wrap import (ROOT, AXES, CENTRE, HALF, axis_coords, wrap, unwrap, planes, polyhedron, volume, key, sub, dot)

OUT=ROOT/'research/strominger/results/esd7-wrap-phase-transport'
CONTRACT=ROOT/'research/strominger/contracts/esd7-wrap-phase-transport-v1.json'


def supporting_plane(face):
    a,b,c=[q[:3] for q in face]
    u,v=sub(b,a),sub(c,a)
    n=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
    return n,dot(n,a)


def pieces_for(carrier):
    raw={'vertices':carrier['vertices'],'faces':list(combinations(carrier['vertices'],3))}
    ps=planes(raw)
    original=polyhedron(ps)
    assert original is not None
    result=[]
    for su,sv in product((-1,1),repeat=2):
        clipped=polyhedron(ps+[(-su,-su,0,-su),(-sv,0,-sv,-sv)])
        if clipped is None:
            continue
        vs,fs=clipped
        result.append({'branch':(su,sv),'vertices':[(*q,1-sum(q)) for q in vs], 'faces':[[(*q,1-sum(q)) for q in face] for face in fs], 'source_volume':volume(vs,fs)})
    assert sum(p['source_volume'] for p in result)==volume(*original)
    return result


def interface_image(pieces,face):
    n,d=supporting_plane(face)
    return {key(wrap(q,p['branch']) for q in f) for p in pieces for f in p['faces'] if all(dot(n,q[:3])==d for q in f)}


def main():
    contract=json.loads(CONTRACT.read_text())
    translation=tuple(contract['placement']['translation'])
    assert len(translation)==4 and sum(translation)==0 and all(isinstance(x,int) for x in translation)
    place=lambda q:tuple(F(x)+t for x,t in zip(q,translation))
    # Fresh closure check, not reuse of an old wrap receipt.
    subprocess.run([sys.executable,str(ROOT/'research/strominger/checkers/check_octahedron_esd7_wrap.py')],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
    exported=subprocess.check_output(['node','research/strominger/checkers/export_esd7_wrap_phase_inputs.mjs'],cwd=ROOT,text=True)
    data=json.loads(exported)
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        assert condition,name
    check('fresh_upstream_wrap_check',True)
    check('three_native_reference_fixtures',len(data['fixtures'])==3)
    sector=data['sector']
    source_hosts=set()
    summaries=[]
    geometric_packets=[]
    for fixture in data['fixtures']:
        isotope=fixture['isotope']
        check(isotope+'_native_and_wrapped_phase_checks',all(fixture['checks'].values()))
        points={k:place(q) for k,q in fixture['points'].items()}
        check(isotope+'_all_five_slot_reference_points_inside_source',all(sum(abs(t) for t in axis_coords(q))<=1 for q in points.values()))
        encoded={f'wrapped:{isotope}:{name}':wrap(q) for name,q in points.items()}
        check(isotope+'_point_registry_exact_inverse',all(unwrap(encoded[f'wrapped:{isotope}:{name}'])==q for name,q in points.items()))
        carriers={c['id']:{**c,'vertices':[place(q) for q in c['vertices']]} for c in fixture['carriers']}
        pieces={cid:pieces_for(c) for cid,c in carriers.items()}
        host_rows=[]
        for cid,c in carriers.items():
            vertices={tuple(q) for q in c['vertices']}
            hosts=[h for h in sector if vertices.issubset({tuple(q) for q in h['vertices']})]
            assert len(hosts)==1
            host=hosts[0];source_hosts.add(host['id'])
            host_rows.append({'physical_carrier':cid,'physical_species':c['species'],'geometric_host':host['id'],'geometric_role':host['role'],'whole_cell_equal':key(c['vertices'])==key(host['vertices'])})
        check(isotope+'_primitive_carriers_have_exact_geometric_hosts',len(host_rows)==len(carriers))
        check(isotope+'_species_is_not_inferred_from_host_colour',any(r['physical_species']!=r['geometric_role'] for r in host_rows))
        contact_rows={}
        for e in fixture['reference']['edges']:
            a,b=[fixture['reference']['charts'][e[k]] for k in ('from','to')]
            if e['kind']=='reader-phase-advance':
                assert a['cell']==b['cell']
                continue
            fa={tuple(q) for q in carriers[a['cell']]['vertices']}
            fb={tuple(q) for q in carriers[b['cell']]['vertices']}
            face=sorted(fa&fb)
            assert len(face)==3
            left,right=interface_image(pieces[a['cell']],face),interface_image(pieces[b['cell']],face)
            assert left and left==right
            cid=tuple(sorted((a['cell'],b['cell'])))
            contact_rows[cid]={'source_carriers':cid,'source_face':face,'wrapped_face_fragments':sorted(left)}
        check(isotope+'_all_actual_contacts_retain_equal_piecewise_faces',len(contact_rows)==fixture['nativeAudit']['contacts']['requiredContacts'])
        seam_comparisons=0
        carrier_rows=[]
        for cid,ps in pieces.items():
            for p in ps:
                images=[wrap(q,p['branch']) for q in p['vertices']]
                assert all(unwrap(w)==q for q,w in zip(p['vertices'],images))
                mapped_faces=[[wrap(q,p['branch'])[:3] for q in f] for f in p['faces']]
                assert volume([q[:3] for q in images],mapped_faces)==p['source_volume']/4
                for q in p['vertices']:
                    u,v,_=axis_coords(q)
                    for alt in product((-1,1) if u==0 else (p['branch'][0],),(-1,1) if v==0 else (p['branch'][1],)):
                        assert wrap(q,alt)==wrap(q,p['branch'])
                        seam_comparisons+=alt!=p['branch']
                carrier_rows.append({'source_carrier':cid,'source_species':carriers[cid]['species'],'branch':p['branch'],'target_vertices':images,'target_faces':mapped_faces,'source_volume':p['source_volume']})
        check(isotope+'_every_carrier_piece_has_exact_inverse_and_volume',len(carrier_rows)>0)
        check(isotope+'_chart_seam_agreement',seam_comparisons>0)
        check(isotope+'_actual_carriers_cross_chart_seams',any(len(ps)>1 for ps in pieces.values()))
        # The coordinate registry cannot merge occurrence identities. Every
        # frame must retain the actual five-slot geometric bindings; origins
        # and histories are carried by the owning certificate, not coordinates.
        for state in fixture['wrappedCertificate']['states']:
            frame=state['frame']
            assert all(o['vertex'] in encoded for o in frame['window']+[frame['context']])
        check(isotope+'_all_wrapped_occurrences_resolve_without_new_labels',True)
        summaries.append({'isotope':isotope,'primitive_carriers':len(carriers),'phase_charts':len(fixture['wrappedCharts']),'operation_edges':len(fixture['reference']['edges']),'certificate_states':len(fixture['wrappedCertificate']['states']),'physical_contacts':len(contact_rows),'wrapped_contact_polygons':sum(len(r['wrapped_face_fragments']) for r in contact_rows.values()),'carrier_chart_fragments':len(carrier_rows),'seam_comparisons':seam_comparisons,'host_binding':host_rows,'operation_kinds':dict(Counter(e['kind']+':'+fixture['reference']['charts'][e['from']]['species'] for e in fixture['reference']['edges'])),'native_checks':fixture['checks']})
        geometric_packets.append({'isotope':isotope,'placement':translation,'point_registry':encoded,'carrier_pieces':carrier_rows,'contacts':list(contact_rows.values())})
    check('source_alphabet_exercises_all_five_operation_kinds', {e['kind'] for f in data['fixtures'] for e in f['reference']['edges']}=={'PN','inverse-PN','NE','reader-phase-advance','NN-phase-advance'})
    check('P_and_N_reader_operations_both_exercised',{loop['species'] for f in data['fixtures'] for loop in f['readerLoops']}=={'proton','neutron'})
    check('global_679_cell_phase_assignment_not_supplied',len(source_hosts)<len(sector))
    # This only obstructs a species-exchanging lift in the current alphabet.
    # Geometric P/E roles and physical phase species are different types.
    check('species_exchanging_reader_duality_not_supplied',all(not any(e['from']==i for e in f['reference']['edges']) for f in data['fixtures'] for i,c in enumerate(f['reference']['charts']) if c['species']=='electron'))
    OUT.mkdir(parents=True,exist_ok=True)
    diagram={'id':'esd7-wrap-phase-transport-pilot','objects':[],'arrows':[],'cells':[], 'obstructions':[], 'claims':[{'id':'whole-sector-phase-transport','requires':['whole-sector-phase-assignment','whole-sector-contact-witnesses']},{'id':'full-state-PE-duality','requires':['geometric-role-to-phase-species-binding','full-state-duality-operation']}], 'available_witnesses':['local-phase-operation-transport','local-contact-sewing','source-history-recovery'],'higher_coherence':[{'id':'whole-sector-phase-coherence','degree':2,'state':'unsupported'}]}
    digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    for f in data['fixtures']:
        for r in f['routeComparisons']:
            ident=f"{f['isotope']}-edge{r['edge']}-origin{r['origin']}"
            a,b=ident+'-request',ident+'-wrapped-witness'
            diagram['objects'].extend([{'id':a,'type':'native edge request: both marked charts and absolute origin'},{'id':b,'type':'wrapped witness packet with all occurrence and reference records'}])
            paths=[]
            for route in ['source_then_encode','encode_then_source']:
                aid=ident+'-'+route
                diagram['arrows'].append({'id':aid,'source':a,'target':b,'map_token':digest(r[route]),'evaluation_locator':f"native-and-wrapped-phase-records.json#{f['isotope']}/edge{r['edge']}/origin{r['origin']}/{route}"})
                paths.append([aid])
            diagram['cells'].append({'id':ident,'kind':'evaluated source-operation/encoding square','routes':paths})
    diagram_path=OUT/'phase-route-diagram.json'
    diagram_path.write_text(json.dumps(diagram,indent=2)+'\n')
    scc=ROOT/'research/aspect/scc/scc.py'
    compiled=json.loads(subprocess.check_output([sys.executable,str(scc),'categorical',str(diagram_path)],cwd=ROOT,text=True))
    (OUT/'categorical-verification.json').write_text(json.dumps(compiled,indent=2)+'\n')
    check('SCC_all_144_evaluated_route_cells_pass',compiled['passed'] and len(compiled['cells'])==144)
    hostile=json.loads(json.dumps(diagram))
    changed=json.loads(json.dumps(data['fixtures'][0]['routeComparisons'][0]['encode_then_source']))
    changed['from']['window'][0]['index']+=2
    hostile['arrows'][1]['map_token']=digest(changed)
    hostile_path=OUT/'wrong-phase-route-hostile.json'
    hostile_path.write_text(json.dumps(hostile,indent=2)+'\n')
    run=subprocess.run([sys.executable,str(scc),'categorical',str(hostile_path)],cwd=ROOT,text=True,capture_output=True)
    hostile_result=json.loads(run.stdout)
    (OUT/'wrong-phase-route-verification.json').write_text(json.dumps(hostile_result,indent=2)+'\n')
    check('SCC_wrong_phase_route_is_rejected',not hostile_result['passed'] and not hostile_result['cells'][0]['passed'])
    inputs=[CONTRACT,Path(__file__),ROOT/'research/strominger/checkers/export_esd7_wrap_phase_inputs.mjs',ROOT/'research/strominger/checkers/check_octahedron_esd7_wrap.py']+[ROOT/'research/strominger/demos/particle-overlap-tetrahedron'/p for p in ['phase-assembly-model.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','window-construction-model.mjs','deuterium-tunnel-model.mjs']]
    report={'status':'bounded-phase-pilot-transport-verified-global-assignment-open','checks':checks,'native_node_assertions':sum(len(f['checks']) for f in data['fixtures']),'evaluated_route_cells':len(compiled['cells']),'placement':contract['placement'],'fixtures':summaries,'sector_coverage':{'whole_geometric_hosts_touched':len(source_hosts),'total_geometric_cells':len(sector),'hosts':sorted(source_hosts),'meaning':'Local reference fixtures embedded geometrically; not a coherent whole-sector phase assignment.'},'residuals':json.loads(CONTRACT.read_text())['residuals'],'native_export_sha256':hashlib.sha256(exported.encode()).hexdigest(),'input_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'scope':'Transport of existing reference phase laws and their certificates through an invertible geometric encoding. No new source phase law, isotope inventory, 256-capacity proof or nuclear stability claim. Source geometric roles and physical species remain separately typed.'}
    OUT.mkdir(parents=True,exist_ok=True)
    encode=lambda x:str(x) if isinstance(x,F) else (_ for _ in ()).throw(TypeError(type(x).__name__))
    (OUT/'native-and-wrapped-phase-records.json').write_text(exported)
    (OUT/'wrapped-geometric-witnesses.json').write_text(json.dumps(geometric_packets,indent=2,default=encode)+'\n')
    (OUT/'verification.json').write_text(json.dumps(report,indent=2,default=encode)+'\n')
    print(json.dumps(report,indent=2,default=encode))


if __name__=='__main__':
    main()
