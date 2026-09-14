# v88: totalized physical amplitude interface

`rzk/114-physical-comparison-fibre.rzk.md` now constructs the generic strict
fibre of the coefficient/physical difference map, with typed constructors and
projections. It records the H1/H0/negative-cohomology interpretation while
leaving the missing physical comparison map as an explicit input.

`rzk/115-totalized-physical-amplitude-interface.rzk.md` retains endpoint, Cech,
normal-cube, group, and operation-bar coordinates as five distinct totalization
directions. It constructs their generic comparison fibre and defines the type
of an amplitude functional on physical fillings. Homotopy invariance,
specialization compatibility, and symmetry covariance are formulated as Rzk
types.

Both modules pass fresh standalone Rzk typechecks (14 and 17 declarations).
Module 115's symbol closure is one file with no `#assume` declarations.

The next construction gate is concrete rather than formal: instantiate the
physical filling type and its comparison map, then define the supported
trace/residue evaluation inhabiting the amplitude-functional type.
