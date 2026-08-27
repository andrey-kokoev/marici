# Bulk-localization spectral-index fiber: WP754

## Question

Does the existing anomaly-compatible flavor representation packet determine
the positive signed spectral index required by WP753?

## Spectral counting rule

For the massless Scherk–Schwarz system used in WP753, the one-loop coefficient
is proportional to

\[
\kappa=2+N_V-N_H.
\]

Here \(N_V\) and \(N_H\) are degree-weighted bulk vector and hypermultiplet
counts. This is the coefficient in the one-loop potential derived by
[von Gersdorff, Quiros, and Riotto](https://arxiv.org/abs/hep-th/0204041).

For

\[
SU(3)_c\times SU(2)_A\times SU(2)_B\times U(1)_Y,
\]

the bulk gauge multiplicity is

\[
N_V=8+3+3+1=15.
\]

## Two lifts of the same four-dimensional grammar

The bifundamental link has degree-weighted hypermultiplet count \(4\). If only
the link and gauge sector propagate in the bulk while \(L,H,\Psi_R\) are
boundary fields, then

\[
\kappa_{\mathrm{link}}=2+15-4=13>0.
\]

This lift selects the half twist.

On the \(S^1/Z_2\) orbifold, a 5D hypermultiplet decomposes into two 4D chiral
multiplets with opposite parities, so only one member has a zero mode. A 4D
vectorlike zero-mode pair therefore requires two 5D hypermultiplets. This
orbifold counting is explicit in the 4D-superfield construction of
[Marti and Pomarol](https://arxiv.org/abs/hep-th/0106256).

The source-required portal operands contribute

\[
N_H(L,H,\Psi_R)=3(2)+2+3(2)(2)(2)=32.
\]

Putting the same fields in the bulk together with the link gives

\[
\kappa_{\mathrm{portal}}=2+15-(4+32)=-19<0.
\]

This lift selects the zero twist. The four-dimensional gauge representations
and zero-mode interaction grammar have not changed; only their
bulk-versus-boundary realization has.

Including the WP738 vectorlike quark and lepton mediators in the bulk adds
\(36+12\) hypermultiplet degrees and gives

\[
\kappa_{\mathrm{mediated}}=-67.
\]

## Disposition

The currently admitted four-dimensional flavor packet does not determine a
five-dimensional spectral sign. It supplies neither a unique bulk lift nor a
five-dimensional anomaly-inflow condition selecting one. Consequently WP753
cannot yet be promoted from conditional theorem to physical source selector.

This is not a failure of the radiative mechanism. It identifies the missing
constructor: a five-dimensional locality and anomaly-inflow principle must
derive which multiplets are bulk, which are boundary, and which Chern–Simons
or boundary states accompany them. Only then is \(\kappa\) an authorized
source output.

The smallest exact falsifier is the relocation of the already required
\(L,H,\Psi_R\) packet. It changes \(\kappa\) from \(13\) to \(-19\) and reverses
the full-tower endpoint ordering.

## Claim boundary

The count uses massless degree-weighted multiplets. Bulk masses and multiple
twist charges replace the single integer index by a weighted spectral measure.
Five-dimensional anomaly completion may forbid one or both witness lifts, but
that completion is not currently present and cannot be inferred from
four-dimensional anomaly cancellation.

The gauge fixed point, radion stabilization, boundary counterterms, threshold
accessibility, physical16 descent, and calibrated instrument remain open.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp754_bulk_localization_spectral_index_fiber.py

Generated result:
research/flavor/results/wp754_bulk_localization_spectral_index_fiber.json
