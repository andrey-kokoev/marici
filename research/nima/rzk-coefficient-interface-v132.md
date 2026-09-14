# v132: cyclic physical trace kills commutators

The commutator-killing premise needed by the reflection theorem is now derived
from standard trace structure.

Module 160 proves in Rzk that an additive readout preserving negation and
satisfying cyclicity sends `xy-yx` to zero. The proof explicitly transports the
commutator identity through the readout, distributes over addition and
negation, applies cyclicity, and cancels a scalar with its inverse.

Combined with module 159, odd physical reflection parity follows from cyclicity
of the concrete supported readout. The remaining gate is therefore narrower:
prove that the supported physical trace used by the amplitude is cyclic on the
specific native products `r11*r00` and `r00*r11`; no separate commutator
vanishing axiom is needed.

`rzk/160-cyclic-physical-trace-kills-commutators.rzk.md` passes all five
declarations without assumptions.
