"""Compose the bounded profile evidence without selecting the universal scope."""
import copy
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
PACKAGE = 'research/conjecture_net/contracts/bounded-foundation-profile.v1.json'
NOTE = 'research/voevodsky/bounded-foundation-profile-v1.md'
OUT = 'research/voevodsky/results/bounded-foundation-profile-v1.json'

def load(p):
    return json.loads((ROOT/p).read_text(encoding='utf-8'))

def sha(p):
    return sha256((ROOT/p).read_bytes()).hexdigest()

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def validate(p):
    require(p['disposition'] == 'constructed_bounded_profile_not_parent_formulation', 'scope promotion')
    require(not any(p['boundaries'].values()), 'unsupported root claim')
    require(p['K']['literal_seeds'] == ['false-seed'] and p['K']['maximum_recursive_arity'] == 2, 'seed/arity drift')
    require(p['K']['rules'] == ['identity', 'Pi-Bool', 'E-Bool'], 'rule coverage changed')
    require(not p['K']['all_twelve_rule_schemas'] and not p['K']['semantic_seed_closure_equals_syntax'], 'semantic overclaim')
    require(p['P_mathematical']['physical_account'] is None and not p['resources']['hardware_or_physical_cost_bound'], 'physical promotion')
    require(p['resources']['guard'] == 'exists remaining: cost(t)+remaining=budget', 'guard drift')
    require({e['id'] for e in p['evidence']} == {'seed-arity','native-execution','budget'}, 'missing component')
    common = 'research/voevodsky/agda/RestrictedSeedArityProfile.agda'
    paths = []
    for e in p['evidence']:
        r = load(e['receipt']); require(r['passed'] and r['returncode'] == 0, 'failed component')
        require({'--safe','--ignore-interfaces'} <= set(r['command']), 'unsafe/stale compilation mode')
        require(e['source'] in r['command'], 'wrong compiled root')
        actual = r.get('theorems', r.get('claims', []))
        require(set(e['obligations']) <= set(actual), 'uncovered obligation')
        require(r['source_sha256'][common] == sha(common), 'incompatible source grammar')
        for src, expected in r['source_sha256'].items():
            require(sha(src) == expected, 'component drift: '+src)
        paths += [e['source'],e['checker'],e['receipt']]
    rival = load(p['retained_failed_candidate']['receipt'])
    require(rival['passed'] and rival['endpoint_assignments_rejected'] == 1024 and not rival['native_Resolve_semantics_realized'], 'rival scope lost')
    for src, expected in rival['source_sha256'].items():
        require(sha(src) == expected, 'rival evidence drift: '+src)
    return paths

def main():
    # Recompile the combined dependency closure via the budget root.
    run = subprocess.run([sys.executable,str(ROOT/'research/voevodsky/checkers/check_restricted_native_budget.py')],
                         cwd=ROOT,capture_output=True,text=True,timeout=300)
    require(run.returncode == 0, run.stdout+run.stderr)
    p = load(PACKAGE); paths = validate(p); controls = []
    for mode in ('universal', 'physical-budget', 'missing-component', 'wrong-guard'):
        bad = copy.deepcopy(p)
        if mode == 'universal': bad['boundaries']['universal_coverage_proved'] = True
        elif mode == 'physical-budget': bad['resources']['hardware_or_physical_cost_bound'] = True
        elif mode == 'missing-component': bad['evidence'].pop()
        else: bad['resources']['guard'] = 'endpoint equality'
        try: validate(bad)
        except ValueError: controls.append(mode)
        else: raise AssertionError('promotion accepted')
    paths += [PACKAGE,NOTE,p['retained_failed_candidate']['receipt'],Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.bounded-foundation-profile-validation.v1',passed=True,
                  components_validated=3, fresh_combined_safe_closure=True, corruption_controls=controls,
                  parent_formulation_discharged=False, physical_realization_admitted=False,
                  source_sha256={src:sha(src) for src in sorted(set(paths))})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__ == '__main__': main()
