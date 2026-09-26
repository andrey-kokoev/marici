# Source audit: rational rotors precede analytic integration

Active SCC obligations: forward realization, coefficient transport and readout
admission. This audits actual files, rather than treating the previous analytic
formulas as evidence that their inputs were selected by the native source.

## What was actually found

- `agda/ComponentArithmetic.agda` constructs addition and multiplication on its
  component-word model, with an additive-endomorphism classifier. The geometric
  identification with a one-generator component monoid remains a declared
  premise; the arithmetic construction itself is genuine.
- `agda/RationalComponentArithmetic.agda` constructs signed-fraction quotient
  arithmetic and positive-denominator inverses, faithfully related to rationals.
- `agda/NativeRationalComponentArithmetic.agda` transports such coefficient
  calculations through native executions. Its generic bridge TAKES a weight
  assignment as input; it does not select a Clifford observable algebra.
- `agda/NativeTableRules.agda` packages supplied equivalences, endpoint witnesses,
  paths and higher comparisons. A supplied real/analytic family can therefore
  be represented, but representability is not a proof of its source selection
  or of its interpretation as active physical evolution.

No source-authorized response-to-implementer identification or analytic
completion policy was obtained from these declarations. This is a bounded audit,
not a claim that no possible native construction could provide one. Voevodsky's
`source-algebra-selection-boundary.md` supplies the independent selection
objections; its complete formal/checker suite was not rerun here.

## Positive construction before real exponentiation

Once the chosen rational Clifford product and J squared=-1 are supplied, no
trigonometry or real exponential is needed to build infinitely many rotors:

\[
V(t)=\frac{(1-t^2)1+2tJ}{1+t^2},\qquad t\in\mathbb Q.
\]

They obey

\[
V(t)^\top V(t)=1,\qquad V(-t)=V(t)^{-1},
\qquad V(t)V(u)=V\!\left(\frac{t+u}{1-tu}\right).
\]

The last displayed chart excludes tu=1. There is no group singularity there:
use a nonzero rational homogeneous pair (m,n), with

\[
V[m:n]=\frac{(n^2-m^2)1+2mnJ}{n^2+m^2}.
\]

Composition is represented by

\[
(m,n)\star(r,s)=(ms+nr,\ ns-mr).
\]

The denominator of this product is the product of the original denominators.
The infinity chart (1,0) gives -1; t=0,1,-1 give 1,J,-J. Thus this algebraic
family preserves the existing even source samples while exposing its chart
boundary rather than discarding it.

`agda/RationalRotorNumerators.agda` proves the norm and composition numerator
identities and instantiates them in the ACTUAL constructed rationalRing. Fresh
safe/cubical compilation passes. This is a coefficient-level result: it does
not supply the missing native Clifford product or comparison admission.

The formal rational differential is already determined:

\[
V'(t)=\frac{2}{1+t^2}J V(t),
\qquad d\theta=\frac{2\,dt}{1+t^2}.
\]

The differential is invariant under the rational composition law. Integration
to a real angular function, its winding and a physical clock are separate
steps. A rational parameterization of an algebraic group is not an additive
rational-time flow.

## A concrete obstruction to time refinement over the rationals

J has no square root anywhere in Mat_2(Q), not just among the selected finite
source lifts. If X squared=J, then X commutes with J. Its centralizer is exactly
Q*1+Q*J, so write X=a+bJ. The equations become

\[
a^2-b^2=0,\qquad 2ab=1.
\]

Eliminating a gives 4b^4-1=0. Both rational factors 2b^2-1 and 2b^2+1 are
irreducible over Q, so no rational b exists. Equivalently the real roots require
coefficients plus or minus 1/sqrt(2).

Thus even an abstract additive divisible-parameter group valued in Mat_2(Q)
cannot reach J: halving the parameter would require this missing square root.
This is stronger than merely saying the rational point set is not a real
continuous group. Adding algebraic roots, formal series, or a norm completion
are genuinely different possible enrichments; none follows just by composing
the original rational matrices.

Under the PREVIOUSLY DECLARED real ambient algebra and Euclidean norm, these
rational rotors are dense in the real unit circle. That observation uses the
chosen real completion; it is not a construction selecting that completion
from the native calculus.

## A concrete comparison-admission hostile

At t=1/2, the rational adjoint rotor sends the active response basis to

\[
B_1\longmapsto -\frac7{25}B_1-\frac{24}{25}B_2,
\qquad
B_2\longmapsto \frac{24}{25}B_1-\frac7{25}B_2.
\]

This fixes the proposed unit B0 and preserves the counting norm on the active
B1,B2 plane. But the original pointwise product B1*B2 is zero, while the product
of these images is nonzero. Therefore this concrete rational transformation
cannot be admitted as an automorphism of the unchanged pointwise source algebra.
A preserved norm and fixed marked value do not suffice.

This does NOT require pointwise multiplication to be the physical product. It
requires an explicit policy stating what product/readout is preserved or
transported, and whether this comparison is a change of presentation or an
active evolution. Calling the generic native equivalence constructor does not
answer that question. The earlier non-isometric counting/Clifford metric
identification remains a separate issue.

## Outcome and nonredundant continuations

The audit separates four levels:

1. Actual constructed component coefficient arithmetic.
2. A conditional algebraic rotor group and its infinitesimal derivative.
3. An additional integration/completion and path-lifting choice.
4. Native product/readout admission and an active-dynamics interpretation.

Two successors remain live:

- Locally construct compatible finite FORMAL flow jets using rational factorial
  coefficients and the chosen J. Test composition, inverse, truncation and the
  generator without pretending that a formal parameter evaluates at a finite
  physical time. This is a separate completion from choosing the real circle.
- Ask the source-profile owner to resolve admission for the explicit t=1/2
  map, with the pointwise-product failure above as a fixed hostile. Identify an
  actual product/readout transport and its role, or record the missing
  response-to-implementer constructor. The owner's files are not mutated.

Verification:

```text
pwsh -NoProfile -File research/nima/checkers/check_rational_rotor_numerators.ps1 -Fresh
uv run --with sympy python research/aspect/scc/scc.py check nima-rational-rotor-source-audit
```

The exact checker validates rational Cayley identities, 576 homogeneous-pair
products, the invariant differential, the centralizer/root obstruction and the
pointwise-product hostile. It binds current local proof imports to the fresh
Agda receipt. No formal impossibility theorem for the full native source, real
analytic completion, physical clock or quantum dynamics is claimed.
