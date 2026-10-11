"""Replay the complete archived phase model; no phase fitting or historical writes.
uv run --with scipy python research/nima/checkers/collect_phase_readout_diagnostics.py
"""
import ast
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import numpy as np
from collect_continuum_diagnostics import load

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-phase-readout-evidence'
FULL = ROOT/'quarantine/20261007-generation-evidence/checkers/check_full_12x12_gram.py'


def encode(a):
    a = np.asarray(a)
    return {'real':a.real.tolist(),'imag':a.imag.tolist()}


def main():
    receipts = [ROOT/'results'/name for name in
                ('full-12x12-gram.json','flavor-puzzle-solver.json','ckm-cross-sector-closure.json')]
    before = [p.read_bytes() if p.exists() else None for p in receipts]
    full = load(FULL)  # Entire original computation, only its receipt write suppressed.
    U, V = full['V_up'], full['V_down']
    C = U.conj().T @ V
    v = C[:2,2]
    r = np.linalg.norm(v)
    assert r > 1e-3
    W = np.eye(3,dtype=complex)
    W[:2,:2] = np.array([[v[0],-v[1].conjugate()],
                        [v[1], v[0].conjugate()]])/r
    R = np.array([[1,1,0],[-1,1,0],[0,0,2**0.5]])/(2**0.5)
    changed = []
    for basis in (U @ W,U @ W @ R):
        residual = np.max(np.abs(basis @ np.diag(full['evals_up']) @ basis.conj().T-full['M_up_sq']))
        assert residual < 1e-7
        changed.append({'squared_modulus_02':float(abs((basis.conj().T@V)[0,2])**2),
                        'reconstructed_operator_max_residual':float(residual)})
    assert abs(changed[0]['squared_modulus_02']-changed[1]['squared_modulus_02']) > 1e-3
    # Execute the exact original function bodies and setup, not its 37^4 search.
    solver_path = ARCHIVE/'checkers/check_flavor_solver.py'
    tree = ast.parse(solver_path.read_text(encoding='utf-8'))
    cut = next(i for i,node in enumerate(tree.body) if isinstance(node,ast.For))
    assert isinstance(tree.body[cut].target,ast.Name) and tree.body[cut].target.id == 'pU1'
    tree.body = tree.body[:cut]
    solver = {'__file__':str(solver_path),'__name__':'_retained_functions_'}
    with redirect_stdout(io.StringIO()):
        exec(compile(tree,str(solver_path),'exec'),solver)
    trials = [[0,0,0],list(full['delta_type']),[0,float(np.pi),0]]
    values = [solver['yukawa_eigenvalues'](phi) for phi in trials]
    for values_i in values:
        assert np.max(np.abs(np.array(values_i)-[2304,576,576])) < 1e-7
    variational = ARCHIVE/'checkers/check_ckm_variational.py'
    try:
        ast.parse(variational.read_text(encoding='utf-8'))
    except SyntaxError as exc:
        defect = {'type':'SyntaxError','lineno':exc.lineno,'message':exc.msg}
    else:
        raise AssertionError('Expected preserved quote/syntax defect')
    assert before == [p.read_bytes() if p.exists() else None for p in receipts]
    paths = [Path(__file__).resolve(),ROOT/'checkers/collect_continuum_diagnostics.py',FULL,solver_path,variational]
    result = {
        'schema':'marici.nima.phase-readout-transport.v1',
        'evidence_role':'source-bound full numerical replay and bounded function probes; not exact proof or physical selection',
        'base_gram':full['G_base'].tolist(),'theta':full['theta'].tolist(),
        'indices':{k:full[k] for k in ('up_indices','down_indices','doublet_indices')},
        'matrices':{k:encode(full[k]) for k in ('G_phased','G_up','G_down','M_up_sq','M_down_sq','CKM')},
        'printed_angles':full['result']['predicted_CKM_angles_with_input_phases'],
        'fixed_original_source_eigenframe_change':changed,
        'solver':{'trials':trials,'singular_values':values,'target':solver['y_target'],
                  'execution_scope':'original setup and functions only; 37^4 search skipped, no fitted replacement'},
        'variational_execution_defect':defect,'historical_receipts_unchanged':True,
        'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):
                          hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/phase-readout-transport.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'collected','original_angles':result['printed_angles'],
                      'same_source_different_readouts':changed,'syntax_defect':defect},indent=2))


if __name__ == '__main__':
    main()
