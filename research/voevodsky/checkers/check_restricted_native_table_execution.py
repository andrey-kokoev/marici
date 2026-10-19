"""Fresh safe native execution agreement and wrong-output/source controls."""
import json
import subprocess
import tempfile
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
SOURCE = 'research/voevodsky/agda/RestrictedNativeTableExecution.agda'
NOTE = 'research/voevodsky/restricted-native-table-execution-v1.md'
OUT = 'research/voevodsky/results/restricted-native-table-execution-v1.json'
BASE = ['agda', '--ignore-interfaces', '--safe', '--cubical', '--guardedness', '--transliterate',
        '-i', 'research/voevodsky/agda', '-i', 'research/nima/agda',
        '-i', 'C:/Users/andrey/tools/cubical-agda/cubical-0.9']

def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=280)

def main():
    good = run(BASE+[SOURCE])
    if good.returncode:
        raise RuntimeError(good.stdout+good.stderr)
    controls = {
        'BadNativeSelectedIndex': 'bad : fst (N.value (native selected-example)) ≡ true\nbad = refl\n',
        'BadNativeSourceErasure': 'bad : fst (run-native selected-example) ≡ literal false-seed\nbad = refl\n'}
    rejected = []
    with tempfile.TemporaryDirectory(prefix='native-profile-') as tmp:
        for name, body in controls.items():
            p = Path(tmp)/(name+'.agda')
            p.write_text('{-# OPTIONS --safe --cubical --guardedness #-}\nmodule '+name+' where\n'
                         'open import Cubical.Foundations.Prelude\n'
                         'open import Cubical.Data.Bool.Base using (true)\n'
                         'open import RestrictedSeedArityProfile\n'
                         'open import RestrictedNativeTableExecution\n'+body, encoding='utf-8')
            bad = run(BASE+['-i',tmp,str(p)])
            message = bad.stdout+bad.stderr
            if bad.returncode == 0 or 'error: [UnequalTerms]' not in message or 'expression refl' not in message:
                raise RuntimeError('wrong rejection: '+name+'\n'+message)
            rejected.append(dict(module=name, body=body, returncode=bad.returncode, diagnostic_tail=message[-1400:]))
    paths = [SOURCE, NOTE, 'research/voevodsky/agda/RestrictedSeedArityProfile.agda',
             'research/nima/agda/NativeTableRules.agda', 'research/nima/agda/NativeTableResolution.agda',
             'research/nima/agda/IndexedConstructorTables.agda', 'research/nima/agda/IndexedResolutionTransport.agda',
             'research/nima/agda/WholePackageSigmaPi.agda', 'research/nima/agda/WholePackageResolution.agda',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.restricted-native-table-execution.v1', passed=True,
                  command=BASE+[SOURCE], returncode=good.returncode, negative_controls=rejected,
                  theorems=['agreement', 'native-history-endpoint', 'original-derivation-recovered', 'syntax-recovered'],
                  native_evaluator_uses_old_decoder=False, native_derivation_uses_existing_transfer=True,
                  all_twelve_rule_fragment=False, physical_realization_admitted=False,
                  runtime_cost_theorem=False, formulation_gate_discharged=False,
                  source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(passed=True, fresh_safe_closure=True, negative_controls=len(rejected),
                         formulation_gate_discharged=False),indent=2))

if __name__ == '__main__':
    main()
