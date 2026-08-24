# The magnetic interior core is triangular in source coordinates

Companion to `checkers/magnetic_core_triangular_checks.py` and
`results/magnetic_core_triangular.json`.

The oscillatory-core census concealed a simpler all-grade theorem.  In the
source-derived Hall order, the alternate-chart interior core is upper
triangular.

Write a column label as `(a,sigma)`.  Its support interval is

\[
I(a,-)=[-a-g,1-a],\qquad I(a,+)=[g+8-a,2g+9-a].
\]

After removing the two endpoint labels, the semantic order is

\[
(0,+),(2,-),(2,+),(4,-),(4,+),\ldots,(g+8,-).
\]

The Hall observation attached to a label is

\[
r(0,+)=2g+8,
\quad r(a,-)=-g-a,
\quad r(a,+)=g+8-a.
\]

For every label, every observation appearing later in this order lies outside
its support interval.  Hence all entries below the diagonal vanish.  This is
a support theorem, independent of coefficient cancellation.

The diagonal characters are

\[
d(0,+)=-(2g+9)(4)^{\overline g},
\]

\[
d(a,-)=-(3g+7+a)a^{\overline g},
\qquad
d(a,+)=-(g+9-a)a^{\overline g}.
\]

All factors before the minus sign are positive for even `g>=2` and every
admissible label.  Therefore every Gaussian pivot is strictly negative.  The
core has dimension `g+8`, which is even, so

\[
\det A_g=\prod d(a,\sigma)>0.
\]

Thus the apparent fixed-width transport has zero determinant memory here:
the exterior character is already the product of local endpoint characters.
There is no possibility of an internal cancellation or a late rank defect.

The swapped-first-two-rows control remains essential.  It is not a legal
source relabelling, is not upper triangular, and has zero first pivot.  The
theorem belongs to the source-oriented Hall atlas, not to arbitrary matrix
coordinates.

The checker verifies the exact generated matrices through even grade 60,
audits the support inequalities through grade 200, and retains the hostile
row-swap falsifier.  The displayed inequalities and coefficient formulas are
valid symbolically for every even grade.
