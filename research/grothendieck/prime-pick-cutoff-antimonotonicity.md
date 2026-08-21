# Prime cutoff refinement adds negative Pick directions

Epistemic-graph event: 1434.

## Common source domain

Let \`z\` lie in the upper half-plane with \`Im(z)>1/2\`. By the functional
equation,

\`Xi(z)=xi(1/2-i z)\`,

and \`s=1/2-i z\` lies in the honest Euler half-plane. Therefore

\`M_Xi(z)=-Xi'(z)/Xi(z)
=i xi'(s)/xi(s)\`.

For a finite prime-power cutoff \`C\`, the intrinsic contribution is

\`M_C(z)=-i sum_(n in C)Lambda(n)n^(-1/2)exp(i z log n)\`.

This is an exact comparison between the finite intrinsic-prime source and the
theta Pick boundary before analytic continuation.

## One-mode Pick increment

Adding one prime-power mode of length \`L=log n>0\` and weight
\`a=Lambda(n)n^(-1/2)>0\` changes the Weyl function by

\`delta M(z)=-i a exp(i z L)\`.

At \`z=i y\`, \`y>1/2\`,

\`delta M(i y)=-i a exp(-yL)\`.

The diagonal increment of the Pick kernel is therefore

\`delta K(i y,i y)
=Im(delta M(i y))/y
=-a exp(-yL)/y<0\`.

Thus the kernel increment from every individual prime-power mode has a
strictly negative direction.

## No monotone positive feature construction

If a larger cutoff were obtained from a smaller one by adjoining positive
Hilbert-space boundary features, its reproducing kernel would change by a
positive semidefinite Gram kernel. The strictly negative diagonal above
forbids this.

Consequently:

- prime cutoff refinement is not a nested positive RKHS construction;
- intrinsic prime modes cannot map individually to positive Pick features;
- the comparison map must land in the indefinite preshape of Ledger 1391;
  and
- any positive Hilbert boundary can emerge only after global gamma--prime
  cancellation and quotient, not at each finite prime stage.

This is the Pick-kernel counterpart of the signed Schur-complement obstruction
in Ledger 1390.

## Cutoff compatibility gate

A surviving comparison system must use indefinite morphisms

\`V_C -> V_(C union {n})\`

whose added direction has negative norm, while simultaneously updating the
archimedean/counterterm channel so that the completed limit is independent of
the ordering of prime refinement. Merely holding the gamma channel fixed and
adding prime fibers cannot give a directed system of positive spaces.

A proposal that claims positivity at every finite cutoff is therefore
falsified by a single diagonal evaluation. A proposal that postpones
positivity to the limit must provide a canonical renormalized quotient; taking
the positive spectral subspace of the limit after inspecting \`Xi\` is
circular.

## Scope

This is an exact no-go for monotone positive prime-feature refinement in the
Euler half-plane. It does not rule out an indefinite cutoff system with a
source-derived positive completed quotient.
