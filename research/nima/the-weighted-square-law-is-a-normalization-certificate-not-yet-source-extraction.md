# The weighted square law is a normalization certificate, not yet a source extraction

## Current logical status

The weighted family

\[
D_{p,\pm}(\lambda_p,\mu_p,\alpha_p)
=
\frac12
\left(
\lambda_p I+|\alpha_p|^2H^{*}H
\right)
\pm
\frac{i\mu_p\alpha_p}{2}
\left(
H-H^{*}
\right)
\]

has a clean algebraic positivity theory. In the matched real-sign convention,

\[
|\mu_p|=\sqrt{\lambda_p}
\]

produces an exact shifted-history square after placing \(\alpha_p\) consistently.

But the source programme has not yet derived this equality. It has only identified candidate ingredients:

- the coefficient-wall residue whose representation is expected to be \(I\);
- the full seam-history Gram \(H^{*}H\);
- causal oddness \(H-H^{*}\);
- Euler and prime weights.

Therefore the normalization gauge is closed conditionally, not yet constructively.

## Three equalities that must be proved

A source square theorem must establish one commuting diagram with all coefficients:

1. wall representation:
   \[
   \pi(R_{\mathrm{wall},p})
   =
   \lambda_p I;
   \]
2. seam Gram representation:
   \[
   \pi(G_{\mathrm{seam},p})
   =
   |\alpha_p|^2H^{*}H;
   \]
3. oriented history representation:
   \[
   \pi(J_{\mathrm{odd},p})
   =
   \mu_p\alpha_p\,i(H-H^{*}).
   \]

Only then can one test whether the coefficients satisfy the square-law relation needed for one Gram factorization.

Matching scalar endpoint values does not prove these operator identities.

## Exact versus sufficient history ratio

Define

\[
\kappa_p^{(1)}
=
\frac{|\alpha_p|M_\Phi}{\sqrt{\lambda_p}}.
\]

This is a source-simple sufficient loading ratio because

\[
\|H\|\le M_\Phi.
\]

The exact operator ratio is

\[
\kappa_p^{\mathrm{op}}
=
\frac{|\alpha_p|\|H\|}{\sqrt{\lambda_p}}.
\]

For the full half-line convolution with nonnegative kernel, one expects equality

\[
\|H\|=M_\Phi
\]

by approximate constant packets translated away from the boundary. But finite cutoffs satisfy only \(\|H_L\|\le M_\Phi\), and the equality or convergence statement must be proved in the declared topology.

Thus \(\kappa_p^{(1)}<1\) is a robust sufficient theorem, not automatically the exact margin at every finite stage.

## Gauge behavior

Under auxiliary retyping

\[
I\mapsto r_p^2 I,
\qquad
H\mapsto r_p H,
\]

the three coefficients transform together. The ratio \(\kappa_p\) may remain invariant while the absolute lower scale changes. The exact square law fixes this retyping only if the wall, history Gram, and odd incidence are all images of one source constructor.

If they are assembled from separately normalized packets, equality \(|\mu_p|=\sqrt{\lambda_p}\) can be imposed after the fact and has no authority.

## Minimal source falsifiers

1. The wall residue represents \(2I\), while the seam and odd packets retain unit normalization.
2. The odd current has the correct scalar Euler value but represents a proper compression of \(i(H-H^{*})\).
3. Prime weight \(\alpha_p\) appears quadratically in the seam Gram but is omitted from the odd incidence.
4. The square law holds at every finite prime after a cutoff-dependent rephasing, but no compatible completed frame exists.

## Correct status hierarchy

The current hierarchy is:

\[
\text{source coefficient extraction}
\longrightarrow
\text{square-law verification}
\longrightarrow
\text{fixed normalization frame}
\longrightarrow
\kappa_p<1
\longrightarrow
\text{auxiliary coercivity}.
\]

We have proved the implications after square-law verification. The first two arrows remain open.

## Next packet

Construct the coefficient-space wall/history/odd block before analytic representation, apply the representation functor to the complete block, and read off

\[
(\lambda_p,\mu_p,\alpha_p)
\]

without rephasing. The decisive output is whether the represented block is literally a shifted-history Gram or only a positive form with unrelated coefficients.
