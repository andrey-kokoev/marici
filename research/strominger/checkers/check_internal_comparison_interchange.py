"""Fresh native internal comparison/interchange proofs and exact finite controls."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
LIB=Path.home()/'tools/cubical-agda/cubical-0.9'
EXE=shutil.which('agda')
assert EXE and LIB.is_dir()
sources=[BASE/'agda/InternalSourceComparisons.agda',BASE/'agda/InternalComparisonInterchange.agda',
         BASE/'agda/negative/InternalBadContinuation.agda',BASE/'agda/negative/InternalBadPortComparison.agda',
         BASE/'agda/NativeExtensionFamilyAudit.agda',BASE/'agda/SourceIndexedExtensionFamilies.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
         ROOT/'research/nima/agda/ProofRelevantCoherenceClosure.agda',
         ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
pos=subprocess.run(common+['--ignore-interfaces',str(sources[1])],capture_output=True,text=True,timeout=300)
log=pos.stdout+pos.stderr
(BASE/'results/internal-comparison-interchange-positive.log').write_text(log,encoding='utf-8')
assert pos.returncode==0 and 'UnsupportedIndexedMatch' not in log,log[-6000:]
negatives=[]
for path in sources[2:4]:
    neg=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(path)],capture_output=True,text=True,timeout=120)
    log=neg.stdout+neg.stderr
    (BASE/'results'/f'{path.stem}-negative.log').write_text(log,encoding='utf-8')
    assert neg.returncode!=0 and ('UnequalTerms' in log),log
    negatives.append({'module':path.stem,'exit':neg.returncode,'diagnostic':log.strip()})
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
edges={label:(s,t) for label,s,t in PACKETS}
out={v:tuple(e for e,(s,t) in edges.items() if s==v) for v in 'ABCD'}
sigma=dict(zip('ABCD','BADC'));by_edge={edge:label for label,edge in edges.items()}
instances=[];value_checks=0
for mode in ('stay','exchange'):
    actor={v:v for v in 'ABCD'} if mode=='stay' else sigma
    edge_map={e:by_edge[(actor[s],actor[t])] for e,(s,t) in edges.items()}
    edge_inv={v:k for k,v in edge_map.items()}
    # Source-port preservation checked on the whole comparison carrier.
    graph=tuple((x,actor[x],'eq') for x in 'ABCD')
    for x,y,w in graph:assert actor[x]==y
    for v in 'ABCD':
        for selected in out[v]:
            moved=edge_map[selected]
            assert moved in out[actor[v]]
            # Set-specialized endpoint loops have one witness. The Agda theorem
            # is general and does NOT assume all loop spaces are contractible.
            left_carrier=[((e,'refl'),(edge_map[e],'refl'),'eq') for e in out[v]]
            right_carrier=[(e,'refl') for e in out[actor[v]]]
            def forward(z):return edge_map[z[0][0]],'refl'
            def backward(z):
                e=edge_inv[z[0]]
                return (e,'refl'),(z[0],'refl'),'eq'
            assert set(map(forward,left_carrier))==set(right_carrier)
            for z in left_carrier:
                assert backward(forward(z))==z
                # Identity source action on the two completed route boundaries.
                assert edges[z[1][0]][1]==edges[forward(z)[0]][1]
                value_checks+=1
            for z in right_carrier:assert forward(backward(z))==z
            selected_left=((selected,'refl'),(moved,'refl'),'eq')
            assert forward(selected_left)==(moved,'refl')
            instances.append({'mode':mode,'source':v,'selected':selected,'transported':moved,
                              'continuation_boundary':edges[moved][1],
                              'comparison_route_carrier_size':len(left_carrier),
                              'attachment_route_carrier_size':len(right_carrier)})
assert len(instances)==12 and value_checks==20
assert 'AD' in out['A'] and 'AD' not in out['B'] and 'BC' in out['B']
assert sigma['D']=='C' and edges['CA']==('C','A')
for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':pos.returncode,'negative_controls':negatives,
        'finite_interchange_instances':instances,'finite_interchange_value_checks':value_checks,
        'formal_results':['Native nonidentity comparison admitted with full source-port compatibility',
            'Operands, readers, incidence witnesses and native histories retained in Body',
            'Target-side continuation explicit and native attachment allowed after comparison',
            'Generic pointed loop transport without truncating arbitrary loop witnesses',
            'Derived pointed, port-preserving equivalence between the two construction routes',
            'Interchange itself compiled through the actual native comparison rule',
            'Both route derivations recovered from the interchange native premises',
            'The route Complete packages remain provably unequal',
            'A further actual native attachment follows the interchange result'],
        'scope':['Source modes are identity and the fixed seed symmetry',
                 'Target-side continuation is a declared policy, not forced by equivalence alone',
                 'Interchange is a retained comparison, not literal equality of construction histories',
                 'No global coherent interchange calculus, arbitrary policy discovery or physical traversal claim'],
        'source_hashes':hashes}
(BASE/'results/internal-comparison-interchange.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'pass','fresh_agda_exit':pos.returncode,
                  'negative_exits':[n['exit'] for n in negatives],
                  'interchange_instances':len(instances),'value_checks':value_checks}))
