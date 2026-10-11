"""Exact S4 neighborhood of the retained proton-like coefficient network.
Compare orientation-repaired linear action with parity-semilinear action.
These are explicit mathematical conventions, not particle transition laws.
"""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import argparse
import json

from check_proton_merkle_reassembly import verify as verify_focus, construct, cycle_list, weight, times, ONE

BASE=Path(__file__).resolve().parents[1]
FOCUS=BASE/'results/proton_merkle_store.json'
LABELS='ABCD'; AXES='xyz'
POINTS=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
GROUP=list(permutations(range(4))); ID=tuple(range(4))
GENERATORS={'(AB)':(1,0,2,3),'(BC)':(0,2,1,3),'(CD)':(0,1,3,2)}

def parity(p): return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
def compose(p,q): return tuple(p[q[i]] for i in range(4))
def matrix(p):
    numerator=[[sum(POINTS[p[k]][i]*POINTS[k][j] for k in range(4)) for j in range(3)] for i in range(3)]
    if any(x%4 for row in numerator for x in row): raise ValueError('nonintegral tetrahedral matrix')
    return [[x//4 for x in row] for row in numerator]
def determinant(m):
    return sum((1 if parity3==0 else -1)*m[0][p[0]]*m[1][p[1]]*m[2][p[2]]
               for p in permutations(range(3)) for parity3 in [sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2])

def port_image(port,p,repair=True):
    stage,triangle,axis=port
    triangle=''.join(LABELS[p[LABELS.index(v)]] for v in triangle)
    if repair and parity(p): triangle=triangle[::-1]
    m=matrix(p); j=AXES.index(axis)
    entries=[(i,m[i][j]) for i in range(3) if m[i][j]]
    if len(entries)!=1 or abs(entries[0][1])!=1: raise ValueError('not a signed permutation')
    i,sign=entries[0]
    return (stage,triangle,AXES[i]),sign

def transform(rows,p,semilinear):
    out=[]
    for r in rows:
        source,a=port_image(tuple(r['source']),p); target,b=port_image(tuple(r['target']),p)
        real,imag=weight(r); sign=a*b
        if semilinear and parity(p): imag=-imag
        out.append({'source':list(source),'target':list(target),'weight_real':str(sign*real),'weight_imag_sqrt3':str(sign*imag)})
    return sorted(out,key=lambda r:(r['source'],r['target']))

def digest(rec): return sha256(b'marici.proton-s4.v1\0'+json.dumps(rec,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def state(rows):
    return {'kind':'coefficient-state','arrows':sorted(rows,key=lambda r:(r['source'],r['target']))}

def make_packet(focus):
    _,rows=verify_focus(focus); objects={}
    def put(rec): key=digest(rec); objects[key]=rec; return key
    base=put(state(rows)); images={}; witnesses=[]
    for mode in ('linear','semilinear'):
        for p in GROUP:
            target=put(state(transform(rows,p,mode=='semilinear')))
            rec={'kind':'S4-action-witness','source':base,'target':target,'permutation':list(p),
                 'mode':mode,'orientation_repair':'reverse outer edge on odd permutations',
                 'spatial_matrix':matrix(p),'conjugate_coefficients':mode=='semilinear' and bool(parity(p))}
            witnesses.append(put(rec)); images[mode,''.join(LABELS[i] for i in p)]=target
    root=put({'kind':'S4-neighborhood','focus_package':focus['root'],'coefficient_view':base,'actions':witnesses})
    return {'schema':'marici.proton-s4-store.v1','focus':focus,'root':root,'objects':objects}

def verify_packet(packet):
    if set(packet)!={'schema','focus','root','objects'} or packet['schema']!='marici.proton-s4-store.v1': raise ValueError('packet schema')
    report,rows=verify_focus(packet['focus']); store=packet['objects']
    def get(ref):
        if ref not in store or digest(store[ref])!=ref: raise ValueError('hash mismatch')
        return store[ref]
    root=get(packet['root'])
    if set(root)!={'kind','focus_package','coefficient_view','actions'} or root['kind']!='S4-neighborhood' or root['focus_package']!=report['root']: raise ValueError('focus binding')
    if get(root['coefficient_view'])!=state(rows): raise ValueError('wrong coefficient view')
    seen=set(); images={}; generators=[]
    for ref in root['actions']:
        r=get(ref); p=tuple(r['permutation']); mode=r['mode']
        if p not in GROUP or mode not in ('linear','semilinear') or (mode,p) in seen: raise ValueError('action inventory')
        seen.add((mode,p))
        expected={'kind':'S4-action-witness','source':root['coefficient_view'],'target':r['target'],'permutation':list(p),
                  'mode':mode,'orientation_repair':'reverse outer edge on odd permutations','spatial_matrix':matrix(p),
                  'conjugate_coefficients':mode=='semilinear' and bool(parity(p))}
        if r!=expected or get(r['target'])!=state(transform(rows,p,mode=='semilinear')): raise ValueError('incorrect transported state or witness')
        images[mode,p]=r['target']
        for label,g in GENERATORS.items():
            if p==g: generators.append({'generator':label,'mode':mode,'target':r['target'],'fixes_focus_view':r['target']==root['coefficient_view'],'witness':ref})
    if seen!={(mode,p) for mode in ('linear','semilinear') for p in GROUP}: raise ValueError('incomplete group action inventory')
    return {'verified':True,'focus_root':report['root'],'focus_coefficient_view':root['coefficient_view'],
            'linear_orbit_size':len({images['linear',p] for p in GROUP}),
            'linear_stabilizer_size':sum(images['linear',p]==root['coefficient_view'] for p in GROUP),
            'semilinear_orbit_size':len({images['semilinear',p] for p in GROUP}),
            'semilinear_stabilizer_size':sum(images['semilinear',p]==root['coefficient_view'] for p in GROUP),
            'generator_neighbors':generators,'actions_verified':len(seen)}

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    focus=json.loads(FOCUS.read_text(encoding='utf-8')); report,rows=verify_focus(focus)
    packet=make_packet(focus); result=verify_packet(packet)
    geo=focus['objects'][focus['objects'][focus['root']]['geometry']]['payload']
    owner={r['outer_arrow']:r['triangle'][0][2:] for r in geo['triangles_and_transports']}
    ports=sorted({tuple(r['source']) for r in rows})
    checks={'focus_pruning_certificate_reverified':report['fixed_weight_pruning_minimal'],
            'all_24_spatial_matrices_have_correct_orientation':all(determinant(matrix(p))==(-1)**parity(p) for p in GROUP),
            'proper_A4_stabilizes_linear_state':all(transform(rows,p,False)==transform(rows,ID,False) for p in GROUP if not parity(p)),
            'linear_orbit_two_and_stabilizer_twelve':result['linear_orbit_size']==2 and result['linear_stabilizer_size']==12,
            'semilinear_orbit_one_and_stabilizer_twenty_four':result['semilinear_orbit_size']==1 and result['semilinear_stabilizer_size']==24}
    conjugate=deepcopy(rows)
    for r in conjugate: r['weight_imag_sqrt3']=str(-weight(r)[1])
    checks['every_odd_linear_image_is_exact_complex_conjugate']=all(state(transform(rows,p,False))==state(conjugate) for p in GROUP if parity(p))
    checks['orientation_repair_preserves_parent_face_attachments']=all(
        owner[port_image(('raw',edge,'x'),p)[0][1]]==''.join(sorted(LABELS[p[LABELS.index(v)]] for v in face))
        for p in GROUP for edge,face in owner.items())
    checks['odd_naive_relabeling_fails_parent_face_attachment']=any(
        owner[port_image(('raw',edge,'x'),GENERATORS['(AB)'],repair=False)[0][1]]!=''.join(sorted(LABELS[GENERATORS['(AB)'][LABELS.index(v)]] for v in face))
        for edge,face in owner.items())
    # Representation law at every typed port with signs, for all 576 products.
    law=True
    for p in GROUP:
        for q in GROUP:
            pq=compose(p,q)
            for port in ports:
                middle,b=port_image(port,q); last,a=port_image(middle,p); direct,c=port_image(port,pq)
                if last!=direct or a*b!=c: law=False
            if parity(pq)!=(parity(p)+parity(q))%2: law=False
    checks['all_576_group_products_act_correctly_on_108_ports']=law
    for mode in (False,True):
        checks[('semilinear' if mode else 'linear')+'_generator_involutions']=all(state(transform(transform(rows,g,mode),g,mode))==state(rows) for g in GENERATORS.values())
    # Exact positive closed-cycle weights survive signed permutation and conjugation.
    reflected=transform(rows,GENERATORS['(AB)'],False)
    original_cycles=cycle_list(rows); new_cycles=cycle_list(reflected)
    def cycle_weights(rs,cs):
        values=[]
        for c in cs:
            value=ONE
            for i in c: value=times(value,weight(rs[i]))
            values.append(value)
        return Counter(values)
    checks['pruning_cycle_weight_multiset_preserved']=cycle_weights(rows,original_cycles)==cycle_weights(reflected,new_cycles)
    reflected_package=construct(reflected,geo)
    checks['conjugate_state_full_operator_and_pruning_reverify']=verify_focus(reflected_package)[0]['fixed_weight_pruning_minimal']
    checks['three_generator_witnesses_remain_distinct']=len({r['witness'] for r in result['generator_neighbors'] if r['mode']=='semilinear'})==3
    checks['marked_corner_orbit_has_four_points']=len({p[0] for p in GROUP})==4 and sum(p[0]==0 for p in GROUP)==6
    bad=deepcopy(packet); root=deepcopy(bad['objects'][bad['root']]); ref=next(ref for ref in root['actions'] if bad['objects'][ref]['mode']=='semilinear' and bad['objects'][ref]['conjugate_coefficients']); r=deepcopy(bad['objects'][ref]); r['conjugate_coefficients']=False; new=digest(r); bad['objects'][new]=r; root['actions'][root['actions'].index(ref)]=new; bad['root']=digest(root); bad['objects'][bad['root']]=root
    checks['rehashed_missing_conjugation_witness_rejected']=rejected(lambda:verify_packet(bad))
    checks['serialized_neighborhood_reverifies']=verify_packet(json.loads(json.dumps(packet)))==result
    out=BASE/'results'
    (out/'proton_s4_neighborhood_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    receipt={'schema':'marici.proton-s4-neighborhood-check.v1','passed':all(checks.values()),'checks':checks,'neighborhood':result,
             'source_artifact_sha256':sha256(FOCUS.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
             'scope':'Two explicit extensions of retained A4 data to S4. Linear odd permutations exchange conjugate coefficient states; parity-semilinear action fixes the unmarked state. No charge, mass or particle transition identification.'}
    (out/'proton_s4_neighborhood.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    if not receipt['passed']: raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--verify',type=Path); args=parser.parse_args()
    if args.verify: print(json.dumps(verify_packet(json.loads(args.verify.read_text(encoding='utf-8'))),indent=2))
    else: main()
