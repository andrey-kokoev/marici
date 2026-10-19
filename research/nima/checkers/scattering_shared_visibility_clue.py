"""Two native source energies; shared-visibility hypothesis versus its hostile."""
import json
from pathlib import Path
import numpy as np
from scattering_coherent_port_clue import coherent_effect, ports
from scattering_reflection_record_clue import load, read_packet, require, sha

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration8.v1.json'


def project(nuisance, jet, threshold):
    u, s, _ = np.linalg.svd(nuisance, full_matrices=False)
    rank = int(np.sum(s > threshold))
    result = (np.eye(len(nuisance)) - u[:, :rank] @ u[:, :rank].T) @ jet
    values = np.linalg.svd(result, compute_uv=False)
    return {'nuisance_rank': rank, 'projected_coupling_rank': int(np.sum(values > threshold)),
            'projected_singular_values': values.tolist()}, result


def audit():
    c = json.loads(CONTRACT.read_text())
    tol = c['tolerances']
    helper = load(ROOT / c['source_checker'], 'shared_visibility_source')
    projection = load(ROOT / c['projection_checker'], 'shared_visibility_projection')
    prior, data, prior_packet = read_packet(ROOT / c['four_probe_result'])
    phase_prior, phase_data, phase_packet = read_packet(ROOT / c['phase_result'])
    rho = phase_data['witness_density']
    model, _, provenance, _, _ = helper.source(json.loads((ROOT / c['source_contract']).read_text()))
    basis = data['preparation_basis']
    old_f = [data[str(e) + '/effect'] for e in prior['energies_over_epsilon']]
    old_d = [[data[str(e) + '/effect_derivative/' + p] for p in ('log_nu', 'log_eta')] for e in prior['energies_over_epsilon']]
    v, phi = c['visibility_evaluation_point'], c['phase']
    half = np.eye(4) / 2
    fs, ds, probabilities, susceptibilities = [], [], [], []
    packet = {'witness_density': rho}
    errors = []
    for e in c['phase_energies']:
        sol = helper.stationary(model, e, derivatives=True, **c['source_parameters'])
        errors.extend(sol['residuals'].values())
        r, t = ports(model, sol)
        h = coherent_effect(r, t, phi)
        f = half + v * (h - half)
        derivatives = [v * coherent_effect(r, t, phi, *ports(model, sol, d)) for d in sol['d_S_d_log_parameters']]
        fs.append(f)
        ds.append(derivatives)
        probabilities.append(float(np.trace(f @ rho).real))
        susceptibilities.append(float(np.trace(v * (h - half) @ rho).real))
        require(np.linalg.eigvalsh(f).min() > -tol['source_and_effect'] and np.linalg.eigvalsh(f).max() < 1 + tol['source_and_effect'], 'invalid positive effect')
        packet[str(e) + '/effect'] = f
        packet[str(e) + '/derivatives'] = np.array(derivatives)
        packet[str(e) + '/full_S'] = sol['S']
    require(max(errors) < tol['source_and_effect'], 'source solve failed')
    require(np.linalg.norm(fs[0] - phase_data['visibility_plus_effect']) < tol['source_and_effect'], 'phase source changed')
    projected = projection.projection(old_f + fs, old_d + ds, rho, basis, tol['rank'])
    shared_column = np.r_[np.zeros(len(old_f)), susceptibilities][:, None]
    shared_n = np.column_stack((projected['nuisance'], shared_column))
    independent_columns = np.zeros((len(old_f) + len(fs), len(fs)))
    independent_columns[len(old_f):] = np.diag(susceptibilities)
    independent_n = np.column_stack((projected['nuisance'], independent_columns))
    shared, shared_jet = project(shared_n, projected['jet'], tol['rank'])
    independent, independent_jet = project(independent_n, projected['jet'], tol['rank'])
    duplicate_base = projection.projection(old_f + [fs[0], fs[0]], old_d + [ds[0], ds[0]], rho, basis, tol['rank'])
    duplicate_column = np.r_[np.zeros(len(old_f)), susceptibilities[0], susceptibilities[0]][:, None]
    duplicate, _ = project(np.column_stack((duplicate_base['nuisance'], duplicate_column)), duplicate_base['jet'], tol['rank'])
    require(independent['projected_coupling_rank'] == 1 and duplicate['projected_coupling_rank'] == 1, 'nuisance or duplicate hostile falsely adds a direction')
    packet.update({'joint_preparation_nuisance': projected['nuisance'], 'joint_coupling_jet': projected['jet'],
                   'shared_visibility_nuisance': shared_n, 'shared_visibility_projected_jet': shared_jet,
                   'independent_visibility_nuisance': independent_n, 'independent_visibility_projected_jet': independent_jet})
    output = HOME / 'results/scattering-clues-iteration8-full-packet.npz'
    np.savez_compressed(output, **packet)
    survives = shared['projected_coupling_rank'] == 2 and shared['projected_singular_values'][-1] > tol['minimum_restored_singular_value']
    sources = [CONTRACT, Path(__file__), prior_packet, phase_packet] + [ROOT / c[k] for k in
        ('source_contract', 'source_checker', 'phase_checker', 'projection_checker', 'four_probe_result', 'phase_result', 'prior_research')] + [HOME / 'checkers/scattering_reflection_record_clue.py']
    return {'schema': 'marici.scattering.shared-visibility-result.v1', 'status': 'pass', 'validation_only': True,
            'conjecture_disposition': 'survives_under_shared_visibility_hypothesis' if survives else 'falsified_at_positive_witness',
            'shared_unknown_visibility': shared, 'independent_unknown_visibilities': independent, 'duplicate_energy_control': duplicate,
            'known_visibility': {'preparation_rank': projected['preparation_rank'], 'projected_coupling_rank': projected['projected_rank'], 'projected_singular_values': projected['projected_singular_values'].tolist()},
            'phase_probabilities': probabilities, 'log_visibility_susceptibilities': susceptibilities,
            'maximum_source_residual': max(errors), 'source_provenance': provenance,
            'full_packet': {'path': output.relative_to(ROOT).as_posix(), 'sha256': sha(output), 'array_count': len(packet)},
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in sources},
            'physical_visibility_sharing_validated': False, 'physical_instrument_constructed': False,
            'physical_scattering_explained': False, 'latest_model_recomputed': False, 'root_outcome': None}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration8.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'conjecture_disposition', 'shared_unknown_visibility',
                     'independent_unknown_visibilities', 'duplicate_energy_control', 'root_outcome')}, indent=2))
