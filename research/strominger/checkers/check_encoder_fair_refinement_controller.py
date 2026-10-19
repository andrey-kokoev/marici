"""Bounded source-bound refinement controller over actual certified artifacts.

The baseline is a known finite witness sequence, NOT a complete word enumerator.
Tests policy isolation and exact admission; no universal compiler is claimed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
CORE=('research/strominger/results/neutron-seam-control-transport.json',
      'research/strominger/results/neutron-comparison-memory.json',
      'research/strominger/results/neutron-autonomous-rim-scattering.json')


def classify(certificate,epsilon,source_contract):
    if {p:certificate['source_hashes'].get(p) for p in CORE} != source_contract:
        return 'source_mismatch'
    upper=F(certificate['total_encoding_error_bound'])
    lower=F(certificate['exact_word_error_lower_bound'])
    assert 0<=lower<=upper
    if upper<epsilon:return 'accepted'
    if lower>epsilon:return 'refuted'
    return 'unresolved'


def run_controller(certificates,source_contract,epsilon,heuristic,ticks=6):
    # A policy supplies ONE precomputed proposal identifier, never arbitrary
    # code running inside the scheduler. Real external producers need separate
    # bounded execution/cancellation. Even slots cannot be captured by policy.
    baseline=['old','new_coarse','new_fine']
    cursor=0;trace=[]
    for tick in range(ticks):
        if tick%2==0:
            if cursor==len(baseline):continue
            channel='baseline';proposal=baseline[cursor];cursor+=1
        else:
            channel='heuristic';proposal=heuristic[tick//2 % len(heuristic)]
        if proposal not in certificates:
            trace.append({'tick':tick,'channel':channel,'proposal':proposal,'disposition':'unknown_proposal'})
            continue
        result=classify(certificates[proposal],epsilon,source_contract)
        trace.append({'tick':tick,'channel':channel,'proposal':proposal,'disposition':result})
        if result=='accepted':
            return {'accepted':proposal,'trace':trace,'baseline_steps':cursor}
    return {'accepted':None,'trace':trace,'baseline_steps':cursor}


def main():
    names={'old':'encoder-control-word-acceptance.json',
           'new_coarse':'encoder-control-word-refined-coarse-evaluator.json',
           'new_fine':'encoder-control-word-refined-accepted-1e-6.json'}
    raw={k:(BASE/'results'/v).read_bytes() for k,v in names.items()}
    certificates={k:json.loads(v) for k,v in raw.items()}
    for cert in certificates.values():
        assert cert['status']=='pass'
        for p,h in cert['source_hashes'].items():
            assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    contract={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in CORE}
    epsilon=F(1,1000000)
    # Actual accepted status is not reusable without rebasing its tolerance.
    old=certificates['old']
    assert old['word_accepted'] is True
    assert classify(old,epsilon,contract)=='refuted'
    assert classify(certificates['new_coarse'],epsilon,contract)=='unresolved'
    assert classify(certificates['new_fine'],epsilon,contract)=='accepted'
    # Source contract cannot be changed to make an old certificate reusable.
    wrong_contract=dict(contract);wrong_contract[CORE[0]]='0'*64
    assert classify(certificates['new_fine'],epsilon,wrong_contract)=='source_mismatch'
    # Resource comparison is typed by a shared request. The apparently cheaper
    # old implementation is ineligible, not an optimization at epsilon=1e-6.
    old_cost=old['primitive_operation_count_with_R_inverse_macro']
    new_cost=certificates['new_fine']['primitive_operation_count_with_R_inverse_macro']
    assert old_cost<new_cost
    assert classify(old,epsilon,contract)!='accepted'
    # Adversarial cooperative policies cannot capture reserved baseline slots.
    policies={'repeat_refuted':['old'],'repeat_unresolved':['new_coarse'],
              'invalid_ids':['does_not_exist'],'mixed':['old','new_coarse','does_not_exist'],
              'helpful':['new_fine']}
    runs={name:run_controller(certificates,contract,epsilon,proposals) for name,proposals in policies.items()}
    for name,run in runs.items():
        assert run['accepted']=='new_fine'
        assert run['trace'][-1]['tick']<=4
    # Exact finite prefixes of a deliberately unfair recurrence: always take
    # the heuristic's old proposal and never advance the baseline cursor.
    # The written induction extends this deterministic recurrence to all ticks.
    unfair_trace=[classify(old,epsilon,contract) for _ in range(32)]
    assert set(unfair_trace)=={'refuted'}
    assert not any(x=='accepted' for x in unfair_trace)
    # Tightening to 1e-8 exhausts these stored witnesses without success. This
    # finite controller must report incomplete, never infer task impossibility.
    tight=run_controller(certificates,contract,F(1,10**8),['old'])
    assert tight['accepted'] is None
    hashes={(BASE/'results'/names[k]).relative_to(ROOT).as_posix():hashlib.sha256(v).hexdigest() for k,v in raw.items()}
    own=Path(__file__).resolve();hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    result={'status':'pass','requested_epsilon':str(epsilon),
        'actual_old_accepted_flag_is_not_acceptance_at_new_request':True,
        'source_mismatch_rejected':True,
        'cheaper_but_inaccurate_old_word_rejected_as_optimization':True,
        'fair_runs':runs,'unfair_prefix_dispositions':unfair_trace,
        'tighter_request_finite_baseline':tight,
        'completion_scope':'All five tested cooperative proposal policies preserve acceptance by tick 4 for this fixed three-certificate baseline. For any baseline success at zero-based step k, reserved even slots supply it by tick 2k if each step returns.',
        'missing':'A complete word/precision baseline enumerator, bounded external producer execution, formal WG composition and all-tolerance termination implementation.',
        'source_hashes':hashes}
    (BASE/'results/encoder-fair-refinement-controller.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','cross_tolerance_reuse':'refuted','policy_cases':len(runs),
                      'latest_accepted_tick':max(r['trace'][-1]['tick'] for r in runs.values()),
                      'tight_request':'incomplete_finite_baseline'}))


if __name__=='__main__':main()
