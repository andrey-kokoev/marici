# Theta prime-shift defect is a full-rank Hankel boundary window

## Bounded question

Does replacing the failed finite boundary jet by the complete moving-cut
history produce the missing oscillator--seam coupling?

## The history synthesis

For a positive cut (q), retain

\[
h_q(t)=\mathbf 1_{0\le t\le q}\Phi(q-t).
\]

For a finite packet (c=\sum_jc_j\delta_{q_j}), define

\[
(Hc)(t)=\sum_jc_jh_{q_j}(t).
\]

The full seam Gram is (H^*H). Distinct cuts give linearly independent
atoms, so this history port has the cutoff-growing rank that every fixed jet
lacks.

## Bilateral covariance and the half-line defect

Without the physical boundary (t=0), the kernel depends only on (q-t) and
intertwines cut translation with observation translation. Let (T_L) send
(q) to (q+L), and let

\[
(\tau_Lf)(t)=\mathbf 1_{t\ge L}f(t-L)
\]

be the unilateral shift. Direct subtraction gives

\[
(HT_L-\tau_LH)c(t)
=\mathbf 1_{0\le t<L}
\sum_jc_j\Phi(q_j+L-t).
\]

Thus the prime-shift defect is neither a bulk term nor a two-coordinate
endpoint jet. It is a complete boundary window of width (L).

## Toeplitz-to-Hankel rotation

Put (u=L-t). On (0<u\le L), the defect becomes

\[
(R_Lc)(u)=\sum_jc_j\Phi(q_j+u).
\]

The seam history uses the difference coordinate (q-t); the boundary defect
uses the sum coordinate (q+u). Half-line compression therefore rotates a
translation-covariant Toeplitz kernel into a Hankel kernel.

This is the first source-derived operation in the current lane that both:

- breaks common prime-shift covariance through the physical origin;
- retains a function-valued output whose rank can grow with the cutoff.

The operator is source-native: its interval length is (L=log p), and its
kernel is the unchanged completed theta source.

## Rank of the boundary window

For distinct positive cuts (q_1,ldots,q_N), the window columns are

\[
u\longmapsto\Phi(q_j+u),
\qquad 0<u<L.
\]

If a finite combination vanishes on this interval, analyticity makes it vanish
on the connected continuation domain. For the theta source, whose exponential
rates are distinct, uniqueness of the resulting exponential series forces all
coefficients to vanish. Hence every finite family of distinct translated
columns is linearly independent.

Therefore the boundary-window Gram

\[
B_{L,X}(i,j)=\int_0^L
\Phi(q_i+u)\Phi(q_j+u)\,du
\]

has rank (N), not rank two. Nima's finite-jet obstruction is avoided because
the commutator codomain is the whole window (L^2(0,L)).

## Exact remaining sign question

Full rank is not domination. The live comparison is whether the source-weighted
Hankel-window Gram controls the prime-resolved seam Gram with the coefficient
required by the doubled Green identity. At a finite cutoff (X), the sharp
quantity is the smallest generalized eigenvalue of

\[
B_{L,X}v=\lambda K_Xv.
\]

The route fails uniformly if these eigenvalues tend to zero along increasing
prime-power blocks. It advances if the von Mangoldt-weighted window has a
source-derived lower bound in the completed packet topology.

## Single-atom completion obstruction

The uniform comparison already fails on one column translated to infinity.
For a cut (q), its seam norm is

\[
\|h_q\|^2
=\int_0^q|\Phi(v)|^2\,dv
\longrightarrow\|\Phi\|_{L^2(0,\infty)}^2>0.
\]

Its boundary-window norm is

\[
\|R_L\delta_q\|^2
=\int_0^L|\Phi(q+u)|^2\,du
\longrightarrow0.
\]

Consequently

\[
\frac{B_L(q,q)}{K(q,q)}\longrightarrow0.
\]

The smallest generalized eigenvalue is at most this diagonal Rayleigh
quotient, so no cutoff-uniform positive lower bound can hold. A static
von Mangoldt factor (L=\log p) does not change the conclusion along the
(p)-power orbit (q=kL\to\infty).

Thus the Hankel boundary window is injective at every finite cutoff but loses
all quantitative control at completion. This is the same distinction seen in
the broader programme: algebraic faithfulness is weaker than a stable decoder.

## Interpretation

The fixed origin is not a finite sensor. Under a finite prime displacement it
emits the entire history swept across the boundary. This reconciles the rank
requirements at every finite cutoff:

- moving history supplies faithful rank;
- half-line incidence supplies noncommutation.

But it does not reconcile completion stability. The window remains fixed near
the origin while the seam state travels outward. A surviving coupling must
transport the observation window with the state and simultaneously break the
resulting translation covariance. Reciprocal modular sewing is the remaining
source-native candidate because it can return a distant cut to the fixed seam
without replacing history by a finite trace.

## Scope

This packet derives the exact prime-shift defect, proves finite-cutoff
injectivity of its theta translate columns, and disproves uniform domination
of the seam Gram by the fixed-origin boundary window. It does not compute a
reciprocal-sewing repair, determine the Green-identity coefficient, close the
Evans determinant bridge, or prove RH.
