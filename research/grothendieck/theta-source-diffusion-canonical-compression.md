# The completed theta kernel supplies a canonical finite-rank compression

Author: `marici.Grothendieck`

## 1. Purpose

Literal finite theta-label packets cannot preserve Poisson sewing.  This
packet constructs a different finite regulator from the already completed
positive theta kernel.  It is canonical at the scalar-source level and
preserves reflection and the constant endpoint channel exactly.

It does not construct the RH Fredholm comparison.

## 2. Source Hilbert space and Dirichlet form

Let (Phi(u)>0) be the even completed theta Fourier kernel, and normalize

\[
 d\mu(u)=Z^{-1}\Phi(u)\,du,
 \qquad
 Z=\int_{\mathbb R}\Phi(u)\,du.
\]

On

\[
 \mathcal H_\Phi=L^2(\mathbb R,d\mu)
\]

consider the closed Dirichlet form

\[
 \mathcal E(f,g)=\int_{\mathbb R}f'(u)\overline{g'(u)}\,d\mu(u).
\]

Its nonnegative Friedrichs generator is formally

\[
 A_\Phi f
 =-\Phi^{-1}(\Phi f')'
 =-f''-(\log\Phi)'f'.
\]

This construction uses the completed source density itself; it introduces no
zero data and no fitted potential.

## 3. Exact structural properties

Let

\[
 (Jf)(u)=f(-u).
\]

Because (Phi) is even,

\[
 JA_\Phi=A_\Phi J.
\]

The constant endpoint mode

\[
 \Omega(u)=1
\]

belongs to (mathcal H_\Phi), has unit norm under the chosen normalization,
and satisfies

\[
 A_\Phi\Omega=0.
\]

Moreover, for the exponential feature (e_z(u)=e^{izu}),

\[
 \langle\Omega,e_z\rangle_{\mathcal H_\Phi}
 =Z^{-1}\int_{\mathbb R}\Phi(u)e^{izu}\,du.
\]

Thus the same source space contains both the endpoint mode and the completed
theta scalar readout.

## 4. Schrödinger form and compact resolvent

Put

\[
 V(u)=-\log\Phi(u).
\]

The unitary map

\[
 Uf=Z^{-1/2}\Phi^{1/2}f
\]

conjugates (A_\Phi) to

\[
 H_\Phi=-\frac{d^2}{du^2}+W_\Phi(u),
 \qquad
 W_\Phi(u)=\frac{V'(u)^2}{4}-\frac{V''(u)}2.
\]

For (u\to+\infty), the (n=1) theta summand gives

\[
 \log\Phi(u)
 =-\pi e^{2u}+\frac92u+O(1),
\]

with exponentially smaller corrections.  Evenness supplies the corresponding
estimate as (u\to-\infty).  Hence

\[
 W_\Phi(u)=\pi^2e^{4|u|}+O(e^{2|u|})
 \longrightarrow+\infty.
\]

The associated one-dimensional Schrödinger operator therefore has compact
resolvent.  Equivalently, (A_\Phi) has a discrete spectrum of finite
multiplicity accumulating only at (+\infty).

## 5. Canonical finite projections

Let (E_N) be the spectral projection onto the first (N) eigenspaces of
(A_\Phi), with complete eigenspaces retained at degeneracies.  Then

\[
 E_N^2=E_N=E_N^*,
 \qquad
 E_NJ=JE_N,
 \qquad
 E_N\Omega=\Omega,
 \qquad
 E_N\to I\ \text{strongly}.
\]

Thus (E_N) satisfies the admissibility conditions left open by the
finite-label no-go.  The construction order is

\[
 \boxed{
 \text{complete the theta source}
 \longrightarrow
 \text{form its reversible diffusion}
 \longrightarrow
 \text{take spectral compressions}.}
\]

No label cutoff occurs.

## 6. What has and has not been made canonical

The projections are canonical for the completed **scalar theta density**.
They preserve:

1. reciprocal reflection;
2. the positive source measure;
3. the constant endpoint mode; and
4. the exhaustion topology of the source Hilbert space.

They do not automatically preserve the finer prime or theta-label grading.
Consequently they are suitable for a completed scalar Fredholm comparison
only if that comparison is itself functorially determined by
((\mathcal H_\Phi,A_\Phi,J,\Omega)).  If arithmetic labels remain essential
operator data, this compression is too coarse.

This is a precise source-faithfulness gate, not a cosmetic caution.

## 7. Next coercivity calculation

The next construction should seek a comparison (T_s) on
(mathcal H_\Phi) whose determinant section is the completed readout and
whose Green identity is compatible with (A_\Phi).  Only then define

\[
 T_s^{(N)}=E_NT_sE_N\big|_{E_N\mathcal H_\Phi}.
\]

The finite coercivity reserve would be the smallest generalized eigenvalue of
the compressed energy form against

\[
 \|f\|_{\mathrm{ref}}^2
 =\|f\|_{\mathcal H_\Phi}^2+\mathcal E(f,f).
\]

The decisive limit question is whether an off-seam lower bound survives as
(N\to\infty).  Positivity at every finite (N) would not by itself answer
that question.

## 8. Hostile test

Multiplying the scalar readout by the quartet factor (P_a) leaves the source
density (Phi), and therefore (A_\Phi) and every (E_N), unchanged.  This
is useful: it proves that the regulator alone cannot protect the divisor.

Any successful (T_s) must couple to more source structure than the scalar
diffusion spectrum, or else explain why its determinant is uniquely fixed by
the full feature family (e_z).  The (P_a) test therefore remains active at
the Fredholm-construction stage.

## 9. Scope

The reversible source generator, reflection covariance, ground-state mode,
compact-resolvent conclusion, and canonical spectral exhaustion follow from
the positive even theta kernel and its tail asymptotics.  The construction is
source-derived but scalarized.  It is not yet the reciprocal Fredholm pair,
does not establish determinant convergence or off-seam coercivity, and does
not prove RH.
