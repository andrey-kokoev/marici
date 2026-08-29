# Rank-one portal sewing is sufficient but forms a selector torsor

At the continued rational point

\[
(g,d)=\left(6,\frac{17}{3}\right),
\]

the reduced odd collision core has rank two. Its primitive integral null
direction is

\[
v=(147407,-131220,38556).
\]

This is the exact local residual direction suggested by the vanishing core
determinant.

Let \(F\) be the full nine-row path map on the same three candidate columns.
It has rank three, and

\[
w=Fv
\]

is nonzero. In the canonical row ordering \(0,\ldots,8\),

\[
w=
(0,0,0,-17656934400,1799280000,-350259840,
59270400,-2016000,-2620800).
\]

Thus the local core relation fails globally in exactly six tail rows.

## Minimal algebraic sewing

An operator-changing portal correction \(K\) activates \(v\) precisely when

\[
(F+K)v=0,
\qquad\text{equivalently}\qquad
Kv=-w.
\]

Since \(w\ne0\), \(K\) cannot have rank zero. Rank one is sufficient: choose
any covector \(\phi\) satisfying

\[
\phi(v)=1
\]

and set

\[
K=-w\otimes\phi.
\]

Then \(Kv=-w\). Hence the minimal algebraic portal correction has rank one.

## Selector torsor

The equation \(\phi(v)=1\) does not select a unique covector. Its solutions
form an affine plane translated by

\[
\operatorname{Ann}(v)=\{\psi:\psi(v)=0\}.
\]

All three coordinate gauges are available because every coordinate of \(v\)
is nonzero. They agree on the desired kernel direction but differ on generic
complementary source directions. A successor readout can therefore distinguish
them.

This is the portal analogue of Kitaev's protected-kernel shear torsor:

- the desired cancellation fixes \(K\) only on the line spanned by \(v\);
- it leaves \(K\) undetermined on the two-dimensional complementary quotient;
- selecting a point requires a source-derived relation line, locality rule,
  symmetry, endpoint incidence, or protected-readout condition.

## Interpretation

We have now separated existence from authority.

A rank-one portal capable of activating the rational magnetic state certainly
exists algebraically. But the universal construction

\[
K=-Fv\otimes\phi
\]

is fitted from the desired null vector. It is not an explanation and carries
no source authority by itself.

The next legitimate theorem must derive \(\phi\), or equivalently the action of
\(K\) on complementary source directions, from an independent constructor.
The cleanest possibility is a charged cross-sector tail incidence whose
endpoint anchor forces one covector. If no such datum exists, the portal
remains a two-parameter family of equally valid algebraic activations.

## Scope correction: activation is not explanation

The complete fractional three-column transport is already injective. Its
reduced scalar/core coordinate can vanish because a projection forgets the
nonzero tail obstruction \(w\). Therefore the rank-one construction above
does not explain why the scalar residual vanishes. It performs a stronger
operation: it changes the full transport so that a projected interference
direction becomes an actual kernel.

Accordingly, the honest order of questions is:

1. authorize or reject the enlarged labelled fractional source grammar;
2. retain its full route and charge packet;
3. explain the scalar projection and orientation of its interference crossing;
4. introduce a portal only if an independent source law genuinely couples or
   quotients those labels.

Without step 4 authority, portal activation is artificial kernelization.

The falsifier is a source symmetry or incidence law that selects a unique
\(\phi\) from the affine plane. A second falsifier is a proof that every
allowed \(\phi\) gives identical protected outputs, which would make the
torsor operationally irrelevant. Exact coordinate gauges already disprove
that second possibility for unrestricted successor observations.

Replay:

\`python research/strominger/checkers/magnetic_rank_one_portal_sewing_checks.py\`