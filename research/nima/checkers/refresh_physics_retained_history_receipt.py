"""Fresh compiler closure for central reuse; preserve the source owner's receipts."""
import hashlib
import json
import os
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
TOOLS=Path(os.environ['USERPROFILE'])/'tools/cubical-agda'
COMPILER=TOOLS/'agda-2.8.0/agda.exe'
LIBRARY=TOOLS/'cubical-0.9'
SOURCE=ROOT/'research/sontag/agda/RetainedHistoryTransport.agda'
RESULT=ROOT/'research/nima/results/physics-retained-history-agda-v1.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():
    dirs=[ROOT/'research/sontag/agda',ROOT/'research/nima/agda',ROOT/'research/voevodsky/agda',ROOT/'research/nima/adapters',LIBRARY]
    return {str(p):sha(p) for d in dirs for p in sorted(d.rglob('*.agda'))}

if __name__=='__main__':
    before=inventory();compiler_before=sha(COMPILER)
    args=[str(COMPILER),'--ignore-interfaces','--safe','--cubical','--guardedness','--transliterate']
    for d in ('research/sontag/agda','research/nima/agda','research/voevodsky/agda','research/nima/adapters/native-application','research/nima/adapters/application-extension'):
        args+=['-i',str(ROOT/d)]
    args+=['-i',str(LIBRARY),str(SOURCE)]
    run=subprocess.run(args,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=240)
    log=RESULT.with_suffix('.log');log.write_text(run.stdout+run.stderr,encoding='utf-8')
    after=inventory();stable=before==after and compiler_before==sha(COMPILER)
    out={'schema':'marici.nima.physics-retained-history-agda.v1','exit_code':run.returncode,
        'passed':run.returncode==0 and stable,'inputs_stable':stable,'ignore_interfaces':True,
        'compiler_sha256':sha(COMPILER),'source_sha256':sha(SOURCE),'source_inventory_sha256':after,
        'checker_sha256':sha(Path(__file__)),'args':args,'log':str(log)}
    RESULT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':out['passed'],'exit_code':run.returncode,'inputs_stable':stable,
        'inventory_count':len(after),'receipt':str(RESULT)},indent=2))
    if not out['passed']:print((run.stdout+run.stderr)[-6000:])
    raise SystemExit(0 if out['passed'] else 1)
