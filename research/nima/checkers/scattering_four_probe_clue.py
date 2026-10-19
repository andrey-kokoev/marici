"""Four inherited source energies; preparation nuisance and local coupling jets.

No source/preparation fit. Rank statements are numerical and fixture-local.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration3.v1.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def projection(effects, tangents, rho, basis, threshold):
    nuisance = np.array([[np.trace(f @ b).real for b in basis] for f in effects])
    jet = np.array([[np.trace(df @ rho).real for df in pair] for pair in tangents])
    # One absolute rank threshold for SVD and construction of the nuisance image.
    u, singular, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(singular > threshold))
    left = np.eye(len(effects)) - u[:, :rank] @ u[:, :rank].T
    projected = left @ jet
    values = np.linalg.svd(projected, compute_uv=False)
    return {'nuisance': nuisance, 'jet': jet, 'projector': left, 'projected': projected,
            'contrast_basis': u[:, rank:].T, 'contrast_jet': u[:, rank:].T @ jet,
            'preparation_singular_values': singular, 'preparation_rank': rank,
            'projected_singular_values': values,
            'projected_rank': int(np.sum(values > threshold))}


def audit():
    contract = json.loads(CONTRACT.read_text())
    helper = load(ROOT / contract['source_checker'], 'four_probe_contact_source')
    effect_helper = load(ROOT / contract['effect_checker'], 'four_probe_effect_source')
    original = json.loads((ROOT / contract['source_contract']).read_text())
    model, saved, provenance, _, _ = helper.source(original)
    energies, tol = contract['energies_over_epsilon'], contract['tolerances']
    require(len(model.ground) == 4 and model.n == 20, 'source carrier/ground type changed')
    require(all(any(abs(row['incoming_kinetic_over_epsilon'] - e) < 1e-12 for row in saved['sample_scattering']) for e in energies), 'probe not in inherited source sample list')
    basis = effect_helper.hermitian_basis(4)
    rho = np.eye(4) / 4
    bg = model.B[np.ix_(model.ground, model.ground)]
    values, vectors = np.linalg.eigh(bg)
    dark = vectors[:, values < tol['rank']]
    require(dark.shape[1] == 2, 'dark-preparation type changed')
    dark_rho = dark @ dark.conj().T / dark.shape[1]
    packet = {'native_eigenframe': model.V, 'ground_indices': model.ground, 'rho_evaluation': rho,
              'dark_density': dark_rho, 'preparation_basis': basis}
    effects, tangents, flux, dark_flux, errors, fd_errors = [], [], [], [], [], []
    for energy in energies:
        sol = helper.stationary(model, energy, derivatives=True, **contract['base_parameters'])
        f = effect_helper.effect(model, sol)
        pair = [effect_helper.effect(model, sol, ds) for ds in sol['d_S_d_log_parameters']]
        effects.append(f)
        tangents.append(pair)
        flux.append(float(np.trace(f @ rho).real))
        dark_flux.append(float(np.trace(f @ dark_rho).real))
        require(np.linalg.eigvalsh(f).min() > -tol['equation_and_source'] and np.linalg.eigvalsh(f).max() < 1 + tol['equation_and_source'], 'invalid excitation effect')
        old = next(row for row in saved['sample_scattering'] if abs(row['incoming_kinetic_over_epsilon'] - energy) < 1e-12)
        errors.extend([abs(flux[-1] - old['outgoing_native_excited']), *sol['residuals'].values()])
        for name in ('S', 'state', 'open'):
            packet[f'{energy}/' + name] = sol[name]
        packet[f'{energy}/effect'] = f
        for name, df in zip(('log_nu', 'log_eta'), pair):
            packet[f'{energy}/effect_derivative/' + name] = df
        for index, name in enumerate(('nu', 'eta')):
            h = contract['derivative_control_log_step']
            plus, minus = dict(contract['base_parameters']), dict(contract['base_parameters'])
            plus[name] *= np.exp(h)
            minus[name] *= np.exp(-h)
            fp = effect_helper.effect(model, helper.stationary(model, energy, **plus))
            fm = effect_helper.effect(model, helper.stationary(model, energy, **minus))
            fd_errors.append(float(np.linalg.norm((fp - fm) / (2 * h) - pair[index])))
    measured = projection(effects, tangents, rho, basis, tol['rank'])
    contrast_operators = np.einsum('ae,eij->aij', measured['contrast_basis'], np.array(effects))
    contrast_operator_error = float(max(np.linalg.norm(f) for f in contrast_operators)) if len(contrast_operators) else 0.0
    require(contrast_operator_error < tol['equation_and_source'], 'nuisance contrast fails full operator relation')
    three = projection(effects[:3], tangents[:3], rho, basis, tol['rank'])
    indices = [energies.index(e) for e in contract['duplicate_probe_control']]
    duplicate = projection([effects[i] for i in indices], [tangents[i] for i in indices], rho, basis, tol['rank'])
    grid = np.arange(4)
    frame = np.exp(2j * np.pi * grid[:, None] * grid[None, :] / 4) / 2
    transformed = projection([frame.conj().T @ f @ frame for f in effects],
                             [[frame.conj().T @ df @ frame for df in pair] for pair in tangents],
                             frame.conj().T @ rho @ frame, basis, tol['rank'])
    frame_error = float(np.linalg.norm(measured['projected_singular_values'] - transformed['projected_singular_values']))
    require(max(errors) < tol['equation_and_source'], 'source or conservation mismatch')
    require(max(fd_errors) < tol['frame_and_derivative'], 'full effect derivative mismatch')
    require(frame_error < tol['frame_and_derivative'], 'passive-frame readout mismatch')
    require(three['projected_rank'] == 1 and duplicate['projected_rank'] == 1, 'duplicate data created a direction or prior rank not recovered')
    require(max(abs(np.array(dark_flux))) < tol['equation_and_source'], 'dark input falsely excites')
    for name in ('nuisance', 'jet', 'projector', 'projected', 'contrast_basis', 'contrast_jet'):
        packet[name] = measured[name]
    packet['contrast_operators'] = contrast_operators
    packet['frame_control'] = frame
    path = HOME / 'results/scattering-clues-iteration3-full-packet.npz'
    np.savez_compressed(path, **packet)
    survives = measured['preparation_rank'] == 2 and measured['projected_rank'] == 2 and measured['projected_singular_values'][-1] > tol['minimum_new_projected_singular_value']
    sources = [CONTRACT, Path(__file__), ROOT / contract['source_checker'], ROOT / contract['effect_checker'], ROOT / contract['source_contract'], ROOT / contract['source_note'], ROOT / contract['prior_result']]
    summary = lambda r: {'preparation_rank': r['preparation_rank'], 'projected_coupling_rank': r['projected_rank'],
                         'preparation_singular_values': r['preparation_singular_values'].tolist(),
                         'projected_coupling_singular_values': r['projected_singular_values'].tolist()}
    return {'schema': 'marici.scattering.four-probe-result.v1', 'status': 'pass', 'validation_only': True,
            'conjecture_disposition': 'survives_at_source_fixture' if survives else 'falsified_at_source_fixture',
            'energies_over_epsilon': energies, 'equal_mixture_flux': flux,
            'three_probes': summary(three), 'four_probes': summary(measured), 'duplicate_probe_control': summary(duplicate),
            'dark_preparation_flux': dark_flux, 'maximum_source_and_conservation_residual': max(errors),
            'maximum_full_effect_derivative_error': max(fd_errors), 'passive_frame_singular_value_error': frame_error,
            'coupling_jacobian': measured['jet'].tolist(), 'nuisance_projected_coupling_jacobian': measured['projected'].tolist(),
            'source_derived_contrast_basis': measured['contrast_basis'].tolist(),
            'contrast_coupling_jacobian': measured['contrast_jet'].tolist(),
            'full_effect_contrast_operator_residual': contrast_operator_error,
            'source_provenance': provenance,
            'full_packet': {'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path), 'array_count': len(packet)},
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in sources},
            'physical_scattering_explained': False, 'physical_preparation_supplied': False,
            'global_parameter_uniqueness': False, 'latest_strained_model_recomputed': False, 'root_outcome': None}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration3.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'conjecture_disposition', 'four_probes', 'duplicate_probe_control',
                     'maximum_full_effect_derivative_error', 'passive_frame_singular_value_error', 'root_outcome')}, indent=2))
