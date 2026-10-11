"""Retained C2 holonomy on the existing six-belt using the two linear S4 states.
No charge/dynamics. The twist class is an explicit candidate choice, not a
neutron deduction. Gauge relabellings cannot erase it; compression may retain it.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

from check_proton_six_belt import verify_packet as verify_belts, topology, components
from check_proton_s4_neighborhood import verify_packet as verify_s4, transform, state, digest as s4_digest, GENERATORS

BASE=Path(__file__).resolve().parents[1]
BELT=BASE/'results/proton_six_belt_store.json'
STATES=BASE/'results/proton_s4_neighborhood_store.json'

def rank2(rows):
    pivots={}
    for row in rows:
        while row:
            pivot=row.bit_length()-1
            if pivot in pivots: row^=pivots[pivot]
            else: pivots[pivot]=row; break
    return len(pivots)

def structure(belt):
    faces=belt['quadrilaterals']; vertices=sorted({v for q in faces for v in q})
    edges=sorted({tuple(sorted((a,b))) for q in faces for a,b in zip(q,q[1:]+q[:1])})
    index={e:i for i,e in enumerate(edges)}
    masks=[sum(1<<index[tuple(sorted((a,b)))] for a,b in zip(q,q[1:]+q[:1])) for q in faces]
    gauges=[sum(1<<i for i,e in enumerate(edges) if v in e) for v in vertices]
    counts=Counter(tuple(sorted((a,b))) for q in faces for a,b in zip(q,q[1:]+q[:1]))
    adj=defaultdict(set)
    for (a,b),count in counts.items():
        if count==1: adj[a].add(b); adj[b].add(a)
    loops=[]
    for comp in components(set(adj),adj):
        start=min(comp); path=[start]; previous=None; current=start
        while True:
            nxt=next(v for v in sorted(adj[current]) if v!=previous)
            if nxt==start: break
            path.append(nxt); previous,current=current,nxt
        loops.append(path)
    loop_masks=[sum(1<<index[tuple(sorted((a,b)))] for a,b in zip(p,p[1:]+p[:1])) for p in loops]
    return vertices,edges,masks,gauges,loops,loop_masks

def cover(belt,edges,bits):
    index={e:i for i,e in enumerate(edges)}; arrows=[]; faces=[]
    def name(v,s): return v+'#'+str(s)
    for i,(a,b) in enumerate(edges):
        bit=(bits>>i)&1
        for sheet in (0,1):
            u,v=name(a,sheet),name(b,sheet^bit)
            arrows.extend([[u,v],[v,u]])
    for q in belt['quadrilaterals']:
        for initial in (0,1):
            sheet=initial; face=[]
            for a,b in zip(q,q[1:]+q[:1]):
                face.append(name(a,sheet)); sheet^=(bits>>index[tuple(sorted((a,b)))])&1
            if sheet!=initial: raise ValueError('panel fails to close in the cover')
            faces.append(face)
    adj=defaultdict(set)
    for a,b in arrows: adj[a].add(b)
    return {'arrows':arrows,'faces':faces,'components':len(components(set(adj),adj)),'topology':topology(faces)}

def digest(r): return sha256(b'marici.glue-holonomy.v1\0'+json.dumps(r,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def verify(packet):
    if set(packet)!={'schema','belt_packet','state_packet','root','record'} or packet['schema']!='marici.glue-holonomy-store.v1': raise ValueError('schema')
    verify_belts(packet['belt_packet']); sr=verify_s4(packet['state_packet'])
    record=packet['record']
    if digest(record)!=packet['root'] or set(record)!={'kind','belt_source','state_source','belt_index','action','states','edge_order','edge_bits','claimed_holonomy','lifted_cover'}: raise ValueError('record hash/schema')
    if record['kind']!='C2-belt-glue' or record['belt_source']!=packet['belt_packet']['root'] or record['state_source']!=packet['state_packet']['root'] or record['belt_index']!=0 or record['action']!='linear (AB), not semilinear': raise ValueError('attachment/action binding')
    target=next(r['target'] for r in sr['generator_neighbors'] if r['mode']=='linear' and r['generator']=='(AB)')
    if record['states']!=[sr['focus_coefficient_view'],target]: raise ValueError('state binding')
    belt=packet['belt_packet']['record']['belts'][0]
    _,edges,masks,_,_,loop_masks=structure(belt)
    bits=record['edge_bits']
    if type(bits) is not int or not 0<=bits<(1<<len(edges)) or record['edge_order']!=[list(e) for e in edges]: raise ValueError('edge bit encoding')
    if any((bits&m).bit_count()%2 for m in masks): raise ValueError('nonflat panel transport')
    holonomy=[(bits&m).bit_count()%2 for m in loop_masks]
    if holonomy!=record['claimed_holonomy']: raise ValueError('false holonomy claim')
    if record['lifted_cover']!=cover(belt,edges,bits): raise ValueError('incorrect lifted witness complex')
    return {'verified':True,'root':packet['root'],'panel_holonomy':[0]*len(masks),'boundary_holonomy':holonomy,
            'cover_components':record['lifted_cover']['components'],'cover_boundary_loops':record['lifted_cover']['topology']['boundary_loops'],
            'directed_unit_coefficient_arrows':len(record['lifted_cover']['arrows'])}

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    bp=json.loads(BELT.read_text(encoding='utf-8')); sp=json.loads(STATES.read_text(encoding='utf-8'))
    verify_belts(bp); sr=verify_s4(sp); belt=bp['record']['belts'][0]
    vertices,edges,masks,gauges,loops,loop_masks=structure(belt)
    index={e:i for i,e in enumerate(edges)}; q=belt['quadrilaterals'][0]
    # One panel gets swaps on its outer AND inner circumference edges.
    twist=(1<<index[tuple(sorted((q[0],q[3])))])|(1<<index[tuple(sorted((q[1],q[2])))])
    # Exhaust the 2^18 raw edge assignments; flat assignments have dimension 12.
    flat=[b for b in range(1<<len(edges)) if all((b&m).bit_count()%2==0 for m in masks)]
    gauges_seen={0}
    for g in gauges: gauges_seen|={x^g for x in list(gauges_seen)}
    hist=Counter((b&loop_masks[0]).bit_count()%2 for b in flat)
    state0=sr['focus_coefficient_view']; state1=next(r['target'] for r in sr['generator_neighbors'] if r['mode']=='linear' and r['generator']=='(AB)')
    checks={'actual_belt_and_S4_witnesses_reverified':True,
            'two_distinct_retained_linear_states':state0!=state1,
            'six_panel_constraints_independent':rank2(masks)==6,
            'gauge_relabelling_rank_eleven':rank2(gauges)==11,
            'one_dimensional_C2_cohomology':len(edges)-rank2(masks)-rank2(gauges)==1,
            '4096_flat_assignments_exhaustively_enumerated':len(flat)==4096,
            '2048_assignments_per_holonomy_class':dict(hist)=={0:2048,1:2048},
            'gauge_orbit_exhausts_trivial_class':len(gauges_seen)==2048 and gauges_seen=={b for b in flat if (b&loop_masks[0]).bit_count()%2==0},
            'twisted_glue_locally_flat':twist in flat,
            'both_boundary_circuits_swap_the_state':all((twist&m).bit_count()%2==1 for m in loop_masks),
            'no_vertex_gauge_erases_twist':twist not in gauges_seen,
            'all_vertex_gauges_preserve_both_loop_invariants':all(all(((twist^g)&m).bit_count()%2==1 for m in loop_masks) for g in gauges_seen)}
    objects=sp['objects']; original=objects[state0]['arrows']; partner=objects[state1]['arrows']
    checks['two_laps_return_original_full_coefficient_state']=state(transform(transform(original,GENERATORS['(AB)'],False),GENERATORS['(AB)'],False))==state(original)
    checks['one_lap_is_the_checked_conjugate_state']=s4_digest(state(transform(original,GENERATORS['(AB)'],False)))==state1
    packets=[]; reports=[]
    for bits in (0,twist):
        lifted=cover(belt,edges,bits)
        record={'kind':'C2-belt-glue','belt_source':bp['root'],'state_source':sp['root'],'belt_index':0,
                'action':'linear (AB), not semilinear','states':[state0,state1],
                'edge_order':[list(e) for e in edges],'edge_bits':bits,
                'claimed_holonomy':[(bits&m).bit_count()%2 for m in loop_masks],'lifted_cover':lifted}
        packet={'schema':'marici.glue-holonomy-store.v1','belt_packet':bp,'state_packet':sp,'root':digest(record),'record':record}
        packets.append(packet); reports.append(verify(packet))
    checks['trivial_cover_two_components_twisted_cover_one']=reports[0]['cover_components']==2 and reports[1]['cover_components']==1
    checks['four_boundary_loops_become_two_in_twisted_cover']=reports[0]['cover_boundary_loops']==4 and reports[1]['cover_boundary_loops']==2
    checks['same_72_arrows_different_global_invariant']=reports[0]['directed_unit_coefficient_arrows']==reports[1]['directed_unit_coefficient_arrows']==72
    # Contracting to a one-loop interface can preserve parity as a product.
    checks['lossless_coarse_loop_retains_swap']=sum((twist>>index[tuple(sorted((a,b)))])&1 for a,b in zip(loops[0],loops[0][1:]+loops[0][:1]))%2==1
    bad=deepcopy(packets[1]); bad['record']['claimed_holonomy']=[0,0]; bad['root']=digest(bad['record'])
    checks['rehashing_does_not_validate_erased_invariant']=rejected(lambda:verify(bad))
    bad=deepcopy(packets[1]); bad['record']['edge_bits']^=1<<index[tuple(sorted((q[0],q[3])))]; bad['root']=digest(bad['record'])
    checks['single_unpaired_seam_swap_fails_local_flatness']=rejected(lambda:verify(bad))
    checks['serialized_twisted_glue_reverifies']=verify(json.loads(json.dumps(packets[1])))==reports[1]
    result={'schema':'marici.glue-holonomy-check.v1','passed':all(checks.values()),'checks':checks,
            'cases':dict(zip(('trivial','twisted'),reports)),
            'cohomology':{'flat_dimension':12,'gauge_dimension':11,'invariant_dimension':1,'classes':2},
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'disposition':'A retained loop-state permutation distinguishes two glue classes even at identical arrow count. Twisted class is a declared hypothesis, not selected by belt geometry and not a neutron identification. Lossless compression can retain the bit; erasing it changes the interface.'}
    out=BASE/'results'
    (out/'glue_holonomy_invariant.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (out/'glue_holonomy_store.json').write_text(json.dumps(packets[1],indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
