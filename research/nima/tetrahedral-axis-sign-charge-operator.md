# Axis-charge candidates: corrected scope

## Question

Do the V4 axis half-turns provide a physical charge operator on the
36-coordinate tetrahedral construction?

## Correction to the earlier conclusion

The previous version claimed that no A4-commuting Hermitian operator could
have unit expectation on the collective mode and spectrum in {0,+1,-1}.
**That claim was false.** The identity is one counterexample. More usefully,

\[
N=uu^*/80,\qquad Nu=u,
\]

commutes with the combined position/fiber A4 action and has spectrum {0,1}.
The operator 2N-I has spectrum {-1,1} and also gives eigenvalue +1 on u.
Even within the V4-generated algebra, \(-H_x-H_y-H_z=I\).

These statements do not identify electric charge. They show that the proposed
spectral and symmetry conditions were insufficient to rule it out. A physical
charge construction needs independently specified sectors and a coupling law.
A vector in the algebraic kernel of N is not thereby a neutron.

## Exact candidate scan

The collective vector is assembled from the twelve transported vectors
\(v_x=r_xv_0\), not twelve identical ambient copies of \(v_0\). Its norms are
\(\|v_0\|^2=20/3\), \(\|u\|^2=80\), and each fixed axis contributes 80/3
to the latter. For a repeated diagonal block,

\[
\langle Q\rangle_u=(q_x+q_y+q_z)/3.
\]

| Fiber block | Spectrum | Expectation | Variance |
|---|---|---:|---:|
| diag(1,-1,-1) | {-1,1} | -1/3 | 8/9 |
| diag(1,0,0) | {0,1} | 1/3 | 2/9 |
| diag(0,1,1) | {0,1} | 2/3 | 2/9 |
| diag(1,-1,0) | {-1,0,1} | 0 | 2/3 |
| diag(-3,3,3) | {-3,3} | 1 | 8 |
| I | {1} | 1 | 0 |

An expectation of +1 is not a charge eigenvalue: the scaled half-turn has
nonzero variance. Individual axis selectors and half-turns do not commute
with all tetrahedral rotations. Their failure supplies no theorem about all
operators on the full space.

## Disposition and verification

The bounded candidate values survive; the universal no-go and the assertion
that charge must live on an extended rotor space are withdrawn. Whether any
algebraic candidate is physically appropriate remains unproved.

```text
python research/nima/checkers/check_tetrahedral_axis_charge_operator.py
```

The dependency-free checker tests eleven diagonal candidates, exact variances,
A4 commutation, and the collective-projector counterexample with an explicit
nonzero neutral vector. It writes `results/tetrahedral-axis-charge-operator.json`.
The [binary tetrahedral bridge](binary-tetrahedral-spinor-bridge.md) separately
checks the full collective-projector idempotence and the spinor/operator
representation boundary. No external masses, electromagnetic field, or rotor
dynamics are supplied by these tests.
