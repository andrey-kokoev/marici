"""Audit the fresh Yoneda proof and independently test a noncommutative monoid."""
import hashlib
import json
from itertools import product
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def require(p, message):
    if not p:
        raise RuntimeError(message)

def finite_test():
    # One-object category with ALL four endofunctions of a two-element set.
    arrows = tuple(product(range(2), repeat=2))
    identity = arrows.index((0, 1))
    mul = lambda f, g: arrows.index(tuple(arrows[f][arrows[g][x]] for x in range(2)))
    natural = lambda alpha: all(mul(alpha[g], f) == alpha[mul(g, f)]
        for f, g in product(range(4), repeat=2))
    raw = tuple(product(range(4), repeat=4))
    naturals = tuple(a for a in raw if natural(a))
    require(len(naturals) == 4, 'expected four natural transformations')
    for a in naturals:
        recovered = a[identity]
        require(a == tuple(mul(recovered, g) for g in range(4)), 'reconstruction failed')
    for f in range(4):
        extension = tuple(mul(f, g) for g in range(4))
        require(natural(extension) and extension[identity] == f, 'extension failed')
    constant, raw_id = (identity,) * 4, tuple(range(4))
    require(constant[identity] == raw_id[identity] and constant != raw_id,
            'missing counterexample to unrestricted recovery')
    require(not natural(constant), 'constant raw map should fail naturality')
    wrong_variance = tuple(mul(g, 0) for g in range(4))
    require(not natural(wrong_variance), 'opposite variance must be detected')
    require(any(mul(f, g) != mul(g, f) for f, g in product(range(4), repeat=2)),
            'test category accidentally commutative')
    return {'arrows': 4, 'raw_transformations': 256, 'natural_transformations': 4,
            'controls': ['drop-naturality', 'wrong-composition-variance'],
            'category': 'one-object noncommutative endofunction monoid'}

def main():
    kernel_path = BASE / 'results/ordinary-yoneda-kernel.json'
    kernel = json.loads(kernel_path.read_text(encoding='utf-8-sig'))
    require(kernel['schema'] == 'marici.ordinary-yoneda.kernel-audit.v1', 'receipt schema')
    require(kernel['passed'] and kernel['fresh'] and kernel['inputs_stable'], 'fresh proof absent')
    require(kernel['module'] == 'YonedaRegression' and kernel['positive_exit_code'] == 0, 'wrong root')
    require('--ignore-interfaces' in kernel['args'], 'cached proof only')
    require(kernel['negative_exit_code'] != 0 and kernel['negative_diagnostic'] == '[UnequalTerms]', 'negative control failed')
    require(sha(kernel['compiler']) == kernel['compiler_sha256'].lower(), 'compiler changed')
    require(sha(BASE / 'checkers/check_ordinary_yoneda_kernel.ps1') == kernel['checker_sha256'].lower(), 'driver changed')
    for path, digest in kernel['source_sha256'].items():
        require(sha(path) == digest.lower(), 'source changed: ' + path)
    for path in (BASE / 'adapters/yoneda').glob('*.agda'):
        require(str(path) in kernel['source_sha256'], 'unrecorded source: ' + str(path))
    freeze = json.loads((BASE / 'adapters/finite-stone/core-freeze.json').read_text())
    for name, digest in freeze['sha256'].items():
        require(sha(BASE / 'agda' / name) == digest, 'frozen core changed: ' + name)
    result = {
        'schema': 'marici.ordinary-yoneda.audit.v1',
        'status': 'ordinary-yoneda-kernel-checked',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'theorem_scope': 'Universe-polymorphic categories with set-valued homs and set-valued presheaves; inverses not required.',
        'kernel_sha256': sha(kernel_path), 'checker_sha256': sha(__file__),
        'core_unchanged': True, 'finite_test': finite_test(),
        'residuals': ['No derivation of categorical composition and laws from a four-channel interface.',
                      'Native adapter is specialized to universe zero; general theorem is universe-polymorphic.',
                      'No automatic category discovery or reconstruction of arbitrary raw object labels.',
                      'Interrupted uniform finite Stone algorithm has not been verified or integrated.']}
    (BASE / 'results/ordinary-yoneda-audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
