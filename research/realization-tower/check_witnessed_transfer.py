"""Audit the proposed transfer against the actual generating WG schedule.

Dependency scripts execute unchanged. Their JSON write_text receipts are
redirected beneath this test's directory, preserving owner results.
"""
from contextlib import redirect_stdout
from dataclasses import replace
import hashlib
import io
import json
from pathlib import Path
import runpy
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
HOME = Path(__file__).resolve().parent
OUT = HOME / 'results' / 'witnessed-transfer-v1'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    original_write = Path.write_text
    receipts = []

    def redirected_write(path, text, *args, **kwargs):
        path = path.resolve()
        rel = path.relative_to(ROOT)
        # Fail closed if an imported checker attempts an unrelated write.
        assert 'results' in rel.parts and path.suffix == '.json', str(path)
        target = OUT / 'dependency-receipts' / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        receipts.append(str(rel).replace('\\', '/'))
        return original_write(target, text, *args, **kwargs)

    source = ROOT / 'research/strominger/checkers/check_generating_horizontal_schedule.py'
    with patch.object(Path, 'write_text', redirected_write), redirect_stdout(io.StringIO()):
        schedule = runpy.run_path(str(source))

    adapter = schedule['a']
    left = schedule['examples']['inherited'][0]
    result = schedule['generate'](left)
    leaves = adapter['verify'](result.binding)
    first = schedule['promote'](leaves, 1, 'inherited')
    second = schedule['promote'](first, 2, 'inherited')
    assert second == schedule['recover'](result)
    assert len(leaves) == 137 and len(first) == len(second) == 32
    assert result.parents == (left,)
    assert schedule['leaves'](second) == leaves
    assert result.binding.generated_packet.parent.parent['primitive_rows'] == schedule['primitive_rows']

    # The constructed family is literally the next operation's member input,
    # not just a matching readout or an unrelated saved source.
    consumed_first = tuple(member for family in second for member in family.members)
    assert consumed_first == first  # inherited keys yield singleton second fibres
    for family in first:
        assert family.members
        assert len({member.target for member in family.members}) == 1
        assert family.mass == sum(member.mass for member in family.members)
    for family, member in zip(second, first):
        assert family.members == (member,)
        assert family.mass == member.mass and family.value == member.value
        assert family.label != member.label and family.source != member.source
        assert family.target != member.target

    # Recompute every typed comparison witness boundary and filler boundary.
    owner = adapter['owner']
    roots = result.binding.root_policy
    _, delta, _, _, _ = owner['build'](roots)
    for slot in result.binding.slots:
        boundary = owner['plus'](owner['word'](slot.left_leg, slot.right_leg),
                                 owner['minus'](owner['word'](result.binding.direct_name)))
        assert delta(slot.witness_first) == boundary
        assert delta(slot.witness_second) == boundary
        assert delta(slot.filler) == owner['plus'](slot.witness_second,
                                                 owner['minus'](slot.witness_first))

    rejected = []
    def reject(name, action):
        try:
            action()
        except (AssertionError, TypeError, AttributeError, KeyError, ValueError):
            rejected.append(name)
        else:
            raise AssertionError('Accepted hostile: ' + name)

    reject('erase_source_parent', lambda: schedule['verify_right'](replace(result, parents=())))
    reject('erase_construction_trace', lambda: schedule['verify_right'](replace(result, trace=())))
    # Select a nonzero filler so deletion is an actual change.
    slots = list(result.binding.slots)
    k = next(i for i, slot in enumerate(slots) if slot.filler)
    slots[k] = replace(slots[k], filler={})
    reject('erase_nonzero_filler', lambda: adapter['verify'](replace(result.binding, slots=tuple(slots))))
    # Preserve outer numerical values while deleting their retained inputs.
    corrupted = tuple(replace(family, members=()) for family in second)
    reject('same_outer_values_without_members',
           lambda: schedule['verify_right'](replace(result, view=corrupted)))
    reject('iterate_full_G_on_right_node', lambda: schedule['generate'](result))

    # Distinguish indexed re-presentation from actual operation outputs.
    reindexed = schedule['vertical'](left)
    assert schedule['recover'](reindexed) == schedule['recover'](left)
    assert len(schedule['recover'](left)) == 12
    assert len(result.binding.slots) == 137
    assert set(slot.branch for slot in result.binding.slots) == {'a', 's'}
    branch_counts = {b: sum(slot.branch == b for slot in result.binding.slots) for b in ('a', 's')}
    assert branch_counts == {'a': 121, 's': 16}

    # No arbitrary fifteen-token partition is fitted to this source.
    report = {
        'status': 'pass',
        'source_scope': 'Existing generating horizontal WG schedule, inherited-key fixture; exact executable algebra, not a fresh proof-assistant closure.',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'dependency_receipts_redirected': receipts,
        'profile': {'primitive_arrows': 12, 'generated_comparisons': branch_counts,
                    'first_families': len(first), 'second_families': len(second),
                    'witnessed_slots': len(result.binding.slots),
                    'first_family_sizes': sorted(len(f.members) for f in first)},
        'positive_results': [
            'Actual constructed first-stage families become actual second-stage inputs.',
            'Source, slot factors, two comparison witnesses, filler, memberships and trace remain recoverable/validated.',
            'Second-stage inherited families have fresh labels/endpoints even when their scalar values stay unchanged.',
            'Source indexing is lossless re-presentation, distinct from horizontal comparison generation.'
        ],
        'rejected_controls': rejected,
        'interpretation': 'Supported at this fixture: constructed witnessed output is reused as subsequent input. Not a single marked-apex transfer: the actual schedule generates comparisons and promotes whole families.',
        'not_established': [
            'A conserved fifteen-element input/output partition',
            'One transferred apex at each numerical rung',
            'A serial nine-state tower or full 12-to-4-to-12 cycle',
            'A bound join-factor adapter to the actual WG APIs',
            'Physical dynamics or calibration'
        ]
    }
    (OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'witnessed_slots': len(leaves),
                      'rejected_controls': len(rejected),
                      'receipt': str(OUT / 'verification.json')}))


if __name__ == '__main__':
    main()
