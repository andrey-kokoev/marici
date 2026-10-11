"""Verify the fresh formal receipt and bounded history/readout controls.
The generic bridge and no-endpoint-clock theorem are in the Agda module,
not inferred from the finite word controls below.
"""
from itertools import product
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]

def main():
    receipt=json.loads((ROOT/'results/agda-RetainedSquareConeClock.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
    checked=[]
    for name in ('RetainedSquareConeClock.agda','RetainedSquareReversal.agda',
                 'ObserverCoherenceCube.agda','ThreeWitnessRetainedCone.agda',
                 'RetainedTetrahedralPackage.agda','MarkedTetrahedronCoherence.agda',
                 'MarkedTriangleCoherence.agda'):
        digest=hashlib.sha256((ROOT/'agda'/name).read_bytes()).hexdigest()
        assert receipt['owner_source_inventory_sha256'][name]==digest
        checked.append(name)
    assert receipt['source_sha256']==hashlib.sha256((ROOT/'agda/RetainedSquareConeClock.agda').read_bytes()).hexdigest()
    # Here a tag records which of the two forward schedules is listed first.
    # Both are preserved by the real formal Tick, not erased after comparison.
    histories=[tuple(h) for n in range(4) for h in product(('LR','RL'),repeat=n)]
    comparisons=0
    for h in histories:
        for k in histories:
            assert len(h+k)==len(h)+len(k)
            comparisons+=1
    assert ('LR',)!=('RL',) and len(('LR',))==len(('RL',))
    # Bool notEquiv square: both forward orders reach the same target, and
    # the reflected whole-square endpoint returns to the exact source.
    returns=0
    for u,v in product((False,True),repeat=2):
        left=(not u,v);right=(u,not v)
        target_left=(left[0],not left[1])
        target_right=(not right[0],right[1])
        assert target_left==target_right==(not u,not v)
        returned=(not target_left[0],not target_left[1])
        assert returned==(u,v)
        # Empty history and one completed square have identical endpoints;
        # their counts differ. This is a nonzero clock-descent residual.
        assert len(())-len(('LR',))==-1
        returns+=1
    result=dict(schema='marici.nima.retained-square-cone-clock.v1',status='pass',
        classification='formal record-level square-to-cone bridge with additive completion count',
        formal_receipt='research/nima/results/agda-RetainedSquareConeClock.json',
        current_direct_inputs_checked=checked,
        formal_results=['decode(encode(tick))=tick; encode is injective',
                        'both source schedules, their comparison, return section and attachment are retained',
                        'history encoding preserves concatenation and completion count',
                        'completion count is additive',
                        'no endpoint-only natural-number clock reads all these histories',
                        'different schedule records can have the same count'],
        finite_word_composition_controls=comparisons,bool_square_return_controls=returns,
        hostile_residuals={'empty_vs_one_return_count':-1,'equal_count_different_schedule_records':True},
        clock_convention='One admitted complete square-and-return record is counted as one tick. The two forward schedules are alternative descriptions, not asserted to be two sequential executions.',
        scope='The retained whole supports an intrinsic completion-count readout. Coning a record does not itself advance this clock.',
        not_shown=['an autonomous law generating successive returns',
                   'unique clock normalization, rate or preferred orientation',
                   'identification with the separate continuous rotor clock',
                   'a physical-time map for charge/mass/recoil dynamics'])
    (ROOT/'results/retained-square-cone-clock.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
