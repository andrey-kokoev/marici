# Constant doubling does not supply the theta half-plane exclusion form

## Question

Does doubling the native theta-tail phase plane immediately produce a constant nondegenerate Hermitian form capable of excluding off-seam Evans intersections?

## Conjugate doubling

For the pair of gauged generators at `s` and `conjugate(s)`, the exact block form built from the native symplectic matrix is conserved for arbitrary real forcing. It is nondegenerate but has signature `(2,2)`. Hence conjugate doubling preserves a Krein form, not a positive energy. Null lines and transverse intersections remain possible.

## Reciprocal-Real doubling

For the pair at `s` and `-conjugate(s)`, solve the constant cross-block equation. The variable forcing first forces the cross block into the form

\[
K=\begin{pmatrix}0&k\\-k&d\end{pmatrix}.
\]

The drift residual has off-diagonal entry

\[
k(-a+it),
\]

for `s=a+it`. At a generic spectral parameter this forces `k=0`, leaving a degenerate block. Thus the reciprocal pair has no generic nondegenerate constant cross form of this type.

## Strongest falsification result

Constant doubling splits into two failures: conjugate pairing exists but is indefinite; reciprocal-Real pairing is generically degenerate. Neither supplies the desired positive half-plane exclusion law.

## Disposition

The next candidate must be source-sewn and coordinate-dependent: solve the matrix transport equation for a `q`-dependent form with boundary data fixed by reciprocal modular sewing, then inspect its signature and endpoint flux. A metric fitted from zero locations is inadmissible.
