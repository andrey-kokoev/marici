# The full rotor phase lift fixes its angular constant conditionally

Active SCC obligation: attachment transport, including comparison, reversal and
readout descent. This continues `retained-rotor-generator.md` using its declared
real Clifford realization and symplectic form. It does not silently promote the
ambient analytic enlargement to a native-source theorem.

## Types and the additional compatibility condition

The base is the same algebra carrier Q=s+q*e1+p*e2+z*J. The retained rotor is
U(theta)=cos(theta)+J*sin(theta). Its adjoint action rotates (q,p) through twice
the angle and fixes s,z.

Use the existing matrices' defining real module R^2 as the phase fiber. Write a
fiber vector as w=u+i*v, with i the scalar complex coordinate on that real plane;
it is not a claim that J is central in the Clifford algebra. The matrices act as

\[
e_1w=\overline w,\qquad e_2w=i\overline w,
\qquad U(\theta)w=e^{-i\theta}w.
\]

Odd elements act anti-linearly in this complex coordinate. Their underlying
maps remain real-linear. Unit fiber vectors define a phase circle. Full retained
histories, including winding, remain separate from this lossy fiber reading.

Compatibility means that the fiber action must extend the ALREADY SPECIFIED
real matrix action, rather than merely agree with its finite group samples.
This is an explicit requirement of this realization, not a result inferred from
abstract phase retention or all native higher-source witnesses.

## Construct and classify the phase transport

Let kappa be a positive, uncalibrated action-phase scale. Define

\[
F(Q)=\frac{qp+sz}{2},\qquad
\beta=p\,dq+s\,dz,\qquad
\alpha=d\varphi-\beta/\kappa.
\]

The symmetric primitive beta-dF is preserved by even rotors and reversed by
odd elements. If psi is the defining-module fiber angle, use the phase chart
phi=psi+F/kappa. It follows, rather than being fitted at the return point, that

\[
\widetilde U_\theta(Q,\varphi)=
\left(T_\theta Q,\,
\varphi+\frac{F(T_\theta Q)-F(Q)}{\kappa}-\theta\right).
\]

Phase coordinates are modulo 2*pi; real angle lifts used in calculations carry
separate history/winding information. Here T is the adjoint action. This formula
preserves alpha and composes for arbitrary angles by telescoping the F terms.

More generally write a Pin element as g=U(theta)*e1^e, with e=0 or 1, and let
orientation=(-1)^e. The full lift is

\[
\widetilde g(Q,\varphi)=
\left(\operatorname{Ad}_g Q,\,
(-1)^e\varphi+
\frac{F(\operatorname{Ad}_g Q)-(-1)^eF(Q)}{\kappa}-\theta\right).
\]

It pulls alpha back to orientation*alpha. Composition uses
(theta,e)*(eta,d)=(theta+orientation*eta,e XOR d). The checker verifies all four
parity combinations with symbolic angles, inverses, and signed connection
preservation. In particular e1 sends phi to -phi, while e2 sends it to
-phi+pi/2. Their two orders retain the original opposite J lifts.

For completeness, fixing this base action and connection determines a rotor
lift up to a spatially constant circle character. Continuity and the group law
make its angular part -k*theta with integer k. Matching all existing finite
matrix samples fixes only k=1 modulo 4. Weight five passes those finite samples.
But weight five fails the real-linear matrix identity
U(theta)=cos(theta)*1+sin(theta)*J at theta=pi/4. Requiring the declared defining
module fixes weight ONE on the whole circle. The finite-group test by itself
would not have selected it.

## Generator and action

Differentiating the constructed lift gives

\[
q'=2p,\quad p'=-2q,\quad s'=z'=0,
\qquad \varphi'=(p^2-q^2)/\kappa-1.
\]

Consequently the Hamiltonian normalized by this phase connection is

\[
H^+=-\kappa\alpha(\widetilde D)=q^2+p^2+\kappa.
\]

The old base generator determined H=q^2+p^2+C only up to C. The specified
module-compatible phase lift fixes C=kappa in the chosen conventions. This is
not a new force: the trajectories remain unchanged. Nor is it a derived
physical zero-point energy, a value of hbar, or a time calibration.

On a trajectory the earlier zero-offset action satisfies
S0=F(final)-F(initial). The complete phase is equivalently

\[
\exp(iS_0/\kappa)e^{-i\theta}
=\exp\bigl(i(S_0-\kappa\theta)/\kappa\bigr).
\]

Thus one may retain the module transport separately or absorb it into the
constant of the action. Adding BOTH corrections would double-count it and
incorrectly give +1 at the full adjoint period theta=pi. The correct phase is
-1 there, and the half-period phases represent J and -J as -i and +i in the
specified module coordinate.

## HJ charts through the projection caustics

Let qi,pi denote the initial canonical coordinates. The type-I action is

\[
S^+(q,q_i,\theta)=
\frac{(q^2+q_i^2)\cos(2\theta)-2qq_i}{2\sin(2\theta)}
-\kappa\theta.
\]

It requires sin(2*theta) nonzero. A mixed, type-II generating function is

\[
G^+(q,p_i,\theta)=
\frac{qp_i}{\cos(2\theta)}
-\frac{q^2+p_i^2}{2}\tan(2\theta)-\kappa\theta.
\]

It requires cos(2*theta) nonzero. These domains cover every angular time. On
the overlap, qi=(q-pi*sin(2*theta))/cos(2*theta), and

\[
G^+=S^++p_iq_i.
\]

That is the exact initial-endpoint Legendre boundary term, not an identification
of unequal action values. Both local functions satisfy, in their respective
fixed-initial-data charts,

\[
\partial_\theta A+(\partial_q A)^2+q^2+\kappa=0.
\]

At theta=n*pi/2 the mixed chart is regular and gives
G^+=(-1)^n*q*pi-kappa*n*pi/2. Keeping its initial-boundary term recovers the
retained fiber phase, without dropping momentum at a position-projection
caustic. The full phase-space transformation is smooth for all angles.

This constructs two classical generating-function charts and their comparison.
It does not derive a position-space quantum propagator, its amplitude, a Maslov
half-density prescription, or all native higher-source cells.

## Outcome and continuation

The conditional rotor-sector phase lift now preserves composition, inverse,
both elementary reversers and the retained signs, and has regular HJ chart
comparisons across the position-projection caustics. The selection of weight
one comes from the declared real defining module, not merely from the sign at
one period.

The next local question is a clock on full rotor/reversal histories. Angle is
periodic in the lift, its action has a shorter period, and odd developments
reverse orientation. An ordinary additive scalar clock on their endpoint group
may fail; retaining an unwrapped, orientation-dependent history coordinate must
be tested. The independent native analytic-enlargement audit remains open.

Closing reconciliation: Voevodsky's
`source-algebra-selection-boundary.md` gives two dimension-free inner crossed
products for the same source action, and identifies the missing
response-to-implementer selection map. Its formal root and center-dimension
calculations were not rerun here. An independent counting-metric control here
confirms Gram matrix diag(1,2,2,4) on the native active basis, not the identity
Clifford Gram. Using that counting metric directly with left multiplication by
J does not even give the skew form used above. This does not select counting
norm as physical; it prevents silently treating our supplied metric and defining
module as source-inherited. The constant selection in this note is explicitly
conditional on those choices.

Verification:

```text
uv run --with sympy python research/aspect/scc/scc.py check nima-retained-rotor-phase-transport
```

The exact symbolic checker also rejects weight-five finite-sample overfitting
and double-counted return phase. Receipt:
`results/retained-rotor-phase-transport.json`. No fresh Agda or quantum-physical
verification is claimed.
