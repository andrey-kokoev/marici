"""Source-API patch replay plus independent Python homogeneous-copy readout."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.voevodsky.ramsey_certificate import verify

ATTEMPT = 'research/voevodsky/contracts/ramsey-marked-patch-attempt.v1.json'
PROOF = 'research/voevodsky/ramsey-marked-dilation-patch-v1.md'
JS_CHECKER = 'research/voevodsky/checkers/check_ramsey_marked_patch.mjs'


def main():
    # Run under structured-command/SCC, like the existing source-bound checkers.
    run = subprocess.run(['node', str(ROOT / JS_CHECKER)], cwd=ROOT,
                         capture_output=True, text=True, check=True, timeout=90)
    summary = json.loads(run.stdout)
    assert summary['status'] == 'passed'
    geometry_path = ROOT / 'research/voevodsky/results/ramsey-marked-patch-geometry-v1.json'
    fixture_path = ROOT / 'research/voevodsky/results/ramsey-marked-patch-fixture-v1.json'
    geometry = json.loads(geometry_path.read_text(encoding='utf-8'))
    fixture = json.loads(fixture_path.read_text(encoding='utf-8'))
    attempt = json.loads((ROOT / ATTEMPT).read_text(encoding='utf-8'))
    assert attempt['id'] == 'marked-dilation-patch'
    assert attempt['scope_id'] == 'D3-source-geometry-marked-dilation-patch-v1'
    assert len(geometry['rows']) == 27 and len(geometry['composition']) == 9
    assert len(geometry['rejectedControls']) == 10
    assert verify(fixture['instance'], fixture['certificate']) is True
    assert fixture['patchHasOppositeColoredSubdivisionVertex'] is True
    for key in ('nativeReaderPacketsProduced', 'nativeParticleAdmissionProved',
                'uniformRamseyBoundProved', 'rootResolved'):
        assert geometry[key] is False
    sources = dict(geometry['sourceHashes'])
    for relative, digest in sources.items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT) and sha256(path.read_bytes()).hexdigest() == digest
    for relative in [ATTEMPT, PROOF, 'research/voevodsky/ramsey_certificate.py',
                     'research/voevodsky/checkers/check_ramsey_marked_patch.py']:
        sources[relative] = sha256((ROOT / relative).read_bytes()).hexdigest()
    result = {
        'schema': 'marici.ramsey-marked-patch.verification.v1', 'status': 'passed',
        'scope_id': attempt['scope_id'], 'outcome': '++',
        'verification_level': 'written geometric construction and exact-safe source-API controls; not native packet admission or kernel verified',
        'patch_cases': len(geometry['rows']), 'composition_cases': len(geometry['composition']),
        'negative_controls': len(geometry['rejectedControls']),
        'source_primitive_neighbor_replays': geometry['sourcePrimitiveNeighborReplays'],
        'independent_certificate_fixture_accepted': True,
        'homogeneous_marks_imply_homogeneous_patch': False,
        'native_reader_packets_produced': False, 'native_source_operations_fully_admitted': False,
        'uniform_Ramsey_bound_proved': False, 'root_resolved': False,
        'execution_envelope': attempt['execution_envelope'],
        'geometry_receipt': {'path': str(geometry_path.relative_to(ROOT)).replace('\\', '/'),
                             'sha256': sha256(geometry_path.read_bytes()).hexdigest()},
        'certificate_fixture': {'path': str(fixture_path.relative_to(ROOT)).replace('\\', '/'),
                                'sha256': sha256(fixture_path.read_bytes()).hexdigest()},
        'source_sha256': dict(sorted(sources.items())),
    }
    target = ROOT / 'research/voevodsky/results/ramsey-marked-patch-v1.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'geometry_receipt', 'certificate_fixture')}))


if __name__ == '__main__':
    main()
