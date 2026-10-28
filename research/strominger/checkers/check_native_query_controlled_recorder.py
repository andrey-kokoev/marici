"""Fresh safe Agda check of the native recorder; retain norm counterexample."""
from pathlib import Path
import hashlib, json, subprocess, sys, time
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
OUT=BASE/'results/native-query-controlled-recorder';OUT.mkdir(parents=True,exist_ok=True)
roots=[BASE/'agda',ROOT/'research/nima/agda',ROOT/'research/voevodsky/agda',
       ROOT/'research/voevodsky/observer-relative-computation/agda',ROOT/'research/grothendieck/agda',
       Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')]
def snapshot():
    files=set(f for r in roots for f in r.rglob('*.agda'))
    return {str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(files)}
args=['agda','--transliterate','--no-libraries','--safe','--cubical','--guardedness','--no-import-sorts']
for r in roots:args+=['-i',str(r)]
before=snapshot();start=time.time()
with (OUT/'positive.log').open('w',encoding='utf-8') as log:
    positive=subprocess.run(args+['--ignore-interfaces',str(BASE/'agda/NativeQueryControlledRecorder.agda')],
                            stdout=log,stderr=subprocess.STDOUT,timeout=600)
with (OUT/'negative.log').open('w',encoding='utf-8') as log:
    negative=subprocess.run(args+['-i',str(BASE/'agda/negative'),str(BASE/'agda/negative/NativeRecorderBadBlank.agda')],
                            stdout=log,stderr=subprocess.STDOUT,timeout=180)
after=snapshot()
neglog=(OUT/'negative.log').read_text(encoding='utf-8',errors='replace')
passed=positive.returncode==0 and negative.returncode!=0 and '[UnequalTerms]' in neglog and before==after
subprocess.run([sys.executable,str(BASE/'checkers/check_native_query_recording_orthogonality.py')],check=True)
report={'status':'pass' if passed else 'fail','positive_exit':positive.returncode,'negative_exit':negative.returncode,
        'ignore_interfaces':True,'stable_inputs':before==after,'conservative_source_files':len(before),
        'elapsed_seconds':time.time()-start,'source_sha256':before,
        'scope':'Native admitted reversible query recorder and native-table agreement; physical norm preservation remains an additional premise.',
        'warnings':'Inherited Cubical UnsupportedIndexedMatch diagnostics are retained in positive.log.'}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('source_sha256','scope','warnings')}))
if not passed:raise SystemExit(1)
