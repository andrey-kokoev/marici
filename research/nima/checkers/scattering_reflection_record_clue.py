"""Source reflection/transmission effects and relative-gain hostile.

Archived local predecessor only; never interprets a gain assumption as an
admitted physical detector or a fixture density as a physical beam.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration5.v1.json'


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


def read_packet(result_path):
    result = json.loads(result_path.read_text())
    require(result['root_outcome'] is None, 'input scope promotion')
    for name, digest in result['source_sha256'].items():
        require(sha(ROOT / name) == digest, 'input source drift: ' + name)
    path = ROOT / result['full_packet']['path']
    require(sha(path) == result['full_packet']['sha256'], 'input packet drift')
    with np.load(path, allow_pickle=False) as data:
        packet = {name: data[name].copy() for name in data.files}
    return result, packet, path


def direction_effect(model, solution, direction, excited_only=False, tangent=None):
    opened = solution['open']
    count = len(opened)
    cols = np.array([list(opened).index(i) for i in model.ground])
    rows = np.arange(count)
    if excited_only:
        rows = rows[model.el[opened] - model.el[0] > 1e-8]
    if direction == 'transmission':
        rows = rows + count
    amplitudes = solution['S'][np.ix_(rows, cols)]
    if tangent is None:
        return amplitudes.conj().T @ amplitudes
    delta = tangent[np.ix_(rows, cols)]
    return delta.conj().T @ amplitudes + amplitudes.conj().T @ delta


def audit():
    contract = json.loads(CONTRACT.read_text())
    tol = contract['tolerances']
    helper = load(ROOT / contract['source_checker'], 'reflection_contact_source')
    effect_helper = load(ROOT / contract['effect_checker'], 'reflection_effect_source')
    project_helper = load(ROOT / contract['projection_checker'], 'reflection_projection_source')
    prior, old, prior_packet_path = read_packet(ROOT / contract['four_probe_result'])
    witness, state_packet, witness_packet_path = read_packet(ROOT / contract['witness_result'])
    require(contract['energies_over_epsilon'] == prior['energies_over_epsilon'], 'energy interface changed')
    model, saved, provenance, _, _ = helper.source(json.loads((ROOT / contract['source_contract']).read_text()))
    rho = state_packet['witness_density']
    require(np.linalg.eigvalsh(rho).min() > 1e-8 and abs(np.trace(rho) - 1) < tol['source_and_operator'], 'witness not positive trace one')
    energies = contract['energies_over_epsilon']
    effects = [old[str(e) + '/effect'] for e in energies]
    tangents = [[old[str(e) + '/effect_derivative/' + p] for p in ('log_nu', 'log_eta')] for e in energies]
    basis = effect_helper.hermitian_basis(4)
    energy = contract['reflection_energy_over_epsilon']
    sol = helper.stationary(model, energy, derivatives=True, **contract['parameters'])
    require(max(sol['residuals'].values()) < tol['source_and_operator'], 'stationary conservation or boundary failure')
    r = direction_effect(model, sol, 'reflection')
    t = direction_effect(model, sol, 'transmission')
    rx = direction_effect(model, sol, 'reflection', excited_only=True)
    dr = [direction_effect(model, sol, 'reflection', tangent=d) for d in sol['d_S_d_log_parameters']]
    dt = [direction_effect(model, sol, 'transmission', tangent=d) for d in sol['d_S_d_log_parameters']]
    drx = [direction_effect(model, sol, 'reflection', excited_only=True, tangent=d) for d in sol['d_S_d_log_parameters']]
    reference = energies.index(energy)
    complement = float(np.linalg.norm(r + t - np.eye(4)))
    excitation_duplicate = float(np.linalg.norm(rx - effects[reference] / 2))
    duplicate_jet = max(float(np.linalg.norm(a - b / 2)) for a, b in zip(drx, tangents[reference]))
    require(max(complement, excitation_duplicate, duplicate_jet) < tol['source_and_operator'], 'direction/effect identity failed')
    require(max(np.linalg.norm(a + b) for a, b in zip(dr, dt)) < tol['source_and_operator'], 'direction derivative complement failed')
    for f in (r, t, rx, r - rx):
        ev = np.linalg.eigvalsh(f)
        require(ev.min() > -tol['source_and_operator'] and ev.max() < 1 + tol['source_and_operator'], 'invalid positive direction effect')
    old_row = next(row for row in saved['sample_scattering'] if abs(row['incoming_kinetic_over_epsilon'] - energy) < 1e-12)
    source_error = abs(float(np.trace(r).real / 4) - old_row['reflection'])
    require(source_error < tol['source_and_operator'], 'historical reflection not recovered')
    projected = lambda fs, ds: project_helper.projection(fs, ds, rho, basis, tol['rank'])
    # Readout relation from full source operators, not from fitting probabilities.
    feature = lambda f: np.r_[f.real.ravel(), f.imag.ravel()]
    operator_columns = np.column_stack([feature(f) for f in effects])
    reflection_coefficients = np.linalg.lstsq(operator_columns, feature(r), rcond=tol['rank'])[0]
    reflection_span_residual = float(np.linalg.norm(r - sum(c * f for c, f in zip(reflection_coefficients, effects))))
    original = projected(effects, tangents)
    reflected = projected(effects + [r], tangents + [dr])
    transmitted = projected(effects + [t], tangents + [dt])
    duplicated = projected(effects + [rx], tangents + [drx])
    require(original['projected_rank'] == 1 and duplicated['projected_rank'] == 1, 'baseline or duplicate rank mismatch')
    require(transmitted['projected_rank'] == reflected['projected_rank'], 'complement changes direction rank')
    gain_column = np.r_[np.zeros(len(energies)), float(np.trace(r @ rho).real)]
    gain_nuisance = np.column_stack((reflected['nuisance'], gain_column))
    u, values, _ = np.linalg.svd(gain_nuisance, full_matrices=False)
    gain_rank = int(np.sum(values > tol['rank']))
    gain_projected = (np.eye(len(gain_column)) - u[:, :gain_rank] @ u[:, :gain_rank].T) @ reflected['jet']
    gain_singular = np.linalg.svd(gain_projected, compute_uv=False)
    grid = np.arange(4)
    frame = np.exp(2j * np.pi * grid[:, None] * grid[None, :] / 4) / 2
    transformed = project_helper.projection([frame.conj().T @ f @ frame for f in effects + [r]],
        [[frame.conj().T @ d @ frame for d in pair] for pair in tangents + [dr]],
        frame.conj().T @ rho @ frame, basis, tol['rank'])
    frame_error = float(np.linalg.norm(transformed['projected_singular_values'] - reflected['projected_singular_values']))
    require(frame_error < tol['derivative_and_frame'], 'passive frame mismatch')
    fd_errors = []
    for index, name in enumerate(('nu', 'eta')):
        plus, minus = dict(contract['parameters']), dict(contract['parameters'])
        h = contract['derivative_step']
        plus[name] *= np.exp(h)
        minus[name] *= np.exp(-h)
        fp = direction_effect(model, helper.stationary(model, energy, **plus), 'reflection')
        fm = direction_effect(model, helper.stationary(model, energy, **minus), 'reflection')
        fd_errors.append(float(np.linalg.norm((fp - fm) / (2 * h) - dr[index])))
    require(max(fd_errors) < tol['derivative_and_frame'], 'full reflection derivative mismatch')
    survives = reflected['projected_rank'] == 2 and reflected['projected_singular_values'][-1] > tol['minimum_restored_singular_value']
    output_packet = {'witness_density': rho, 'reflection_effect': r, 'transmission_effect': t,
                     'reflected_excitation_effect': rx, 'elastic_reflection_effect': r - rx,
                     'reflection_effect_derivatives': np.array(dr), 'full_S': sol['S'],
                     'contact_state': sol['state'], 'open_modes': sol['open'],
                     'joint_nuisance': reflected['nuisance'], 'joint_coupling_jet': reflected['jet'],
                     'relative_gain_nuisance': gain_nuisance, 'relative_gain_projected_jet': gain_projected,
                     'reflection_operator_span_coefficients': reflection_coefficients}
    packet_path = HOME / 'results/scattering-clues-iteration5-full-packet.npz'
    np.savez_compressed(packet_path, **output_packet)
    summarize = lambda p: {'preparation_rank': p['preparation_rank'], 'projected_coupling_rank': p['projected_rank'],
                           'projected_singular_values': p['projected_singular_values'].tolist()}
    paths = [CONTRACT, Path(__file__), prior_packet_path, witness_packet_path] + [ROOT / contract[key] for key in
            ('source_contract', 'source_checker', 'effect_checker', 'projection_checker', 'four_probe_result', 'witness_result', 'source_note')]
    return {'schema': 'marici.scattering.direction-record-result.v1', 'status': 'pass', 'validation_only': True,
            'conjecture_disposition': 'survives_at_positive_witness_with_known_relative_gain' if survives else 'falsified_at_positive_witness',
            'excitation_only': summarize(original), 'plus_total_reflection': summarize(reflected),
            'plus_total_transmission': summarize(transmitted), 'plus_reflected_excitation': summarize(duplicated),
            'unknown_relative_reflection_gain': {'nuisance_rank': gain_rank, 'projected_coupling_rank': int(np.sum(gain_singular > tol['rank'])), 'projected_singular_values': gain_singular.tolist()},
            'witness_total_reflection': float(np.trace(r @ rho).real),
            'witness_elastic_reflection': float(np.trace((r - rx) @ rho).real),
            'witness_reflected_excitation': float(np.trace(rx @ rho).real),
            'complement_operator_residual': complement, 'duplicate_excitation_operator_residual': excitation_duplicate,
            'reflection_full_operator_span_residual': reflection_span_residual,
            'reflection_full_operator_span_coefficients': reflection_coefficients.tolist(),
            'duplicate_excitation_derivative_residual': duplicate_jet, 'historical_reflection_residual': source_error,
            'maximum_full_reflection_derivative_error': max(fd_errors), 'passive_frame_error': frame_error,
            'maximum_source_conservation_residual': max(sol['residuals'].values()),
            'source_provenance': provenance,
            'full_packet': {'path': packet_path.relative_to(ROOT).as_posix(), 'sha256': sha(packet_path), 'array_count': len(output_packet)},
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in paths},
            'physical_detector_constructed': False, 'physical_preparation_supplied': False, 'physical_scattering_explained': False,
            'global_parameter_uniqueness': False, 'latest_model_recomputed': False, 'root_outcome': None}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration5.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'conjecture_disposition', 'plus_total_reflection',
                     'plus_reflected_excitation', 'unknown_relative_reflection_gain', 'root_outcome')}, indent=2))
