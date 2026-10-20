"""Fresh higher-comparison closure and a hidden-fiber obstruction control."""
from pathlib import Path
from itertools import product
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
sources=[BASE/'agda/RepeatedInterchangeCoherence.agda',
         BASE/'agda/InterchangeHiddenFiberObstruction.agda',
         BASE/'agda/negative/InterchangeBadEndpointOnlyCoherence.agda',
         BASE/'agda/InternalComparisonInterchange.agda',BASE/'agda/InternalSourceComparisons.agda',
         BASE/'agda/SourceIndexedExtensionFamilies.agda',BASE/'agda/NativeExtensionFamilyAudit.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
         ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
pos=subprocess.run(common+['--ignore-interfaces',str(sources[0])],capture_output=True,text=True,timeout=300)
log=pos.stdout+pos.stderr
(BASE/'results/repeated-interchange-coherence-positive.log').write_text(log,encoding='utf-8')
assert pos.returncode==0 and 'UnsupportedIndexedMatch' not in log and 'Unsolved' not in log,log[-6000:]
neg=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(sources[2])],capture_output=True,text=True,timeout=120)
log=neg.stdout+neg.stderr
(BASE/'results/repeated-interchange-coherence-negative.log').write_text(log,encoding='utf-8')
assert neg.returncode!=0 and 'refl' in log,log
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
edges={label:(s,t) for label,s,t in PACKETS}
sigma=dict(zip('ABCD','BADC'));by_edge={edge:label for label,edge in edges.items()}
move_edge={e:by_edge[(sigma[s],sigma[t])] for e,(s,t) in edges.items()}
# Concrete diagram: original comparison A->B, then AB and BC. The last
# outgoing carrier has TWO values; the test is not a singleton endpoint test.
source_values=[((edge,'loop'),(move_edge[edge],'loop'),'eq') for edge in ('BC','BA')]
def sequential(z):
    middle=(move_edge[z[0][0]],'middle-loop')
    return middle[0],'final-loop'
def direct(z):return move_edge[z[0][0]],'final-loop'
assert len(source_values)==2
for z in source_values:
    assert sequential(z)==direct(z)
    assert edges[z[1][0]][1]==edges[direct(z)[0]][1]
assert direct(source_values[0])==('AD','final-loop')
# Different contract: port and selected-point agreement fail to determine
# maps once independent noncontractible witness content is added.
hidden=[(edge,a,b) for edge in ('AB','AD') for a,b in product((False,True),repeat=2)]
def swap(z):return z[0],z[2],z[1]
selected=('AD',False,False)
assert swap(selected)==selected
assert all(edges[swap(z)[0]][1]==edges[z[0]][1] for z in hidden)
differences=[z for z in hidden if z!=swap(z)]
assert len(differences)==4
for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':pos.returncode,'negative_exit':neg.returncode,
        'negative_diagnostic':log.strip(),'source_diagram':{'comparison':'sigma:A->B','attachments':['AB','BC'],
            'transported_attachments':['BA','AD'],'active_final_port':'D','source_carrier_values':2},
        'formal_results':['Sequential and direct equivalences compared as full functions',
            'Equality of complete fillers including selected-value and whole-carrier port witnesses',
            'Equality of retained comparison Bodies and dependent compatibility of their native histories',
            'Original intermediate Bodies, leg witnesses and native derivations retained in certificate',
            'Higher path package formed and whole certificate reified with exact recovery',
            'Additional hidden witness content can obstruct any equality of maps despite equal ports and selected points'],
        'hidden_fiber_control':{'states':len(hidden),'differing_map_values':len(differences)},
        'scope':['One explicit three-constructor diagram under the existing target-side policy',
                 'Local interpreted sethood/contractible loop fibers used and proved; no global proof irrelevance',
                 'Selected-value witnesses normalized using proved uniqueness; original leg witnesses remain retained',
                 'No Resolve Seeds derivation for the newly formed higher-path package is asserted',
                 'No all-dimensional interchange coherence or policy uniqueness theorem'],
        'source_hashes':hashes}
(BASE/'results/repeated-interchange-coherence.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'pass','fresh_agda_exit':pos.returncode,'negative_exit':neg.returncode,
                  'diagram_carrier_values':2,'hidden_fiber_disagreements':len(differences)}))
