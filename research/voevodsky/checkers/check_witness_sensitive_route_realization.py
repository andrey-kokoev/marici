"""Fresh headless Cubical closure and deliberate endpoint-erasure rejection."""
from pathlib import Path
from hashlib import sha256
import json, subprocess, re
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/witness-sensitive-route-realization.v1.json'
NOTE='research/voevodsky/witness-sensitive-route-realization-v1.md'
OUT='research/voevodsky/results/witness-sensitive-route-realization-v1.json'
POS='research/voevodsky/agda/WitnessedRouteContinuation.agda'
NEG='research/voevodsky/agda/WitnessedRouteBadErasure.agda'
COMPILER=Path.home()/'tools/agda-2.8.0.1/agda.exe'
LIBRARY=Path.home()/'tools/cubical-agda/cubical-0.9'
INCLUDES=[ROOT/'research/voevodsky/agda',ROOT/'research/nima/agda',
          ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension',LIBRARY]

def digest(path):return sha256(path.read_bytes()).hexdigest()
def inventory():
    out={}
    for directory in INCLUDES:
        prefix='cubical-library' if directory==LIBRARY else directory.relative_to(ROOT).as_posix()
        for p in sorted(directory.rglob('*.agda')):out[prefix+'/'+p.relative_to(directory).as_posix()]=digest(p)
    out['compiler']=digest(COMPILER)
    for p in [DEF,NOTE,Path(__file__).relative_to(ROOT).as_posix()]:out[p]=digest(ROOT/p)
    return out

def main():
    before=inventory();argv=[str(COMPILER),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for directory in INCLUDES:argv+=['-i',str(directory)]
    version=subprocess.check_output([str(COMPILER),'--version'],text=True).strip()
    results=[]
    for label,source in [('positive',POS),('negative',NEG)]:
        call=subprocess.run(argv+[str(ROOT/source)],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=300)
        log=call.stdout+'\n'+call.stderr
        path=f'research/voevodsky/results/witness-sensitive-route-{label}.log'
        (ROOT/path).write_text(log,encoding='utf-8')
        results.append(dict(label=label,source=source,exit_code=call.returncode,log=path,
                            log_sha256=digest(ROOT/path),warnings='warning:' in log.lower()))
        if label=='negative':negative_log=log
    after=inventory();stable=before==after
    negative_rejected=results[1]['exit_code']!=0 and bool(re.search(
        r'WitnessedRouteBadErasure\.agda:\d+\.\d+[^\n]*error: \[UnequalTerms\]', negative_log)) and (
        'false != Cubical.Data.Bool.Base.true' in negative_log and 'probe (triangle M.stay)' in negative_log)
    passed=stable and results[0]['exit_code']==0 and negative_rejected
    receipt=dict(schema='marici.witness-sensitive-route-realization-validation.v1',passed=passed,
                 compiler_version=version,compiler=str(COMPILER),library=str(LIBRARY),
                 ignore_interfaces=True,safe=True,inputs_stable=stable,
                 positive_and_negative=results,negative_erasure_rejected=negative_rejected,
                 verification_level='fresh safe Cubical Agda dependency closure',
                 source_inventory=after,source_inventory_note='All .agda sources in include directories plus contract/note/checker and compiler binary; inventory is not an exact import graph. Compiler built-in data is a separate trust boundary.',
                 proposed_outcomes={'generated-routes-have-witness-sensitive-completions':'++',
                                    'return-diagonal-suffices-for-all-witness-sensitive-continuations':'-+'},
                 independent_admission=False,physical_execution=False)
    (ROOT/OUT).write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='source_inventory'},indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
