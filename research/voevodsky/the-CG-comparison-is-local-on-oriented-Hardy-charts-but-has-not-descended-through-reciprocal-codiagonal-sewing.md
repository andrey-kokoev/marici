# The CG comparison is local on oriented Hardy charts but has not descended through reciprocal codiagonal sewing

The `CG` comparison is not wholly absent.  The full-line translation model and
two-port Weyl reservoir already realize, on each oriented Hardy chart, the
source/endpoint cross-entry and weighted Weyl identity.  In cone-package
language this supplies local comparisons

\[
\kappa_{CG}^{+}:X_{CG}^{\rm rec,+}\xrightarrow{\sim}X_{CG}^{\rm Gr,+},
\qquad
\kappa_{CG}^{-}:X_{CG}^{\rm rec,-}\xrightarrow{\sim}X_{CG}^{\rm Gr,-}.
\]

The recent seam work also glues their Fredholm determinant frames and proves
the scalar transition unitary.  That does not yet glue the comparisons above:
a determinant transition forgets the kernel/cokernel package, left cofactor
covector, and oriented cross minor.

Let `J_rec` and `J_Gr` denote the reciprocal chart-sewing maps on the two
candidate `CG` packages.  Descent requires the square

\[
\begin{CD}
X_{CG}^{\rm rec,+} @>{\kappa_{CG}^{+}}>> X_{CG}^{\rm Gr,+}\\
@V{J_{\rm rec}}VV @VV{J_{\rm Gr}}V\\
X_{CG}^{\rm rec,-} @>{\kappa_{CG}^{-}}>> X_{CG}^{\rm Gr,-}
\end{CD}
\]

to commute as a map of flagged cones, not merely after applying `Det`.
Equivalently, the seam defect is

\[
\delta_{CG}
=J_{\rm Gr}\kappa_{CG}^{+}
-\kappa_{CG}^{-}J_{\rm rec}.
\]

The global obstruction `Ob_CG` is therefore refined: its restrictions to both
open Hardy charts are acyclic, and any remaining class is supported on the
seam descent.  The unproved data are the cone-level Green sewing map, equality
`delta_CG=0`, and preservation of the distinguished incidence chamber.

Thus the correct status is:

- local determinant--Green mate: constructed;
- scalar determinant-frame sewing: constructed;
- global flagged-cone mate: not constructed;
- chamber preservation under sewing: not proved.

This localization prevents repeating local bulk analysis.  The next target is
the seam descent square and its cross-minor flag, not another local resolvent
constructor.
