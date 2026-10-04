"""Audit the explicitly extended native application runtime, not the old closure."""
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
    path = BASE / 'results/application-extension-kernel.json'
    k = json.loads(path.read_text(encoding='utf-8-sig'))
    require(k['schema'] == 'marici.application-extension.kernel-audit.v1', 'receipt schema')
    require(k['module'] == 'ApplicationExtensionRegression', 'wrong root')
    require(k['passed'] and k['fresh'] and k['inputs_stable'], 'fresh proof absent')
    require(k['positive_exit_code'] == 0 and '--ignore-interfaces' in k['args'], 'positive closure')
    require(k['negative_exit_code'] != 0 and k['negative_diagnostic'] == '[UnequalTerms]', 'wrong argument accepted')
    require(sha(k['compiler']) == k['compiler_sha256'].lower(), 'compiler drift')
    require(sha(BASE / 'checkers/check_application_extension_kernel.ps1') == k['checker_sha256'].lower(), 'driver drift')
    for source, digest in k['source_sha256'].items():
        require(sha(source) == digest.lower(), 'source drift: ' + source)
    required = list((BASE / 'adapters/application-extension').glob('*.agda'))
    required += [BASE / 'adapters/native-application/NativeApplicationGate.agda']
    for source in required:
        require(str(source) in k['source_sha256'], 'unrecorded source: ' + str(source))
    frozen = json.loads((BASE / 'adapters/finite-stone/core-freeze.json').read_text())
    for name, digest in frozen['sha256'].items():
        require(sha(BASE / 'agda' / name) == digest, 'frozen core changed: ' + name)
    result = {
        'schema': 'marici.application-extension.audit.v1',
        'status': 'explicit-dependent-application-extension-kernel-checked',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'kernel_sha256': sha(path), 'checker_sha256': sha(__file__),
        'frozen_core_unchanged': True, 'additional_rule_schemas': 1,
        'old_rules_embedded': 12, 'strict_extension_not_old_macro': True,
        'checked': ['Generic dependent application from two certified premises with both inputs retained.',
                    'Old obstruction fixture now has an actual extended derivation under its unchanged seed policy.',
                    'Beta coherencer is derived by the existing reflexivity rule, not admitted as a seed.',
                    'Application and coherencer are combined by the existing P-kind rule.',
                    'Full combined package and derivation reify one universe higher with exact recovery.',
                    'Dependent fixture changes codomain between Unit and Bool.',
                    'Replacing the argument certificate with a function certificate is rejected.'],
        'residuals': ['This is a separately named 13-schema runtime, not a theorem that the original 12 schemas already implement application.',
                      'Reification forms a higher-universe package; no next-level seed admission is inferred.',
                      'Full native Yoneda derivation, including inverse-law assembly and function extensionality, remains open.']}
    (BASE / 'results/application-extension-audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
