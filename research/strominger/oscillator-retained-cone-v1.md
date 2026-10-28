# Promoted oscillator: retained tetrahedron and standalone triangle recovery

## Binding to existing machinery

Use `ThreeWitnessRetainedCone.Cone`, not a new geometric vertex chosen to complete a drawing. Its arguments here are:

- P: the actual twice-promoted oscillator packet, including nested members;
- first: its raw record presentation;
- second: its source-indexed presentation;
- third: its target-indexed presentation.

The apex is `(P,p)`. The other three vertices are the existing constructor's focused views `(p,select(p),certificate)`. A focus explicitly retains the whole promoted packet; this is the constructor's declared storage, not an implicit copy of the original oscillator supplied to the decoder.

The generic constructor has six path edges, a three-face horn and a call to `RetainedTetrahedralPackage.Cells.build`, which supplies the fourth face and filler. Its comparisons are between lossless presentations. They are not physical propagation paths or assertions that Berry curvature vanishes.

## Fresh specialization tests

`check_oscillator_retained_cone.py` specializes the focus/decoration/recovery maps to both existing promotion endpoint policies. It checks six edge comparisons and inverses, all four direct-versus-composite face equations, and the two whiskered face routes against the direct route.

The triangle opposite the apex is extracted as a separately copied object graph. Its decoder accepts only those three focused vertices, validates their selection certificates and shared retained packet, and returns the actual second-level family records. From this result alone it recovers the intermediate families, original coefficient rows and oscillator readout. No external source packet is an argument to recovery or readout.

For both policies:

    r = 3/5, q = -4/5, |r|^2 + |q|^2 = 1

at the existing resonant fixture. Symbolic expressions agree at arbitrary positive real coupling amplitudes and real detuning within the supplied Markov model.

The bath remains underneath the promoted interface. Deleting its nested coefficient changes the recovered commutator to 9/25. A stale displayed focus and a face combining different retained packets are rejected. Thus the coherent presentation does not hide a corrupted physical payload.

## What is now established

A concrete oscillator binding to the existing **typed retained tetrahedral constructor**, with a standalone recoverable presentation triangle and preserved response/noise, is supplied. The apex is the retained whole already present after promotion; no fourth physical subsystem was invented.

The fresh checker establishes finite/symbolic map equations and recovery. The generic Cubical horn/filler construction is reused from inspected source, not freshly compiled in this work; checking equality of Python maps is not a new proof of all higher path coherence.

This typed tetrahedron does not establish a Euclidean tetrahedral metric or an FCC lattice. Nor does it show that tetrahedral packaging is uniquely necessary: the generic retained-cone constructor accepts arbitrary supplied packets and focus maps. That is the remaining distinction between this positive instance and the governing claim that physical-law domains have the proposed common form.

## Verification

`uv run --with sympy python research/strominger/checkers/check_oscillator_retained_cone.py`, exit zero, execution `structured_command_execution:e_42200_1792520637013020100_33`. Source-hashed receipt: `research/strominger/results/oscillator-retained-cone/verification.json`. No owner-source edits or formal compiler run.
