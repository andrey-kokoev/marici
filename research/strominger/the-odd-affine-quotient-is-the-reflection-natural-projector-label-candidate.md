# The Odd Affine Quotient Is the Reflection-Natural Projector Label Candidate

## Attachment candidates

After correcting cyclic restriction from a state map to a character grading, the attachment problem becomes set-valued: can an affine quotient label the spectral projectors of (C_n), with reflection acting by character inversion?

Let

\[
n=4s-1,
\qquad
\ell=3x-2y,
\qquad
\ell_X=3y-2x
\pmod n.
\]

There are four immediate candidates.

### Unary chart

The unary affine cokernel has the correct cardinality (n), but row reflection does not descend to it. Exact conjugation gives a coefficient (5/n), which is nonintegral for every integer (s\geq1). It cannot label the projectors naturally under reflection.

### Joint chart packet

The joint image has cardinality

\[
\frac{n^2}{\gcd(n,5)}.
\]

This is never (n) in the integer-spin family. It retains more information than the set of (n) character projectors and is not their minimal label carrier.

### Even quotient

The even coordinate

\[
q_+=\ell+\ell_X=x+y
\]

has (n) values, but reflection fixes it. Character projectors transform by (r\mapsto-r). For odd (n>1), the even quotient therefore has the wrong reflection action.

### Odd quotient

The odd coordinate is

\[
q_-=\ell-\ell_X=5(x-y).
\]

Reflection sends (q_-mapsto-q_-), exactly matching character inversion. Its image contains

\[
\frac{n}{\gcd(n,5)}
\]

labels. Therefore it labels all (n) projectors exactly when (5) is invertible modulo (n).

## Physical spin two

For the source-authorized Einstein value (s=2), one has (n=7) and (5^{-1}=3). The normalized odd label is

\[
r=5^{-1}q_-=x-y\pmod7.
\]

It is surjective and obeys

\[
r(X(x,y))=-r(x,y).
\]

Thus the affine construction and cyclic restriction supply a correctly typed, reflection-natural algebraic candidate at spin two:

```text
affine pair
  -> primitive odd residue x-y mod 7
  -> label of the corresponding C7 character projector
```

This is a comparison of label sets and reflection actions. It is not an additive map from physical state vectors to residues. A state in one weight eigenspace has that label; a superposition need not. Nor does this comparison by itself implement the spectral projectors as executable observations on the same prepared boundary packet.

## Exceptional formal spins

When (s\equiv4\pmod5), the existing odd coordinate has only (n/5) values. It cannot label all (n) spectral projectors. This restates the obstruction without inventing five physical states:

> the affine reflected observation lacks enough primitive odd labels to index the full cyclic spectral decomposition.

A primitive odd constructor would repair the label attachment, but only a higher-spin source can authorize that constructor. In Einstein gravity the exceptional case is absent.

## Categorical outcome

The earlier alternatives now separate cleanly:

| Affine carrier | Cardinality | Reflection action | Projector attachment |
|---|---:|---|---|
| unary chart | (n) | undefined | rejected |
| joint charts | (n^2/\gcd(n,5)) | chart exchange | over-refined |
| even quotient | (n) | trivial | rejected |
| odd quotient | (n/\gcd(n,5)) | inversion | valid iff (5\nmid n) |

The physical spin-two case lies in the algebraically viable lane. The five-primary family is precisely where the otherwise natural odd attachment loses one factor of five.

## Updated Aspect germ disposition

Aspect's current admission tester requires six independent fields. The candidate has the following profile:

| Gate | Status | Evidence |
|---|---|---|
| source provenance | pass | Bondi spin-two carrier, affine fold, and axis-marked cyclic restriction |
| well-typed term | pass | affine residue set to character-projector label set |
| discriminating target | pass | separates the seven cyclic character sectors |
| operational witness | missing | no authorized implementation of the seven projectors on the same prepared boundary packet |
| nonredundancy | pass | relates two previously separate typed constructions rather than renaming one coordinate |
| bounded decisive test | missing | existing checks are algebraic and contain no physical intervention record |

The resulting disposition is `defer`. The algebraic candidate must not be promoted to a physical attachment until the two missing gates are supplied. In particular, the existence of celestial rotations proves a symmetry representation, not executable preparation and readout of the required projector family.

## Evidence replay

The checker verifies these cardinalities and actions for (1\leq s\leq100), together with complete reflection-equivariant algebraic labelling at spin two. It also records the updated Aspect disposition and the two missing gates.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/reflection_natural_projector_attachment_checks.py
```

Machine-readable results are written to `research/strominger/results/reflection_natural_projector_attachment_checks.json`.
