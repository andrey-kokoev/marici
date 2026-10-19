"""Fresh safe compilation and deliberately ill-typed continuation controls."""
import json
import subprocess
import tempfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = 'research/voevodsky/agda/FiniteDomainInterfaceAudit.agda'
OUT = 'research/voevodsky/results/finite-domain-interface-audit-v1.json'
BASE = ['agda', '--ignore-interfaces', '--safe', '--cubical', '--guardedness',
        '--transliterate', '-i', 'research/voevodsky/agda', '-i', 'research/nima/agda',
        '-i', 'research/nima/adapters/yoneda', '-i',
        'C:/Users/andrey/tools/cubical-agda/cubical-0.9']

def run(args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=280)

def main():
    good = run(BASE + [SOURCE])
    if good.returncode:
        raise RuntimeError(good.stdout + good.stderr)
    controls = {
        'BadRepeatedCompute': '''bad : B.H.at 2 (inl false) ≡ inr (false , false)
bad = refl
''',
        'BadRequestRelabel': '''bad : true ≡ false
bad = refl
''',
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix='finite-domain-audit-') as tmp:
        for name, body in controls.items():
            p = Path(tmp) / (name + '.agda')
            p.write_text('{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ' + name + ' where\n'
                + 'open import Cubical.Foundations.Prelude\n'
                + 'open import Cubical.Data.Sum.Base using (inl; inr)\n'
                + 'open import Cubical.Data.Bool.Base using (false; true)\n'
                + 'open import FiniteDomainInterfaceAudit\n' + body, encoding='utf-8')
            bad = run(BASE + ['-i', tmp, str(p)])
            message = bad.stdout + bad.stderr
            if bad.returncode == 0 or not all(fragment in message for fragment in (
                    name + '.agda:8.7-11: error: [UnequalTerms]',
                    'true != false of type Cubical.Data.Bool.Base.Bool',
                    'when checking that the expression refl has type')):
                raise RuntimeError('Missing expected type mismatch: ' + name + '\n' + message)
            rejected.append({'module': name, 'body': body, 'returncode': bad.returncode,
                             'diagnostic_tail': message[-1500:]})
    paths = [SOURCE, 'research/voevodsky/checkers/check_finite_domain_interface_audit.py',
             'research/voevodsky/finite-domain-interface-audit-v1.md',
             'research/conjecture_net/contracts/stagewise-mathematical-interface.v1.json',
             'research/nima/agda/DomainWitnessCompiler.agda',
             'research/nima/agda/TypedGeneratorLayers.agda',
             'research/nima/adapters/yoneda/OrdinaryYoneda.agda']
    result = {'schema': 'marici.finite-domain-interface-audit.v1', 'passed': True,
              'command': BASE + [SOURCE], 'returncode': good.returncode,
              'positive_diagnostic_tail': (good.stdout + good.stderr)[-1500:],
              'negative_controls': rejected,
              'theorems': ['response-stationary', 'request-endpoint', 'retained-length',
                           'evaluated-then-idle', 'two-edges-retained',
                           'boolean-twice-is-response-true', 'no-output-as-admitted-request',
                           'supplied-law-recovered', 'same-operation-response'],
              'native_category_law_generation': False,
              'multi_step_native_category_binding': False,
              'universal_realization': False,
              'source_sha256': {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}}
    (ROOT / OUT).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'passed': True, 'safe_compile': True, 'negative_controls': len(rejected),
                      'receipt': OUT}, indent=2))

if __name__ == '__main__':
    main()
