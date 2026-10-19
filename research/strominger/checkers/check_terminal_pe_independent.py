"""Independent finite-witness checker: no JS generator, solver, or probe imports."""
import json, hashlib, itertools, copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger/results'
files={}
def load(path):
    data=path.read_bytes(); files[str(path.relative_to(ROOT))]=hashlib.sha256(data).hexdigest(); return json.loads(data)
probe=load(BASE/'terminal-pe-probe/verification.json')
hydrogen=load(BASE/'hydrogen-edge-attachment/verification.json')
NAMES={'proton':['C0','M0','C1','M1'],'neutron':['M0','C1','M1','C2'],'electron':['M1','C1','C2','M2']}
MAPS={'PN':[3,1,2,0,4],'inverse-PN':[3,1,2,0,4],'NE':[0,4,2,3,1],'P-advance':[2,3,0,1,4],'N-advance':[0,3,4,1,2]}
def point(v): return tuple(map(int,v.split(',')))
def vertices(c): return frozenset(c['aliases'][n] for n in NAMES[c['species']])
def regular(vs):
    ps=list(map(point,vs)); return all(sum((x-y)**2 for x,y in zip(a,b))==2 for a,b in itertools.combinations(ps,2))
def volume(vs):
    ps=[point(v)[:3] for v in vs]; a=ps[0]; u,v,w=[tuple(p[i]-a[i] for i in range(3)) for p in ps[1:]]
    return abs(u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))
def frame(c,p):
    return [(c['aliases'][n],n[0],int(n[1:])+p['origin']) for n in NAMES[c['species']]]
def check_chart(c):
    a=c['aliases']; needed=['C0','M0','C1','M1','C2']+(['M2'] if c['species']=='electron' else [])
    assert len({a[k] for k in needed})==len(needed)
    for k in needed: assert len(point(a[k]))==4 and sum(point(a[k]))==1
    assert regular([a[k] for k in NAMES['proton']])
    assert volume([a[k] for k in NAMES['neutron']])==1
    assert not regular([a[k] for k in NAMES['neutron']])
    assert volume(vertices(c))==1
    if c['species']=='electron':
        # Distinct opposite apices enforce geometric neighbor side, not merely
        # a coincident triangular face. Native all-unit lattice cells retained.
        assert len(vertices(c)&frozenset(a[k] for k in NAMES['neutron']))==3

def assemble(packets,charts,selected,root,expected,claimed=None):
    p={x['id']:x for x in packets}; c={int(x['id'].split('-')[-1]):x for x in charts}
    selected=set(selected); assert root in selected
    for i in selected:
        assert p[i]['origin']>=0 and sorted(p[i]['permutation'])==list(range(5));check_chart(c[p[i]['chart']])
    def chart(i): return c[p[i]['chart']]
    def cell(i): return chart(i)['cell']
    def same_refs(a,b): return all(a['aliases'][k]==b['aliases'][k] for k in ['C0','M0','C1','M1','C2'])
    def transition(i,j):
        a,b=chart(i),chart(j); sa,sb=a['species'],b['species']; delta=p[j]['origin']-p[i]['origin']; shared=vertices(a)&vertices(b)
        kind=None; perm=None
        if delta==0 and same_refs(a,b):
            kind={('proton','neutron'):'PN',('neutron','proton'):'inverse-PN',('neutron','electron'):'NE'}.get((sa,sb))
            if kind and len(shared)==3: perm=MAPS[kind]
        elif delta==1 and sa==sb and sa in ('proton','neutron'):
            fa,fb=frame(a,p[i]),frame(b,p[j]); valid=fa[2]==fb[0] and fa[3]==fb[1]
            if sa=='proton': valid=valid and fa[0][0]==fb[2][0] and fa[1][0]==fb[3][0] and cell(i)==cell(j)
            else: valid=valid and fa[1][0]==fb[3][0] and (cell(i)==cell(j) or shared==frozenset(a['aliases'][k] for k in ['M1','C1','C2']))
            if valid: kind='reader-phase-advance' if cell(i)==cell(j) else 'NN-phase-advance';perm=MAPS['P-advance' if sa=='proton' else 'N-advance']
        if perm is None or [p[i]['permutation'][k] for k in perm]!=p[j]['permutation']: return None
        return (i,j,kind,perm)
    bodies={}; roles={}
    for i in selected:
        a=chart(i); key=cell(i); v=vertices(a)
        if key in bodies: assert bodies[key]==(a['species'],v)
        bodies[key]=(a['species'],v)
        for name,vertex in a['aliases'].items():
            if vertex in roles: assert roles[vertex]==name[0]
            roles[vertex]=name[0]
    counts={s:sum(sp==s for sp,_ in bodies.values()) for s in NAMES};assert counts==expected
    native=[e for i,j in itertools.permutations(sorted(selected),2) if (e:=transition(i,j))]
    shortcuts=[]
    for i in sorted(selected):
        if chart(i)['species']!='proton' or any(e[0]==i for e in native): continue
        for n in p:
            if chart(n)['species']!='neutron' or cell(n) in bodies: continue
            pn=transition(i,n)
            if pn is None or pn[2]!='PN': continue
            for j in sorted(selected):
                ne=transition(n,j)
                if ne is None or ne[2]!='NE': continue
                assert chart(j)['species']=='electron' and not any(e[0]==j for e in native)
                edge=vertices(chart(i))&vertices(chart(j)); assert edge==frozenset(chart(i)['aliases'][k] for k in ['C1','M1'])
                assert p[i]['origin']==p[j]['origin']; composite=[pn[3][k] for k in ne[3]]
                assert [p[i]['permutation'][k] for k in composite]==p[j]['permutation']
                shortcuts.append((i,j,'PE-edge',composite,cell(n)))
    # Reader histories may yield repeated identical factors; deduplicate.
    shortcuts=list({(e[0],e[1]):e for e in shortcuts}.values())
    if claimed is not None:
        actual={(e[0],e[1],tuple(e[3]),e[4]) for e in shortcuts}
        stated={(e['source'],e['target'],tuple(e['permutation']),e['referenceNeutronCell']) for e in claimed}
        assert actual==stated
    edges=native+shortcuts
    # Boolean transitive closure, independent of JS BFS and ranking encodings.
    order=sorted(selected); index={x:i for i,x in enumerate(order)}; reach=[1<<i for i in range(len(order))]
    for e in edges: reach[index[e[0]]]|=1<<index[e[1]]
    for k in range(len(order)):
        for i in range(len(order)):
            if reach[i]&(1<<k): reach[i]|=reach[k]
    exits=sum(1<<index[i] for i in selected if chart(i)['species']=='electron')
    rooted=reach[index[root]]==(1<<len(order))-1; exit_ok=all(row&exits for row in reach)
    contacts=0
    for a,b in itertools.combinations(bodies,2):
        sa,va=bodies[a];sb,vb=bodies[b];face=va&vb
        if len(face)!=3:continue
        contacts+=1;assert not (sa==sb and sa!='neutron');assert {sa,sb}!={'proton','electron'}
        kind='NE' if 'electron' in (sa,sb) else 'NN' if sa==sb else 'PN';assert sum(roles[v]=='M' for v in face)==(2 if kind=='PN' else 1)
        assert any({cell(e[0]),cell(e[1])}=={a,b} for e in native)
    return {'counts':counts,'records':len(selected),'nativeEdges':len(native),'shortcuts':len(shortcuts),'contacts':contacts,'rooted':rooted,'allReachExit':exit_ok,'passes':rooted and exit_ok}

results=[];cases=[]
for isotope in ['n15','ne22']:
    base=BASE/f'reference-{isotope}-search'; summary=load(base/'verification.json'); row=next(r for r in summary['rows'] if r['witnessFile']); w=load(base/row['witnessFile'])['witness']
    for d in probe['deletions']:
        if d['sourceIsotope']!=isotope:continue
        target=d['variants']['electron-and-proton-record-terminal'];claimed=[e for e in d['shortcuts'] if e['recordTerminal']]
        args=(w['packets'],w['charts'],d['selectedPackets'],0,d['counts'],claimed)
        result=assemble(*args);assert result['passes']==target['passesHypotheticalChecks'];results.append({'source':isotope,'deleted':d['deletedNeutron']['cell'],**result})
        if result['passes']:cases.append(args)
for h in hydrogen['rows']:
    charts=[]
    for p,b in zip(h['packets'],h['bodies']): charts.append({'id':'chart-'+str(p['chart']),'cell':b['cell'],'species':b['species'],'aliases':b['aliases']})
    root,n,e=[p['id'] for p in h['packets']]
    h1=assemble(h['packets'],charts,[root,e],root,{'proton':1,'neutron':0,'electron':1});h2=assemble(h['packets'],charts,[root,n,e],root,{'proton':1,'neutron':1,'electron':1})
    assert h1['passes'] and h1['shortcuts']==1;assert h2['passes'] and h2['shortcuts']==0
negative=[]
for args in cases:
    altered=list(copy.deepcopy(args));altered[5][0]['permutation'][0],altered[5][0]['permutation'][1]=altered[5][0]['permutation'][1],altered[5][0]['permutation'][0]
    try:assemble(*altered)
    except AssertionError:negative.append('corrupt-map-rejected')
    else:raise AssertionError('Corrupt map accepted')
    altered=list(copy.deepcopy(args));altered[4]['neutron']+=1
    try:assemble(*altered)
    except AssertionError:negative.append('wrong-count-rejected')
    else:raise AssertionError('Wrong count accepted')
    altered=list(copy.deepcopy(args));altered[5][0]['referenceNeutronCell']=-1
    try:assemble(*altered)
    except AssertionError:negative.append('wrong-reference-rejected')
    else:raise AssertionError('Wrong reference accepted')
    altered=list(copy.deepcopy(args)); victim=altered[5][0]['target']; next(p for p in altered[0] if p['id']==victim)['origin']+=1
    try:assemble(*altered)
    except AssertionError:negative.append('wrong-origin-rejected')
    else:raise AssertionError('Wrong origin accepted')
    altered=list(copy.deepcopy(args)); a=altered[1][0]['aliases'];a['C0'],a['M0']=a['M0'],a['C0']
    try:assemble(*altered)
    except AssertionError:negative.append('wrong-role-binding-rejected')
    else:raise AssertionError('Wrong role binding accepted')
out=BASE/'terminal-pe-independent';out.mkdir(exist_ok=True)
receipt={'status':'independent-python-check-passed','isotopeTrials':results,'hydrogenMarkings':len(hydrogen['rows']),'negativeControls':negative,'sourceHashes':files,'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Separate Python implementation from saved packets/charts/coordinates. Reconstructs native and experimental terminal-reader PE relations, coordinate intersections and role guards; bitset transitive closure checks rooted/exit paths. Shares native rule specification and saved source data, not JS validation code. Finite witness audit, not global field sewing or derivation of contraction.'}
(out/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'isotopeTrials':len(results),'positiveIsotopeTrials':sum(r['passes'] for r in results),'hydrogenMarkings':len(hydrogen['rows']),'negativeControls':len(negative)}))
