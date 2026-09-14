# The global transform wrapper overstates two dependency scopes

A fresh execution audit captures the declared status lines of three Voevodsky modules.

The global conductor Čech dependency reports:

`left_ringed_morphism: NOT_YET_CONSTRUCTED`.

The framed-identification dependency reports:

`ringed_algebraic_six_functor_lift: NOT_YET_CONSTRUCTED`.

Nevertheless, the global wrapper reports both:

`mixed_variance_transform_components: ALL_CONSTRUCTED`

and

`normalization_sheet_kernel_in_Kato_sector: COMPLETE`.

These scopes are not simultaneously justified by executable dataflow. The safe retained result is the finite cellular/coefficient connector candidate, its local invariants, Čech combinatorics, and the displayed integral pullback complex. The first missing geometric datum occurs earlier than our previous serialization contract stated: it is the left ringed morphism. Only after constructing it can one form and serialize the algebraic six-functor lift and then its road homotopy pullback.

This also blocks geometric realization of the target-typed `(a,b,c)` packet. Nontrivial inertia cannot repair a missing underlying ringed morphism; it is a later coefficient refinement.

Executable evidence: `checkers/check_global_transform_dependency_scope_consistency.py`.
