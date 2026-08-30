# The Jacobi source orbit supplies its own uniform positive heat sub-time

## Scope

The positive-time estimate for the derivative-comb observer was previously
conditional on retaining an intermediate heat-history energy. On the
source Jacobi orbit that intermediate state is already part of the same
two-parameter carrier.

Let

\[
\Theta_r(z)=\Theta(z,r)
=\sum_{n\in\mathbb Z}e^{-\pi r(n+z)^2},
\qquad r>0.
\]

The heat semigroup satisfies

\[
\Theta_r=P_\tau\Theta_{r-\tau}
\]

whenever \(0<\tau<r\).

## Uniform factorization on compact scale regions

Fix a compact region

\[
K=[r_-,r_+]\subset(0,\infty)
\]

and choose

\[
\tau_K=\frac{r_-}{2}.
\]

For every \(r\in K\),

\[
\Theta_r=P_{\tau_K}\Theta_{r-\tau_K},
\qquad
r-\tau_K\ge\frac{r_-}{2}>0.
\]

Thus the preimage is another source Jacobi section, not an arbitrary
backward-heat reconstruction. All spatial derivatives commute with
\(P_{\tau_K}\), so the first- and fifth-order odd front jets inherit the
same fixed smoothing time.

The derivative-comb estimate therefore gives

\[
|O(P_{\tau_K}f)|^2
\le
C(\tau_K)\,
\mathcal E(P_{\tau_K/2}f),
\qquad
C(\tau_K)
=
\sum_{n\ne0}e^{-\pi\tau_K n^2}.
\]

Applied to the source jet with \(f=J_{\mathrm{odd}}(r-\tau_K)\), the
midpoint state is again on the Jacobi heat history. Hence the required
midpoint energy is source-derived and retained by the full heat carrier.

## Consequences

On every compact positive-scale region:

1. the odd derivative-comb contraction is bounded in the source heat-history
   graph norm;
2. the bound is uniform in \(r\);
3. prime idempotents and cutoff truncations commute with the factorization,
   because heat propagation acts only in the Jacobi factor;
4. no arbitrary sixth-order ambient Sobolev completion is required for the
   source-generated orbit.

The bound degenerates as \(r_-\downarrow0\). The reciprocal Poisson chart
must cover that end; no direct-chart uniformity through \(r=0\) is claimed.

## Seam qualification

This closes upper boundedness, not scalar faithfulness. Reciprocal symmetry
still forces

\[
\Phi'(0)=0.
\]

Therefore a scalar odd lower frame bound cannot hold on a set containing the
seam. The completed observer must retain the normal jet there, or use a jointly
faithful even-odd port.

## Remaining Adams gate

The even and odd Jacobi channels now each have source-derived compact-region
upper control. The unresolved local theorem is their assembly into one
relative Green block with:

- the Wronskian wall boundary class;
- the oriented seam normal jet;
- endpoint loading;
- radical descent for the complete block;
- and a lower bound for the joint observer in the correctly weighted frame.

No global Adams edge or coercivity theorem follows from upper boundedness
alone.
