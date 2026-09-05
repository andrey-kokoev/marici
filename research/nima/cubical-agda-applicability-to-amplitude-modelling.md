# Cubical Agda applicability to amplitude modelling

## Question

Which parts of Voevodsky's checked Cubical Agda work can model scattering-amplitude and cosmological-wavefunction factorization?

## Claim boundary

The current Agda development is applicable to the typed incidence, composition, quotient, and coherence layer of amplitude models. It does not calculate amplitudes, derive singularities, establish unitarity or positivity, supply complex phases, or identify an abstract path with a physical process.

## What is checked

`CyclicCoherence.agda` represents a generic three-vertex lax cycle with typed residue transports and native path, square, and cube types. Its inhabited cube is constant; it proves boundary typing, not nontrivial amplitude coherence.

`PastingComplex.agda` checks an oriented integer fixture complex, including the chain identity, middle exactness, surjectivity, and filler uniqueness modulo vertex adjustments. This certifies one incidence matrix over the integers, not an amplitude complex over kinematic functions or distributions.

The generated-fixture pipeline rejects malformed orientations, nonparallel cells, omitted completion flags, and unsupported promotion claims before Agda typechecking. It still imports descriptive source and target sorts rather than deriving them from amplitude sources.

The unrestricted `C3` equivalence conjecture was falsified by a tangent-dimension mismatch. The surviving architecture is lax and permits noninvertible residue transports.

## Amplitude dictionary

For a source-labelled graph, let objects be divisor strata `q_g=0`. Let edges be source-normalized residue or restriction maps for compatible connected subgraphs. A square states equality, or a named comparison, between two admissible sequential-residue orders. A cube states coherence among three compatible residues, sewing operations, or crossing comparisons. Local frame changes act as adjustments; a quotient retains only equivalence classes proved invariant under those adjustments.

This dictionary is useful only after a source map assigns each graph divisor and residue to the formal cell. Matching dimensions or incidence matrices does not define that map.

## Applicable amplitude obligations

1. **Factorization typing.** Reject a sequential residue when source and target strata do not match.
2. **Order coherence.** Distinguish strict commutation from an explicit comparison path between residue orders.
3. **Orientation signs.** Detect wrong incidence signs through failure of the chain identity.
4. **Gauge and spin-frame independence.** Represent a common cut fiber and prove that allowed frame changes act trivially on the glued pairing or descend through a quotient.
5. **Associator observability.** Retain two bracketed construction routes until their relative phase is compared. Cubical paths organize the routes and higher coherence; a source-fixed complex phase and physical recombiner remain external data.
6. **Crossing and sewing.** Encode commuting faces and higher compatibility once analytic continuation domains and branch data have been supplied by the source theory.

## Inapplicable promotions

A cubical path is an identity witness, not a propagator, analytic continuation, or physical-time trajectory. A filler is a coherence witness, not an integrated amplitude. Integer exactness does not imply exactness over localized rational functions, boundary values, distributions, or completed function spaces. Contractibility of a formal filler type would not imply uniqueness of a physical amplitude unless the source interpretation is faithful. The present constant cube cannot encode a nontrivial associator phase or monodromy.

## Minimal amplitude formalization target

The next meaningful module should use one smallest source-audited graph and provide:

- labelled divisor objects and compatibility proofs;
- coefficient objects appropriate to its rational functions or boundary distributions;
- source-normalized single and sequential residues;
- a square comparing each admissible residue order;
- one hostile wrong-orientation or incompatible-overlap module that must fail;
- an interpretation theorem from source divisors and residues into the cubical fixture.

Only after that theorem should quotient or higher-filler results be interpreted as amplitude statements.

## Disposition

Cubical Agda can be a structural proof backend for amplitude factorization diagrams and coherence-preserving quotients. Its current results validate the backend and one integer fixture. Applicability to amplitudes stops at the absent source-derived interpretation from labelled factorization divisors, cut fibers, and residue maps into the cubical types.
