# Coefficient interface v9: Hom differential and postcomposition

## Checked construction

`rzk/14-hom-complex-window.rzk.md` adds 12 definitions using the Hom-complex
conventions in `references/homotopy-complexes.md` (Stacks 0A8H).

A homogeneous family is the dependent product of component maps
L(i) -> M(shift(i)). A separate predicate records component linearity.
Composition uses composed index translations. Both parity components of the
Hom differential are defined with explicit transports aligning the source
and target degree shifts. Odd includes degree -1:

\[
\delta f=d_Mf-(-1)^{|f|}f d_L.
\]

For an aligned operator window, the module derives delta-squared zero for
both parities from square-zero post/pre operators, their commutation, and
additive/subtractive laws. It does not assume the desired Hom square-zero
identity itself.

A further theorem derives the induced Hom restriction-square identity from
an actual target chain square and preservation of addition/subtraction.
Thus the v7 mapping restriction no longer needs an independent square once
these target and module hypotheses have been instantiated.

For postcomposition h(f)=Hf, both parity components of

\[
\delta h+h\delta=1-(I\Pi)_*
\]

are proved pointwise from dH+Hd=1-I Pi in the target. The source-differential
terms cancel with opposite signs. No source contraction is required. These
lemmas provide the algebraic connection from v8's support contraction to the
Hom-level secondary calculation.

## Exact scope

These are degree-window and componentwise theorems, not yet a fully assembled
integer-indexed DG category. In particular:

- Integer translations and coherence of the transport witnesses must still
  be instantiated. The operator-window hypotheses are not automatically
  synthesized from arbitrary chosen transports.
- Preservation of the supplied linearity predicate, actual module structures,
  and component equality versus equality of whole mapping spaces remain
  obligations. No function extensionality is assumed by the pointwise proofs.
- General graded composition is defined; its full arbitrary-degree Leibniz
  theorem is not proved in Rzk in this increment. The induced degree-zero
  postcomposition square and degree-minus-one contraction cases are proved.
- Hom computes homotopy-category maps in general. RHom requires suitable
  resolutions or applicable projectivity/injectivity hypotheses; the nodal
  source is not declared perfect.
- Product-valued Hom is not replaced by a direct sum. No tensor/Hom comparison
  is promoted from a morphism to an equivalence.

The local reference's final evaluation in Remark 15.73.7 has a type mismatch
(Hom(L,K) where the composition requires Hom(L,M)); no code uses that line.
Its authoritative upstream text has not been re-fetched in this increment.

## Verification

Command:

`pwsh -NoProfile -File research/nima/rzk/check-boundary-framed.ps1 -Module 14-hom-complex-window`

Fresh closure passed, exit 0, `Everything is ok!`: 49 definitions across
modules 11-14 (13 + 8 + 16 + 12). Result with dependency/executable digests:
`results/14-hom-complex-window.typecheck.json`. Execution reference:
`structured_command_execution:e_39824_1788731204424603300_17`.
Persistent LSP feedback was attempted and timed out; no LSP success is claimed.

`checkers/check_hom_complex_window.py` independently checks finite integer
matrix complexes. Its 390 assertions cover Hom square-zero, the full graded
Leibniz composition equation for sampled degrees -3 through 3, postcontraction
for degrees -4 through 4, and projection chain compatibility. The wrong
Leibniz sign is detected in odd degree. Result:
`results/hom-complex-window-control.json`; execution reference:
`structured_command_execution:e_39824_1788731212576982000_18`.
This is a finite exact control, not a Rzk integer-module instance or proof of
unbounded generality. It does not compute physical parity.

## Remaining integration

Instantiate coherent indexing and actual coefficient modules, derive their
operator-window hypotheses, and connect the incoming spatial Gysin map and
its independently constructed Q-homotopy to these Hom components. Then use
v7's secondary witness criterion and v8's support projection. No Q-homotopy
or physical outcome has been selected by this formal layer.
