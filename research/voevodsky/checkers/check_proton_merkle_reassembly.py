"""Exact 1836-arrow Merkle packaging, tetrahedral centers and pruning witness.
Source: research/nima's retained twelve-triangle L/G/N coefficient network.
Pruning minimality is fixed-weight edge deletion, not arbitrary refactoring.
"""
from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import argparse
import json

BASE=Path(__file__).resolve().parents[1]
NIMA=BASE.parent/'nima'
ARROWS=NIMA/'results/twelve-triangle-1836-arrows.json'
GEOMETRY=NIMA/'results/twelve-triangle-positive-geometry.json'
POINTS={'A':[1,1,1],'B':[1,-1,-1],'C':[-1,1,-1],'D':[-1,-1,1]}
FACES=['ABC','ABD','ACD','BCD']
ZERO=(Q(0),Q(0)); ONE=(Q(1),Q(0))
def plus(a,b): return a[0]+b[0],a[1]+b[1]
def times(a,b): return a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def digest(r): return sha256(b'marici.proton-merkle.v1\0'+json.dumps(r,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def weight(r): return Q(r['weight_real']),Q(r['weight_imag_sqrt3'])

def cycle_list(rows):
    by_source=defaultdict(list)
    for i,r in enumerate(rows): by_source[tuple(r['source'])].append(i)
    cycles=[]
    for i,r in enumerate(rows):
        if r['source'][0]!='raw': continue
        for j in by_source[tuple(r['target'])]:
            for k in by_source[tuple(rows[j]['target'])]:
                if rows[k]['target']==r['source']: cycles.append([i,j,k])
    return cycles

def construct(rows,geometry):
    store={}
    def put(r): key=digest(r); store[key]=r; return key
    owner={r['outer_arrow']:''.join(sorted(r['triangle'][0][2:])) for r in geometry['triangles_and_transports']}
    ports={}
    for r in rows:
        for endpoint in (r['source'],r['target']):
            p=tuple(endpoint)
            ports[p]=put({'kind':'port','stage':p[0],'triangle':p[1],'axis':p[2],'owner':owner[p[1]],'type':'Q(sqrt(-3))'})
    arrows=[]
    for r in rows:
        coefficient=put({'kind':'coefficient','type':'Q(sqrt(-3))','real':r['weight_real'],'imag_sqrt3':r['weight_imag_sqrt3']})
        arrows.append(put({'kind':'arrow','source':ports[tuple(r['source'])],'target':ports[tuple(r['target'])],'coefficient':coefficient}))
    sectors=[]; bridges=[]
    for face in FACES:
        center=[str(sum(Q(POINTS[v][axis]) for v in face)/4) for axis in range(3)]
        geometry_ref=put({'kind':'constituent-tetrahedron','face':face,'vertices':{'O':['0']*3,**{v:list(map(str,POINTS[v])) for v in face}},'barycenter':center})
        owned=[arrows[i] for i,r in enumerate(rows) if owner[r['source'][1]]==owner[r['target'][1]]==face]
        sectors.append(put({'kind':'sector','owner':face,'geometry':geometry_ref,'arrows':sorted(owned)}))
    for a,b in combinations(FACES,2):
        refs=[arrows[i] for i,r in enumerate(rows) if {owner[r['source'][1]],owner[r['target'][1]]}=={a,b}]
        bridges.append(put({'kind':'coupling','owners':[a,b],'arrows':sorted(refs)}))
    cycles=[put({'kind':'closed-cycle','arrows':[arrows[i] for i in c]}) for c in cycle_list(rows)]
    cert=put({'kind':'pruning-witness','rule':'complete-positive-trace-cycle-cover; fixed weights; deletion only','cycles':sorted(cycles)})
    geo=put({'kind':'source-geometry','payload':geometry})
    root=put({'kind':'proton-like-package','geometry':geo,'sectors':sectors,'couplings':bridges,'pruning_witness':cert,
              'source_files':{'arrows_sha256':sha256(ARROWS.read_bytes()).hexdigest(),'geometry_sha256':sha256(GEOMETRY.read_bytes()).hexdigest()}})
    return {'schema':'marici.proton-merkle-store.v1','root':root,'objects':store}

def verify(artifact):
    if set(artifact)!={'schema','root','objects'} or artifact['schema']!='marici.proton-merkle-store.v1': raise ValueError('artifact schema')
    store=artifact['objects']; reached=set()
    def get(ref,kind,fields):
        if ref not in store or digest(store[ref])!=ref: raise ValueError('missing object or hash mismatch')
        r=store[ref]; reached.add(ref)
        if r.get('kind')!=kind or set(r)!={'kind'}|set(fields.split()): raise ValueError('record shape')
        return r
    root=get(artifact['root'],'proton-like-package','geometry sectors couplings pruning_witness source_files')
    geo=get(root['geometry'],'source-geometry','payload')['payload']
    triangles=geo['triangles_and_transports']
    owner={r['outer_arrow']:''.join(sorted(r['triangle'][0][2:])) for r in triangles}
    expected_owner={a+b:face for face,cycle in [('ABC','ABC'),('ABD','ADB'),('ACD','ACD'),('BCD','BDC')] for a,b in zip(cycle,cycle[1:]+cycle[:1])}
    if owner!=expected_owner or len(triangles)!=12: raise ValueError('source face ownership')
    if len(root['sectors'])!=4 or len(root['couplings'])!=6: raise ValueError('package count')
    rows=[]; arrow_refs=[]; package_counts={}; centers={}; seen_owners=set(); seen_pairs=set(); all_ports=set()
    for kind,refs in [('sector',root['sectors']),('coupling',root['couplings'])]:
        for ref in refs:
            r=get(ref,kind,'owner geometry arrows' if kind=='sector' else 'owners arrows')
            if kind=='sector':
                face=r['owner']
                if face not in FACES or face in seen_owners: raise ValueError('duplicate/unknown sector')
                seen_owners.add(face)
                g=get(r['geometry'],'constituent-tetrahedron','face vertices barycenter')
                expected_center=[str(sum(Q(POINTS[v][i]) for v in face)/4) for i in range(3)]
                expected_vertices={'O':['0']*3,**{v:list(map(str,POINTS[v])) for v in face}}
                if g!={'kind':'constituent-tetrahedron','face':face,'vertices':expected_vertices,'barycenter':expected_center}: raise ValueError('constituent geometry')
                centers[face]=expected_center; expected_set={face}; expected_count=135
            else:
                pair=tuple(r['owners'])
                if pair not in list(combinations(FACES,2)) or pair in seen_pairs: raise ValueError('coupling ownership')
                seen_pairs.add(pair); expected_set=set(pair); expected_count=216
            if len(r['arrows'])!=expected_count: raise ValueError('support size changed')
            package_counts[ref]=len(r['arrows'])
            for ar in r['arrows']:
                a=get(ar,'arrow','source target coefficient'); endpoints=[]; owners=set()
                for endpoint in (a['source'],a['target']):
                    p=get(endpoint,'port','stage triangle axis owner type'); all_ports.add(endpoint)
                    if p['triangle'] not in owner or p['owner']!=owner[p['triangle']] or p['type']!='Q(sqrt(-3))' or p['axis'] not in ('x','y','z'): raise ValueError('typed port')
                    endpoints.append([p['stage'],p['triangle'],p['axis']]); owners.add(p['owner'])
                if owners!=expected_set or (endpoints[0][0],endpoints[1][0]) not in [('raw','local'),('local','aligned'),('aligned','raw')]: raise ValueError('stage or owner attachment')
                w=get(a['coefficient'],'coefficient','type real imag_sqrt3')
                if w['type']!='Q(sqrt(-3))' or [str(Q(w[k])) for k in ('real','imag_sqrt3')]!=[w['real'],w['imag_sqrt3']] or (Q(w['real']),Q(w['imag_sqrt3']))==ZERO: raise ValueError('nonzero exact coefficient')
                rows.append({'source':endpoints[0],'target':endpoints[1],'weight_real':w['real'],'weight_imag_sqrt3':w['imag_sqrt3']}); arrow_refs.append(ar)
    keys=[(tuple(r['source']),tuple(r['target'])) for r in rows]
    if len(rows)!=1836 or len(set(keys))!=1836 or len(set(arrow_refs))!=1836 or len(all_ports)!=108: raise ValueError('arrow/port occurrence loss')
    stage_counts=Counter(r['source'][0] for r in rows)
    if stage_counts!={'raw':108,'local':432,'aligned':1296}: raise ValueError('stage support')
    # Full target operator: GL=N; dense N is a rank-one Hermitian trace-one projector.
    matrices={stage:{} for stage in stage_counts}
    for r in rows: matrices[r['source'][0]][tuple(r['target'][1:]),tuple(r['source'][1:])]=weight(r)
    L,G,N=(matrices[s] for s in ('raw','local','aligned'))
    GL=defaultdict(lambda:ZERO)
    for (i,k),a in G.items():
        for (kk,j),b in L.items():
            if k==kk: GL[i,j]=plus(GL[i,j],times(a,b))
    if {k:v for k,v in GL.items() if v!=ZERO}!=N: raise ValueError('full operator GL != N')
    labels=sorted({i for i,j in N}); z=labels[0]
    if len(labels)!=36 or len(N)!=1296: raise ValueError('target dimension')
    for i in labels:
        for j in labels:
            if times(N[i,j],N[z,z])!=times(N[i,z],N[z,j]) or N[i,j]!=(N[j,i][0],-N[j,i][1]): raise ValueError('target rank-one Hermitian condition')
    trace=ZERO
    for i in labels: trace=plus(trace,N[i,i])
    if trace!=ONE: raise ValueError('target trace')
    cert=get(root['pruning_witness'],'pruning-witness','rule cycles')
    if cert['rule']!='complete-positive-trace-cycle-cover; fixed weights; deletion only': raise ValueError('pruning rule')
    expected={tuple(arrow_refs[i] for i in c) for c in cycle_list(rows)}
    actual=[]; lookup={ref:r for ref,r in zip(arrow_refs,rows)}; losses={ref:Q(0) for ref in arrow_refs}; total=Q(0)
    for ref in cert['cycles']:
        c=get(ref,'closed-cycle','arrows')['arrows']; actual.append(tuple(c)); value=ONE
        if len(c)!=3 or any(a not in lookup for a in c): raise ValueError('cycle membership')
        for a in c: value=times(value,weight(lookup[a]))
        if value[1]!=0 or value[0]<=0: raise ValueError('nonpositive cycle trace weight')
        total+=value[0]
        for a in c: losses[a]+=value[0]
    if len(actual)!=1296 or len(set(actual))!=1296 or set(actual)!=expected or total!=1 or min(losses.values())<=0: raise ValueError('incomplete positive cycle cover')
    # Complete positive trace coverage proves every nonempty fixed-weight deletion
    # removes positive trace weight and creates no cycle; the return cannot equal N.
    return {'verified':True,'root':artifact['root'],'arrows':len(rows),'ports':len(all_ports),
            'sector_sizes':[135]*4,'coupling_sizes':[216]*6,'stage_supports':[108,432,1296],
            'barycenters':centers,'positive_cycles':len(actual),'cycle_trace_sum':str(total),
            'minimum_single_arrow_trace_loss':str(min(losses.values())),
            'full_return_operator_verified':True,'fixed_weight_pruning_minimal':True,
            'reachable_objects':len(reached),'distinct_coefficient_objects':sum(store[k]['kind']=='coefficient' for k in reached),
            'scope':'Fixed-weight deletion only; four face sectors are not independently normalized particles; no physical proton mass identification.'},rows

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def run():
    rows=json.loads(ARROWS.read_text(encoding='utf-8')); geo=json.loads(GEOMETRY.read_text(encoding='utf-8'))
    artifact=construct(rows,geo); report,decoded=verify(artifact)
    key=lambda r:(r['source'],r['target'])
    checks={'all_source_arrows_reconstructed_exactly':sorted(rows,key=key)==sorted(decoded,key=key),
            'four_sectors_six_couplings_partition_support':sum(report['sector_sizes'])+sum(report['coupling_sizes'])==1836,
            '1836_unique_arrows_and_108_typed_ports':report['arrows']==1836 and report['ports']==108,
            'full_operator_and_pruning_witness_verified':report['full_return_operator_verified'] and report['fixed_weight_pruning_minimal'],
            'all_1296_positive_cycles_retained':report['positive_cycles']==1296 and report['cycle_trace_sum']=='1',
            'barycenters_form_reflected_quarter_scale_tetrahedron':all([Q(x) for x in report['barycenters'][face]]==[-Q(x)/4 for x in POINTS[next(v for v in POINTS if v not in face)]] for face in FACES),
            'coefficient_sharing_does_not_merge_arrows':report['distinct_coefficient_objects']<1836}
    def rewrite(art,ref,rec): art['objects'][digest(rec)]=rec; return digest(rec)
    tamper=deepcopy(artifact); ar=next(k for k,v in tamper['objects'].items() if v['kind']=='coefficient'); tamper['objects'][ar]['real']='999'
    checks['unrehashed_weight_tamper_rejected']=rejected(lambda:verify(tamper))
    erase=deepcopy(artifact); root=deepcopy(erase['objects'][erase['root']]); sref=root['sectors'][0]; sector=deepcopy(erase['objects'][sref]); sector['arrows'].pop(); root['sectors'][0]=rewrite(erase,sref,sector); erase['root']=rewrite(erase,erase['root'],root)
    checks['honestly_rehashed_arrow_deletion_rejected']=rejected(lambda:verify(erase))
    lost=deepcopy(artifact); root=deepcopy(lost['objects'][lost['root']]); pref=root['pruning_witness']; witness=deepcopy(lost['objects'][pref]); witness['cycles'].pop(); root['pruning_witness']=rewrite(lost,pref,witness); lost['root']=rewrite(lost,lost['root'],root)
    checks['honestly_rehashed_incomplete_pruning_witness_rejected']=rejected(lambda:verify(lost))
    wrong=deepcopy(artifact); root=deepcopy(wrong['objects'][wrong['root']]); sref=root['sectors'][0]; sector=deepcopy(wrong['objects'][sref]); aref=sector['arrows'][0]; arrow=deepcopy(wrong['objects'][aref]); wref=arrow['coefficient']; coefficient=deepcopy(wrong['objects'][wref]); coefficient['real']=str(Q(coefficient['real'])+1)
    arrow['coefficient']=rewrite(wrong,wref,coefficient); sector['arrows'][0]=rewrite(wrong,aref,arrow); root['sectors'][0]=rewrite(wrong,sref,sector); wrong['root']=rewrite(wrong,wrong['root'],root)
    checks['honestly_rehashed_coefficient_change_rejected']=rejected(lambda:verify(wrong))
    shifted=deepcopy(artifact); root=deepcopy(shifted['objects'][shifted['root']]); sref=root['sectors'][0]; sector=deepcopy(shifted['objects'][sref]); gref=sector['geometry']; geometry=deepcopy(shifted['objects'][gref]); geometry['barycenter'][0]='0'; sector['geometry']=rewrite(shifted,gref,geometry); root['sectors'][0]=rewrite(shifted,sref,sector); shifted['root']=rewrite(shifted,shifted['root'],root)
    checks['honestly_rehashed_false_barycenter_rejected']=rejected(lambda:verify(shifted))
    misbound=deepcopy(artifact); root=deepcopy(misbound['objects'][misbound['root']]); cref=root['couplings'][0]; coupling=deepcopy(misbound['objects'][cref]); coupling['owners']=['ABC','ACD']; root['couplings'][0]=rewrite(misbound,cref,coupling); misbound['root']=rewrite(misbound,misbound['root'],root)
    checks['honestly_rehashed_coupling_attachment_rejected']=rejected(lambda:verify(misbound))
    checks['serialized_store_reverifies']=verify(json.loads(json.dumps(artifact)))[0]==report
    out=BASE/'results'; out.mkdir(exist_ok=True)
    (out/'proton_merkle_store.json').write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    receipt={'schema':'marici.proton-merkle-reassembly-check.v1','passed':all(checks.values()),'checks':checks,'construction':report,
             'source_arrows_sha256':sha256(ARROWS.read_bytes()).hexdigest(),'source_geometry_sha256':sha256(GEOMETRY.read_bytes()).hexdigest(),
             'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (out/'proton_merkle_reassembly.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    if not receipt['passed']: raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--verify',type=Path); args=parser.parse_args()
    if args.verify: print(json.dumps(verify(json.loads(args.verify.read_text(encoding='utf-8')))[0],indent=2))
    else: run()
