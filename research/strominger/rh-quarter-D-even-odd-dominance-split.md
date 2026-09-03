# D dominance by parity sectors

## Question

Can the dominance coefficients be proved nonnegative by treating the even and odd modulus-square differences separately?

## Claim boundary

No. In every tested depth/shift pair, both parity-sector differences already have a negative coefficient at internal index 1. Their shifted sum remains coefficientwise nonnegative by the established total-dominance result. This rejects paritywise positivity but does not reject an adjacent even/odd minor identity. The governing DPC case remains `rh-quarter-D-imaginary-axis-dominance.md`.

## Disposition

Cancellation between parity sectors is essential. Since

\[
[\omega^{2k}](|P|^2-|R|^2)=E_k+O_{k-1},
\]

the next proof target is an adjacent-index inequality `E_k >= -O_{k-1}` and its expression as a Hermite–Biehler or Hurwitz minor. Separate Toeplitz positivity of `E` and `O` is rejected.
