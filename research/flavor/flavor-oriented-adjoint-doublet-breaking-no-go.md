# Oriented-adjoint doublet-breaking no-go: WP1089

## Question

Can the current source derive WP1084's requested second-stage
\(SU(2)_B\)-doublet breaking?

## Nima reply evidence

Nima event 10687 gives an exact current-source disposition.

On the irreducible \(SU(2)_B\) doublet, every symmetry-natural endomorphism is
scalar by Schur's lemma, so it cannot split the doublet. A second-stage
\(1+1\) refinement is equivalent to choosing a nonzero adjoint direction

\[
n\in su(2)_B,
\]

which reduces \(SU(2)_B\) to its \(U(1)\) stabilizer. Ordering the two weight
lines additionally requires orienting \(n\), because \(n\) and \(-n\) exchange
them.

No admitted localization, flux, boundary, or WP1080/WP1084 tensor selects that
oriented adjoint ray.

## Conditional quartet compatibility

A block-diagonal operation acting only on the complementary \(B\)-doublet can
preserve the WP1084 localized quartet, because the quartet contains the full
\(A\)-triplet and the \(B\)-singlet. This compatibility is conditional on a
source-fixed oriented adjoint ray.

The operation still does not supply:

- a cyclic seed with nonzero projection on all three ordered \(B\) lines;
- nondestructive three-grade history dilation;
- the reference \(\rho\);
- physical16 descent.

## Classification

Current-source no-go. The requested second-stage operation is absent, not
derived. Fitting \(n\), its sign, the cyclic seed, or history from target
flavor data is forbidden.

The remaining gate is a source packet that derives an oriented adjoint ray in
\(su(2)_B\), followed by cyclic-ray preparation, history dilation, \(\rho\),
and physical16 descent.

Checker: `research/flavor/checkers/wp1089_oriented_adjoint_doublet_breaking_no_go.py`

Result: `results/wp1089_oriented_adjoint_doublet_breaking_no_go.json`
