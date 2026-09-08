# v73: W03 Cech support and reciprocal-trace descent

Independent replay passed 24,450 checks.

`rzk/99-w03-cech-support-trace-descent.rzk.md` records the complete supported
Hom calculation for `V(X02,X35)`: cochain ranks `(9,66,151)`, differential
ranks `(9,55)`, and rank-two cohomology. The two reciprocal trace classes have
explicit independent lifts through the local-cohomology counit, with an
integral cycle basis.

The literal mixed occurrence-Laurent continuation is impossible over the
normalization node: since `X02*X35=0`, simultaneously inverting both produces
the zero ring. Separate localizations remain nonzero, and their homotopy fibre
is the correctly typed supported target retaining both trace classes and both
edge endpoints.

The Rzk module passes a fresh check. This is coefficient-supported trace
descent, not a scalar trace, geometric Gysin identification, or physical
conductor--Morse class.
