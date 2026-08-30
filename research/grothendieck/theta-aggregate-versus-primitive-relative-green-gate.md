# All-prime sampling closes to one aggregate flow, but its absolute Green identity is tautological

Status: exact sampling closure and revised relative target; no RH claim

Let the primitive tail feature be

\[
 G(q,z)=e^{-(1/2+iz)q}\int_q^\infty\phi_1(v)e^{izv}dv.            \tag{1}
\]

Its arithmetic samples are the half-line transforms of the individual theta
labels.  Instead of forming their quadratic expression label by label, define
the coherently shifted aggregate

\[
 \boxed{
 \mathscr G(q,z)=\sum_{n\ge1}G(q+\log n,z).
 }                                                     \tag{2}
\]

The source tails make this sum absolutely convergent on every admitted
spectral compact set.

## Sampling closure theorem

Differentiate (2) and use the primitive scale flow.  The forcing sum is

\[
 \begin{aligned}
 \sum_{n\ge1}e^{-(q+\log n)/2}\phi_1(q+\log n)
 &=e^{-q/2}\sum_{n\ge1}n^{-1/2}\phi_1(q+\log n)\\
 &=e^{-q/2}\Phi(q).
 \end{aligned}                                        \tag{3}
\]

Therefore

\[
 \boxed{
 \partial_q\mathscr G(q,z)
 =-(1/2+iz)\mathscr G(q,z)-e^{-q/2}\Phi(q).
 }                                                     \tag{4}
\]

At the modular seam,

\[
 \boxed{
 \mathscr G(0,z)
 =\sum_{n\ge1}G(\log n,z)
 =\int_0^\infty\Phi(u)e^{izu}du.
 }                                                     \tag{5}
\]

Thus sampling at all integer scales, including every cross-label coherence,
closes to one forced Mellin-scale flow whose forcing is the full completed
theta kernel.  No divergent bare character Gram or prime multiplier division
appears.

## Clark differentiation and shear also commute with aggregation

Put

\[
 \mathscr H=(1+ia\partial_z)\mathscr G,
 \qquad
 \mathscr K=\mathscr H-aq\mathscr G.                 \tag{6}
\]

Then

\[
 \mathscr G_q=-s\mathscr G-\mathfrak f,
 \qquad
 \mathscr K_q=-s\mathscr K+(aq-1)\mathfrak f,
 \qquad
 \mathfrak f(q)=e^{-q/2}\Phi(q)>0.                  \tag{7}
\]

Their seam values are the full half-line theta and Clark transforms.  Adding
the reflected chamber reconstructs `X` and `E_a` exactly.

## Why the absolute aggregate Green identity does not prove anything

Applying the positive-bulk Green identity to `mathscr K` gives

\[
 \begin{aligned}
 i(\bar w-z)\int\mathscr K_z\overline{\mathscr K_w}
 ={}&\int(\mathscr K_z-\mathfrak g)
 \overline{(\mathscr K_w-\mathfrak g)}\\
 &-\int\mathfrak g^2
 -\mathscr K(0,z)\overline{\mathscr K(0,w)},          \tag{8}
 \end{aligned}
\]

where `mathfrak g=(aq-1)mathfrak f`.  But the final seam line is now the
complete physical Clark output.  After reflected sewing, its antisymmetric
difference is precisely the de Branges current we are trying to prove
positive.

Hence the aggregate Green identity alone merely moves the target between the
boundary and the bulk.  This explains why the same identity holds for generic
decaying seeds: it has not yet used the arithmetic comparison between the
primitive and completed sources.

## Correct relative target

The arithmetic content lies in the relation

\[
 \mathfrak f(q)=sum_{n\ge1}f(q+\log n),              \tag{9}
\]

not in positivity of either forced flow separately.  The next theorem must be
a **relative Green identity** comparing `(mathscr G,mathscr K)` with the
orthogonal family of shifted primitive flows.

Its desired form is

\[
 \boxed{
 \text{aggregate Clark current}
 =\text{sum of primitive positive bulks}
 +\text{arithmetic interference correction}
 -\text{one primitive seam line}
 -\text{one sheet-odd first-moment line}.             \tag{10a}
 }                                                     \tag{10}
\]

The correction must be computed exactly from overlaps of shifted tails.  If
it is positive, or telescopes with the logarithmic commutator cocycle, it must
repair both declared lines.  If it has another independent negative
direction, the all-prime sampling mechanism fails.

This relative formulation prevents two opposite errors:

1. treating labels as orthogonal after the physical scalar sum, which drops
   interference; and
2. summing first and declaring the generic aggregate Green bulk explanatory,
   which leaves the desired theorem in its own seam term.
