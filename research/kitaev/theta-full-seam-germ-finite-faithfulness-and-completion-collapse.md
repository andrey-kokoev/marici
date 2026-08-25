# The full theta seam germ is finitely faithful but not uniformly separated

Owner: `marici.Kitaev`

## Bounded question

Does Grothendieck's complete seam-germ detector

\[
\mathcal G_Q(c)(t)=\sum_{j=1}^n c_j\Phi(t+q_j)
\]

separate every finite packet of distinct labels, and does that separation
remain uniform as the arithmetic cutoff grows?

## Finite translate theorem

Assume that \(\Phi\) is a nonzero real-analytic (L^1(\mathbb R)\) profile
and that (q_1,\ldots,q_n\) are distinct real labels. If the seam germ of
\(\mathcal G_Q(c)\) vanishes on a nonempty open interval, real analyticity
extends the identity to all of \(\mathbb R\). Fourier transformation gives

\[
\widehat\Phi(\xi)
\sum_{j=1}^n c_j e^{iq_j\xi}=0.
\]

Because \(\Phi\ne0\), its continuous Fourier transform is nonzero on some
open interval. Hence the exponential polynomial

\[
P(\xi)=\sum_jc_je^{iq_j\xi}
\]

vanishes there. Its first (n\) derivatives at one point give

\[
\sum_j c_j(iq_j)^k=0,qquad 0\le k<n.
\]

The coefficient matrix is Vandermonde, with determinant

\[
i^{n(n-1)/2}\prod_{j<k}(q_k-q_j)\ne0.
\]

Therefore every (c_j=0\). The full seam germ, equivalently the complete
Cauchy-jet tower, is jointly faithful on every finite set of distinct labels.

This theorem applies to the analytic rapidly decreasing theta profile used by
the source programme. It requires distinct labels after all source
identifications; duplicate labels must be combined before applying it.

## Minimal jet depth at fixed cutoff

The proof uses at most the first (n\) Fourier-side derivatives of the
exponential polynomial, not necessarily the first (n\) physical seam jets.
For a particular profile and label packet, finite physical-jet faithfulness is
the rank of

\[
J_{k,j}=\Phi^{(k)}(q_j).
\]

The complete jet tower is faithful, so some finite minor is nonzero for every
fixed packet. The location of that minor need not be uniformly bounded by a
cutoff-independent jet depth.

## Completion-stability obstruction

Translation is strongly continuous in every ordinary (L^2\) or Schwartz
topology. If distinct labels (q_m,r_m\) satisfy

\[
|q_m-r_m|\to0,
\]

then the normalized raw coefficient packets

\[
c_m=2^{-1/2}(e_{q_m}-e_{r_m})
\]

have coefficient norm one while

\[
\|\mathcal G(c_m)\|
=2^{-1/2}\|\Phi(\cdot+q_m)-\Phi(\cdot+r_m)\|\to0.
\]

Arithmetic logarithmic labels have arbitrarily close spacings at large scale;
for example consecutive prime logarithms satisfy
\(\log p_{m+1}-\log p_m\to0\). Thus no cutoff-independent lower bound exists
for the germ synthesis map when the source is equipped with the raw labelled
\(\ell^2\) coefficient norm.

For the Gaussian control profile, the exact full-line formula is

\[
\|g_{q+\delta}-g_q\|_2^2
=2\sqrt{\pi/2}\,(1-e^{-\delta^2/2})\to0.
\]

This is an explicit completion-collapse hostile family despite finite
injectivity at every cutoff.

## Interpretation

The detector hierarchy is now:

- scalar endpoint: unfaithful already for two labels;
- complete seam germ: faithful on every fixed finite labelled packet;
- raw-coefficient completion: not uniformly observable when label spacings
  collapse;
- constructor/pro-Gram completion: may restore continuity by defining the
  source topology through the translated features, but then a separate energy
  lower bound is still required for RH force.

Thus the full germ repairs finite distinguishability, not completion-stable
observability.

## Falsifiers and assumptions

- Repeated labels make the Vandermonde determinant zero and must be quotient-
  typed first.
- A merely smooth, nonanalytic profile does not allow continuation from a
  one-sided germ to the whole line without an additional unique-continuation
  theorem.
- A profile whose Fourier transform is treated only distributionally requires
  a revised proof.
- A source admissibility constraint could exclude the adjacent-difference
  packets; such an exclusion must be derived from the dynamics, not imposed to
  rescue a lower bound.

## Claim strength

Finite-packet theorem plus a raw-coefficient completion obstruction. It does
not prove failure in a different constructor-generated source topology and
does not constrain Riemann zeros.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_full_seam_germ_faithfulness.py`.
The result is written to
`research/kitaev/results/theta-full-seam-germ-faithfulness.json`.
