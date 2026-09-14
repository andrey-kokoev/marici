# v131: physical trace theorem for odd reflection

The conditional parity calculation is now an actual Rzk equality proof rather
than a status tag.

Given the strict law `sW = -W + commutator`, an additive readout preserving
negation, a proof that the commutator reads as zero, and the scalar right-unit
law, module 159 constructs a path
`readout(sW) = -readout(W)`. The proof explicitly composes reflection transport,
additivity, negation compatibility, commutator killing, and unit reduction.

Thus odd physical reflection parity no longer needs to be separately chosen
once a commutator-killing additive physical trace is supplied. The unresolved
input is precisely that the concrete physical readout has those properties
(and retains W nontrivially if nonvacuous parity is required).

`rzk/159-physical-trace-selects-odd-reflection.rzk.md` passes all five
declarations without assumptions.
