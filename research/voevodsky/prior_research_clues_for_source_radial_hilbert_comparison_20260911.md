# Prior-research clues for the source radial Hilbert comparison

## Question

Which existing Marici results constrain or partially construct the missing comparison from the diagonal-shell/all-jet carrier to a radial Hilbert/operator model?

## Claim boundary

This packet is a compatibility audit of existing research. It selects a better next interface but does not construct the missing source map or identify the synthetic periodic circle with the source radial carrier.

## Strongest positive clues

### The radial Hilbert target already exists

`research/aspect/contracts/theta-rh-g4-radial-interface.v1.json` declares the unitary comparison

\[
C_u:L^2(\mathbb R)\longrightarrow L^2(\mathbb R_+)\oplus L^2(\mathbb R_+),
\qquad
C_uq=(q(r),u q(-r)),
\]

with the doubled first-order operator, wall domain, reciprocal swap, graph metric, and Real structure. This is closer to the source separation variable than the synthetic periodic circle. The periodic-circle limit should therefore remain a numerical model, not the default source target.

### A common completed domain is available

`research/voevodsky/common-graph-norm-pullback-domain.md` constructs the completion \(\mathcal D_*\) of the polynomial core in the sum of the leading GNS and Hardy norms, with continuous maps to both observer spaces. This supplies a comparison span and a method for transporting bounded forms. It explicitly withholds injectivity, closed range, a common arithmetic/Weil form domain, and a graph-norm-dense Gaussian-jet inclusion.

### The source jets obey a recurrence

`research/nima/laplace-transform-of-the-gaussian-pair-green-identity-gives-an-exact-spectral-jet-recurrence.md` proves that every parameter jet of each ordered-pair shell is generated recursively from endpoint transforms and one source initial value. The all-jet family is therefore structured rather than freely infinite. This may permit a graph-domain realization by a first-order parameter differential operator, but the packet explicitly withholds identification with a frozen G4 port.

### Finite cutoffs have an exact faithful augmentation

`research/nima/a-spanning-forest-cycle-port-is-the-minimal-finite-observer-completing-common-radial-history.md` proves that common radial history has cycle-space kernel at each finite cutoff and that one chord coordinate per fundamental cycle is the minimal faithful augmentation. This gives canonical finite stages whose dimensions grow with the source graph. It is a better source-derived tower than arbitrary radial point sampling.

### Four ports are a compression, not the state space

`research/voevodsky/four_port_observer_is_source_derived_analytically_but_not_from_valuation_alone_20260910.md` shows that the analytic theta source supplies the four boundary ports, while valuation-only data cannot recover the odd additive phase. The four-port packet is a boundary compression of a larger growing Tate carrier. Hence the four ports should be outputs of the Hilbert comparison, not treated as a faithful finite source carrier.

## Negative constraints

`research/nima/the-diagonal-shell-wronskian-family-is-infinite-rank-and-cannot-factor-through-the-scalar-wall-incidence-plane.md` rules out every fixed finite scalar carrier for the complete shell family. Aspect's `finite-bandwidth-continuum-completion.md` independently requires a named continuum space, measure, normalization, anti-alias condition, convergence map, and uniform resolvent bound. These results jointly rule out promoting the coherent trace26 or fixed finite-jet packets.

## Revised interface

The best-supported source route is

\[
C_1(G_D)
\xrightarrow{(B_D,Z_D)}
\mathcal H_D\oplus\mathbb C^{\beta_1(G_D)}
\longrightarrow
L^2(\mathbb R_+)\oplus L^2(\mathbb R_+),
\]

followed by the existing radial comparison, graph-domain response, and four boundary traces. Here \(B_D\) is function-valued common radial history and \(Z_D\) retains the finite-cutoff cycle kernel. The second arrow is missing.

For a growing cutoff, the finite stages must retain their graph inclusions and cycle-coordinate transition maps. Any completion must prove density or conservativity in a declared topology. The all-jet recurrence should be represented as an operator-domain condition on the function-valued history, not flattened into finitely many scalar derivative ports.

## First executable acceptance test

A source comparison packet should provide:

1. the measure and weight making each \(B_Dc\) an element of the doubled half-line Hilbert space;
2. a bound \(\lVert B_Dc\rVert\leq C_D\lVert c\rVert\) with the exact cutoff dependence;
3. compatibility of graph inclusions and spanning-forest cycle coordinates;
4. the parameter-derivative domain implementing the jet recurrence;
5. Real and reciprocal equivariance;
6. a uniform bound or an explicit statement that only cutoffwise comparison is established.

## Disposition

Prior research does contain the architecture needed for a source comparison, but it points away from the periodic-circle trace tower. The next object should bind function-valued common radial histories plus cycle ports into the existing doubled-half-line graph domain. The missing norm bound and transition compatibility are precise; physical calibration remains separate.
