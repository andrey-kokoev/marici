"""Audit generation and validity of rank-six Taylor remainder artifacts."""
import json
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).parents[1]
LOW, HIGH = D('.0025'), D('.0075')


def chart_path(low_count):
    center = (LOW,) * low_count + (HIGH,) * (6 - low_count)
    tag = '_'.join(str(x).replace('.', 'p') for x in center)
    return ROOT / 'results' / (
        'central-rank-six-hessian-taylor-majorant-center-' + tag +
        '-radius-0p0025-current-v3.json')


def classify(path, expected_degree, expected_radius, expected_center,
             expected_exact_degree=None, expected_tail_start=39):
    if not path.exists():
        return {'file': path.name, 'status': 'missing'}
    source = json.loads(path.read_text())
    reasons = []
    if source.get('rank') != 6:
        reasons.append('rank')
    if source.get('taylor_degree') != expected_degree:
        reasons.append('degree')
    if D(source.get('taylor_radius', '-1')) != expected_radius:
        reasons.append('radius')
    if tuple(D(x) for x in source.get('taylor_center', ())) != expected_center:
        reasons.append('center')
    if source.get('source_tail_coordinate_multiplicity') != 6:
        reasons.append('source-tail-multiplicity')
    if source.get('directed_scalar_arithmetic_version') != 2:
        reasons.append('directed-scalar-arithmetic')
    if source.get('source_remainder_binomial_version') != 1:
        reasons.append('closed-binomial-source-remainder')
    if source.get('taylor_product_kernel_version') != 2:
        reasons.append('degree-bucket-Taylor-product')
    if (D(source.get('source_coefficient_envelope', '-1')) != D('6.038308') or
            (expected_exact_degree is not None and
             source.get('source_exact_coefficient_degree') != expected_exact_degree) or
            source.get('source_tail_first_enveloped_degree') != expected_tail_start or
            source.get('source_tail_explicit_degree_cutoff') != 200 or
            not source.get('source_tail_geometric_ratio_below_one', False)):
        reasons.append('analytic-source-envelope')
    if (source.get('inverse_lower_bound_count') != 15 or
            D(source.get('minimum_inverse_lower_bound', '0')) <= 0 or
            not source.get('all_inverse_lower_bounds_positive', False)):
        reasons.append('rational-LDL-inverse-floors')
    if not source.get('interval_certified', False):
        reasons.append('interval-certification')
    return {
        'file': path.name,
        'status': 'corrected-certified' if not reasons else 'stale-or-invalid',
        'reasons': reasons,
    }


def main():
    charts = []
    for low_count in range(7):
        center = (LOW,) * low_count + (HIGH,) * (6 - low_count)
        row = classify(chart_path(low_count), 8, D('.0025'), center, 49, 50)
        row['low_coordinate_count'] = low_count
        charts.append(row)
    global_path = ROOT / 'results' / 'central-rank-six-hessian-taylor-majorant-radius-0p01.json'
    global_chart = classify(global_path, 7, D('.01'), (D('.01'),) * 6)
    corrected = sum(row['status'] == 'corrected-certified' for row in charts)
    result = {
        'binary_charts': charts,
        'corrected_certified_binary_chart_count': corrected,
        'all_seven_binary_charts_current': corrected == 7,
        'global_one_chart': global_chart,
        'artifact_generation_guard': (
            'rank == source_tail_coordinate_multiplicity == 6 and '
            'directed_scalar_arithmetic_version == 2 and '
            'source_remainder_binomial_version == 1 and '
            'taylor_product_kernel_version == 2 and source-envelope '
            'exact source degree 49, envelope degrees 50..200 with '
            'geometric ratio < 1, and 15 positive '
            'rational LDL inverse floors'),
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-taylor-artifact-audit.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
