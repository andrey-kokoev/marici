"""Fresh headless Agda closure, deliberate negative control, finite fiber audit."""
from pathlib import Path
from itertools import permutations
import hashlib
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
LIB=Path.home()/'tools/cubical-agda/cubical-0.9'
EXE=shutil.which('agda')
assert EXE and LIB.is_dir(), 'Agda and Cubical 0.9 are required'
files=[BASE/'agda/NativeExtensionFamilyAudit.agda',
       BASE/'agda/negative/NativeBadIncidenceAdmission.agda',
       ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
       ROOT/'research/nima/agda/WholePackageResolution.agda',
       ROOT/'research/nima/agda/BoundaryGeneratedQuestions.agda',
       ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
version=subprocess.run([EXE,'--version'],capture_output=True,text=True,check=True).stdout.strip()
positive=subprocess.run(common+['--ignore-interfaces',str(files[0])],capture_output=True,text=True,timeout=300)
log=positive.stdout+positive.stderr
(BASE/'results/native-extension-family-audit-positive.log').write_text(log,encoding='utf-8')
assert positive.returncode==0,log[-6000:]
negative=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(files[1])],capture_output=True,text=True,timeout=120)
negative_log=negative.stdout+negative.stderr
(BASE/'results/native-extension-family-audit-negative.log').write_text(negative_log,encoding='utf-8')
assert negative.returncode!=0, 'Invalid incidence witness was accepted'
assert 'sigma' in negative_log and 'tau' in negative_log and 'Edge' in negative_log,negative_log
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
names='ABCD';edges={(names.index(s),names.index(t)) for _,s,t in PACKETS}
pointed=[p for p in permutations(range(4)) if p[0]==1]
structured=[p for p in pointed if {(p[s],p[t]) for s,t in edges}==edges]
assert len(pointed)==6 and structured==[(1,0,3,2)]
assert (1,0,2,3) in pointed and (1,0,2,3) not in structured
for file,h in hashes.items():assert hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==h
result={'status':'pass','agda_version':version,'fresh_positive_exit':positive.returncode,
        'negative_exit':negative.returncode,'negative_diagnostic':negative_log.strip(),
        'fixed_A_to_B_native_equivalence_candidates':len(pointed),
        'fixed_A_to_B_incidence_preserving_candidates':len(structured),
        'source_policy':'All four graph-retaining vertex-pointed packages are supplied seeds',
        'formal_results':['Exact family of formed rules and premise derivations compiles to native Closure',
            'Complete application recovered after next-universe reification',
            'Actual native sigma comparison derived from declared seed family',
            'Actual native graph-breaking tau comparison derived from same seeds',
            'Both source codes retain graph; retention alone does not enforce incidence',
            'Sigma has forward and inverse incidence witnesses; tau cannot have one',
            'Sigma is not a pointed self-comparison at A; distinct pointed fillers retained'],
        'source_hashes':hashes,
        'scope':'Native twelve-schema signature; declared seeds and encoded graph provenance. No source-free rule/index selection, universal higher filling, physical process or generic canonical extension enumeration.'}
(BASE/'results/native-extension-family-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','agda_version','fresh_positive_exit','negative_exit',
    'fixed_A_to_B_native_equivalence_candidates','fixed_A_to_B_incidence_preserving_candidates')}))
