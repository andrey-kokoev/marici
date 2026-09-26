# Planar biadjoint amplitude-net implementation ladder

Keep this implementation ladder separate from existing amplitude formula proofs and the exploratory nine-point component nets.

| Level | Contract | Implementation status |
|---|---|---|
| Infrastructure | Typed exact-scalar identity transport; not an amplitude | Implemented and tested |
| Rooted base case (two-boundary convention) | Amputated unit current J(i)=1 | Implemented and tested |
| Internal-edge primitive | Separate stripped propagator 1/X at nonzero exact rational X | Implemented and tested |
| Separate scalar two-point library | Identity, current, kinetic/inverse kernels, propagators, correlators, one-particle overlap | Typed symbolic emitters tested; see scope below |
| n=3 | Coupling-stripped planar cubic seed, convention fixed explicitly | Next |
| n=4 | Two planar channel contributions and their sum | Not implemented in this ladder |
| n=5 | Five planar diagrams, independent existing-formula comparison | Not implemented in this ladder |
| general n | Recursive planar biadjoint tree emitter | Not implemented in this ladder |

## Identity interface (two boundaries, not particle multiplicity)

`INPUT--ID` emits VALUE at OUT, retaining exactly the input Scalar(Fraction), and a separate CLEAN--TICKET obligation. Consuming that obligation emits DONE at ACK. Publication is not completion. The cleanup token is an explicit interface convention, not a physical operation. There is no propagator or coupling in this model.

Five exact values, including zero and negative fractions, pass typed-input, preserved-denotation, one-shot consumption, immutable-observation and terminal-topology tests. Two sequential host-instantiated identities return the same value; this is NOT net-level composition. Inputs are attributed exact rational values, not arithmetic encoded as finite agent graphs.

Implementation: `research/nima/checkers/amplitude_identity_net.py`.
Checker: `research/nima/checkers/check_amplitude_identity_net.py`.
Result: `research/nima/results/amplitude-identity-net.json`.

## Unit current and propagator

`biadjoint_seed_net.py` adds explicit UNIT and PROP requests, using the same linear publication/completion template. UNIT emits the single-leg amputated rooted current J(i)=1. PROP evaluates 1/X for a specified nonzero exact channel value, matching the stripped planar cubic-tree convention in `arbitrary-n-planar-biadjoint-amplitude-proof.md`. This is not the Feynman propagator with i-epsilon or an on-shell two-particle S-matrix. The external seed does not silently include an external propagator.

Five primitive cases and invalid-input controls pass in `research/nima/checkers/check_biadjoint_seed_net.py`; the identity regression also passes. Result: `research/nima/results/biadjoint-seed-net.json`. Arithmetic remains an attributed primitive; recursive net wiring is not implemented. Symbolic channel expressions are now supported by the separate library below.

## Scoped scalar two-point library

`scalar_two_point_primitives.py` implements ten typed request kinds, including symbolic stripped edges, free scalar Feynman/time-ordered and Wightman kernels, the distinct kinetic and inverse-propagator kernels, a supplied-self-energy Dyson expression, and covariantly normalized free one-particle identity. See `research/nima/scalar-two-point-primitive-contracts.md` for conventions and exclusions. All ten emitters and eight refusal controls pass. This is not every theory's primitive set and does not add interactions or LSZ/sewing automatically.
