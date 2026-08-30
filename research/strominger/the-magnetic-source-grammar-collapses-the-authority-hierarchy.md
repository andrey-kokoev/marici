# The magnetic source grammar collapses the authority hierarchy

## Question

Do the zero-, one-, and two-matrix presentations represent distinct levels of
source authority?

## Result

No. In the present magnetic model the source is a free-group grammar. It
already contains:

- word concatenation;
- inverse letters and word inversion;
- finite repeated composition.

Consequently it constructs both

\[
C^n
\quad\text{and}\quad
C^{-n}
\]

for every \(n\in\mathbb Z\). The three presentations have the same
source-derived algebraic capability.

## What actually differs

The presentations allocate resources differently.

| retained packet | constructor work delegated to readout |
|---|---|
| grade \(n\) | build powers and inverses |
| matrix \(C^n\) | build the inverse |
| pair \((C^n,C^{-n})\) | multiply retained matrices into the fixed readout |

This is a resource distinction, not an authority distinction.

## Hostile source change

Replace the free group by the free monoid on the same positive generators. The
monoid has identity and concatenation but no inverse constructor. Negative
grades cease to be constructible.

That fixture does not produce a weaker presentation of the same
\(\mathbb Z\)-orbit. It produces a different orbit, indexed only by the
nonnegative monoid.

Therefore withholding inversion while claiming to preserve the full magnetic
source object is inconsistent. The inverse capability can disappear only when
the source grammar itself changes.

## Second correction: coordinates are not computer memory

The statement that \(C^n\) has 16 coordinates does not imply bounded storage
in bits. Its integral entries grow with \(n\), so their bit lengths grow.
Likewise the source word for \([x,y]^n\) has length \(4|n|\).

The exact state has fixed arity, not fixed bit cost.

This yields three separate resource measures:

\[
\text{arity},\qquad
\text{integer bit length},qquad
\text{constructor depth}.
\]

None determines the others without a declared computation model.

## Theorem-level statement

For the neutral-commutator orbit in the faithful integral response:

1. word inversion constructs matrix inversion on every admitted source word;
2. repeated word composition constructs every integral power;
3. the grade-only, one-matrix, and two-matrix packets are extensionally
   equivalent under the source grammar;
4. their differences are resource placements, not differences of source
   authority.

The first three claims follow for all integral grades from free-group and
representation identities. The checker replays them over bounded word and
grade families and separately exhibits increasing bit cost.

## Explanatory consequence

Deutsch's question removes another apparent primitive. We cannot explain a
presentation by declaring some source-generated operation unavailable.

The next genuine object must be a costed constructor grammar: the source
constructors together with explicit measures of arity, bit size, and
constructor depth. Only relative to that object can one presentation be called
more economical than another.

## Claim boundary

This result does not supply a physical cost model. It shows why such a model is
necessary and why source authority alone does not select among the three
presentations.
