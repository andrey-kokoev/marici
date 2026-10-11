"""Fresh sequential verification of the classical interacting construction.
Run: uv run --with numpy --with scipy --with sympy python THIS_FILE
Upstream receipts outside this chain are retained inputs, not re-proved here.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

BASE=Path(__file__).resolve().parents[1]


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    stages=['electron_tetrahedral_spinor','spinor_matter_link_adapter',
            'spinor_face_magnetic_action','spinor_fixed_flux_relaxation',
            'spinor_ground_orbit','spinor_orbit_dynamics','spinor_constrained_leads',
            'spinor_tangent_dynamics','spinor_finite_dynamics']
    retained={name:digest(BASE/'results'/f'{name}.json') for name in
              ['electron_charge_spin_frontier','weighted_matter_link_adapter','all_face_contact']}
    rows=[]
    for name in stages:
        checker=BASE/'checkers'/f'check_{name}.py'
        result=BASE/'results'/f'{name}.json'
        run=subprocess.run([sys.executable,str(checker)],capture_output=True,text=True)
        if run.returncode:
            raise RuntimeError(f'{name} failed:\n{run.stdout}\n{run.stderr}')
        data=json.loads(result.read_text(encoding='utf-8'))
        assert data['verification_passed'], name
        rows.append({'stage':name,'checker_sha256':digest(checker),'result_sha256':digest(result)})
        print(f'PASS {name}',flush=True)
    for name,value in retained.items():assert digest(BASE/'results'/f'{name}.json')==value
    # Downstream receipts must bind to the freshly regenerated predecessors.
    for child,key,parent in [
        ('spinor_constrained_leads','ground_orbit_sha256','spinor_ground_orbit'),
        ('spinor_tangent_dynamics','constrained_result_sha256','spinor_constrained_leads'),
        ('spinor_finite_dynamics','tangent_result_sha256','spinor_tangent_dynamics')]:
        data=json.loads((BASE/'results'/f'{child}.json').read_text(encoding='utf-8'))
        assert data[key]==digest(BASE/'results'/f'{parent}.json')
    report={'verification_passed':True,'scope':'Fresh nine-stage classical construction chain, conditional on the recorded upstream receipts. Not a repository-wide or quantum validation.',
            'retained_upstream_receipts':retained,'stages':rows,
            'classical_state_space':'Locally CP^3 x T* T^3; source phase lifts retained separately.',
            'ground_set':'Four tori, one for each minimizing matter ray with its matching conserved exterior flux.',
            'dynamics':'Fixed-lead Hamiltonian; no inter-sector transitions in the admitted action.',
            'unresolved':['Physical implementation of the hard source-flux constraint','Quantization and physical charge/time normalization','Any additional boundary interaction permitting lead-sector transitions']}
    (BASE/'results/spinor_interacting_construction.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
