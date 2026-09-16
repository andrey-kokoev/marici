# Correction: resolved-graph covariance is already closed, and the frontier is the theta-zero to ordered-flux intertwiner

## Audit result

The proposed next step of proving seam transport covariance for the resolved three-port graph has already been completed in prior research.

For the seam reassembly transport \(T_{b\leftarrow a}\), the established identity is

\[
\mathcal R_bT_{b\leftarrow a}
=
T_{b\leftarrow a}^{\oplus3}\mathcal R_a,
\]

where

\[
\mathcal R_a f=(f,B_af,M_\Phi f).
\]

Consequently

\[
T_{b\leftarrow a}^*
\left[(1+M_\Phi^2)I+B_b^*B_b\right]
T_{b\leftarrow a}
=
(1+M_\Phi^2)I+B_a^*B_a
\]

on the transported graph domain and after closure.

The endpoint observer is separately natural under the same seam transport. Equality of the endpoint metric and resolved graph metric is neither true nor required.

Primary references:

- `research/nima/reassembly-conjugation-closes-the-resolved-graph-under-moving-seam-transport.md`
- `research/voevodsky/prior_research_moves_gate_to_ordered_bulk_polarization_20260908.md`

## External flux is also closed

The anti-diagonal zero-trace identity already proves cancellation of the typed external flux:

\[
\mathfrak b_\partial^+
-
\mathfrak b_\partial^-
+
\mathfrak F_B
=0.
\]

Thus endpoint attachment and external boundary cancellation are not the remaining obstruction.

## Ordered bulk polarization

The unresolved oriented quantity is

\[
\mathcal C_z(K)=\langle DK,zK\rangle.
\]

Define reciprocal face states

\[
x_+=(D+z)K,
\qquad
x_-=(D-z)K.
\]

Then

\[
\|x_+\|^2-
\|x_-\|^2
=
4\operatorname{Re}
\langle DK,zK\rangle.
\]

The ordered instrument therefore exists algebraically. Its missing datum is source transport from the completed theta zero-state.

## Conditional positive-mode factorization

For a positive exponential resolvent packet, prior work gives

\[
\Delta_{\rm face}
=
2a
\left[
|K_z(0)|^2-4t^2S_z
\right],
\qquad
z=a+it,
\]

and

\[
|K_z(0)|^2-4t^2S_z
=
X_z^2+Y_z^2.
\]

For \(t\ne0\), the positive-mode assumptions imply \(Y_z\ne0\). Under those assumptions, vanishing face flux forces \(a=0\).

## Exact missing bridge

Two statements remain unproved:

1. a completed theta zero produces zero total ordered face flux for the same state \(K_z\);
2. the differentiated completed theta source belongs to the positive exponential-mode cone used in the sum-of-squares factorization.

The first missing typed object is an intertwiner

\[
J_{\theta\to\rm face}
\]

from the completed theta zero-section to the ordered face-flux instrument, satisfying

\[
\Theta(z)=0
\quad\Longrightarrow\quad
\Delta_{\rm face}(J_{\theta\to\rm face}\Theta_z)=0.
\]

The state on the right must be the same source-constructed state used by the positive-mode factorization. Choosing it after imposing zero flux would be circular.

## Consequence

The current frontier is not:

- Fourier sewing;
- resolved graph covariance;
- endpoint attachment;
- external flux cancellation;
- prime-cell metric rigidity.

Those structures terminate before the common-state identification needed by the ordered face argument.

## Next admissible construction

Start from the differentiated theta summands

\[
\left(
4\pi^2n^4e^{9u/2}
-
6\pi n^2e^{5u/2}
\right)

e^{-\pi n^2e^{2u}}.
\]

The next test is to determine whether each summand, or a source-fixed grouped packet of summands, admits the positive exponential resolvent representation required for \(K_z(0),S_z,X_z,Y_z\).

A negative coefficient in every admissible grouped representation rejects the positive-mode bridge. A valid representation supplies the common state needed for the theta-zero to flux implication.

## Disposition

The resolved metric and its seam covariance are already constructed. The exact open construction is the common-state intertwiner between the completed theta zero and the ordered positive-mode flux instrument.
