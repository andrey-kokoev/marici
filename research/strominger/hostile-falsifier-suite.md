# Hostile falsifiers for the parity-cohomology theorem

This packet records counterexamples to the strongest nearby false statements.
They are part of the theorem boundary, not discarded scratch.

## F1. Full-target classification does not survive target truncation

At grade two, take source columns `(a,m)=(0,-4),(0,-3)`.  The full magnetic
matrix has rank two.  Retaining only target exponents in the square
`[-1,1]^2` leaves

\[
\begin{pmatrix}0&60\\0&-60\end{pmatrix},
\]

of rank one.  The first source column becomes a spurious kernel vector.
Therefore target truncation is a different operator, not a visibility change.

## F2. Individual nonzero residues do not give depthwise cohomology

At grade two, the depth-two and depth-four residues are `-60` and `-120`.
The combination

\[
2D_{2,2}-D_{2,4}
\]

has zero residue and a rational primitive.  Hence the ordinary rational
quotient is not the direct sum of one line per depth.

## F3. Pairwise primitive circuits need not form a saturated basis

For the reduced residue row `(10,21,36)`, reference-pair circuits span an
index-five sublattice of the full kernel and miss `(-12,4,1)`.  Primitive
individual columns do not imply a primitive generated lattice.

## F4. Rational stabilization does not imply integral stabilization

At grade three, a single visible depth four already gives rational quotient
rank one, but its residue index is `3360`.  Adding depth six leaves rational
rank one while reducing the index to

\[
\gcd(3360,7056)=336.
\]

Rank and arithmetic granularity are independent stabilization questions.

## F5. Source deletion does not descend to kernels

The circuit `1-bar(z)^(-2)` is magnetic-zero at grade two.  Projecting away
either supported source vertex leaves a nonzero column.  Kernel naturality is
covariant under inclusion, not contravariant under coordinate deletion.

## F6. Full rank does not provide a natural observer family

One may gauge-transform the parity readout independently at each cutoff and
retain full rank everywhere.  Unless the gauge and its inverse commute with
source inclusions, the reconstruction squares fail.  Naturality requires a
transported splitting, not objectwise rank.

## F7. Integer-depth enlargement is not conservative

At grade two and depths `{0,4,5}`, the all-integer constructor has the mixed
circuits `C_6` and `C_7` recorded in
`constructor-extension-classification.md`.  The even theorem cannot be
continued by replacing “even” with “integer.”

## F8. No hidden rational residue divisor

For every tower, radialization puts the form on the `u`-line.  Its denominator
has only the irreducible divisors `u` and `1+u`; the residue at infinity is
zero.  After subtracting `r*eta`, Hermite reduction produces a rational
primitive.  Thus within the proved tower family there is no third hidden
logarithmic direction.

Together these falsifiers separate source visibility, target loss, parity
aliasing, rational contraction, integral accessibility, presentation gauge,
and constructor enlargement.
