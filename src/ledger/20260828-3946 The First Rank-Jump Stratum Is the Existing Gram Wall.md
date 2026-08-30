# 3946 — The First Rank-Jump Stratum Is the Existing Gram Wall

> Retracted by Entry 3949. The equation (x^2+y^2-z^2=0) is an orthogonality locus, not the Gram/branch discriminant. The rank census survives; its carrier classification does not.

## Frozen stratum

Use the independently chosen source point

\[
(x,y,z)=(3,4,5),
\qquad
h=x^2+y^2-z^2=0.
\]

Thus the point lies on an existing Gram carrier wall; it was not selected by scanning the Bockstein output.

## Result

With the repaired inhomogeneous kernel solver and free-quotient projection, both kinematic directions and both primes give

\[
(\dim R_0,\dim R_{\rm lift},\dim R_{\rm obs},
\operatorname{rank}\beta,\operatorname{rank}(\beta,{\rm mixed}))
=(3,1,2,0,1).
\]

Relative to the generic audited point, the exact-relation module gains one class, the fiber Bockstein disappears, two relations become obstructed, and one mixed direction survives.

## Narrow conclusion

The first observed rank jump is supported on an already frozen Gram wall. It does not require a new cosmological carrier divisor. The generic rank-three first saturation does not extend unchanged across this wall; its specialization must be treated by a support-sensitive nearby/Gysin comparison.

## Next falsifier

Derive the Gram-wall specialization map from the existing (h=0) support complex. Test whether its costalk accounts for the two obstructed relations and the surviving mixed direction. No fitted support summand is admissible.

## Artifacts

- `research/benincasa/checkers/check_rank26_gram_wall_lift_stratum.py`
- `research/benincasa/results/rank26-gram-wall-lift-stratum.json`

Ledger sequence claim: `seqclaim-1d2799dadff50e56a8cbd214`.
