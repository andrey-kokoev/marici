# Real-sign relations for all polygon sizes

## Question

How many independent real-sign constraints remain after quotienting triangulation coefficients by labelled facet signs?

## Claim boundary

The theorem follows from the integer incidence Smith theorem. It classifies sign factorability, not source coefficient values or provenance.

For an `n`-gon let

\[
d=n-3,\qquad F=\frac{n(n-3)}2,
\]

and let the number of triangulations be the Catalan number `C_(n-2)`. The incidence Smith invariants are `F-1` copies of one and one copy of `d`. Reducing modulo two gives rank `F` when `d` is odd and `F-1` when `d` is even.

Therefore the number of independent sign relations is `C_(n-2)-F` for even `n`, and `C_(n-2)-F+1` for odd `n`. At odd `n`, every triangulation contains an even number of channels, so changing every facet sign is the nontrivial kernel element. At even `n`, the facet-sign map is injective.

The checker enumerates exact polygon incidence matrices through `n=8`, compares their `F2` ranks with the formula, and independently checks the Catalan triangulation counts. An attempted `n=9` run was stopped at the 120-second bound because the current helper enumerates all subsets of 27 diagonals. This computational limit does not affect the generic statement, which is a direct reduction of the proved Smith invariants.

## Disposition

The earlier finite counts extend to a closed all-polygon formula. Any real source coefficient packet must satisfy the corresponding parity constraints; passing them determines facet signs uniquely for even `n` and up to global minus for odd `n`.
