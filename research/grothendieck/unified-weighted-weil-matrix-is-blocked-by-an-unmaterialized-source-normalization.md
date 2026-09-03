# The unified weighted Weil matrix is blocked by an unmaterialized source normalization

## Question

Can the compact operator `K_L=A^(-1/2)B_LA^(-1/2)` now be assembled numerically?

## Audit

The existing packets establish boundedness, compact weighting, translation matrix elements, and several comparison constants. They do not yet place the complete local Weil form in one source-normalized formula fixing all of:

- Fourier-transform convention;
- convolution/reflection convention for the test function;
- sign and prefactor of each prime translation;
- whether prime powers at `+log n` and `-log n` are combined before weighting;
- the constant `log pi` term;
- the exact archimedean multiplier normalization;
- pole/endpoint rank-one vectors and coefficients;
- the unitary map from the source test-function space to `L^2(-L,L)`.

The current Dirichlet translation scout explicitly omits the explicit-formula prefactor. Its norms therefore cannot be combined with the archimedean, Carleman, endpoint, or localization matrices in a positivity test.

## First missing typed object

The first missing object is a single source-derived identity

`W_L=A+B_L`

on a declared common core, with every summand written in the same `L^2(-L,L)` normalization and with its sign, coefficient, adjoint convention, and domain stated. An acceptance test is:

1. evaluate the identity on a real even Gaussian fixture for which both the classical explicit formula and the operator expression are independently computed;
2. verify equality with directed numerical enclosures;
3. test adjoint symmetry of every matrix cell;
4. include a deliberate sign reversal of one prime term and require a nonzero residual.

## Consequence

Until this identity is materialized, assembling `K_L` would silently choose normalization and could manufacture apparent positivity or negativity. Bounds that use an abstract coefficient `kappa` remain valid as inequalities but cannot decide the finite spectrum.

## Disposition

The unified-matrix branch stops at this source blocker. The compact factorization remains valid abstractly. Computation resumes only after a normalized explicit-formula packet and fixture are supplied; enlarging the current prime matrix cannot change this disposition.
