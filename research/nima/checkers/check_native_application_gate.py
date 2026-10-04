"""Validate source-bound evidence for the smallest native application gate."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def main():
    path = BASE / 'results/native-application-kernel.json'
    k = json.loads(path.read_text(encoding='utf-8-sig'))
    require(k['schema'] == 'marici.native-application.kernel-audit.v1', 'receipt schema')
    require(k['module'] == 'NativeApplicationGate', 'wrong proof root')
    require(k['passed'] and k['fresh'] and k['inputs_stable'], 'fresh stable proof missing')
    require(k['positive_exit_code'] == 0 and '--ignore-interfaces' in k['args'], 'positive proof not fresh')
    require(k['negative_exit_code'] != 0 and k['negative_diagnostic'] == '[UnequalTerms]', 'wrong rejection')
    require(sha(k['compiler']) == k['compiler_sha256'].lower(), 'compiler drift')
    require(sha(BASE / 'checkers/check_native_application_kernel.ps1') == k['checker_sha256'].lower(), 'driver drift')
    for source, digest in k['source_sha256'].items():
        require(sha(source) == digest.lower(), 'source drift: ' + source)
    required = list((BASE / 'adapters/native-application').glob('*.agda'))
    required += [BASE / 'agda' / n for n in ('NativeTableResolution.agda', 'NativeTableRules.agda',
        'IndexedConstructorTables.agda', 'GeneratingGrammarMacros.agda')]
    for source in required:
        require(str(source) in k['source_sha256'], 'source absent: ' + str(source))
    frozen = json.loads((BASE / 'adapters/finite-stone/core-freeze.json').read_text())
    for name, digest in frozen['sha256'].items():
        require(sha(BASE / 'agda' / name) == digest, 'core changed: ' + name)
    result = {
        'schema': 'marici.native-application.audit.v1',
        'status': 'canonical-native-application-obstructed-certified-family-specialization-checked',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'kernel_sha256': sha(path), 'checker_sha256': sha(__file__), 'core_unchanged': True,
        'positive': ['Specialization of a constructed P-family recovers the actual native premise derivation.',
                     'Both function and argument are retained by an actual P-kind application.',
                     'External readout computes the correct application value.'],
        'obstruction': 'With only the maps-node constant function Unit→Bool and atomic Unit argument admitted, no native derivation yields the evaluated atomic Bool package, even after retaining both operands.',
        'proof_method': 'All twelve rule outputs have non-atomic principal code after stripping retain nodes. A principal-atomic endpoint must be admitted. Every admitted principal-atomic carrier here is propositional, whereas Bool is not.',
        'residuals': ['Not a theorem excluding application under every alternative encoding or observational equivalence.',
                      'Certified-family specialization assumes existing component derivations; it does not manufacture them from an opaque function seed.',
                      'Native Yoneda witness construction is not closed by this test; no core extension was made.']}
    (BASE / 'results/native-application-audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
