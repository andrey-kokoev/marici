# Milnor K2 primitive-source gate

## Question

Does the natural Milnor symbol on the exceptional torus realize the missing primitive source filler?

## Claim boundary

On `U=G_m^2`, the symbol `{u,v}` has regulator image

`dlog(u) wedge dlog(v)=Xi_log`.

Its iterated logarithmic residue is one, so it realizes the primitive nonzero exceptional class source-naturally. This is not the required horn: `{u,v}` is a closed motivic/K2 class mapping to cohomological degree two, not a degree-one precycle whose boundary is `Xi_log`. In any regulator-compatible complex, making the symbol a boundary would force its nonzero de Rham image to be exact.

The Steinberg comparator `{u,1-u}` has vanishing dlog wedge because both factors differentiate along `u`; that relation does not apply to algebraically independent `u,v`.

## Disposition

The K2 candidate is rejected as a filler but retained as a sourced realization of the obstruction. The next leaf must test genuine relative higher-Chow or open-change precycles by their complete boundary vector `(Xi_log,-sigma123,0,...)`; a degree shift of the closed symbol is inadmissible.

## Verification

- `research/voevodsky/check_cosmology_milnor_K2_primitive_source_gate.py`
- `research/voevodsky/results/cosmology_milnor_K2_primitive_source_gate.json`
