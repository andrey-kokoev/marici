# The reflection nullhomotopy first fails at the loaded face grade

Date: 2026-08-23

The independently derived carrier nullhomotopy can be tested grade by grade
against the frozen literal support diagram.

Its forced degree-zero map uses six edges

\[
\{S_{\rm src}(i),S_{\rm lit}(i)\},\qquad 0\le i<6.
\]

These are exactly the six same-sheet short-facet edges.  Each endpoint pair
has a one-label literal intersection, so the degree-zero homotopy has an
ordinary support-preserving lift.

The next homotopy equation is nonzero and uses the triangular cells derived
from the legal one-skeleton.  There are exactly eight such cells.  The
intersection of the three frozen literal endpoint supports is empty for
every one of them.  Consequently no ordinary face-poset object can carry
the required degree-one homotopy:

\[
\boxed{
H_0\text{ lifts ordinarily},\qquad
H_1\text{ requires extraordinary support change}.
}
\]

Thus the carrier nullhomotopy does not lift to the ordinary loaded category.
The first obstruction is precisely typed: extraordinary Beck--Chevalley
face cells are required. A joint integral solve shows that the top
homotopy can be gauged to zero, so the primitive relative interior controls
homotopy ambiguity but is not an additional required coherence cell for
this reflection comparison.

Imposing the stronger condition that (H_1) use only mixed faces yields a
unique integral solution with (H_2=0).  Hence the minimal repair consists
of six mixed extraordinary face cells.  Neither pure-sheet face is needed
for this reflection comparison.

This does not prove that the extraordinary lift exists.  It proves that the
universal conductor/mixed-variance mechanism is required at the first
failed grade rather than being optional architecture.

Evidence:

- `research/nima/checkers/check_tate_reflection_discrepancy_homotopy.py`
- `research/nima/checkers/check_tate_reflection_loaded_support_gate.py`
- Entries 258, 324--325, 328, and 627.
