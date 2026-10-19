"""Declared coherent-port readout, not an admitted physical interferometer.

Prior optical packets supply calibration distinctions, never a carrier map.
"""
import json
from pathlib import Path
import numpy as np
from scattering_reflection_record_clue import load, read_packet, require, sha

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration6.v1.json'


def ports(model, sol, tangent=None):
    opened = sol['open']
    n = len(opened)
    cols = np.array([list(opened).index(i) for i in model.ground])
    matrix = sol['S'] if tangent is None else tangent
    return matrix[:n, cols], matrix[n:, cols]


def coherent_effect(r, t, phase, dr=None, dt=None):
    a = (r + np.exp(1j * phase) * t) / np.sqrt(2)
    if dr is None:
        return a.conj().T @ a
    da = (dr + np.exp(1j * phase) * dt) / np.sqrt(2)
    return da.conj().T @ a + a.conj().T @ da


def audit():
    contract = json.loads(CONTRACT.read_text())
    tol = contract['tolerances']
    helper = load(ROOT / contract['source_checker'], 'coherent_contact_source')
    effect_helper = load(ROOT / contract['effect_checker'], 'coherent_effect_source')
    project_helper = load(ROOT / contract['projection_checker'], 'coherent_projection_source')
    prior, old, prior_packet_path = read_packet(ROOT / contract['four_probe_result'])
    direction, saved, direction_packet_path = read_packet(ROOT / contract['direction_result'])
    rho = saved['witness_density']
    require(np.linalg.eigvalsh(rho).min() > 1e-8, 'not the positive source witness')
    model, _, provenance, _, _ = helper.source(json.loads((ROOT / contract['source_contract']).read_text()))
    effects = [old[str(e) + '/effect'] for e in prior['energies_over_epsilon']]
    tangents = [[old[str(e) + '/effect_derivative/' + p] for p in ('log_nu', 'log_eta')] for e in prior['energies_over_epsilon']]
    basis = effect_helper.hermitian_basis(4)
    energy, phase, visibility = (contract[k] for k in ('readout_energy_over_epsilon', 'quadrature_phase', 'known_visibility_fixture'))
    sol = helper.stationary(model, energy, derivatives=True, **contract['source_parameters'])
    source_error = float(np.linalg.norm(sol['S'] - saved['full_S']))
    require(max(source_error, *sol['residuals'].values()) < tol['source_and_effect'], 'source solve changed')
    r, t = ports(model, sol)
    h = coherent_effect(r, t, phase)
    minus = coherent_effect(r, t, phase + np.pi)
    h0 = coherent_effect(r, t, contract['phase_null'])
    dh = [coherent_effect(r, t, phase, *ports(model, sol, ds)) for ds in sol['d_S_d_log_parameters']]
    dh0 = [coherent_effect(r, t, contract['phase_null'], *ports(model, sol, ds)) for ds in sol['d_S_d_log_parameters']]
    half = np.eye(4) / 2
    hv = half + visibility * (h - half)
    hv_minus = np.eye(4) - hv
    dephased = half + contract['dephasing_null_visibility'] * (h - half)
    complement = float(np.linalg.norm(h + minus - np.eye(4)))
    null_error = max(float(np.linalg.norm(h0 - half)), float(np.linalg.norm(dephased - half)), *[float(np.linalg.norm(d)) for d in dh0])
    require(max(complement, null_error) < tol['source_and_effect'], 'complement or phase/dephasing null failed')
    for f in (h, minus, hv, hv_minus):
        ev = np.linalg.eigvalsh(f)
        require(ev.min() > -tol['source_and_effect'] and ev.max() < 1 + tol['source_and_effect'], 'unphysical mathematical effect')
    project = lambda f, d: project_helper.projection(effects + [f], tangents + [d], rho, basis, tol['rank'])
    ideal = project(h, dh)
    calibrated = project(hv, [visibility * d for d in dh])
    phase_null = project(h0, dh0)
    dephasing_null = project(dephased, [np.zeros((4, 4), complex)] * 2)
    require(phase_null['projected_rank'] == 1 and dephasing_null['projected_rank'] == 1, 'null created a coupling direction')
    # Visibility is interior (.8), so its local nuisance direction is admissible.
    v_column = np.r_[np.zeros(len(effects)), float(np.trace(visibility * (h - half) @ rho).real)]
    n = np.column_stack((calibrated['nuisance'], v_column))
    u, singular, _ = np.linalg.svd(n, full_matrices=False)
    n_rank = int(np.sum(singular > tol['rank']))
    unknown_visibility_jet = (np.eye(len(n)) - u[:, :n_rank] @ u[:, :n_rank].T) @ calibrated['jet']
    unknown_sv = np.linalg.svd(unknown_visibility_jet, compute_uv=False)
    alpha = contract['passive_reflection_port_rephase']
    rephased = coherent_effect(np.exp(1j * alpha) * r, t, phase + alpha)
    phase_transport_error = float(np.linalg.norm(rephased - h))
    frozen_phase_error = float(np.linalg.norm(coherent_effect(np.exp(1j * alpha) * r, t, phase) - h))
    require(phase_transport_error < tol['source_and_effect'], 'port/recombiner phase transport failed')
    fd_errors = []
    for index, name in enumerate(('nu', 'eta')):
        plus, negative = dict(contract['source_parameters']), dict(contract['source_parameters'])
        step = contract['derivative_step']
        plus[name] *= np.exp(step)
        negative[name] *= np.exp(-step)
        sp = helper.stationary(model, energy, **plus)
        sm = helper.stationary(model, energy, **negative)
        hp = coherent_effect(*ports(model, sp), phase)
        hm = coherent_effect(*ports(model, sm), phase)
        fd_errors.append(float(np.linalg.norm((hp - hm) / (2 * step) - dh[index])))
    require(max(fd_errors) < tol['derivative_and_frame'], 'full coherent effect derivative failed')
    survives = calibrated['projected_rank'] == 2 and calibrated['projected_singular_values'][-1] > tol['minimum_restored_singular_value']
    packet = {'witness_density': rho, 'ideal_plus_effect': h, 'ideal_minus_effect': minus,
              'visibility_plus_effect': hv, 'visibility_minus_effect': hv_minus, 'phase_zero_effect': h0,
              'ideal_effect_derivatives': np.array(dh), 'full_S': sol['S'], 'state': sol['state'],
              'reflection': r, 'transmission': t, 'joint_preparation_nuisance': calibrated['nuisance'],
              'joint_coupling_jet': calibrated['jet'], 'unknown_visibility_nuisance': n,
              'unknown_visibility_projected_jet': unknown_visibility_jet}
    output = HOME / 'results/scattering-clues-iteration6-full-packet.npz'
    np.savez_compressed(output, **packet)
    summary = lambda x: {'preparation_rank': x['preparation_rank'], 'projected_coupling_rank': x['projected_rank'],
                         'projected_singular_values': x['projected_singular_values'].tolist()}
    paths = [CONTRACT, Path(__file__), prior_packet_path, direction_packet_path] + [ROOT / contract[k] for k in
        ('source_contract', 'source_checker', 'packet_reader', 'effect_checker', 'projection_checker', 'four_probe_result', 'direction_result')] + [ROOT / name for name in contract['prior_research']]
    return {'schema': 'marici.scattering.coherent-port-result.v1', 'status': 'pass', 'validation_only': True,
            'conjecture_disposition': 'survives_with_known_phase_and_visibility' if survives else 'falsified_at_positive_witness',
            'ideal_coherent_port': summary(ideal), 'known_visibility_point8': summary(calibrated),
            'phase_zero_null': summary(phase_null), 'dephasing_null': summary(dephasing_null),
            'unknown_visibility': {'nuisance_rank': n_rank, 'projected_coupling_rank': int(np.sum(unknown_sv > tol['rank'])), 'projected_singular_values': unknown_sv.tolist()},
            'ideal_witness_plus_probability': float(np.trace(h @ rho).real), 'visibility_witness_plus_probability': float(np.trace(hv @ rho).real),
            'visibility_susceptibility': float(v_column[-1]), 'complement_residual': complement, 'null_residual': null_error,
            'transported_port_phase_error': phase_transport_error, 'untransported_port_phase_change': frozen_phase_error,
            'maximum_full_effect_derivative_error': max(fd_errors), 'source_replay_error': source_error,
            'source_provenance': provenance,
            'full_packet': {'path': output.relative_to(ROOT).as_posix(), 'sha256': sha(output), 'array_count': len(packet)},
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in paths},
            'physical_recombiner_constructed': False, 'physical_phase_or_visibility_calibrated': False,
            'physical_scattering_explained': False, 'latest_model_recomputed': False, 'root_outcome': None}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration6.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'conjecture_disposition', 'known_visibility_point8',
                     'unknown_visibility', 'transported_port_phase_error', 'root_outcome')}, indent=2))
