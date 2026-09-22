"""Two finite replay cycles: view-only versus source-preserving envelopes.

Exact formal response records, NOT a numerical acquisition deployment.
New source-dependent feeds are supplied by the fixture producer explicitly.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json,runpy,copy
ROOT=Path(__file__).resolve().parents[3]
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_minimal_matched_retention.py'))
f=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
manifest_path=ROOT/'research/grothendieck/results/finite-cubic-observer.json'
manifest=json.loads(manifest_path.read_text())
manifest_digest=hashlib.sha256(manifest_path.read_bytes()).hexdigest()
rows=[v['frozen'](r['shape']) for r in manifest['rows']]
assert rows[76]==v['SHAPE']
gains={name:Fraction(n)/Fraction(d) for name,(n,d) in manifest['coefficients_per_w_squared'].items()}
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(canonical(x).encode()).hexdigest()
def wire(x):return json.loads(canonical(x))
def terms(col):return [{'word':list(w),'marks':list(m),'coefficient':str(c)} for (w,m),c in sorted(col.items()) if c]
def sparse(d):return [[key,str(c)] for key,c in sorted(d.items()) if c]
def plus(a,b):
    out=dict(a)
    for key,c in b.items():out[key]=out.get(key,Fraction(0))+c
    return {key:c for key,c in out.items() if c}
def scale(col,c):return {key:c*x for key,x in col.items() if c*x}
P={((0,1),(0,0)):Fraction(1)};Q={((1,0),(0,0)):Fraction(1)}
h=plus(P,scale(Q,-1))
k=f['multiply'](f['multiply'](f['relation']((0,1),0),f['relation']((2,3),0)),f['relation']((4,5),0))
# Independently instantiate the 70->60060 lost source, then prepend the
# retained (5,7) path so its raw readings are uncontextualized at 2->60060.
local={((0,1,4,5),(0,)*4):Fraction(-1,2),((0,1,5,4),(0,)*4):Fraction(-1,2),((0,4,1,5),(0,)*4):Fraction(1)}
lost=f['multiply']({((2,3),(1,1)):Fraction(1)},local)
fixtures={'zero':{},'p':P,'q':Q,'diamond':h,'vacuum_cubic':k,'compression_loss':lost}
policy={'source_model':'fixed marked paths; event indices label primes [2,3,5,7,11,13]',
 'retention':'exact source capsule plus derived view; capsule is authoritative',
 'structure':'endpoints and marks retained; ideal filtration interpreted in the fixed source model',
 'receiver_manifest_sha256':manifest_digest,
 'response_scope':'formal common-filter window-pair symbols, not measured numerical values'}
stages=['terminal','ordered_records','raw_449','scalar_plus_76','vacuum_augmented']
views={};b_final={};handoffs=0
for name,col in fixtures.items():
    source={'schema':'retention-replay-source-v1','start_mask':0,'terms':terms(col),'policy':policy}
    source_hash=digest(source)
    terminal={'record':sparse(f['rho_column'](0,col))}
    n=max((len(w) for w,m in col),default=0)
    jets={str(depth):sparse(v['profile'](col,depth)) for depth in range(1,n+1)}
    # Full-cut rows retain the complete word. Each fixture is homogeneous in
    # length, so its highest-order row reconstructs that fixture exactly.
    rebuilt={}
    if n:
        for (shape,windows),c in v['profile'](col,n).items():
            seams,buffers=shape
            assert not any(buffers)
            word=tuple((b-a).bit_length()-1 for _,a,b,mark in seams)
            marks=tuple(mark for _,a,b,mark in seams)
            rebuilt[word,marks]=c
    assert rebuilt==col
    d3=v['profile'](col,3)
    raw=[{} for _ in rows]
    for index,shape in enumerate(rows):
        raw[index]={windows:c for (sh,windows),c in d3.items() if sh==shape}
    total={}
    for row,reading in zip(manifest['rows'],raw):
        total=plus(total,scale(reading,row['sign']*gains[row['coefficient']]))
    minimal={'combined_formal':sparse(total),'raw_76_formal':sparse(raw[76])}
    vacshape=((('e',0,1,0),('e',3,7,0),('e',15,31,0)),(0,0,0,0))
    vacuum=str(d3.get((vacshape,()),0))
    task_views=[terminal,{'ordered_jets':jets},{'readings_formal':[sparse(r) for r in raw]},
                minimal,dict(minimal,vacuum=vacuum)]
    views[name]={};previous=None
    for index,(stage,view) in enumerate(zip(stages,task_views)):
        # A has only the view. B carries the SAME view plus an exact source
        # capsule. Subsequent B handoffs copy the capsule actually received.
        a=wire({'stage':stage,'view':view})
        capsule=source if previous is None else previous['source_capsule']
        b=wire({'stage':stage,'view':view,'source_capsule':capsule,'source_sha256':source_hash})
        assert digest(b['source_capsule'])==b['source_sha256']
        assert b['source_capsule']['policy']==policy
        restored=f['parse_terms'](b['source_capsule']['terms'])
        assert restored==col and a['view']==b['view']
        views[name][stage]=digest(a['view']);previous=b;handoffs+=1
    b_final[name]=previous
# Collision and reacquisition gates: never reinterpret a fresh feed as an
# inverse computation from a prior lossy view.
assert views['p']['terminal']==views['q']['terminal']
assert views['p']['ordered_records']!=views['q']['ordered_records']
assert views['diamond']['terminal']==views['zero']['terminal']
assert views['vacuum_cubic']['raw_449']==views['zero']['raw_449']
assert views['compression_loss']['raw_449']!=views['zero']['raw_449']
assert views['compression_loss']['scalar_plus_76']==views['zero']['scalar_plus_76']
assert views['vacuum_cubic']['scalar_plus_76']==views['zero']['scalar_plus_76']
assert views['vacuum_cubic']['vacuum_augmented']!=views['zero']['vacuum_augmented']
assert views['compression_loss']['vacuum_augmented']==views['zero']['vacuum_augmented']
assert views['diamond']['vacuum_augmented']==views['zero']['vacuum_augmented']
assert len({b['source_sha256'] for b in b_final.values()})==len(fixtures)
def recover(envelope):
    if 'source_capsule' not in envelope:raise ValueError('missing authoritative source')
    if digest(envelope['source_capsule'])!=envelope['source_sha256']:raise ValueError('source digest mismatch')
    return f['parse_terms'](envelope['source_capsule']['terms'])
bad=copy.deepcopy(b_final['diamond']);del bad['source_capsule']
try:recover(bad)
except ValueError:pass
else:raise AssertionError('missing source accepted')
bad=copy.deepcopy(b_final['diamond']);bad['source_capsule']['terms'][0]['coefficient']='2'
try:recover(bad)
except ValueError:pass
else:raise AssertionError('changed source accepted')
report={'passed':True,'fixtures':list(fixtures),'serialized_handoffs':handoffs,
 'view_hashes':views,'checks':{'same_visible_outputs_in_both_cycles':True,
 'source_preserved_after_every_b_handoff':True,'all_six_inputs_distinct_in_b':True,
 'a_terminal_collision':True,'a_scalar_compression_collision':True,
 'new_vacuum_feed_distinguishes_cubic_but_not_other_losses':True,
 'missing_or_corrupt_capsule_rejected':True},
 'fresh_input_boundaries':['ordered_records is a new source-dependent record feed, not computed from terminal alone',
 'vacuum_augmented includes an independent source-dependent vacuum feed, not inferred from scalar_plus_76'],
 'scope':'Finite exact replay with formal response symbols. Not production receiver integration, a physical acquisition, or completed-source reconstruction. Integrity digests are not authentication. B preserves information by retaining its actual input, not by recovering it from a lossy observer.'}
out=ROOT/'research/voevodsky/results'
(out/'retention-replay-cycles.json').write_text(json.dumps(report,indent=2)+'\n')
(out/'retention-replay-source-capsules.json').write_text(json.dumps(b_final,indent=2)+'\n')
print(json.dumps({key:value for key,value in report.items() if key!='view_hashes'},indent=2))
