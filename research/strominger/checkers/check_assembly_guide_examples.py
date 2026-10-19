"""Replay documented assembly examples without overwriting shared result stores."""
import contextlib
import hashlib
import importlib
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/strominger/results/assembly-guide'
V = ROOT / 'research/voevodsky'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    executions = []
    checks = {}

    def run(arguments, label):
        command = [sys.executable] + arguments
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=300)
        log = OUT / (label + '.log')
        log.write_text(result.stdout + result.stderr, encoding='utf-8')
        executions.append({'command': command, 'returncode': result.returncode,
                           'log': log.relative_to(ROOT).as_posix(), 'log_sha256': digest(log)})
        if result.returncode:
            raise RuntimeError(f'{label} failed; inspect {log}')
        return result

    for label, source, moving, fixed, orders, steps in [
        ('proton', 'relative-proton', 4, 0, [3, 3], 6),
        ('electron', 'relative-electron', 5, 0, [5], 5),
        ('neutron', 'mode-neutron', 6, 2, [3], 3),
    ]:
        output = OUT / f'{label}-cycle.json'
        run(['research/voevodsky/checkers/evolve_relative_geometry_modes.py',
             '--source', f'research/voevodsky/inputs/{source}.json', '--output', str(output)], label)
        data = json.loads(output.read_text())
        states = data['facet_states']
        checks[label + '_counts'] = (sum(s['moving_centroid'] for s in states) == moving
                                    and sum(not s['moving_centroid'] for s in states) == fixed)
        checks[label + '_schedule'] = (data['generator_orders'] == orders and
            data['scheduled_atomic_steps_to_word_return'] == steps and len(data['centroid_motion_trace']) == steps)
        checks[label + '_recovery'] = (data['reverse_history_recovers_every_centroid'] and
            data['fixed_modes_retained'] and data['centroid_motion_trace'][-1]['all_labelled_centroids_returned'])
    run(['research/nima/checkers/check_twelve_triangle_positive_geometry.py', '--source',
         'research/nima/inputs/proton-six-arrows.json', '--output-dir', str(OUT / 'proton-coefficients')], 'proton-coefficients')
    proton = json.loads((OUT / 'proton-coefficients/assembly.json').read_text())
    arrows = json.loads((OUT / 'proton-coefficients/arrows.json').read_text())
    checks['proton_transfers'] = proton['unique_directed_arrows'] == proton['return_cycle_union_measure'] == len(arrows) == 1836
    checks['proton_closed'] = proton['boundary_chain_zero'] and proton['closed_walk_union_covers_every_arrow']
    run(['research/nima/checkers/check_triangle_arrow_source_input.py'], 'proton-input-controls')
    checks['proton_input_controls'] = True

    # Import the unchanged producer, relocate only its BASE output/input root,
    # and copy the prerequisite receipt verbatim. No shared results are written.
    sys.path.insert(0, str(V / 'checkers'))
    module = importlib.import_module('check_electron_tetrahedral_spinor')
    protected = [V / 'results' / name for name in ('electron_charge_spin_frontier.json',
                  'electron_tetrahedral_spinor.json', 'electron_tetrahedral_spinor_store.json')]
    before = {str(p): digest(p) for p in protected}
    sandbox = OUT / 'electron-isolated'
    (sandbox / 'results').mkdir(parents=True, exist_ok=True)
    shutil.copyfile(protected[0], sandbox / 'results' / protected[0].name)
    previous = module.BASE
    log = io.StringIO()
    try:
        module.BASE = sandbox
        with contextlib.redirect_stdout(log):
            module.main()
    finally:
        module.BASE = previous
    (OUT / 'electron-coefficients.log').write_text(log.getvalue(), encoding='utf-8')
    electron = json.loads((sandbox / 'results/electron_tetrahedral_spinor.json').read_text())
    store = json.loads((sandbox / 'results/electron_tetrahedral_spinor_store.json').read_text())
    checks['electron_all_checks'] = electron['verification_passed'] and all(electron['checks'].values())
    checks['electron_transfers'] = electron['support'] == {'L': 16, 'G': 64, 'N': 64} and electron['total_transfers'] == len(store['arrows']) == 144
    checks['electron_rank'] = electron['logical_dimension'] == 2
    checks['electron_exact_stored_manifest'] = store == json.loads(protected[2].read_text())
    checks['shared_electron_stores_unchanged'] = before == {str(p): digest(p) for p in protected}
    evidence = [ROOT / 'research/nima/inputs/proton-six-arrows.json',
        ROOT / 'research/nima/checkers/assemble_triangle_arrow_source.py',
        ROOT / 'research/nima/checkers/check_twelve_triangle_positive_geometry.py',
        ROOT / 'research/nima/checkers/check_triangle_arrow_source_input.py',
        V / 'checkers/assemble_relative_geometry.py', V / 'checkers/evolve_relative_geometry_modes.py',
        V / 'checkers/check_electron_tetrahedral_spinor.py', Path(__file__).resolve()] + protected
    evidence += [V / 'inputs' / (n + '.json') for n in ('relative-proton', 'relative-electron', 'mode-neutron')]
    receipt = {'status': 'passed' if all(checks.values()) else 'failed', 'checks': checks,
        'executions': executions,
        'electron_invocation': 'import unchanged check_electron_tetrahedral_spinor; temporarily redirect BASE to isolated directory; call main()',
        'electron_prerequisite': 'Copied existing frontier receipt verbatim; prerequisite chain NOT regenerated.',
        'evidence_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in evidence},
        'scope': 'Three common centroid cycles, proton source frontend and hostile controls, isolated electron coefficient producer. No browser, energy-bridge or Agda replay.'}
    (OUT / 'verification.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': receipt['status'], 'checks': checks}, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
