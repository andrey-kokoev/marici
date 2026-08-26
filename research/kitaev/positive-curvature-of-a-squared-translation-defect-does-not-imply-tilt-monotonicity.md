# Positive Curvature of a Squared Translation Defect Does Not Imply Tilt Monotonicity

Let

\[
D(b)=\|T_bf-f\|^2,
\qquad
T_0=I,
\]

where \(b\mapsto T_bf\) is differentiable at zero. Writing

\[
T_bf=f+bvf+O(b^2)
\]

with \(vf=T'_0f\) gives

\[
D(b)=b^2\|vf\|^2+O(b^3).
\]

Therefore

\[
D(0)=D'(0)=0,
\qquad
D''(0)=2\|T'_0f\|^2\ge0.
\]

Positive curvature at the reflection-fixed point is automatic whenever the
infinitesimal translation is visible. Negative curvature would falsify the
claim that \(D\) is an honest differentiable squared defect, but positive
curvature does not establish global tilt monotonicity.

## Minimal exact hostile model

Take the real two-dimensional rotation group

\[
R_b=
\begin{pmatrix}
\cos b&-\sin b\\
\sin b&\cos b
\end{pmatrix}
\]

and \(f=(1,0)^T\). Then

\[
D(b)=\|R_bf-f\|^2
=2-2\cos b
=4\sin^2\frac b2.
\]

This defect is nonnegative and even, with

\[
D''(0)=2>0.
\]

But

\[
D'(b)=2\sin b,
\]

which is positive on \((0,\pi)\) and negative on \((\pi,2\pi)\). The defect
returns to zero at \(2\pi\). Thus reflection symmetry, Gram positivity, and
strict positive curvature at zero coexist with complete failure of global
monotonicity and global faithfulness.

## Spectral form of the obstruction

For a unitary translation group with spectral measure \(\mu_f\),

\[
D(b)=2\int_{\mathbb R}(1-\cos(b\xi))\,d\mu_f(\xi),
\]

and

\[
D'(b)=2\int_{\mathbb R}\xi\sin(b\xi)\,d\mu_f(\xi).
\]

The integrand changes sign after phase wraparound. If the spectral support is
bounded by \(|\xi|\le\Omega\), positivity of the integrand is automatic only
inside the local window

\[
0\le b\le\frac{\pi}{\Omega}.
\]

Global monotonicity requires a special source-derived spectral measure or a
different nonunitary semigroup structure. It does not follow from positivity
of the Gram defect.

## Completion consequence

As cutoff grows, new high-frequency support shrinks the automatic monotonicity
window. If \(\Omega_X\to\infty\), then

\[
\frac{\pi}{\Omega_X}\to0.
\]

Every finite cutoff may have positive curvature and a nontrivial local
monotonicity interval while no fixed interval survives completion. The correct
uniform audit must therefore control the full spectral sine transform or prove
a cutoff-independent no-wrap mechanism.

## Revised capability

The additive tilt mechanism needs four separate gates:

1. Honest squared-defect typing.
2. Infinitesimal visibility, \(D''(0)>0\), on the relevant quotient.
3. Global sign control, \(D'(b)\ge0\), on the required half-sector.
4. A cutoff-independent modulus or spectral theorem preserving gate 3 under
   completion.

Only the third and fourth gates carry the new RH-strength content. The first
two are local consistency and observability checks.

## Falsifiers

- A negative \(D''(0)\) for a claimed differentiable squared defect.
- A nonzero source state with \(D''(0)=0\) in the purportedly observed sector.
- A positive-curvature defect whose derivative changes sign.
- A monotonicity interval shrinking to zero with cutoff.
- Inferring global monotonicity from reflection evenness and Gram positivity.
- Importing unitary translation intuition into a nonunitary Mellin tilt without
  deriving its generator and domain.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to determine whether local curvature contains the proposed
global transport capability.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Positive curvature is automatic local visibility; global monotonicity
is exactly the nontrivial spectral no-wrap theorem.
