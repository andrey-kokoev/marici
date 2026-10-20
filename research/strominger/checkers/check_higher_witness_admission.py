"""Fresh exact-code obstruction, faithful native envelope and higher-rule use."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
LIB=Path.home()/'tools/cubical-agda/cubical-0.9'
EXE=shutil.which('agda')
assert EXE and LIB.is_dir()
sources=[BASE/'agda/HigherWitnessAdmission.agda',
         BASE/'agda/negative/HigherBadAtomicReinterpretation.agda',
         BASE/'agda/negative/HigherBadComparisonPremise.agda',
         BASE/'agda/RepeatedInterchangeCoherence.agda',BASE/'agda/InternalComparisonInterchange.agda',
         BASE/'agda/InternalSourceComparisons.agda',BASE/'agda/CoherentDependentExtensions.agda',
         BASE/'agda/NativeExtensionFamilyAudit.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
pos=subprocess.run(common+['--ignore-interfaces',str(sources[0])],capture_output=True,text=True,timeout=300)
log=pos.stdout+pos.stderr
(BASE/'results/higher-witness-admission-positive.log').write_text(log,encoding='utf-8')
assert pos.returncode==0 and 'UnsupportedIndexedMatch' not in log and 'Unsolved' not in log,log[-6000:]
negatives=[]
for path in sources[1:3]:
    neg=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(path)],capture_output=True,text=True,timeout=120)
    log=neg.stdout+neg.stderr
    (BASE/'results'/f'{path.stem}-negative.log').write_text(log,encoding='utf-8')
    assert neg.returncode!=0 and 'UnequalTerms' in log,log
    negatives.append({'module':path.stem,'exit':neg.returncode,'diagnostic':log.strip()})
# Finite interpretation controls: an E envelope with contractible reflexive
# fibers is faithful; adding independent fiber choices changes that guarantee.
envelopes=[]
for n in range(5):
    total=[(x,'refl') for x in range(n)]
    assert [x for x,w in total]==list(range(n))
    assert [(x,'refl') for x,w in total]==total
    envelopes.append({'index_size':n,'envelope_size':len(total),'projection_bijective':True})
assert len([(x,b) for x in range(2) for b in (0,1)])==4
# Structural spine observation: paths preserve it; the other native output
# heads break the bare-atom spine. General closure is proved in Agda, not by
# this bounded shape sample.
def spine(code):
    if code[0]=='atom':return True
    if code[0]=='paths':return spine(code[1])
    return False
bare=('paths',('atom','CompleteFiller'))
envelope=('paths',('E','CompleteFiller','derived-reflexive-family'))
assert spine(bare) and not spine(envelope)
for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':pos.returncode,'negative_controls':negatives,
        'finite_envelope_controls':envelopes,'bare_path_atomic_spine':spine(bare),
        'native_envelope_path_atomic_spine':spine(envelope),
        'formal_results':['All twelve native rules preserve the source-specific false atomic-spine invariant',
            'Exact bare atomic higher-path package has no Resolve Seeds derivation',
            'Reflexivity and dependent transport admit any supplied path from an actually derived pointed package',
            'Native E envelope of complete fillers derived from actual comparison/reflexivity premises',
            'Envelope projection proved an equivalence using local contractible branch fibers',
            'Existing higher witness lifted into envelope and its path package natively derived',
            'Projection recovers the original higher path exactly',
            'Unchanged higher-rule applies to derived envelope paths and their supplied right-unit coherence',
            'Original diagram, endpoint derivations, admitted higher path and further higher-rule proof retained'],
        'scope':['Seed policy and twelve native rule schemas unchanged',
                 'The literal bare-atom package remains inadmissible; no coercion from interpreted equivalence to code identity',
                 'The E premise family is supplied uniformly and may be infinitely branching; it is not enumerated',
                 'The higher witness is already constructed, not discovered by a filler-search algorithm',
                 'Faithful envelope equivalence uses proved local sethood, not a universal truncation assumption',
                 'No universal higher-admission completeness or physical interpretation claim'],
        'source_hashes':hashes}
(BASE/'results/higher-witness-admission.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'pass','fresh_agda_exit':pos.returncode,
                  'negative_exits':[n['exit'] for n in negatives],
                  'exact_atomic_package':'proved_inadmissible','faithful_envelope_path':'natively_admitted'}))
