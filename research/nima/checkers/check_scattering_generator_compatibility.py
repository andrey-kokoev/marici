"""Exact necessary spectral gate; no source-owner main functions are run."""
import importlib.util
import json
from hashlib import sha256
from functools import reduce
from pathlib import Path
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
HOME = ROOT / 'research/nima'
CONTRACT = HOME / 'contracts/scattering-generator-compatibility.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    c = json.loads(CONTRACT.read_text())
    sys.path.insert(0, str(ROOT / 'research/voevodsky/checkers'))
    import check_native_spinor_pair_adapter as native
    from check_pentachoron_spin_interfaces import mm, adj, add, scale, A
    spec = importlib.util.spec_from_file_location('coefficient_source', ROOT / c['coefficient_constructor'])
    coeff = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(coeff)
    sources = set()
    def load_receipt(name, base):
        p = ROOT / name
        receipt = json.loads(p.read_text())
        require(receipt['verification_passed'], 'source receipt not passing: ' + name)
        sources.add(p)
        for relative, digest in receipt.get('source_hashes', {}).items():
            dependency = (base / relative).resolve()
            require(dependency.is_relative_to(ROOT) and sha(dependency) == digest, 'stale source pin: ' + str(dependency))
            sources.add(dependency)
        return receipt
    cycle = load_receipt(c['native_cycle_result'], ROOT)
    spin = load_receipt(c['native_spin_result'], ROOT)
    adapter = load_receipt(c['native_adapter_result'], ROOT / 'research/voevodsky')
    require('results/pentachoron_spin_interfaces.json' in adapter['source_hashes'], 'spin receipt lacks adapter integrity pin')
    classification = coeff.classify()
    selected = tuple(e for e in classification['edges'] if e != 'AB')
    d, gen = coeff.native_generator(classification, selected)
    require(gen.shape == (137, 137) and gen + gen.T == S.zeros(137), 'coefficient generator interface')
    z = -gen * gen
    require(gen * (z - 32*S.eye(137)) * (z - 128*S.eye(137)) == S.zeros(137), 'coefficient polynomial failed')
    low = z*(128*S.eye(137)-z)/3072
    high = z*(z-32*S.eye(137))/12288
    zero = S.eye(137)-low-high
    for p in (low, high, zero):
        require(p*p == p and p.T == p, 'coefficient spectral projector failed')
    dimensions = [int(S.trace(p)) for p in (low, high, zero)]
    require(dimensions == [36, 2, 99], 'coefficient bands changed')
    # Minimal polynomial divides x(x²+32)(x²+128). Multiplying the
    # number of response columns cannot create new spectral values.
    reports = []
    pair_counts = []
    for row in cycle['chirality_results']:
        chirality = row['chirality']
        extension = row['conditional_cycle_defect_extension']
        enc = [extension['attachment_encoding'], extension['opposite_lift_attachment_encoding']]
        ws = [native.matrix(item['cell_isometry']) for item in enc]
        q = add(*(mm(w, adj(w)) for w in ws))
        identity = native.eye(10)
        t = native.transport_matrix(native.matrix(row['spin_lift']))
        upper = next(r for r in spin['chirality_results'] if r['chirality'] == chirality)
        l = add(scale(native.decode(row['low_energy']), q),
                scale(native.decode(upper['higher_energy']), add(identity, scale(A(-1), q))))
        h = add(l, add(scale(A(2), identity), scale(A(-1), add(t, adj(t)))))
        require(h == adj(h), 'native energy not Hermitian')
        spectrum = [(native.decode(r['total_energy']), r['dimension']) for r in extension['complete_joint_spectrum'] if r['dimension'] > 0]
        require(sum(m for _, m in spectrum) == 10 and len({e.c for e, _ in spectrum}) == len(spectrum), 'native spectral labels')
        projectors = []
        for energy, multiplicity in spectrum:
            p = identity
            for other, _ in spectrum:
                if other != energy:
                    p = scale(A(1)/(energy-other), mm(p, add(h, scale(-other, identity))))
            require(p == adj(p) and mm(p,p) == p, 'native projector identity')
            require(mm(h,p) == scale(energy,p) and native.trace(p) == multiplicity, 'native eigenprojector/multiplicity')
            projectors.append(p)
        require(reduce(add, projectors) == identity, 'native spectral completeness')
        # Tensor sums have positive multiplicity products and projectors
        # P_i tensor conjugate(P_j). Completeness above proves the sum law.
        pair = {}
        for e, m in spectrum:
            for f, n in spectrum:
                key = (e+f).c
                pair[key] = pair.get(key, 0) + m*n
        require(sum(pair.values()) == 100, 'full pair dimension lost')
        count = len(pair)
        require(count > 5, 'prospective full-state spectral obstruction did not survive')
        pair_counts.append(count)
        options = [r for r in adapter['adapter_reports'] if r['chirality'] == chirality]
        require(len(options) == 2, 'missing selected doublet control')
        for option, w in zip(options, ws):
            e = native.decode(option['single_conditional_energy'])
            require(mm(h,w) == scale(e,w) and mm(adj(w),w) == native.eye(2), 'selected encounter control failed')
            require(native.decode(option['pair_conditional_core_energy']) == 2*e, 'pair energy changed')
        reports.append({'chirality': chirality, 'single_distinct_energy_count': len(spectrum),
                        'pair_distinct_energy_count': count,
                        'pair_spectrum': [{'energy': A(k).record(), 'complex_multiplicity': m} for k,m in pair.items()],
                        'native_spectral_projectors_verified': True,
                        'selected_doublet_compressions_verified': True})
    # Independent logical hostiles: a nonzero affine energy change preserves
    # distinctness; do not count repeated coordinates as extra frequencies.
    require(len({a for a in [0,1,-1,2,-2]*4}) == 5, 'multiplicity hostile')
    require(len({3*x-7 for x in range(9)}) == 9, 'affine-injection control')
    sources.update([CONTRACT, Path(__file__), ROOT / c['coefficient_constructor'], ROOT / c['native_adapter']])
    sources.update(ROOT / n for n in c['source_notes'])
    result = {'schema': 'marici.scattering.generator-compatibility-result.v1', 'status': 'pass',
              'conjecture_disposition': 'full_native_pair_injective_intertwiner_obstructed',
              'coefficient_annihilating_polynomial': 'x*(x^2+32)*(x^2+128)',
              'coefficient_squared_frequency_dimensions_per_response_column': dimensions,
              'coefficient_real_dimension_four_columns': 548,
              'native_pair_real_dimension': 200,
              'coefficient_maximum_distinct_complex_eigenvalues': 5,
              'native_reports': reports,
              'proof': 'If AB=BG and B is injective then p(A)=0 implies p(G)=0. G realifies -i*a*(H_pair-bI). Its spectrum contains -i*a*(e-b) for every pair energy e. A nonzero a preserves their distinctness for any b. The verified pair spectra have more than five distinct energies; p has degree five. Hence no such B exists, even across all four response columns.',
              'selected_encounter_status': 'not_excluded_by_this_test; four complex scalar-energy coordinates could fit a coefficient frequency band after a supplied rate choice; no source-selected embedding, energy-form or vertex map constructed',
              'scope': 'Time-independent real-linear injective amplitude maps, unchanged laws, one global nonzero rate and common energy offset. Not nonlinear/density-state/time-dependent/controlled maps or enlarged laws. Full native complement retained dynamically, not merely as static provenance.',
              'channel_map_constructed': False, 'physical_scattering_explained': False,
              'root_outcome': None, 'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in sorted(sources)}}
    output = HOME / 'results/scattering-generator-compatibility.json'
    output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','conjecture_disposition','coefficient_maximum_distinct_complex_eigenvalues','selected_encounter_status','root_outcome')}))
    print('native pair distinct energy counts:', pair_counts)


if __name__ == '__main__':
    main()
