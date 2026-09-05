# Symbolic kernel coefficient object

## Question

Can the function-valued discrepancy be retained in a native additive coefficient object before a formal analytic value type is available?

## Claim boundary

The construction represents parameter-indexed kernel and residue expressions as free abelian generators. It preserves symbolic distinction and supports the generic pasting theorem. It does not interpret exponential, cosine, multiplication by analytic parameters, inequalities, limits, or equality of evaluated functions.

## Construction

`SymbolicKernelCoefficients.agda` defines generators for positive-frequency, negative-frequency, tail, normalization-residue, and deformation-residue atoms, each indexed by an arbitrary parameter type. Their free abelian group is a native Cubical higher-inductive type. The generic triangle theorem then supplies exactness for triples valued in this symbolic group.

The tail discrepancy is represented by its own generator. The filler \((0,\mathrm{tail},0)\) has that generator as its second boundary. Every symbolic discrepancy has a filler, and every closed difference of symbolic fillers is a vertex adjustment.

## Strongest falsification attempt

`negative/CollapseSymbolicTail.agda` attempts to make a tail generator equal to additive zero by a constant path. Agda rejects the boundary because the free generator and zero are distinct constructors. Thus missing analytic evaluation cannot be hidden as definitional equality.

## Disposition

The coefficient object is now native and information-preserving at the symbolic level. The remaining first missing map is an analytic evaluation homomorphism from the free kernel coefficient group into a formal abelian group of analytic values or functions, together with proofs for the source formulas, completion substitution, and naturality squares. Symbolic exactness does not certify those analytic identities.

## Verification

- `research/voevodsky/agda/SymbolicKernelCoefficients.agda`
- `research/voevodsky/agda/negative/CollapseSymbolicTail.agda`
- `research/voevodsky/results/cubical_agda_symbolic_kernel_coefficients.json`
