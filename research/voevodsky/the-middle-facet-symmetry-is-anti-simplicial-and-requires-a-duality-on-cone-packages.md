# The middle-facet symmetry is anti-simplicial and requires a duality on cone packages

Fresh inspection of the cone-package contract corrects the initial symmetry
claim.  The reversal

\[
[S,A,R,C,G]\mapsto[G,C,R,A,S]
\]

is not a simplicial automorphism of the ordered standard simplex: the simplex
category permits order-preserving maps, while this reversal is
order-reversing.  The proposed symmetry must therefore be typed as an
anti-simplicial duality, not as an ordinary action on `Delta^4`.

Let `K` be the category of faithful flagged cone packages.  The required datum
is a contravariant involution

\[
(-)^\vee:\mathcal K^{op}\longrightarrow\mathcal K
\]

with coherent bidual comparison, together with object-level identifications

\[
X_S^\vee\simeq X_G,\qquad
X_A^\vee\simeq X_C,\qquad
X_R^\vee\simeq X_R.
\]

Only after these maps are constructed does reversal induce

\[
d_i\longleftrightarrow d_{4-i}.
\]

The middle facet is fixed only setwise:

\[
[S,A,C,G]^\vee=[G,C,A,S],
\]

which is the opposite orientation of the same four vertices.  Calling this
facet self-dual consequently requires comparison cells between every edge and
its reversed mate:

\[
SA\leftrightarrow CG,
\quad SC\leftrightarrow AG,
\quad SG\leftrightarrow SG,
\quad AC\leftrightarrow AC.
\]

(The last two are setwise-fixed edges and require Hermitian/skew orientation
data rather than automatic equality.)  The four triangular faces similarly
pair as

\[
SAC\leftrightarrow ACG,
\qquad
SAG\leftrightarrow SCG.
\]

This gives the first exact issue for the restarted cycle.  Existing reciprocal
resolvent and determinant conjugation results provide candidates for some
edge mates, but the repository has not yet supplied one contravariant duality
functor on the common flagged cone-package category, nor the bidual and
triangle coherences.  Scalar sharp identities are shadows of this structure,
not substitutes for it.

Accordingly, `[S,A,C,G]` is currently a candidate self-dual facet rather than a
literal one.  The next audit must type its six edges as cone-package morphisms
and classify the two fixed edges `SG` and `AC`; only then is it meaningful to
ask for a tetrahedral filler or a finite Xi-sensitive mate cell.
