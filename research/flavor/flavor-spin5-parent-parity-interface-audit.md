# Spin(5) parent-parity interface audit (WP896)

## Question

Do the reused dimuon and tau response objects carry enough generator typing to
serve the CP-even Spin(5) radial source?

## Dimuon branch

Yes, conditionally. WP239 does not infer the decaying particle from the
`MA-130` dataset label. Its event operation selects generator muons whose
mother has PDG identifier 25, and the reconstructed parent masses give the
two WP893 poles. In the generator convention this is a neutral CP-even Higgs
state. Thus the MSSM `MA` token labels the parameter point; it is not the
event-level parent identity used by the instrument.

This preserves WP893's CP-even dimuon adapter on its frozen small-mixing,
no-exotic-decay slice. It does not establish equivalence to a PDG-36
pseudoscalar response.

## Tau branch

The WP251--WP256 tau operation contains no generator-parent PDG or parity
field. Its provenance names an MSSM bottom-associated tau dataset, but the
selection tests trigger and reconstructed-object coherence, not ancestry.
Consequently the finite tau templates remain valid source-labelled detector
records, while transfer of those shapes to a CP-even Spin(5) radial parent is
not typed.

The missing field occurs before detector interpolation:

\[
\text{Spin(5) CP-even radial source}
\longrightarrow
\text{generator-level tau parent}
\longrightarrow
\text{CMS response}.
\]

## Disposition

WP895's direct-pole source cards must therefore declare and validate a neutral
CP-even parent with PDG-25-like Higgs couplings, rather than copying only the
MSSM dataset name or mass. The emitted event record must include the parent
identifier, spin/parity model, daughter ancestry, width, and source-card hash.

The smallest falsifier is any selected tau event whose declared signal
daughters cannot be traced to the admitted CP-even parent. A mixture of parent
types must be split into separately normalized response columns. WP896 is a
typing correction, not a selector and not an executed tau instrument.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp896_spin5_parent_parity_interface_audit.py
~~~
