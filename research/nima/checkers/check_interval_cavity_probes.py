"""Exact conditional three-probe interval identification; no acquired data."""
import itertools
import json
import runpy
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories, supports_component_23

SOURCES = [
    'research/nima/checkers/check_physics_geometric_candidate.py',
    'research/nima/nnmhv_coherence_paths.py',
    'research/nima/physics-observation-resource-interface-v1.md',
    'research/nima/interval-cavity-probe-protocol.md',
    'research/nima/checkers/check_interval_cavity_probes.py',
]


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def hashes():
    return {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}


def main():
    pins = hashes()
    g = runpy.run_path(str(ROOT / SOURCES[0]))
    records = {(h.inner_pair[1]-4, h.outer_pair[1]-4): h
               for h in compile_nnmhv_histories(8) if supports_component_23(h)}
    require(len(records) == 6, 'six source records')
    ports = (1, 4, 7)
    eta, low = F(9, 25), F(9, 25)

    def process(pair):
        i, j = pair
        v = g['eye']()
        for k in range(i-1, j):
            v = g['mm'](g['round_map'](k), v)
        return v

    def response(v, port, memory='R'):
        state = g['lift_column'](v, g['occupation']([port]))
        require(g['inner'](state, state) == 1, 'normalized preparation/evolution')
        require(all(sum(n) == 1 for n in state), 'one-photon domain')
        outcomes = {o: g['probability'](g['instrument'](port, o, [(memory, state)]))
                    for o in ('C', 'N')}
        require(sum(outcomes.values()) == 1, 'complete outcome normalization')
        occupation = sum(a*a*g['weight'](n)*n[port] for n, a in state.items())
        require(outcomes['C'] == (eta*occupation if memory == 'R' else 0), 'independent occupation route')
        return outcomes

    table, full = {}, []
    for pair in records:
        outcomes = [response(process(pair), port) for port in ports]
        rates = tuple(o['C'] for o in outcomes)
        i, j = pair
        expected = tuple(eta*(low if i-1 <= k <= j-1 else 1) for k in range(3))
        require(rates == expected, 'diagonal-signature/instrument square')
        table[pair] = rates
        full.append({'interval': list(pair), 'outcomes': [{o: str(p) for o, p in x.items()} for x in outcomes]})
    require(len(set(table.values())) == 6, 'joint faithfulness')

    def decode(rates):
        require(len(rates) == 3 and all(x in (eta*low, eta) for x in rates), 'response domain')
        selected = [k+1 for k, x in enumerate(rates) if x == eta*low]
        require(selected and selected == list(range(selected[0], selected[-1]+1)), 'interval mask')
        return records[(selected[0], selected[-1])]

    for pair, rates in table.items():
        require(decode(rates) == records[pair], 'full source-record recovery')

    collisions = []
    for size in range(3):
        for subset in itertools.combinations(range(3), size):
            seen = {}
            for pair, rates in table.items():
                projected = tuple(rates[k] for k in subset)
                if projected in seen:
                    collisions.append({'probes': list(subset), 'pair': [list(seen[projected]), list(pair)]})
                    break
                seen[projected] = pair
            else:
                raise AssertionError('proper probe subset unexpectedly faithful')
    require(len(collisions) == 7, 'all proper subsets tested')

    hostiles = []
    require(all(response(process(pair), port, 'D')['C'] == 0 for pair in records for port in ports), 'dead readiness hostile')
    hostiles.append('dead-readiness-collapses-all-signatures')
    require(all(c > 0 and c/c == 1 for rates in table.values() for c in rates), 'click-only conditioning')
    hostiles.append('click-only-selected-frequency-is-one')

    # Unknown *per-port* efficiencies can alias distinct interval masks.
    alias_rates, alias_efficiencies = [], []
    for pair in ((1, 2), (2, 3)):
        occupancies = tuple(c/eta for c in table[pair])
        efficiencies = tuple(eta*low/p for p in occupancies)
        require(all(0 < a <= 1 for a in efficiencies), 'physical efficiency range')
        alias_efficiencies.append([str(a) for a in efficiencies])
        alias_rates.append(tuple(a*p for a, p in zip(efficiencies, occupancies)))
    require(alias_rates[0] == alias_rates[1], 'unknown-efficiency alias')
    hostiles.append('independent-unknown-efficiencies-alias-distinct-intervals')

    # Counts identify only the promised canonical family, not arbitrary operators.
    phase = g['eye']()
    phase[1][1] = -1
    for pair in records:
        v = process(pair)
        rival = g['mm'](phase, v)
        require(v != rival, 'distinct phase rival')
        require(tuple(response(rival, port)['C'] for port in ports) == table[pair], 'intensity phase alias')
    hostiles.append('output-phase-rival-is-invisible')

    reference = tuple(response(g['eye'](), port)['C'] for port in ports)
    require(reference == (eta,)*3, 'actual bypass reference')
    for pair, rates in table.items():
        require(tuple(c/b for c, b in zip(rates, reference)) == tuple(c/eta for c in table[pair]), 'nominal calibrated ratio')
    for factors in ((F(1, 5), F(1, 3), F(4, 5)), (eta, eta, eta)):
        for rates in table.values():
            t = tuple(c/eta for c in rates)
            c = tuple(a*p for a, p in zip(factors, t))
            require(tuple(x/b for x, b in zip(c, factors)) == t, 'static-factor calibration')

    def ratio(c, b):
        require(b > 0, 'zero reference')
        return c/b

    def radius(a_min, eps):
        require(0 <= eps < a_min <= 1, 'uncertainty domain')
        return 2*eps/(a_min-eps)

    def certify(a_min, eps):
        r = radius(a_min, eps)
        require(r < (1-low)/2, 'uncertainty insufficient to certify separation')
        return r

    def rejects(name, action):
        try:
            action()
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('hostile accepted: ' + name)

    rejects('zero-reference', lambda: ratio(F(0), F(0)))
    rejects('noninterval-response', lambda: decode((eta*low, eta, eta*low)))
    rejects('empty-response-mask', lambda: decode((eta,)*3))
    a_min, eps = F(1, 5), F(1, 100)
    bound = certify(a_min, eps)
    require(bound == F(2, 19), 'ratio error bound')
    threshold = (1+low)/2
    corner_count = 0
    for a, t, dc, db in itertools.product((a_min, eta, F(4, 5)), (low, F(1)), (-eps, eps), (-eps, eps)):
        estimated = ratio(a*t+dc, a+db)
        require(abs(estimated-t) <= bound, 'ratio error corner')
        require((estimated < threshold) == (t == low), 'robust threshold corner')
        corner_count += 1
    # At epsilon=4/145 and a_min=1/5 the conservative radius is exactly 8/25.
    rejects('bound-at-half-gap-not-certified', lambda: certify(a_min, F(4, 145)))
    require(hashes() == pins, 'sources changed during test')
    result = {
        'schema': 'marici.nima.interval-cavity-probes.v1', 'passed': True,
        'verdict': 'conditional_jointly_faithful_probe_family',
        'physical_realization_admitted': False,
        'counts': {'intervals': 6, 'probe_distributions': 18, 'proper_subset_collisions': 7, 'ratio_error_corners': corner_count},
        'response_table': full, 'subset_collisions': collisions,
        'unknown_efficiency_alias': {'intervals': [[1, 2], [2, 3]], 'efficiencies': alias_efficiencies,
                                     'common_click_rates': [str(x) for x in alias_rates[0]]},
        'nominal_reference_click_rates': [str(x) for x in reference],
        'calibration': {'model': 'independently justified static shared per-port factors',
                        'a_min': str(a_min), 'rate_error_bound': str(eps), 'ratio_error_bound': str(bound),
                        'classification_threshold': str(threshold), 'measured_or_statistical_guarantee': False},
        'hostiles': hostiles, 'source_sha256': pins,
    }
    out = ROOT / 'research/nima/results/interval-cavity-probes.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('response_table', 'source_sha256')}, indent=2))


if __name__ == '__main__':
    main()
