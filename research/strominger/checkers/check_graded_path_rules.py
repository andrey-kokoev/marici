"""Executable graded, support-labelled path algebra on saved witnesses."""
from dataclasses import dataclass
from pathlib import Path
import json, hashlib, itertools
ROOT=Path(__file__).resolve().parents[3]; BASE=ROOT/'research/strominger/results'; hashes={}
def load(path):
    b=path.read_bytes();hashes[str(path.relative_to(ROOT))]=hashlib.sha256(b).hexdigest();return json.loads(b)
ID=tuple(range(5))
def product(a,b): return tuple(a[i] for i in b) # b after a

def inverse(p):return tuple(p.index(i) for i in range(5))
@dataclass(frozen=True)
class Reader:
    key:int
    species:str
    body:int
    origin:int
    dual:bool=False
    def reverse(self):return Reader(self.key,{'proton':'electron','electron':'proton','neutron':'neutron'}[self.species],self.body,self.origin,not self.dual)
@dataclass(frozen=True)
class Arrow:
    source:Reader
    target:Reader
    grade:int
    permutation:tuple
    occupied:frozenset
    reference:frozenset
    word:tuple
    def __post_init__(self):
        assert sorted(self.permutation)==list(range(5))
        assert self.grade==self.target.origin-self.source.origin
        assert {self.source.body,self.target.body}<=self.occupied<=self.reference
    def reverse(self):
        return Arrow(self.target.reverse(),self.source.reverse(),-self.grade,inverse(self.permutation),self.occupied,self.reference,tuple((name,not backwards) for name,backwards in reversed(self.word)))
def identity(x):return Arrow(x,x,0,ID,frozenset([x.body]),frozenset([x.body]),())
def then(a,b):
    assert a.target==b.source
    return Arrow(a.source,b.target,a.grade+b.grade,product(a.permutation,b.permutation),a.occupied|b.occupied,a.reference|b.reference,a.word+b.word)
def transfer(a):return (a.source,a.target,a.grade,a.permutation)
def contract(pn,ne,edge_vertices,expected_edge,occupied_configuration,terminal_source,terminal_target):
    assert pn.word==(('PN',False),) and ne.word==(('NE',False),)
    assert pn.source.species=='proton' and pn.target.species=='neutron' and ne.target.species=='electron'
    assert pn.grade==ne.grade==0 and pn.target==ne.source
    assert len({pn.source.body,pn.target.body,ne.target.body})==3
    assert pn.target.body not in occupied_configuration
    assert len(edge_vertices)==2 and edge_vertices==expected_edge
    assert terminal_source and terminal_target
    p=then(pn,ne)
    return Arrow(p.source,p.target,p.grade,p.permutation,frozenset([p.source.body,p.target.body]),p.reference,(('PE-contraction',False),))
receipt=load(BASE/'terminal-pe-independent/verification.json');assert receipt['status']=='independent-python-check-passed'
# Refuse stale independent evidence.
for name,digest in receipt['sourceHashes'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
probe=load(BASE/'terminal-pe-probe/verification.json')
counts={'identities':0,'associativity':0,'reversalComposition':0,'doubleReversal':0,'contractions':0,'negativeControls':0}; summaries=[]
for isotope in ['n15','ne22']:
    base=BASE/f'reference-{isotope}-search';summary=load(base/'verification.json');row=next(r for r in summary['rows'] if r['witnessFile']);w=load(base/row['witnessFile'])['witness'];charts={int(c['id'].split('-')[-1]):c for c in w['charts']};packets={p['id']:p for p in w['packets']}
    readers={i:Reader(i,charts[p['chart']]['species'],charts[p['chart']]['cell'],p['origin']) for i,p in packets.items()}
    arrows={}
    for op in w['operations']:
        a,b=readers[op['source']],readers[op['target']];support=frozenset([a.body,b.body]);arrows[op['id']]=Arrow(a,b,op['phaseDelta'],tuple(op['permutation']),support,support,((op['kind'],False),))
    for a in arrows.values():
        assert then(identity(a.source),a)==a and then(a,identity(a.target))==a;counts['identities']+=2
        assert a.reverse().reverse()==a;counts['doubleReversal']+=1
    by_source={x:[] for x in readers.values()}
    for a in arrows.values():by_source[a.source].append(a)
    for a in arrows.values():
        for b in by_source[a.target]:
            assert then(a,b).reverse()==then(b.reverse(),a.reverse());counts['reversalComposition']+=1
            for c in by_source[b.target]:assert then(then(a,b),c)==then(a,then(b,c));counts['associativity']+=1
    for d in probe['deletions']:
        if d['sourceIsotope']!=isotope or not d['variants']['electron-and-proton-record-terminal']['passesHypotheticalChecks']:continue
        occupied={readers[i].body for i in d['selectedPackets']};selected=set(d['selectedPackets']);native=[o for o in w['operations'] if o['source'] in selected and o['target'] in selected]
        for e in d['shortcuts']:
            if not e['recordTerminal']:continue
            pn,ne=[arrows[i] for i in e['nativeFactors']];pc=charts[packets[e['source']]['chart']];ec=charts[packets[e['target']]['chart']]
            pv={pc['aliases'][k] for k in ['C0','M0','C1','M1']};ev={ec['aliases'][k] for k in ['M1','C1','C2','M2']};edge=pv&ev;expected={pc['aliases']['C1'],pc['aliases']['M1']}
            ts=not any(o['source']==e['source'] for o in native);te=not any(o['source']==e['target'] for o in native)
            contracted=contract(pn,ne,edge,expected,occupied,ts,te);original=then(pn,ne)
            assert transfer(contracted)==transfer(original)
            assert contracted.permutation==tuple(e['permutation'])
            assert contracted.reference==original.reference
            assert original.occupied-contracted.occupied==frozenset([e['referenceNeutronCell']]);assert contracted!=original
            assert transfer(contracted.reverse())==transfer(original.reverse())
            assert contracted.reverse().reverse()==contracted
            counts['contractions']+=1
            for changes in [{'occupied_configuration':occupied|{pn.target.body}},{'terminal_source':False},{'terminal_target':False},{'edge_vertices':set()}]:
                args=dict(pn=pn,ne=ne,edge_vertices=edge,expected_edge=expected,occupied_configuration=occupied,terminal_source=ts,terminal_target=te);args.update(changes)
                try:contract(**args)
                except AssertionError:counts['negativeControls']+=1
                else:raise AssertionError('Bad contraction accepted')
            summaries.append({'sourceIsotope':isotope,'deletedNeutron':d['deletedNeutron']['cell'],'source':e['source'],'target':e['target'],'grade':contracted.grade,'permutation':contracted.permutation,'occupiedBefore':sorted(original.occupied),'occupiedAfter':sorted(contracted.occupied),'referenceSupport':sorted(contracted.reference)})
# The reverse PE rewrite is the conjugate of this forward rewrite, with a
# boundary-entry condition; it is not rechecked as a forward terminal rule.
out=BASE/'graded-path-rules';out.mkdir(exist_ok=True)
result={'status':'graded-path-algebra-checks-pass','checks':counts,'contractions':summaries,'sourceHashes':hashes,'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite tests of path category laws, involutive opposite-category reversal and experimental support rewrite. Grade is measured in the original fixed origin coordinate; reversal negates it. Physical chart reversal is a separate layer. Reference support here tracks carrier sites, not every external alias vertex. No production/viewer changes.'}
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'checks':counts}))
