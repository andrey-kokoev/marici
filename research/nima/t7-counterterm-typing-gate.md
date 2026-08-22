# The universal T7 master space cannot type physical counterterms

The frozen asymptotic calculation identifies two independent UV subtraction
directions in the residual of the supported cospan.  This is a theorem about
the universal master-integral space.  It is not yet a theorem about the
counterterms of a physical theory.

The missing arrows are

\[
\text{declared action and numerator}
\longrightarrow
\text{physical coefficient covector on }T_7
\longrightarrow
\text{symmetry-allowed local operator basis}.
\]

The source paper itself keeps these layers separate.  Its universal integral
formula suppresses factors depending on couplings and the cosmological Mellin
weight, and its reduction machinery permits generic numerators.  The nine
objects in the elliptic sector are master forms spanning a differential
system; they are not nine independently declared physical observables or nine
independent counterterm operators.

This distinction is decisive.  On the two-dimensional residual, different
coefficient contractions can activate neither UV grade, either one, or both.
The master-space connection and its supported cospan do not choose among these
contractions.  Furthermore, even an activated divergent combination must be
matched to a local operator compatible with the chosen scalar theory and
cosmological symmetries.

Therefore the strongest presently typed statement is

\[
\boxed{
\operatorname{rank}(\text{universal residual UV image})=2,
\qquad
\operatorname{rank}(\text{physical counterterm image})\text{ undetermined}.
}
\]

The T7 branch cannot be closed physically by quotienting the universal master
space.  The next legitimate calculation must begin with the complete
source-normalized triangle wavefunction integrand for a specified action,
reduce its numerator to the nine-master basis, and compare its UV polynomial
with the symmetry-allowed local operator basis.  Until then, both a complete
cancellation and a surviving physical residual remain possible.

The finite underdetermination witness is
`research/nima/checkers/check_t7_counterterm_typing_gate.py`.
