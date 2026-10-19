"""Prior-source contact experiment: units versus two dimensionless source laws.

Uses immutable archived native matrices. Executes the exact archived ContactModel
class AST, not its main/packet/symbolic reconstruction. Independently assembles
stationary boundary equations and analytic parameter derivatives. No fit or lab.
"""
import ast
import hashlib
import io
import json
import math
from pathlib import Path
from zipfile import ZipFile
import numpy as np
from scipy.linalg import eigh, solve

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parents[1]
CONTRACT = HOME / 'contracts/scattering-clues-iteration1.v1.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source(contract):
    pins = json.loads((ROOT / contract['source_pins']).read_text())
    path = ROOT / contract['source_archive']
    require(sha(path) == pins['sources'][contract['source_archive']]['sha256'], 'archive differs from pinned source')
    with ZipFile(path) as archive:
        manifest = json.loads(archive.read('SHA256.json'))
        for name, expected in manifest.items():
            require(hashlib.sha256(archive.read(name)).hexdigest() == expected, 'archive manifest drift: ' + name)
        text = archive.read('pentachoron_autonomous_contact.py').decode()
        saved = json.loads(archive.read('pentachoron_autonomous_contact_results.json'))
        require(hashlib.sha256(text.encode()).hexdigest() == saved['script_sha256'], 'source script/receipt mismatch')
        with np.load(io.BytesIO(archive.read('native_matrices.npz')), allow_pickle=False) as data:
            ho, hc, p = (data[name].copy() for name in ('H_original', 'H_connected', 'matching_projector'))
    node = next(n for n in ast.parse(text).body if isinstance(n, ast.ClassDef) and n.name == 'ContactModel')
    namespace = {'np': np, 'eigh': eigh, 'solve': solve, 'Path': Path, 'math': math, '__name__': 'archived_contact_class'}
    exec(compile(ast.Module(body=[node], type_ignores=[]), '<byte-pinned archived ContactModel class>', 'exec'), namespace)
    model = namespace['ContactModel'](ho, hc, p)
    return model, saved, {'archive_sha256': sha(path), 'manifest_members_verified': len(manifest),
                          'source_script_sha256': saved['script_sha256'],
                          'native_matrices_sha256': manifest['native_matrices.npz']}, namespace['ContactModel'], (ho, hc, p)


def stationary(model, kinetic_energy, nu=1.0, eta=2.0, energy_scale=1.0, derivatives=False):
    require(nu > 0 and eta > 0 and energy_scale > 0, 'nonpositive model parameter')
    # Retain one original native eigenframe under both parameter and units changes.
    el = model.el * energy_scale
    c = model.C * energy_scale
    b = model.B
    kinetic = nu * energy_scale
    coupling = eta * energy_scale
    energy = (model.el[0] + kinetic_energy) * energy_scale
    offsets = energy - el
    require(np.min(abs(offsets)) > 1e-10, 'threshold needs one-sided control')
    opened = np.flatnonzero(offsets > 0)
    k = np.sqrt((offsets + 0j) / kinetic)
    velocity = 2 * kinetic * k.real
    z = np.diag(2j * kinetic * k)
    count, n = len(opened), model.n
    incoming = np.zeros((n, count), complex)
    incoming[opened, np.arange(count)] = 1 / np.sqrt(velocity[opened])
    matrix = np.block([[z - coupling * b, coupling * b],
                       [coupling * b, energy * np.eye(n) - c - coupling * b]])
    rhs = np.vstack((z @ incoming, np.zeros_like(incoming)))
    state = np.linalg.solve(matrix, rhs)
    boundary, core = state[:n], state[n:]
    t = np.sqrt(velocity[opened, None]) * boundary[opened]
    r = t - np.eye(count)
    scattering = np.block([[r, t], [t, r]])
    cols = np.array([list(opened).index(i) for i in model.ground])
    excited = np.flatnonzero(el[opened] - el[0] > 1e-8)
    probabilities = (np.sum(abs(t[:, cols]) ** 2, axis=1) + np.sum(abs(r[:, cols]) ** 2, axis=1)) / len(cols)
    flux = float(probabilities[excited].sum())
    residuals = {
        'full_S_unitarity': float(np.linalg.norm(scattering.conj().T @ scattering - np.eye(2 * count))),
        'boundary_and_core': float(np.linalg.norm(matrix @ state - rhs)),
        'energy_ledger': abs(float(probabilities @ (energy - el[opened]) + probabilities @ (el[opened] - el[0])) - kinetic_energy * energy_scale)}
    out = {'S': scattering, 'state': state, 'open': opened, 'excited_flux': flux, 'residuals': residuals}
    if derivatives:
        dm_nu = np.zeros_like(matrix)
        dm_nu[:n, :n] = z / 2
        dm_eta = coupling * np.block([[-b, b], [b, -b]])
        values, tangent_matrices = [], []
        for dm, drhs, prefactor in ((dm_nu, rhs / 4, .25), (dm_eta, np.zeros_like(rhs), 0)):
            ds = np.linalg.solve(matrix, drhs - dm @ state)
            dt = prefactor * t + np.sqrt(velocity[opened, None]) * ds[:n][opened]
            selection = np.ix_(excited, cols)
            value = 2 * np.real(np.sum(np.conj(t[selection]) * dt[selection] + np.conj(r[selection]) * dt[selection])) / len(cols)
            values.append(float(value))
            tangent_matrices.append(np.block([[dt, dt], [dt, dt]]))
        out['d_flux_d_log_parameters'] = values
        out['d_S_d_log_parameters'] = tangent_matrices
    return out


def audit():
    contract = json.loads(CONTRACT.read_text())
    require(all(value is False for value in contract['boundary'].values()), 'physical scope promotion')
    model, saved, provenance, cls, matrices = source(contract)
    par, tol = contract['parameters'], contract['tolerances']
    require(model.n == 20 and len(model.ground) == 4, 'source state/ensemble changed')
    gap = float(model.el[4] - model.el[0])
    require(abs(gap - math.sqrt(5)) < 1e-11, 'native threshold not recovered')
    checks = []
    def check(name, condition):
        require(condition, name)
        checks.append(name)
    rows, jacobian, fd_errors = [], [], []
    full_packet = {'native_eigenframe': model.V, 'native_eigenvalues': model.el,
                   'core_in_native_frame': model.C, 'projector_in_native_frame': model.B,
                   'prepared_ground_indices': model.ground}
    max_residual = max_source_error = max_schur_error = max_unit_error = 0.0
    for energy in par['kinetic_energies_over_epsilon']:
        base = stationary(model, energy, derivatives=True)
        label = str(energy)
        for name in ('S', 'state', 'open'):
            full_packet[label + '/base/' + name] = base[name]
        for name, matrix in zip(('log_nu', 'log_eta'), base['d_S_d_log_parameters']):
            full_packet[label + '/dS/' + name] = matrix
        source_full = model.scatter(energy)
        source_reduced = model.scatter(energy, 'eliminated')
        max_source_error = max(max_source_error, float(np.linalg.norm(base['S'] - source_full['S'])))
        max_schur_error = max(max_schur_error, float(np.linalg.norm(source_full['S'] - source_reduced['S'])))
        unit = stationary(model, energy, energy_scale=par['common_energy_unit_rescaling'])
        full_packet[label + '/units_control/S'] = unit['S']
        max_unit_error = max(max_unit_error, float(np.linalg.norm(base['S'] - unit['S'])))
        jacobian.append(base['d_flux_d_log_parameters'])
        h = 1e-5
        for index, parameter in enumerate(('nu', 'eta')):
            nominal = 1.0 if parameter == 'nu' else 2.0
            plus = stationary(model, energy, **{parameter: nominal * math.exp(h)})['excited_flux']
            minus = stationary(model, energy, **{parameter: nominal * math.exp(-h)})['excited_flux']
            fd_errors.append(abs((plus - minus) / (2 * h) - jacobian[-1][index]))
        controls = []
        pairs = [(nu, 2.0) for nu in par['nu_controls']] + [(1.0, eta) for eta in par['eta_controls'] if eta != 2.0]
        for nu, eta in pairs:
            result = stationary(model, energy, nu, eta)
            max_residual = max(max_residual, *result['residuals'].values())
            for name in ('S', 'state', 'open'):
                full_packet[f'{label}/nu{nu}/eta{eta}/' + name] = result[name]
            controls.append({'nu': nu, 'eta': eta, 'excited_native_record_flux': result['excited_flux']})
        rows.append({'kinetic_energy_over_epsilon': energy, 'controls': controls})
    for old in saved['kinetic_choice_controls']:
        nu = old['kinetic_coefficient']
        result = stationary(model, 2.3, nu=nu)
        check('saved kinetic control replay/' + str(nu), abs(result['excited_flux'] - old['outgoing_native_excited']) < tol['independent_solver_and_source_replay'])
        original = cls(*matrices, kinetic=nu).scatter(2.3)
        max_source_error = max(max_source_error, float(np.linalg.norm(result['S'] - original['S'])))
    singular = np.linalg.svd(np.array(jacobian), compute_uv=False)
    check('analytic parameter derivatives agree with finite differences', max(fd_errors) < tol['analytic_vs_finite_difference_derivative'])
    check('two locally distinguishable parameter directions', float(singular[-1]) > tol['minimum_small_singular_value'])
    check('all positive-form controls conserve flux and energy', max_residual < tol['conservation_and_boundary'])
    check('independent full boundary assembly matches source class', max_source_error < tol['independent_solver_and_source_replay'])
    check('source full and Schur solves agree away from poles', max_schur_error < tol['independent_solver_and_source_replay'])
    check('true common energy units change leaves full S unchanged', max_unit_error < tol['independent_solver_and_source_replay'])
    kinetic_fluxes = [row['excited_native_record_flux'] for row in rows[0]['controls'] if row['eta'] == 2]
    contact_fluxes = [row['excited_native_record_flux'] for row in rows[0]['controls'] if row['nu'] == 1]
    check('kinetic ratio changes dimensionless flux', max(kinetic_fluxes) - min(kinetic_fluxes) > tol['minimum_shape_change'])
    check('contact-law rival changes dimensionless flux', max(contact_fluxes) - min(contact_fluxes) > tol['minimum_shape_change'])
    packet = HOME / 'results/scattering-clues-iteration1-full-packet.npz'
    np.savez_compressed(packet, **full_packet)
    return {'schema': 'marici.conjecture-net.scattering-clues-iteration1-result.v1', 'status': 'pass',
            'full_packet': {'path': packet.relative_to(ROOT).as_posix(), 'sha256': sha(packet),
                            'array_count': len(full_packet), 'basis': 'fixed archived native eigenframe',
                            'scope': 'all open/closed contact fields; full two-direction S and analytic S tangents'}, 
            'validation_only': True, 'checks': checks, 'source_provenance': provenance,
            'native_threshold_over_epsilon': gap, 'rows': rows,
            'log_parameter_jacobian': jacobian, 'jacobian_singular_values': singular.tolist(),
            'maximum_derivative_control_residual': max(fd_errors), 'maximum_conservation_residual': max_residual,
            'maximum_independent_source_difference': max_source_error, 'maximum_source_schur_difference': max_schur_error,
            'maximum_common_units_S_difference': max_unit_error,
            'governing_conjecture': 'falsified_dimensionless_shape_is_not_selected_by_conservation_and_native_geometry',
            'surviving_scope': 'Source threshold recovered; local model readouts can distinguish two supplied ratios, conditional on known preparation and detector response. No global identification or physical fit.',
            'physical_scattering_explained': False, 'latest_strained_model_recomputed': False, 'root_outcome': None,
            'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in [CONTRACT, Path(__file__)] + [ROOT / n for n in contract['prior_clues']]}}


if __name__ == '__main__':
    result = audit()
    (HOME / 'results/scattering-clues-iteration1.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'native_threshold_over_epsilon', 'jacobian_singular_values',
                     'maximum_derivative_control_residual', 'maximum_conservation_residual',
                     'maximum_common_units_S_difference', 'governing_conjecture', 'root_outcome')}, indent=2))
