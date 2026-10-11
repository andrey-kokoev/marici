"""Actual amplitude-port algebra versus proposed same-slot response.
Restriction to the invariant selected-local-mode subspace is exact.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_four_packet_record_feedback import mm,basis,rank
ROOT=Path(__file__).resolve().parents[1]

def main():
    rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
    n=len(rows);assert n==12
    I=basis(n);M=tuple((F(1,n),)*n for _ in range(n));Z=tuple((F(0),)*n for _ in range(n))
    amplitudes=tuple(F(1) if r['outer_arrow']=='AB' else F(-1) if r['outer_arrow']=='BA' else F(0) for r in rows)
    D=tuple(tuple(amplitudes[i] if i==j else F(0) for j in range(n)) for i in range(n))
    assert mm(M,M)==M
    assert rank((sum(I,()),sum(M,())))==2
    assert mm(M,D)!=mm(D,M)
    # The existing stages restrict to I, M, M. Every word reduces to I or M;
    # even their linear span cannot contain the proposed local response gate.
    assert rank((sum(I,()),sum(M,()),sum(D,())))==3
    same_slot=mm(mm(mm(M,D),D),M)
    mixed_first=mm(mm(mm(mm(M,D),M),D),M)
    assert same_slot==tuple(tuple(x/6 for x in row) for row in M)
    assert mixed_first==Z
    # Squaring a readable mean and reading a squared retained field differ.
    assert sum(amplitudes)/n==0
    assert sum(a*a for a in amplitudes)/n==F(1,6)
    assert sum((2*a)**2 for a in amplitudes)/n==F(2,3)
    # Literal residual-to-equivalence interpretation at the prior unit trial.
    # I + D has a zero eigenvalue; not an invertible represented comparison.
    gates=[]
    for eps in (F(1),F(1,2)):
        A=tuple(tuple(I[i][j]+eps*D[i][j] for j in range(n)) for i in range(n))
        gates.append(dict(amplitude=str(eps),rank=rank(A),invertible=rank(A)==n,
                          counting_isometry=mm(tuple(zip(*A)),A)==I))
    assert gates[0]['rank']==11 and gates[1]['rank']==12
    assert not any(g['counting_isometry'] for g in gates)
    result=dict(schema='marici.nima.inner-face-response-port-binding.v1',status='pass',
        exact_mode_sector='In transported local eigenvector coefficients, stages are I, M, M with M_ij=1/12.',
        generated_linear_operator_algebra_dimension=2,
        proposed_diagonal_response_gate_in_that_algebra=False,
        before_averaging_same_slot='M D(a) D(a) M = M/6',
        after_averaging='M D(a) M D(a) M = 0',
        comparison_gate_controls=gates,
        actual_native_composition='Composes supplied pointed equivalences through an identical middle package and retains both parents; no numerical same-slot gate or weighting is selected.',
        interpretation='The covariance is a valid retained-record diagnostic. Making it active requires an amplitude-dependent gate and a source-derived port schedule absent from the fixed geometric circuit.',
        scope='No-go for this fixed stage algebra, not for all native rules, nonlinear source extensions or alternative physical realizations.',
        disposition='The proposed nonlinear operation has not been bound to the actual triangle circuit. No persistent electron-like excitation or birth mechanism is derived.')
    (ROOT/'results/inner-face-response-port-binding.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
