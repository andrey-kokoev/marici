# Diagonal quark-flavor SU(3) anomaly completion (WP434)

## Repair of the WP433 gauge proposal

Gauging (SU(3)_Q) on the left-handed quark doublets alone has a nonzero cubic
flavor anomaly. The minimal spectator-free repair is not to add arbitrary
matter, but to gauge the diagonal quark-generation group (SU(3)_F) acting on

$$
Q_L\mapsto UQ_L,
\qquad
u_R\mapsto Uu_R,
\qquad
d_R\mapsto Ud_R.
$$

This is a new physical gauge theory over the diagonal subgroup of the original
weak-basis product. It changes the physical groupoid and must not be treated as
a gauge fixing of the Standard Model flavor quotient.

## Exact anomaly cancellation

Write all fermions as left-handed Weyl fields. The flavor representations and
multiplicities are:

- (Q_L): six fundamentals from three colors and two weak components;
- (u_R^c): three antifundamentals;
- (d_R^c): three antifundamentals.

With fundamental cubic anomaly normalized to (+1), the local
(SU(3)_F^3) anomaly is

$$
6-3-3=0.
$$

For the mixed (SU(3)_F^2U(1)_Y) anomaly, fundamentals and
antifundamentals have the same quadratic index. Omitting the common positive
index factor, the hypercharge-weighted sum is

$$
6\left(\frac16\right)
+3\left(-\frac23\right)
+3\left(\frac13\right)=0.
$$

Mixed anomalies with one flavor generator and two Standard Model nonabelian or
hypercharge generators vanish because every (SU(3)_F) generator is traceless.
The diagonal completion therefore needs no anomaly-canceling spectator fermions.

## Compatibility with the adjoint span

Under the diagonal action the Yukawa maps transform by conjugation,

$$
Y_u\mapsto UY_uU^\dagger,
\qquad
Y_d\mapsto UY_dU^\dagger.
$$

Their Hermitian Gram operators (H_u=Y_uY_u^\dagger) and
(H_d=Y_dY_d^\dagger) are adjoints of the same gauged group. Thus the WP433
commutator mass Gram applies directly to a diagonal (SU(3)_F) realization.
The generic two-adjoint benchmark gives eight massive gauge directions without
the central (U(1)) defect because the gauged group is (SU(3)), not (U(3)).

## What this establishes

WP434 removes the arbitrary-spectator objection and supplies an anomaly-free
gauge grammar for WP433's constructive spectral shape. This is genuine progress:
the matter content is fixed by the observed quark sector rather than appended
to cancel the desired anomaly.

It does not yet establish a physical selector. The theory still requires:

- a dynamical origin for the adjoint Yukawa/flavon fields;
- a source-selected vacuum and absolute scale (g_F f/v);
- consistency of the diagonal gauging with the full Yukawa interactions;
- bounds and instruments for the resulting flavor-changing gauge currents;
- a threshold packet with independently frozen widths and residues.

The smallest exact falsifier is a nonzero (SU(3)_F^3) or
(SU(3)_F^2U(1)_Y) coefficient for the declared quark content. A different
chiral charge assignment is a different theory and must repeat the audit.

Run `uv run --with sympy python
research/flavor/checkers/wp434_diagonal_su3_anomaly_completion.py` to regenerate
the JSON result.
