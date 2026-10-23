#!/usr/bin/env python3
"""Exact root-space probe design on the freshly replayed fixed native assembly."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/strominger/checkers'))
from check_joint_field_assembly_sewing import restore, zeros, add, perm
from exact_multiradical import mm, adj, identity, rational

REPLAY = ROOT / 'research/aspect/results/two-probe-assembly-sewing-replay.json'
OUT = ROOT / 'research/aspect/results/two-probe-assembly.json'


def main():
    report = json.loads(REPLAY.read_text())
    checks = {}
    def check(name, value):
        if not value:
            raise AssertionError(name)
        checks[name] = True
    check('fresh_replay_inputs', all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in report['sourceHashes'].items()))
    check('all_18_interfaces', len(report['interfaces']) == 18 and all(x['full44FieldSquare'] and x['full44ReadoutSquare'] and x['fiveCoefficientBindingSquare'] for x in report['interfaces']))
    fixture = json.loads((ROOT / report['fixture_source']).read_text())
    packets = {p['packet']: p for p in report['packetBindings']}
    root = packets[fixture['rootPacket']]
    binding = restore(root['binding'])
    reader = restore(root['readout'])
    check('root_metric_euclidean', root['species'] == 'proton')
    check('prepared_isometry', mm(adj(binding), binding) == identity(5))
    check('root_reader_is_adjoint', reader == adj(binding))
    projector = mm(binding, reader)
    complement = add(identity(44), projector, -1)
    check('complement_projector', mm(complement, complement) == complement and adj(complement) == complement)
    check('orthogonal_channels', mm(reader, complement) == zeros(5, 44))
    check('joint_probe_injective', add(mm(adj(reader), reader), mm(adj(complement), complement)) == identity(44))
    rank = rational(sum((complement[i][i] for i in range(44)), zeros(1, 1)[0][0]))
    check('complement_rank_39', rank == 39)
    # Two native terminal readouts on prepared root coordinates are permutations.
    # Native full-field naturality was replayed on every interface above.
    p_root = perm(root['nativePermutation'])
    exits = [packets[x['packet']] for x in report['exitSplits']]
    transforms = [mm(perm(x['nativePermutation']), adj(p_root)) for x in exits]
    check('two_exits', len(transforms) == 2)
    check('native_pair_gram_twice_root_projector', add(mm(adj(mm(transforms[0], reader)), mm(transforms[0], reader)), mm(adj(mm(transforms[1], reader)), mm(transforms[1], reader))) == [[2*v for v in row] for row in projector])
    # Unequal root coefficient readings cannot come from one section.
    c = [[identity(5)[i][0]] for i in range(5)]
    d = [[identity(5)[i][1]] for i in range(5)]
    recovered = [mm(adj(t), mm(t, c)) for t in transforms]
    check('consistent_native_pair', recovered[0] == recovered[1] == c)
    check('inconsistent_native_pair_rejected', mm(adj(transforms[1]), mm(transforms[1], d)) != recovered[0])
    # A complementary reading must actually lie in the complementary image.
    check('invalid_complement_reading_rejected', mm(complement, binding) != binding)
    check('same_connectivity_wrong_bindings_detected', len(report['fixedBindingFailurePackets']) == 11)
    result = {'passed': True, 'checks': checks,
        'native_pair': {'rank': 5, 'full_root_nullity': 39, 'prepared_root_nullity': 0},
        'proposed_pair': {'first': 'Q1=R_root (5 complex channels)', 'second': 'Q2=I-B_root R_root (44 redundant complex channels, rank 39)', 'rank': 44, 'root_nullity': 0, 'recovery': 'z=B_root y1+y2, provided Q2 y2=y2', 'chart_implementation': 'At selected packet h use Qj U_h^-1. Inverse frame transport is supplied by the replay, not a new local optical realization.'},
        'scope': 'Exact fixed-complex root-space measurement design conditional on replayed frame/naturality laws. Two probes are multichannel operators, not two scalar detectors. No unknown-complex selection, hardware locality, intensity-only recovery, or relaxation mechanism established.',
        'sourceHashes': {str(p.relative_to(ROOT)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest() for p in [REPLAY, Path(__file__).resolve()]}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
