# `q_G12` finite quotient-interface preflight

## Question

Can the frozen tensor and sewn marked-relative presentations be placed in a common source-labelled finite basis so that their two rank-six quotients can be compared exactly?

## Tensor endpoint

The tensor presentation is executable and basis-explicit. Its ambient basis is

\[
(L_1,L_2,L_3,a^2,b^2,c^2,1).
\]

Restriction to `q_G12=c+E=0` produces the six-element basis

\[
(L_1,L_2,L_3,a^2,b^2,1)
\]

with the principal relation `c^2-E^2=(c-E)(c+E)`. The checker constructs monomial coefficient matrices in `(a,b,c)`, verifies ambient rank seven and restricted rank six, and proves equality between direct restricted coordinates and coordinates induced from the ambient quotient.

## Marked-relative endpoint

The sewn localization artifact records only aggregate invariants:

- ambient rank 35;
- complete five-pole residue quotient rank 20;
- deletion rank 15;
- canonical relative source boundary `rho_phys`;
- no canonical absolute `T7` projection.

It does not expose an ordered basis for `M15`, an ordered basis or inclusion matrix for `M9`, quotient representatives for `Q6=M15/M9`, the coefficient field/specialization, or a generator/checker from which those matrices can be reconstructed.

The sewn wall-residue artifacts give rational one-forms and Čech closure, but no coordinates of those forms in a common `Q6` basis.

## Pullback test

A finite comparison matrix requires two interface descriptors over the same coefficient field:

\[
B_{\rm tensor}\longleftarrow B_{\rm source}
\longrightarrow B_{Q6}.
\]

Only the left endpoint is materialized. The right endpoint is a rank statement without basis vectors or reduction pivots. Therefore no matrix multiplication, kernel comparison, or deliberate `M9` failure vector is currently defined.

This is stronger than failure to find an isomorphism: the finite interface test cannot be formed from the frozen artifacts. Equal quotient dimensions remain non-evidential.

## First missing object

The first missing object is a basis certificate for the marked-relative quotient containing:

1. the coefficient field and kinematic specialization;
2. ordered source-labelled generators of `M15`;
3. the `M9 -> M15` inclusion matrix;
4. quotient reduction pivots or an explicit projection `M15 -> Q6`;
5. coordinates of `rho_phys` and the three oriented sewn wall residues;
6. source digests and the command that reproduces the certificate.

Only after this certificate exists can one ask whether the tensor six-space maps to `Q6` or whether its principal kernel equals `M9` under a typed source map.

## Strongest falsification attempt

Use polynomial monomials from the tensor checker as a presumed common basis for the localization quotient. This fails because the localization classes are marked rational differential forms modulo twisted exact/relative relations, not polynomial interaction numerators. No map from the polynomial basis to those cohomology classes is declared.

## Acceptance test

Construct the basis certificate, verify ranks 15, 9, and 6 from its matrices, reduce every sewn residue, and test a proposed tensor-to-`Q6` matrix for:

- kernel exactly the declared source kernel;
- preservation of `rho_phys` and Čech orientation;
- a nonzero `M9` vector mapping to zero;
- a quotient generator mapping nontrivially;
- compatibility with analytic normalization.

## Disposition

The tensor quotient is finitely explicit, but the sewn localization quotient is not. The comparison is blocked at the missing basis certificate, before any claim about equality, inequivalence, or lower-graph factorization can be tested.

## Evidence

- `research/benincasa/check_tensor_marked_wall_localization.py`
- `research/benincasa/tensor-marked-wall-localization.json`
- `research/benincasa/source-bases-localization-fiber.json`
- `research/benincasa/physical_g12_shared_wall_residues.py`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
