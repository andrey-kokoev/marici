# Generic-coefficient pasting complex

## Question

Does fixture exactness depend on integer coefficients, or only on additive structure available for function-valued discrepancies such as \(\tau H\)?

## Claim boundary

The theorem holds for every Cubical Agda `AbGroup` and pointwise function space valued in one. It does not construct the analytic value group containing the exponential-cosine kernel, nor identify the source maps as homomorphisms or natural transformations.

## Construction

For an abelian group \(M\), `GenericPastingComplex.agda` defines the normalized boundary

\[
\partial_1(a,b,c)=\bigl(-a+b,-b+c,-((-a+b)+(-b+c))\bigr)
\]

and \(\partial_2(x,y,z)=x+y+z\). The third component is the closure-normalized presentation of the cyclic incidence boundary. Cubical Agda proves the chain identity, constructs an explicit preimage for every closed triple, and proves second-boundary surjectivity using only abelian-group laws.

`FunctionCoefficientFixture.agda` instantiates the theorem for every pointwise function group \(X\to M\). Consequently the pasting theorem can retain a function-valued discrepancy without mapping it to integers once the function codomain is supplied as an `AbGroup`. The integer case remains a regression instance.

## Strongest falsification attempt

`negative/NonAbelianCoefficient.agda` attempts to use an arbitrary group as an abelian coefficient object without supplying commutativity. Agda rejects the conversion and exposes the missing commutativity function.

## Disposition

The integer-coordinate mismatch is removed from the algebraic theorem: exactness is coefficient-generic and extends to pointwise function groups. The remaining first missing object is narrower: a formal abelian value group for the analytic kernel values, plus source-derived proofs that the signed-even kernel family and its maps inhabit and preserve the resulting pointwise structure. No source-global naturality is inferred.

## Verification

- `research/voevodsky/agda/GenericPastingComplex.agda`
- `research/voevodsky/agda/FunctionCoefficientFixture.agda`
- `research/voevodsky/agda/negative/NonAbelianCoefficient.agda`
- `research/voevodsky/results/cubical_agda_generic_coefficients.json`
