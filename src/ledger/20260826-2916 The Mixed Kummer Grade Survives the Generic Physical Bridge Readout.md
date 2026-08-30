# 2916 — The Mixed Kummer Grade Survives the Generic Physical Bridge Readout

## Typed operation order

Entry 2914's mixed grade must be tested without conflating three distinct
operations:

1. the source sheet covector on the left triangle;
2. the source sheet covector on the right triangle;
3. the bridge occurrence trace after the ordered \(q_L,q_R\) residue.

Each triangle source covector detects its own marked Kummer class by Entry
2895.  Their tensor product therefore detects

\[
F_LF_R.
\]

## Bridge occurrence factor

Retain resolved bridge occurrences \(y_{34,+},y_{34,-}\).  The physical
diagonal specialization gives

\[
y_{34,+}+y_{34,-}
\longmapsto
2y_{34}.
\]

Consequently the mixed physical readout is

\[
\Phi_{\rm mixed}
=
2y_{34}\,operatorname{FP}_L\operatorname{FP}_R,
\]

up to the already frozen overall sign of the ordered bridge residue.

This is generically nonzero whenever the bridge is nonsoft and the two
individual pointed finite parts are nonzero.

## Why deck-trace vanishing is irrelevant

Tracing the internal two-sheet occurrences inside either triangle before
applying its source sheet covector would kill that triangle's Kummer class.
Entry 2895 proved that such a trace is not the source physical readout.  The
correct source order selects both labelled sheets first and traces only the
resolved bridge occurrence afterward.

## Result

The rank-one mixed Kummer grade survives the generic physical bridge readout.
It vanishes canonically on

\[
y_{34}=0,
\]

which is the already existing bridge-soft support, and on any independently
derived zero locus of an individual finite part.

Thus relations between two local relative-readout classes produce a genuine
global observable without introducing a new carrier stratum.

## Scope and next falsifier

The result remains at the ordered bridge-residue associated grade.  The next
test is extension from that grade to the complete unresidued double-triangle
period: derive the first normal/Rees lift off \(q_L=q_R=0\) and determine
whether the mixed observable persists, becomes torsion, or mixes with bulk
elliptic coefficients.

## Durable artifacts

- `research/benincasa/check_mixed_kummer_physical_readout.py`
- `research/benincasa/mixed-kummer-physical-readout.json`
