"""Fresh formal closure of an explicit finite seed/arity profile."""
import json
import subprocess
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = 'research/voevodsky/agda/RestrictedSeedArityProfile.agda'
NOTE = 'research/voevodsky/restricted-seed-arity-profile-v1.md'
OUT = 'research/voevodsky/results/restricted-seed-arity-profile-v1.json'
BASE = ['agda', '--ignore-interfaces', '--safe', '--cubical', '--guardedness', '--transliterate',
        '-i', 'research/voevodsky/agda', '-i', 'research/nima/agda',
        '-i', 'C:/Users/andrey/tools/cubical-agda/cubical-0.9']

def run(command):
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=280)

def main():
    good = run(BASE + [SOURCE])
    if good.returncode:
        raise RuntimeError(good.stdout + good.stderr)
    controls = {
        'BadLiteralSeed': ('bad : Term\nbad = literal true\n', ['SeedName', 'true']),
        'BadSelectedOnlyCost': ('bad : cost selected-example ≡ 2\nbad = refl\n', ['[UnequalTerms]', 'refl'])}
    rejected = []
    with tempfile.TemporaryDirectory(prefix='seed-arity-') as tmp:
        for name, (body, expected) in controls.items():
            file = Path(tmp) / (name + '.agda')
            file.write_text('{-# OPTIONS --safe --cubical --guardedness #-}\nmodule '+name+' where\n'
                            'open import Cubical.Foundations.Prelude\n'
                            'open import Cubical.Data.Bool.Base using (true)\n'
                            'open import RestrictedSeedArityProfile\n'+body, encoding='utf-8')
            bad = run(BASE + ['-i', tmp, str(file)])
            message = bad.stdout + bad.stderr
            if bad.returncode == 0 or 'error:' not in message or not all(s in message for s in expected):
                raise RuntimeError('Wrong negative result: '+name+'\n'+message)
            rejected.append(dict(module=name, body=body, returncode=bad.returncode, diagnostic_tail=message[-1200:]))
    paths = [SOURCE, NOTE, 'research/nima/agda/WholePackageSigmaPi.agda',
             'research/nima/agda/WholePackageResolution.agda', Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.restricted-seed-arity-profile.v1', passed=True,
                  command=BASE+[SOURCE], returncode=good.returncode, negative_controls=rejected,
                  profile=dict(seed_names=['false-seed'], rules=['identity', 'Pi-Bool', 'E-Bool'],
                               maximum_arity=2, universe_level=0, code_and_complete_level=1),
                  claims=['typed compile into actual Resolve', 'syntactic source recovery', 'both E branches counted'],
                  semantic_closure_characterized=False, all_twelve_rules_covered=False,
                  universal_foundation_selected=False, physical_realization_admitted=False,
                  formulation_gate_discharged=False,
                  source_sha256={p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256', 'negative_controls', 'command')}, indent=2))

if __name__ == '__main__':
    main()
