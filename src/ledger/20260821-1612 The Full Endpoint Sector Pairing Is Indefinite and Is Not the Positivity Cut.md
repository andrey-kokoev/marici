# Entry 1612 — The Full Endpoint Sector Pairing Is Indefinite and Is Not the Positivity Cut

## Claim

The complete finite-time endpoint combination cannot be identified with the
positive Cut norm required by Gaussian second-Rees positivity.  It is an
indefinite response containing interference/dispersive data.

## Calculation

Writing the bulk and boundary endpoint coordinates as \((B,S)\), the source
weights define

\[
Q(B,S)=B^2-4BS-2S^2
=
\begin{pmatrix}B&S\end{pmatrix}
\begin{pmatrix}1&-2\\-2&-2\end{pmatrix}
\begin{pmatrix}B\\S\end{pmatrix}.
\]

The Gram determinant is

\[
-6<0,
\]

so the pairing has one positive and one negative direction.  It cannot be a
norm square in any real change of basis.

## Correction of target

Entries 1608 and 1610 type the positivity completion as a Cut norm.  Entry
1611 rejects a scalar endpoint square.  The present calculation shows why:
the complete loop response is a larger object than its statistical/noise
part.

The legitimate comparison is now

\[
\boxed{
\text{second-Rees covariance excess}
\stackrel?=
\text{Keldysh-noise / physical-Cut projection of the loop kernel},
}
\]

not equality with the full endpoint-sector quadratic form.

## Next falsifier

Apply the Keldysh rotation before endpoint assembly.  Extract the noise block
\(\Sigma^K\), retain its occurrence-resolved two-line Cut representation, and
test whether its induced phase-space covariance is positive semidefinite and
equals the second-Rees uncertainty completion.

## Artifacts

- `research/benincasa/checkers/endpoint_sector_pairing_signature.rs`
- `research/benincasa/results/endpoint-sector-pairing-signature.json`

Allocator claim: `seqclaim-84090c4dfc10d00aefeaf504`.
