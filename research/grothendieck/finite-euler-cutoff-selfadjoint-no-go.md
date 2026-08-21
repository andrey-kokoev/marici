# No finite Euler cutoff is a self-adjoint xi determinant

Epistemic-graph event: 1437.

## Finite intrinsic-prime determinant

For a nonempty finite prime set \`P\`, define

\`D_P(s)=prod_(p in P)(1-p^(-s))\`,
\`zeta_P(s)=D_P(s)^(-1)\`.

These are the exact finite-cutoff determinant and Euler product supplied by
the intrinsic-prime diagonal.

For every \`p in P\`, the equation \`1-p^(-s)=0\` holds when

\`s=2pi i k/log p\`, for \`k in Z\`,

up to the harmless orientation of \`k\`. Thus \`D_P\` has infinite vertical
arithmetic zero lattices on \`Re(s)=0\`, while \`zeta_P\` has poles there.

## Critical-coordinate obstruction

Put \`s=1/2+i z\`. The line \`Re(s)=0\` becomes

\`Im(z)=1/2\`.

Hence the finite determinant \`D_P(1/2+i z)\` has nonreal zeros on the
horizontal line \`Im(z)=1/2\`. It cannot be the characteristic determinant of
a self-adjoint operator in the real spectral coordinate \`z\`.

Using \`zeta_P\` instead does not help: it is meromorphic, whereas a
regularized characteristic determinant of a compact-resolvent operator is
entire after its declared normalization.

The completion factors \`s(s-1)\`, \`pi^(-s/2)\`, and \`Gamma(s/2)\` do not
cancel the nonzero \`k\` local pole lattices. At most the polynomial changes
the special behavior at \`s=0,1\`.

## No positive finite-stage approximation

Therefore no nonempty finite prime cutoff can supply:

- an entire completed determinant in the zeta orientation;
- a real-zero determinant in the reciprocal orientation; or
- a self-adjoint finite-stage boundary whose determinant converges by ordinary
  positive spectral inclusion.

This independently confirms Ledger 1392: positivity cannot hold stagewise.
The desired self-adjoint spectrum, if it exists, is an emergent property of a
renormalized infinite completion, not a monotone limit of finite
self-adjoint Euler determinants.

## Circular repair to avoid

One could cancel each unwanted local lattice by inserting cutoff-dependent
entire counterfactors. But no such counterfactors are supplied by the finite
intrinsic-prime system, and choosing them to leave only the target \`Xi\`
zeros would encode the answer. A permissible renormalization must be derived
uniformly from theta/Poisson completion and prove the final Pick positivity.

## Scope

This is an exact no-go for all nonempty finite Euler cutoffs as self-adjoint
xi determinants. It does not exclude a genuinely global renormalized
infinite-prime boundary.
