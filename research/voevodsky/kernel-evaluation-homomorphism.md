# Kernel evaluation homomorphism

## Question

Given a target abelian group and an interpretation of each symbolic kernel atom, does evaluation extend canonically to all symbolic coefficients while preserving additive structure?

## Claim boundary

The module constructs the universal additive extension of an atom assignment. It does not construct the analytic target group or assign exponential-cosine values to the atoms.

## Construction

For a value group \(V\) and a map from kernel atoms to \(V\), `KernelEvaluation.agda` uses the recursion principle of the free abelian group to define evaluation. Cubical Agda verifies the computation rules on generators, zero, sums, and inverses and packages the map as an `AbGroupHom`.

In particular, evaluating a symbolic tail generator reduces to the value assigned to that atom. No equation identifies that value with an analytic expression unless the caller supplies it.

## Strongest falsification attempt

`negative/MissingAtomEvaluation.agda` selects the integer target group but omits the atom assignment. Agda rejects the purported homomorphism: the remaining term is still a function from atom assignments to homomorphisms.

## Disposition

The universal evaluation arrow is constructed. The remaining missing data are now exactly the analytic target `AbGroup` and an assignment sending each parameter-indexed symbolic atom to its source-derived analytic function or value. Once supplied, additive preservation is automatic; compatibility with generators, transports, completion substitution, and the filler boundary remains a separate naturality proof.

## Verification

- `research/voevodsky/agda/KernelEvaluation.agda`
- `research/voevodsky/agda/negative/MissingAtomEvaluation.agda`
- `research/voevodsky/results/cubical_agda_kernel_evaluation.json`
