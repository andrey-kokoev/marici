# Typed scalar two-point primitives

Implemented a scoped library, not a universal collection of every possible two-point quantity. Convention: real scalar field, 3+1 dimensions, metric (+---), Fourier phase exp(-ip.x), hbar=1. Put K=p^2-m^2. External momentum-conservation delta functions are not included in translationally invariant momentum kernels below. The one-particle overlap instead includes its stated spatial delta explicitly.

| Request | Output | Interpretation |
|---|---|---|
| identity | supplied typed block unchanged | infrastructure, not dynamics |
| unit_current | 1 | amputated rooted single-leg seed |
| stripped_edge | 1/X | stripped planar cubic internal edge, domain X != 0 |
| kinetic | K | free quadratic action kernel |
| inverse_propagator | (K+i epsilon)/i | algebraic inverse of regulated Feynman propagator, not K |
| feynman | i/(K+i epsilon) | free scalar propagator; epsilon positive, limit not evaluated |
| time_ordered | i/(K+i epsilon) | free vacuum time-ordered two-point function, same expression but distinct type |
| wightman | 2 pi theta(p0) delta(K) | formal free vacuum positive-frequency distribution |
| dressed_feynman | i/(K-Sigma+i epsilon) | convention-defined Dyson expression with explicitly supplied self-energy provenance |
| one_particle_identity | 2 E_p (2 pi)^3 delta^3(p-q) | free stable one-particle S=I overlap; connected T=0 |

The two-point labels do not make the unit current or identity wire into a physical connected two-particle scattering amplitude. Sigma is supplied, never computed by this library. No renormalization scheme or interacting spectral density is inferred.

Each request has a principal-port emission rule using the existing linear output/completion template. Output is a frozen typed Block containing an exact symbolic expression, representation, prescription and convention. Primitive symbolic evaluation is host arithmetic, not a finite alphabet arithmetic net. Publication precedes modeled cleanup completion. Identity transport retains the entire block, including its convention.

The regular-expression product helper refuses distribution multiplication and mismatched conventions. It is not physical sewing or net composition. Delta functions are formal, not pointwise values; no distributional integration, epsilon-to-zero evaluation, or LSZ limit is implemented. General states, retarded/advanced prescriptions, gauge/spin/color structure and arbitrary correlators are outside this scoped library.

Fresh tests cover all ten request types, the propagator/inverse identity, distinct kinetic normalization, time-ordering equality in this convention, Sigma=0 reduction, Wightman/overlap formulas, eight invalid-input controls, linear one-shot emission and separated completion. Existing biadjoint seed regression also passes.

Implementation: `research/nima/checkers/scalar_two_point_primitives.py`.
Checker: `research/nima/checkers/check_scalar_two_point_primitives.py`.
Result: `research/nima/results/scalar-two-point-primitives.json`.

Next for the amplitude ladder: the explicit coupling-stripped cubic vertex and composition rules for channel products/sums, checked against the existing planar biadjoint formula. The scalar correlator library should not be silently mixed with the stripped biadjoint amplitude convention.
