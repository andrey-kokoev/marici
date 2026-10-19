"""Safe cost/guard proof closure for the declared native constructor model."""
import json
import tempfile
from hashlib import sha256
from pathlib import Path
from check_restricted_native_table_execution import BASE, ROOT, run

SOURCE = 'research/voevodsky/agda/RestrictedNativeBudget.agda'
NOTE = 'research/voevodsky/restricted-native-budget-v1.md'
OUT = 'research/voevodsky/results/restricted-native-budget-v1.json'

def main():
    good = run(BASE+[SOURCE])
    if good.returncode:
        raise RuntimeError(good.stdout+good.stderr)
    controls = {
        'BadUnderfundedNative': 'bad : BudgetRun selected-example 3\nbad = funded selected-example 0\n',
        'BadFreeIdentity': 'bad : Exec (identity (literal false-seed)) 1 (native (identity (literal false-seed)))\nbad = identity-step literal-step\n'}
    rejected = []
    with tempfile.TemporaryDirectory(prefix='native-budget-') as tmp:
        for name, body in controls.items():
            file = Path(tmp)/(name+'.agda')
            file.write_text('{-# OPTIONS --safe --cubical --guardedness #-}\nmodule '+name+' where\n'
                            'open import RestrictedSeedArityProfile\n'
                            'open import RestrictedNativeTableExecution\n'
                            'open import RestrictedNativeBudget\n'+body, encoding='utf-8')
            bad = run(BASE+['-i', tmp, str(file)])
            message = bad.stdout+bad.stderr
            if bad.returncode == 0 or 'error: [UnequalTerms]' not in message or name+'.agda:' not in message:
                raise RuntimeError('wrong control failure: '+name+'\n'+message)
            rejected.append(dict(module=name, body=body, returncode=bad.returncode, diagnostic_tail=message[-1200:]))
    paths = [SOURCE, NOTE, 'research/voevodsky/agda/RestrictedSeedArityProfile.agda',
             'research/voevodsky/agda/RestrictedNativeTableExecution.agda',
             'research/voevodsky/checkers/check_restricted_native_table_execution.py',
             'research/nima/agda/NativeTableRules.agda',
             'research/nima/agda/NativeTableResolution.agda',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.restricted-native-budget.v1', passed=True, command=BASE+[SOURCE],
                  returncode=good.returncode, negative_controls=rejected,
                  theorems=['execute', 'cost-sound', 'output-sound', 'guard-from-run', 'run-from-guard',
                            'no-underfunded-selected', 'syntax-budget-recovered'],
                  cost_model='one abstract unit per source constructor, both binary premises charged',
                  machine_kind='costed big-step evaluation relation',
                  hardware_runtime_bound=False, physical_budget_calibrated=False,
                  small_step_scheduler_supplied=False, formulation_gate_discharged=False,
                  source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(passed=True, fresh_safe_closure=True, negative_controls=len(rejected),
                         abstract_budget_guard_proved=True, physical_budget_calibrated=False),indent=2))

if __name__ == '__main__':
    main()
