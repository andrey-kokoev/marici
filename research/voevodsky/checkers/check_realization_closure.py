"""Fresh isolated-process closure for the eight realization iterations.
This verifies the declared finite model, not a physical particle assignment.
"""
from pathlib import Path
from hashlib import sha256
import subprocess
import sys
import json

BASE=Path(__file__).resolve().parents[1]
CHECKERS=BASE/'checkers'
RESULTS=BASE/'results'
RUNS=[
    ('check_potential_complex_pullback.py','proton_merkle_store.json','potential_complex_pullback.json'),
    ('check_pullback_retention.py','potential_complex_pullback_store.json','pullback_retention.json'),
    ('check_fold_bearing_vertex.py','potential_complex_pullback_store.json','fold_bearing_vertex.json'),
    ('check_fold_coefficient_attachment.py','fold_bearing_vertex_store.json','fold_coefficient_attachment.json'),
    ('check_projector_fold_sheets.py','fold_coefficient_attachment_store.json','projector_fold_sheets.json'),
    ('check_host_coefficient_pullback.py','projector_fold_sheets_store.json','host_coefficient_pullback.json'),
    ('check_open_mode_pullback.py','host_coefficient_pullback_store.json','open_mode_pullback.json'),
    ('check_inward_realization.py','open_mode_pullback_store.json','inward_realization.json'),
]

def hashes():
    return {p.name:sha256(p.read_bytes()).hexdigest() for p in sorted(CHECKERS.glob('*.py'))}


def main():
    before=hashes(); runs=[]; passed=True
    for checker,input_name,receipt_name in RUNS:
        completed=subprocess.run([sys.executable,str(CHECKERS/checker)],capture_output=True,text=True,timeout=180)
        if completed.returncode:
            raise RuntimeError(f'{checker} failed: {completed.stderr}\n{completed.stdout}')
        stdout=json.loads(completed.stdout)
        receipt=json.loads((RESULTS/receipt_name).read_text(encoding='utf-8'))
        ok=(stdout==receipt and receipt['passed'] and all(value is True for value in receipt['checks'].values())
            and receipt['checker_sha256']==before[checker]
            and receipt['source_file_sha256']==sha256((RESULTS/input_name).read_bytes()).hexdigest())
        passed &= ok
        runs.append({'checker':checker,'input':input_name,'receipt':receipt_name,'passed':ok,
                     'checks':len(receipt['checks']),'root':receipt['root'],
                     'input_sha256':receipt['source_file_sha256'],'receipt_sha256':sha256((RESULTS/receipt_name).read_bytes()).hexdigest()})
    after=hashes(); stable=before==after
    inputs_stable=all(r['input_sha256']==sha256((RESULTS/r['input']).read_bytes()).hexdigest() for r in runs)
    result={'schema':'marici.realization-closure.v1','passed':bool(passed and stable and inputs_stable),
            'isolated_process_runs':runs,'total_checks':sum(r['checks'] for r in runs),
            'checker_tree_unchanged_during_closure':stable,'all_input_bindings_still_current':inputs_stable,
            'local_python_source_hashes':after,'final_realization_root':runs[-1]['root'],
            'completed_scope':'Declared barycentric potential and inward realization; typed mode-bearing pullback; belt/seam/transport derivation. No physical electron/neutron identity or isotope mass count.'}
    target=RESULTS/'realization_closure.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':result['passed'],'fresh_processes':len(runs),'checks':result['total_checks'],
                      'source_tree_stable':stable,'input_bindings_current':inputs_stable,
                      'final_root':runs[-1]['root'],'receipt':str(target)},indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
