"""Source-derived Bloch-ball determinant, not a fitted preparation law.

Numeric witness/bounds in the archived local predecessor only. A singular local
jet is not an exact finite parameter degeneracy or a physical prepared beam.
"""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration4.v1.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def determinant_polynomial(a):
    d0 = float(np.linalg.det(a[0]))
    linear = np.array([a[0, 0, 0] * x[1, 1] + x[0, 0] * a[0, 1, 1]
                       - a[0, 0, 1] * x[1, 0] - x[0, 1] * a[0, 1, 0] for x in a[1:]])
    q = np.diag([np.linalg.det(x) for x in a[1:]])
    for i in range(3):
        for j in range(i + 1, 3):
            q[i, j] = q[j, i] = (np.linalg.det(a[i + 1] + a[j + 1]) - q[i, i] - q[j, j]) / 2
    return d0, linear, q


def audit():
    contract = json.loads(CONTRACT.read_text())
    tol = contract['tolerances']
    prior_path = ROOT / contract['source_result']
    prior = json.loads(prior_path.read_text())
    require(prior['root_outcome'] is None and not prior['physical_scattering_explained'], 'prior scope promotion')
    for name, digest in prior['source_sha256'].items():
        require(sha(ROOT / name) == digest, 'prior source changed: ' + name)
    npz_path = ROOT / prior['full_packet']['path']
    require(sha(npz_path) == prior['full_packet']['sha256'], 'prior full packet changed')
    spec = importlib.util.spec_from_file_location('bright_robustness_source', ROOT / contract['source_checker'])
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    model, _, provenance, _, _ = helper.source(json.loads((ROOT / contract['source_contract']).read_text()))
    bg = model.B[np.ix_(model.ground, model.ground)]
    eigen, vectors = np.linalg.eigh(bg)
    bright, dark = vectors[:, eigen > tol['rank']], vectors[:, eigen < tol['rank']]
    require(bright.shape == (4, 2) and dark.shape == (4, 2), 'bright/dark source type changed')
    with np.load(npz_path, allow_pickle=False) as data:
        contrasts = data['contrast_basis'].copy()
        effects = np.array([data[str(e) + '/effect'] for e in prior['energies_over_epsilon']])
        derivatives = np.array([[data[str(e) + '/effect_derivative/' + p] for p in ('log_nu', 'log_eta')]
                                for e in prior['energies_over_epsilon']])
    operators = np.einsum('re,epij->rpij', contrasts, derivatives)
    reduced = np.einsum('ia,rpij,jb->rpab', bright.conj(), operators, bright)
    support_error = float(np.linalg.norm(operators - np.einsum('ia,rpab,jb->rpij', bright, reduced, bright.conj())))
    require(support_error < tol['source_and_operator'], 'derivative has hidden dark support')
    pauli = np.array([np.eye(2), [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)
    coefficients = np.array([np.einsum('rpij,ji->rp', reduced, s).real / 2 for s in pauli])
    d0, linear, q = determinant_polynomial(coefficients)
    evaluate = lambda b: d0 + linear @ b + b @ q @ b
    jacobian = lambda b: coefficients[0] + np.einsum('i,irp->rp', b, coefficients[1:])
    seeds = [np.zeros(3)] + [s * np.eye(3)[i] for i in range(3) for s in (-1, 1)]
    seeds += [np.array(v) / np.sqrt(3) for v in itertools.product((-1, 1), repeat=3)]
    _, axes = np.linalg.eigh(q)
    seeds += [s * axes[:, i] for i in range(3) for s in (-1, 1)]
    errors = [abs(evaluate(b) - np.linalg.det(jacobian(b))) for b in seeds]
    require(max(errors) < tol['polynomial'], 'determinant polynomial disagrees with operator jet')
    bound = float(abs(d0) - np.linalg.norm(linear) - np.linalg.norm(q, 2))
    # Secondary algebraic characterization of the already-derived polynomial.
    axis = -linear / np.linalg.norm(linear)
    axis_quadratic = float(axis @ q @ axis)
    axis_reduction_error = float(np.linalg.norm(q - axis_quadratic * np.outer(axis, axis)))
    univariate = axis_reduction_error < tol['polynomial']
    coordinate_roots = np.roots([axis_quadratic, -np.linalg.norm(linear), d0]) if univariate else []
    feasible_roots = [float(x.real) for x in coordinate_roots if abs(x.imag) < tol['polynomial'] and abs(x.real) <= 1]
    endpoint = next((b for b in seeds[1:] if evaluate(b) * d0 < 0), None)
    packet = {'bright_frame': bright, 'dark_frame': dark, 'contrast_basis': contrasts,
              'contrast_derivative_operators': operators, 'bright_derivative_operators': reduced,
              'affine_jacobian_coefficients': coefficients, 'determinant_Q': q,
              'determinant_linear': linear, 'test_bloch_vectors': np.array(seeds),
              'critical_moment_axis': axis,
              'ground_bright_projector': bright @ bright.conj().T,
              'ground_preparation_moment': bright @ sum(c * s for c, s in zip(axis, pauli[1:])) @ bright.conj().T}
    witness = None
    if endpoint is not None:
        fraction = brentq(lambda t: evaluate(t * endpoint), 0, 1, xtol=1e-14)
        b = fraction * endpoint
        rhob = sum(c * s for c, s in zip(np.r_[1, b], pauli)) / 2
        weight = contract['bright_weight_for_full_ground_witness']
        rho = weight * bright @ rhob @ bright.conj().T + (1 - weight) * dark @ dark.conj().T / 2
        density_eigen = np.linalg.eigvalsh(rho)
        require(density_eigen.min() > tol['positive_density'] and abs(np.trace(rho) - 1) < tol['polynomial'], 'root witness density not positive trace one')
        c = np.einsum('rpij,ji->rp', operators, rho).real
        sv = np.linalg.svd(c, compute_uv=False)
        flux = np.einsum('eij,ji->e', effects, rho).real
        require(np.max(flux) > tol['signal'] and sv[-1] < tol['rank'] and sv[0] > tol['signal'], 'root witness not bright rank one')
        u = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
        rotated = np.einsum('ia,rpij,jb->rpab', u.conj(), reduced, u)
        transported_rho = u.conj().T @ rhob @ u
        transported_c = weight * np.einsum('rpij,ji->rp', rotated, transported_rho).real
        frame_error = float(np.linalg.norm(transported_c - c))
        require(frame_error < tol['source_and_operator'], 'root witness fails passive bright-frame transport')
        witness = {'bloch_vector': b.tolist(), 'bloch_norm': float(np.linalg.norm(b)), 'bright_weight': weight,
                   'density_eigenvalues': density_eigen.tolist(), 'flux': flux.tolist(),
                   'contrast_jacobian': c.tolist(), 'singular_values': sv.tolist(),
                   'determinant_residual': abs(float(np.linalg.det(c))), 'passive_frame_error': frame_error}
        packet['witness_density'] = rho
        packet['witness_bloch_vector'] = b
        packet['witness_jacobian'] = c
        disposition = 'falsified_by_strictly_positive_non_dark_density'
    elif bound > tol['polynomial']:
        disposition = 'survives_with_conservative_bloch_ball_bound'
    else:
        disposition = 'unresolved_no_root_in_frozen_search_and_no_uniform_bound'
    require(np.linalg.norm(coefficients[0] / 2 - np.array(prior['contrast_coupling_jacobian'])) < tol['source_and_operator'], 'center does not recover prior fixture')
    packet_path = HOME / 'results/scattering-clues-iteration4-full-packet.npz'
    np.savez_compressed(packet_path, **packet)
    paths = [CONTRACT, Path(__file__), prior_path, npz_path, ROOT / contract['source_checker'], ROOT / contract['source_contract'], ROOT / contract['source_note']]
    return {'schema': 'marici.scattering.bright-preparation-result.v1', 'status': 'pass', 'validation_only': True,
            'conjecture_disposition': disposition, 'determinant_constant': d0, 'determinant_linear': linear.tolist(),
            'determinant_quadratic_matrix': q.tolist(), 'conservative_absolute_determinant_lower_bound': bound,
            'seed_determinant_minimum': float(min(evaluate(b) for b in seeds)),
            'seed_determinant_maximum': float(max(evaluate(b) for b in seeds)),
            'maximum_polynomial_error': max(errors), 'dark_support_residual': support_error,
            'secondary_polynomial_characterization': {'one_moment_reduction_supported': univariate,
                'axis': axis.tolist(), 'quadratic_coefficient': axis_quadratic,
                'linear_coefficient': -float(np.linalg.norm(linear)),
                'quadratic_axis_reduction_residual': axis_reduction_error,
                'critical_coordinates_inside_bloch_ball': feasible_roots},
            'witness': witness, 'source_provenance': provenance,
            'full_packet': {'path': packet_path.relative_to(ROOT).as_posix(), 'sha256': sha(packet_path), 'array_count': len(packet)},
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in paths},
            'physical_preparation_supplied': False, 'physical_scattering_explained': False,
            'global_nonlinear_degeneracy_proved': False, 'latest_model_recomputed': False, 'root_outcome': None}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration4.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'conjecture_disposition', 'conservative_absolute_determinant_lower_bound',
                     'seed_determinant_minimum', 'seed_determinant_maximum', 'witness', 'root_outcome')}, indent=2))
