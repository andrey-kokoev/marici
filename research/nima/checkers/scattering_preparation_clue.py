"""Full ground-preparation effects in the archived local contact predecessor.

Finite rival density solves are deliberate identifiability falsifiers, not source
constructions or physical fits. All matrices use one archived native eigenframe.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration2.v1.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def hermitian_basis(n):
    basis = []
    for i in range(n):
        for j in range(i + 1, n):
            x = np.zeros((n, n), complex)
            x[i, j] = x[j, i] = 1 / np.sqrt(2)
            basis.append(x)
            x = np.zeros((n, n), complex)
            x[i, j], x[j, i] = -1j / np.sqrt(2), 1j / np.sqrt(2)
            basis.append(x)
    for j in range(1, n):
        x = np.zeros((n, n), complex)
        x[np.arange(j), np.arange(j)] = 1
        x[j, j] = -j
        basis.append(x / np.sqrt(j * (j + 1)))
    return np.array(basis)


def effect(model, solution, tangent=None):
    opened = solution['open']
    count = len(opened)
    cols = np.array([list(opened).index(i) for i in model.ground])
    excited = np.flatnonzero(model.el[opened] - model.el[0] > 1e-8)
    rows = np.r_[excited, excited + count]
    amplitudes = solution['S'][np.ix_(rows, cols)]
    if tangent is None:
        return amplitudes.conj().T @ amplitudes
    derivative = tangent[np.ix_(rows, cols)]
    return derivative.conj().T @ amplitudes + amplitudes.conj().T @ derivative


def audit():
    contract = json.loads(CONTRACT.read_text())
    path = ROOT / contract['source_checker']
    spec = importlib.util.spec_from_file_location('contact_clue_source', path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    source_contract = json.loads((ROOT / contract['source_contract']).read_text())
    model, _, provenance, _, _ = helper.source(source_contract)
    require(len(model.ground) == 4, 'ground preparation type changed')
    tol = contract['tolerances']
    energies = contract['kinetic_energies_over_epsilon']
    rho0 = np.eye(4) / 4
    basis = hermitian_basis(4)
    gram = np.einsum('aij,bji->ab', basis, basis).real
    require(np.linalg.norm(gram - np.eye(15)) < tol['algebra'], 'preparation basis not orthonormal')
    require(np.max(abs(np.trace(basis, axis1=1, axis2=2))) < tol['algebra'], 'basis changes trace')
    bg = model.B[np.ix_(model.ground, model.ground)]
    values, vectors = np.linalg.eigh(bg)
    dark = vectors[:, values < tol['numerical_rank']]
    bright = vectors[:, values > tol['numerical_rank']]
    require(bright.shape[1] == 2, 'source bright ground type changed')
    witness_path = HOME / 'contracts/scattering-clues-iteration2-preparation-witness.v1.json'
    witness = json.loads(witness_path.read_text())
    require(witness['energies_over_epsilon'] == energies and witness['parameters'] == contract['base_parameters'], 'witness/source interface mismatch')
    a, b = bright.T
    preparations = [a, b, (a + b) / np.sqrt(2), (a - b) / np.sqrt(2),
                    (a + 1j * b) / np.sqrt(2), (a - 1j * b) / np.sqrt(2)]
    pure_densities = [np.outer(v, v.conj()) for v in preparations]
    require(all(abs(np.trace(rho) - 1) < tol['algebra'] and np.linalg.eigvalsh(rho).min() > -tol['algebra'] for rho in pure_densities), 'invalid pure preparation witness')
    packet = {'preparation_basis': basis, 'rho0': rho0, 'ground_native_frame': model.V[:, model.ground], 'dark_frame': dark}
    effects, jacobian, source_errors, residuals = [], [], [], []
    for energy in energies:
        sol = helper.stationary(model, energy, derivatives=True, **contract['base_parameters'])
        f = effect(model, sol)
        effects.append(f)
        source_errors.append(abs(float(np.trace(f).real / 4) - sol['excited_flux']))
        jacobian.append([float(np.trace(effect(model, sol, df)).real / 4) for df in sol['d_S_d_log_parameters']])
        ev = np.linalg.eigvalsh(f)
        require(ev.min() > -tol['algebra'] and ev.max() < 1 + tol['algebra'], 'effect not between zero and identity')
        require(np.linalg.norm(f @ dark) < tol['algebra'], 'source dark input becomes excited')
        for name in ('S', 'state', 'open'):
            packet[f'{energy}/base/' + name] = sol[name]
        packet[f'{energy}/effect'] = f
        residuals.extend(sol['residuals'].values())
    require(max(source_errors) < tol['algebra'], 'Born effect disagrees with source flux')
    pure_curves = np.array([[np.trace(f @ rho).real for f in effects] for rho in pure_densities])
    require(np.min(pure_curves[:, 0]) > tol['algebra'], 'ratio witness has zero reference flux')
    pure_ratios = pure_curves / pure_curves[:, :1]
    witness_difference = float(np.max(np.linalg.norm(pure_ratios - pure_ratios[0], axis=1)))
    packet['source_pure_preparations'] = np.array(pure_densities)
    packet['source_pure_flux_curves'] = pure_curves
    normalized = [f / np.trace(f).real for f in effects]
    scalar_residual = max(float(np.linalg.norm(f - normalized[0])) for f in normalized)
    nuisance = np.array([[float(np.trace(f @ b).real) for b in basis] for f in effects])
    singular = np.linalg.svd(nuisance, compute_uv=False)
    rank = int(np.sum(singular > tol['numerical_rank']))
    projector = np.eye(len(energies)) - nuisance @ np.linalg.pinv(nuisance, rcond=tol['numerical_rank'])
    projected_jacobian = projector @ np.array(jacobian)
    projected_singular = np.linalg.svd(projected_jacobian, compute_uv=False)
    target = np.array([np.trace(f @ rho0).real for f in effects])
    finite = []
    for index, rival in enumerate(contract['finite_rivals']):
        changed = []
        for energy in energies:
            sol = helper.stationary(model, energy, **rival)
            f = effect(model, sol)
            changed.append(f)
            packet[f'{energy}/rival{index}/effect'] = f
            packet[f'{energy}/rival{index}/S'] = sol['S']
            packet[f'{energy}/rival{index}/state'] = sol['state']
            residuals.extend(sol['residuals'].values())
        matrix = np.array([[float(np.trace(f @ b).real) for b in basis] for f in changed])
        unadjusted = np.array([np.trace(f @ rho0).real for f in changed])
        coefficients = np.linalg.lstsq(matrix, target - unadjusted, rcond=tol['numerical_rank'])[0]
        rho = rho0 + np.einsum('a,aij->ij', coefficients, basis)
        matched = np.array([np.trace(f @ rho).real for f in changed])
        error = float(np.linalg.norm(matched - target))
        eig = np.linalg.eigvalsh(rho)
        is_counterexample = bool(error < tol['matching_flux'] and eig.min() > tol['positive_density_floor'])
        packet[f'rival{index}/density'] = rho
        finite.append({'parameters': rival, 'minimum_density_eigenvalue': float(eig.min()),
                       'trace_residual': abs(float(np.trace(rho).real) - 1),
                       'density_change_frobenius': float(np.linalg.norm(rho - rho0)),
                       'unadjusted_flux_change': float(np.linalg.norm(unadjusted - target)),
                       'matching_flux_residual': error, 'positive_shared_density_counterexample': is_counterexample,
                       'flux_after_preparation_change': matched.tolist()})
    require(max(residuals) < tol['algebra'], 'conservative boundary solve failed')
    npz = HOME / 'results/scattering-clues-iteration2-full-packet.npz'
    np.savez_compressed(npz, **packet)
    source_paths = [CONTRACT, witness_path, Path(__file__), path, ROOT / contract['source_contract']] + [ROOT / name for name in contract['source_notes']]
    return {'schema': 'marici.scattering.prior-clue-result.v1', 'status': 'pass', 'validation_only': True,
            'energies_over_epsilon': energies, 'source_provenance': provenance, 'dark_dimension': int(dark.shape[1]),
            'equal_mixture_flux': target.tolist(), 'normalized_effect_difference': scalar_residual,
            'source_pure_preparation_flux_curves': pure_curves.tolist(),
            'source_pure_preparation_normalized_curves': pure_ratios.tolist(),
            'maximum_pure_preparation_normalized_curve_difference': witness_difference,
            'scalar_preparation_conjecture': 'falsified' if scalar_residual > tol['algebra'] else 'survives_sampled_probes_only',
            'preparation_nuisance_singular_values': singular.tolist(), 'preparation_readout_rank': rank,
            'coupling_jacobian_after_preparation_projection': projected_jacobian.tolist(),
            'projected_coupling_singular_values': projected_singular.tolist(), 'finite_rivals': finite,
            'maximum_conservation_residual': max(residuals), 'maximum_source_effect_difference': max(source_errors),
            'full_packet': {'path': npz.relative_to(ROOT).as_posix(), 'sha256': sha(npz), 'array_count': len(packet)},
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in source_paths},
            'physical_preparation_authorized': False, 'physical_parameters_fitted': False,
            'latest_strained_model_recomputed': False, 'root_outcome': None}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration2.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'scalar_preparation_conjecture', 'normalized_effect_difference',
                     'preparation_readout_rank', 'preparation_nuisance_singular_values',
                     'projected_coupling_singular_values', 'finite_rivals', 'root_outcome')}, indent=2))
