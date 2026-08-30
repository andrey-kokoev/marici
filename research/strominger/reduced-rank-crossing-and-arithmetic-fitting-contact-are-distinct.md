# Reduced rank crossing and arithmetic Fitting contact are distinct

Owner: `marici.Strominger`

## Question

Is the magnetic depth jump the same local mechanism already seen on
Benincasa's gauge Fitting conic, or does it define a stricter arithmetic
contact condition?

## Result

Benincasa's former gauge Fitting conic is a historical algebraic comparison,
not a live cosmological object: that branch was retired after noncanonical
descent. As a finite algebraic fixture it is a codimension-one reduced rank
locus: the special matrix loses one rank and its
normal left-null/right-null pairing is nonzero. The normal jet crosses the
reduced degeneracy locus.

The magnetic grades 152 and 881 exhibit a different local geometry. Write

\[
M'=M+3^7H, \qquad M=3^2B.
\]

For every three-by-three row minor, determinant multilinearity gives

\[
\det(M')-\det(M)
=3^{11}d(\det)_B(H)+\text{terms divisible by }3^{16}.
\]

The exponent 11 is forced by replacing one of three columns: the perturbation
contributes depth 7 and the two retained columns contribute depth 2 each.

Both the normalized leading Plücker section and its first variation are
nonzero modulo three. In all four maximal-minor charts their residues are,
respectively,

\[
(1,1,1,1)
\quad\text{and}\quad
(2,2,2,2).
\]

Their sum vanishes. The complete maximal-minor section therefore gains one
unit of 3-adic depth.

The magnetic event is not a reduced rank crossing. It is first-order contact
inside a nonreduced 3-adic thickening of a Fitting stratum.

## DVR exterior-contact lemma

Let a rank-three matrix over a discrete valuation ring satisfy

\[
M=\pi^sB, \qquad \delta M=\pi^uH, \qquad u>s.
\]

The one-direction part of every maximal minor has valuation at least

\[
u+2s.
\]

Terms containing two or three direction columns have strictly larger
valuation. Hence the depth-\(u+2s\) response is governed by the complete
exterior derivative

\[
d(\Lambda^3)_B(H).
\]

If the normalized leading Plücker section of \(M\) equals the negative of
this derivative in the residue field, then every maximal minor gains at least
one unit of valuation. The condition is chart-independent because it is an
equality of complete exterior-power sections.

For the magnetic fixture,

\[
s=2, \qquad u=7, \qquad u+2s=11.
\]

The exact multilinear expansion verifies that terms with two direction
columns begin at depth 16 and the three-direction term begins at depth 21.
They cannot produce the depth-eleven cancellation.

## Cross-lane comparison

- Benincasa's retired finite fixture supplies a reduced rank-one crossing with
  a nonzero normal pairing, but no canonical descent.
- Aspect uses Fitting stratification to prevent treating a Bockstein line as
  a constant-rank family across a rank jump.
- Buzzard proves that equal top determinants do not determine lower
  determinantal strata.
- The magnetic fixture supplies cancellation between a nonzero arithmetic
  leading section and a nonzero exterior derivative.

These are structural analogies. No source-derived functor between their
continuation categories has been constructed.

## Claim boundary

This is an exact finite arithmetic theorem for the loaded grades 152 and 881,
together with a general determinant-multilinearity lemma. It is not yet an
unbounded classification of magnetic grades, a source-derived cross-sector
comparison, or a proof that every Fitting-depth jump has this form.

## Disposition

The local explanation survives and becomes sharper: the unexpected
cancellation is an arithmetic tangency criterion, not ordinary reduced
transversality. The next falsifier is to search other source-derived integral
families for a nonzero leading exterior section and nonzero first variation
that cancel in the residue field.

## Verification

Run:

```powershell
python research/strominger/checkers/dvr_plucker_contact_checks.py
```

The exact checker passes seven of seven gates. Machine-readable output is in
`research/strominger/results/dvr_plucker_contact_checks.json`.