# Quarter order-four symbolic Routh certificate is computationally blocked

## Question

Does the order-four zero-shift condensation pencil admit the same direct Routh–Bernstein certificate as orders two and three?

## Claim boundary

No order-four stability result was obtained. The timeout is not evidence for instability or failure of a Bernstein certificate.

## Disposition

The exact construction reaches a degree-22 open pencil and 23 symbolic Routh entries. Repeated rational-function gcd normalization did not materialize a result within the 120-second execution bound. The order-three implementation therefore does not scale directly. Its acceptance gates remain unchanged: every open-pencil Routh numerator and denominator must be Bernstein-nonnegative, and the degree-dropped endpoint must be Hurwitz stable. This branch is deferred rather than weakened. The next nonredundant leaf is `quarter-order-four-bezoutian-proper-position`, replacing recursive symbolic Routh fractions by a fraction-free Bezoutian or Hermite–Biehler certificate for the same continuous pencil.
