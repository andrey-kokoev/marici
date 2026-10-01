# Completed calculation of the proposed Machian eigenline update

## Outcome

The finite rule tested here is

    K_p=sum_(q!=p) w_q P_q,
    P'_p=lowest contrast-space eigenprojector of K_p,
    q'_p=P'_p e_p.

The full replacement rule has unstable shape modes. A continuous alignment version relaxes the tested deformation while maintaining positive geometry. Both rules erase radial scale. Consequently this calculation produces an orientation-alignment interaction and does not produce a Newtonian gravitational force law.

This outcome concerns the specified response rule. The body → eigenline → body organizing idea admits richer spectral records than the normalized projectors used here.

## Starting data

Four labelled records with their counting inner product and seed cycles (ABC), (ADB) generate the twelve-element group. Group averaging gives E=J_4/4 and the contrast projector H=I-E. The body consists of q_p=H e_p and its normalized lines P_p=(4/3)q_p q_p^T.

The first one-cycle calculation, in [machian-thing-eigenline-cycle.md](machian-thing-eigenline-cycle.md), constructs the body, its source matrices, the selected lines and the reconstructed positive simplex. The current calculation completes its stability, iteration and radial-response tests.

## 1. Exact linearized return

At equal weights, K_p=(4/3)H-P_p. Its lowest eigenvalue is 1/3, with spectral gap one. The derivative of its lowest eigenprojector is

    delta P'_p = -(H-P_p) delta K_p P_p - P_p delta K_p (H-P_p),
    delta K_p = sum_(q!=p) delta P_q.

An exact rational basis spans the eight-dimensional tangent space of four real projective lines in three dimensions. The return multipliers are:

| Perturbation | Multiplicity | Multiplier |
|---|---:|---:|
| Diagonal shape strain | 2 | -5/3 |
| Off-diagonal shape strain | 3 | 1/9 |
| Rigid rotation | 3 | 1 |

The two diagonal-strain modes grow by 5/3 and alternate sign each cycle. The regular tetrahedron is therefore an unstable fixed point of simultaneous full eigenline replacement.

## 2. Repeated cycles

A pure-Python symmetric Jacobi eigensolver checks the residual and normalization of every computed eigenpair. The exact linearization is the primary stability evidence; the iterations show its finite consequences.

Starting from a diagonal strain of size 10^-4, after 37 cycles:

- reconstructed volume is approximately 9.29e-11, from approximately 1/3;
- the smallest source eigenvalue is approximately 4.58e-13;
- the iteration stops at the declared 10^-12 source-degeneracy threshold.

Starting from the symmetric body with B's source weight doubled, after 32 cycles:

- reconstructed volume is approximately 0.250000213;
- the smallest source eigenvalue is approximately 7.98e-13;
- the same source-positivity threshold is reached.

These are numerical approaches to degeneration, not assertions of an exactly singular finite iterate.

## 3. Continuous line alignment

A separate, explicitly specified continuous response is

    dP_p/dtau = -[P_p,[P_p,S]],
    S=sum_q w_q P_q.

The self term commutes with P_p, so the driving commutator is determined by the other constituents. The flow is tangent to rank-one orthogonal projectors: trace, idempotence and matrix positivity are preserved by the corresponding orthogonal-conjugation evolution.

For the energy

    V=Tr(S²)/2,

its derivative is

    dV/dtau = -sum_p w_p ||[P_p,S]||_F² <= 0.

The linearized rates at the equal-weight tetrahedron are -8/3 for diagonal strain, -8/9 for off-diagonal strain, and zero for rigid rotation.

A 600-step integration from a finite diagonal deformation gives:

| Quantity | Initial | Final |
|---|---:|---:|
| Energy | 4 | 8/3 |
| Body volume | 16/81 | 1/3 |
| Smallest source eigenvalue | about 0.20924 | 1/3 |

Every accepted stage has positive body volume and positive source metrics. In this symmetric diagonal-strain family, the interpolating coordinate factors remain positive throughout each step, so positivity also holds between recorded endpoints. The numerical step size is an integration parameter, with energy/positivity backtracking; it is not a physical coupling constant.

This establishes a stable alignment model in the tested family. It does not establish global positivity for arbitrary initial configurations.

## 4. Exact radial-scale obstruction

Normalized eigenline data obey

    P_p = q_p q_p^T/(q_p^T q_p),
    P_p(a q_p)=P_p(q_p)  for every nonzero a.

Holding source weights fixed, every K_p and every selected line is therefore identical for geometries differing only in overall length scale. Repeated application cannot recover the erased scale.

The response carried by this rule has scale exponent zero. At fixed source masses, a Newtonian acceleration has exponent -2 and a Newtonian tidal tensor has exponent -3.

Thus no function of these normalized projectors and fixed source weights alone can provide the required radial dependence. Choosing a distance-dependent weight would supply new input rather than derive that dependence from the tested cycle. A richer eigenline packet would need to retain the geometric scale/eigenvalue information before a force-law calculation is possible.

## Delivered verification

    python research/nima/checkers/check_machian_thing_eigenline_cycle.py
    python research/nima/checkers/check_machian_cycle_dynamics.py

Artifacts:

- `results/machian-thing-eigenline-cycle.json`: exact one-cycle source, eigenline and positive-body reconstruction.
- `results/machian-cycle-dynamics.json`: exact tangent spectrum, numerical iteration histories, dissipative-flow calculation and scale obstruction.

The arithmetic establishes the stability failure and scale obstruction of the proposed full-update rule. The continuous alternative supplies a tested positive alignment dynamics. A physical gravitational derivation and total primitive-arrow construction count have not been obtained.
