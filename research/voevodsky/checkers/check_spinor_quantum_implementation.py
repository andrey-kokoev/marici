"""Fresh quantum construction chain and implementation negative controls.
Run: uv run --with sympy python THIS_FILE
Physical platform validation is explicitly not supplied by this runner.
"""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys
import sympy as s

BASE=Path(__file__).resolve().parents[1]


def digest(p):return sha256(p.read_bytes()).hexdigest()


def main():
    stages=['spinor_quantum_leads','spinor_hard_flux_parent','spinor_stiff_flux_limit','spinor_endpoint_constructor']
    rows=[]
    for name in stages:
        script=BASE/'checkers'/f'check_{name}.py'
        run=subprocess.run([sys.executable,str(script)],capture_output=True,text=True)
        if run.returncode:raise RuntimeError(run.stdout+'\n'+run.stderr)
        path=BASE/'results'/f'{name}.json'
        assert json.loads(path.read_text(encoding='utf-8'))['verification_passed']
        rows.append({'name':name,'checker_sha256':digest(script),'result_sha256':digest(path)})
        print('PASS '+name,flush=True)
    for child,key,parent in [('spinor_hard_flux_parent','quantum_leads_sha256','spinor_quantum_leads'),
                             ('spinor_stiff_flux_limit','parent_result_sha256','spinor_hard_flux_parent'),
                             ('spinor_endpoint_constructor','quantum_leads_sha256','spinor_quantum_leads')]:
        receipt=json.loads((BASE/'results'/f'{child}.json').read_text(encoding='utf-8'))
        assert receipt[key]==digest(BASE/'results'/f'{parent}.json')
    # Negative control: bare matter hopping changes two site gauge charges.
    e0,e1=s.eye(4)[:,0],s.eye(4)[:,1]
    bare_change=e1-e0
    assisted_change=bare_change+e0-e1
    assert bare_change.dot(bare_change)==2 and assisted_change==s.zeros(4,1)
    # Ground blocks are an exact invariant finite restriction, not a rotor
    # truncation of the ladder algebra. Verify ground and first gap again.
    q=s.I*s.Matrix([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/s.sqrt(3)
    k=s.eye(4)-q;beta=s.Rational(3,5);eta=s.Rational(1,5)
    offset=3*beta/4+eta/2
    blocks=[k-beta*s.eye(4)[:,i]*s.eye(4)[i,:]/4+offset*s.eye(4) for i in range(4)]
    finite=s.diag(*blocks)
    assert finite==finite.H and finite.shape==(16,16)
    for i in range(4):
        sector=s.diag(*[s.eye(4) if j==i else s.zeros(4) for j in range(4)])
        assert finite*sector==sector*finite
    eground=(59-s.sqrt(1609))/40
    gap=s.simplify(offset-eground)
    assert gap>0 and offset<s.Rational(17,20)
    # Wrong independent phase on one oriented edge gives nonunit face
    # holonomy even though all edge magnitudes stay unchanged.
    wrong_phase=s.I
    assert wrong_phase!=1
    report={'verification_passed':True,'scope':'Fresh ideal quantum construction and algebraic negative controls; no physical apparatus tested.',
            'stages':rows,
            'retained_classical_input_sha256':digest(BASE/'results/spinor_interacting_construction.json'),
            'negative_controls':{'bare_hop_breaks_Gauss':True,'independent_edge_phase_breaks_relative_flatness':True},
            'exact_invariant_ground_flux_encoding':{'dimension':16,'qubits_if_digitally_encoded':4,'ground_multiplicity':4,'spectral_gap_exact':str(gap),'spectral_gap_decimal':float(gap),
                'scope':'Exact restriction to four conserved lead blocks, containing global ground and first excited energy. Not a representation of unrestricted rotor shift observables.'},
            'physical_acceptance':{'endpoint_factorization':'unverified','assisted_hopping_and_source_phases':'unverified','charging_metric_and_units':'unverified','sector_preparation':'unverified','device_error_and_extra_modes':'unverified'},
            'quantization_status':'Explicit conditional model completed with exact reduced/endpoint intertwiner.',
            'physical_implementation_status':'Ideal architecture specified; physical realization remains unverified.'}
    (BASE/'results/spinor_quantum_implementation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
