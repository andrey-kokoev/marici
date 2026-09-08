# Imported mixed normal/Chern result: review and objective impact

Incoming report:
`research/chatgpt/mixed-normal-chern-comparision/mixed_normal_chern_comparison.md`.
This review does not modify ChatGPT's files or select the physical Q-homotopy.

## Reproduced evidence

The read-only wrapper `checkers/check_mixed_normal_chern_import.py` imports the
incoming checker without executing its file-writing main routine. It writes
only `results/mixed-normal-chern-replay.json`, including input hashes, the full
Hom matrices, operator columns and integral detector.

- All **2,755** incoming exact checks passed.
- All **215** Cech differential columns, cell ordering and degrees matched the
  live `research/voevodsky/check_ringed_alexandrov_pc_target.py` exactly.
- The 16 endpoint states form a subcomplex, giving a **199-generator** finite
  endpoint-relative source. It is not the 208-generator quotient by Q, nor the
  normalization source assumed in the separate physical connector problem.
- The previously untested negative Hom slice degrees -3,-2,-1 are empty;
  all source/target chain degrees lie in [0,3], excluding further degrees.
- T, H and the radial defect each have five columns.
- Replay completed in 168 ms, with input hashes unchanged.
- Execution: `structured_command_execution:e_39824_1788734125984168500_39`.

This matches the live coefficient target, but does not authenticate the commit
identifier asserted in the incoming report. No Git operation was performed.
This is exact Python verification, not an Rzk certificate.

## What the derived argument now supplies

Set R0=Z[X_d,u_d]. The source E_fin=P_fin/V_fin is bounded and termwise finite
free over R0: V is the full, differential-stable endpoint summand and the
quotient has the remaining basis. Consequently Hom_R0(E_fin,E_Cech) computes
RHom_R0(E_fin,E_Cech), regardless of the localized target's failure to be free.
This supplies the needed projectivity justification for THIS coefficient pair.
It is stronger than a nonzero class in Hom with a localized source.

In fine weight w=-e_u03-e_u13, the complete mapping complex has ranks
(5,24,36,16), differential ranks (5,19,16), and only unit nonzero Smith factors.
Unit Smith factors imply saturated images in the free cochain groups, so the
rank calculation yields torsion-free cohomology, with H2=Z and all other
cohomology in this weight zero. The detector annihilates every column of the
24-to-36 differential and evaluates T_Cech Lambda to one. This both excludes
an integral primitive and establishes that the class is primitive.

A derived-null T_Cech would have derived-null composite with Lambda. The
nonzero detected composite therefore proves T_Cech is nonzero in D(R0).
This inference does not require Lambda to be a quasi-isomorphism. The
nonhomogeneous monodromy-unit localization argument separately clears finite
denominators and extracts the original weight, rather than assuming that
localization preserves the fine grading.

## Boundaries that must remain distinct

- The degree-four primary Chern operation vanishes under derived augmentation.
  The nonzero class is its specified ordered secondary comparison, not the
  primary operation surviving augmentation.
- The local Cech primitive has global defect R: dH+Hd=T+R, not T. Omitting those
  five radial columns would give the wrong global conclusion.
- The independent Chern/monodromy four-state differential is curved:
  D2=(c03*u03+c13*u13)1. It cannot be admitted as a square-zero instance of
  Nima module 17 on this independent coefficient base.
- Vanishing Q and endpoint components supplies strict compatibility for these
  particular operators. It does not construct the normalization connector or
  its missing prescribed homotopies.
- A nonzero target endomorphism may annihilate the distinguished connector.
  T kappa and a physical homotopy-group interpretation remain uncomputed.
- The rational stabilizer interpretation is not integral E-infinity formality.

## Updated original-objective status

Original objective: coherent integer indexing, concrete coefficient modules,
and derived-Hom realization status.

1. Modules 15-17 give checked indexing and actual integer Hom square zero,
   with a concrete Z-squared target instance. Full linear DG packaging remains.
2. The incoming calculation now supplies a concrete polynomial/localized
   coefficient construction and a reproducible nonzero derived class, matched
   to the live target. Those modules and matrices are NOT yet instantiated
   as Rzk coefficient objects.
3. For the finite-to-Cech coefficient pair, the derived-Hom model is justified
   by the bounded free source. For the normalization-to-physical pair, the
   replacement/model and mapping-space fibre comparison remain unresolved.

The original objective cannot yet be claimed fully fulfilled in Rzk. The next
concrete formal coefficient target should use this specified finite-to-Cech
mapping slice and its exported detector, rather than invent another pilot or
continue describing every derived-Hom model as wholly unavailable.
