# Function-valued three-prime Clark attachment

## Construction

Use the weighted source space from the Clark receiver domain. For a chamber vector v, form the shell forcing `f_v` and its four tail traces `h_v(z)` in canonical order `(+,0),(-,0),(+,1),(-,1)`. Define the feature

    L(v)(z,t)=h_v(z) exp(i z t)

on an open upper-half-plane region Omega times the positive t-axis.

The three-prime typed source receiver is lifted by applying L independently to each retained event slot. A marked word with retained event features `g_1,...,g_r` is sent to the ordered tensor feature `L(g_1) tensor ... tensor L(g_r)`, while forgotten events retain their source arrow and contribute the vacuum record. Intermediate arithmetic vertices and all cut labels remain in direct-sum blocks.

The conormal and product maps lift pointwise:

- `j_1` sends a source conormal relation to its single-seam path derivative;
- `j_2` sends a product relation to the tensor of its two local seam derivatives;
- the shifted connecting comparison is `Theta=iota[1] pi`.

The source-derived product image is therefore carried into the function-valued joint seam target without using a finite spectral rank surrogate.

## Faithfulness argument

The source shell map is injective by the existing entire/Fourier uniqueness theorem. If `L(v)=0` on Omega times the t-axis, the zeroth tail trace vanishes on the open spectral region. Compact shell support makes that trace entire in z, so it vanishes identically. Fourier uniqueness gives `f_v=0`, and disjoint shell supports give `v=0`.

Tensor powers and typed direct sums preserve this injectivity. Hence the full three-prime joint marked source, including its 48 source columns, is faithfully represented on the function-valued carrier. The finite rank-12 point-sampling experiment is not used in this proof.

## Green comparison

The signed Clark pairing is retained before spectral aggregation. For feature vectors at w and z its kernel is

    <h_u(w) k_w, (C tensor I) h_v(z) k_z>
      = h_u(w)^* C h_v(z) / [-i(z-conjugate(w))].

For finite packets, sum these pairwise entries over spectral indices. Do not divide an aggregated numerator by one common denominator. The forcing reservoir uses the coefficient sums in each packet slot, as required by polarization.

The comparison target for the relation attachment is the restriction of this pairing to the source-generated images of the shifted `j_1`/`j_2` complex. The source attachment and its shift are already exact; the remaining analytical statement is equality with the independently sewn arithmetic Green kernel on this restricted image.

## Boundary

This construction establishes the correct function-valued analytical carrier and its source-side faithfulness conditional on the declared weighted forcing domain. It does not yet prove a uniform lower bound for the completed prime-packet tower, positivity of the signed Clark form, or a terminal invariant Green metric. The finite numerical evaluator is only a regression adapter.
