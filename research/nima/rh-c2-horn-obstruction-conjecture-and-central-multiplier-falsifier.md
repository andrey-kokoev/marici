# RH C2 horn-obstruction conjecture and central-multiplier falsifier

## Strong conjecture

Let `N_src` be the source-derived nerve of the completed theta/Tate system.
Its zero-cells contain the typed source, sheet, cutoff, boundary, and observer
states. Its one-cells are the authorized transports. Its two-cells are the
source comparison laws among transport factorizations.

Let `B(s)` be the complete one-dimensional boundary produced by evaluating the
two-sector packet at a spectral parameter `s`.

The strongest proposed theorem is:

> Every boundary produced by a genuine theta/Tate source admits its canonical
> two-cell filler. If the completed scalar section vanishes away from the seam,
> the induced boundary has a nonzero two-dimensional obstruction and admits no
> filler.

If both clauses were source-derived, an off-seam zero would imply that one and
the same source boundary is both fillable and unfillable.

## Required obstruction map

The conjecture needs a source-defined map

\[
\operatorname{Obs}_2:B(s)\longrightarrow Q_2
\]

with three properties:

1. every constructible source boundary lies in `ker(Obs_2)`;
2. an off-seam scalar zero forces `Obs_2(B(s))` to be nonzero;
3. `Obs_2` is derived without division by the scalar section or inspection of
   its divisor.

The second property is the zero-to-obstruction bridge. Without it, the
conjecture merely renames RH.

## Central-multiplier attack

Choose a complex number `a` away from the seam and away from zero and one.
Define

\[
h_a(s)=\frac{(s-a)(s-(1-a))}{a(1-a)}.
\]

Then

\[
h_a(1-s)=h_a(s),
\qquad
h_a(0)=h_a(1)=1,
\]

while `h_a` has the off-seam zeros `a` and `1-a`.

Given any scalar section `sigma`, form

\[
\widetilde\sigma(s)=h_a(s)\sigma(s).
\]

This modification preserves reciprocal symmetry and endpoint normalization.
If `h_a` is installed as a central scalar decoration common to every path,
then it also preserves:

- equality of parallel composites;
- associativity and interchange;
- all ordinary commuting diagrams;
- every two-cell whose law is homogeneous under common central scaling.

Nevertheless, it inserts two off-seam zeros.

Therefore ordinary two-categorical fillability, even for the complete lower
diagram, cannot by itself imply zero exclusion.

## Exact finite model

Take the terminal strict two-category: one object, one one-cell, and one
two-cell. Every horn has a unique filler. Attach either the constant scalar
section `1` or the section `h_a`. The categorical data and all fillers are
identical, while only the second readout has off-seam zeros.

This is a complete falsifier to any conjecture in which the scalar section is
merely an external readout of the two-category.

## Finite normalization does not repair the conjecture

The attack survives any finite collection of scalar normalization
checkpoints. Given a reciprocal-invariant finite checkpoint set, choose a
symmetric polynomial `p` that vanishes on every checkpoint. For an off-seam
point `a` with `p(a)` nonzero, put

\[
h(s)=1-\frac{p(s)}{p(a)}.
\]

Then `h` equals one at every checkpoint, is invariant under reciprocal
reflection, and vanishes at both `a` and `1-a`.

For example, the checkpoint set consisting of zero, one half, and one is
preserved by

\[
p(s)=s(s-1)(s-1/2)^2,
\qquad
h(s)=1+\frac{256}{3}p(s).
\]

This `h` equals one at all three checkpoints and vanishes at one quarter and
three quarters. Therefore finitely many scalar normalizations do not fix the
central divisor gauge. The repair must be an operator-valued or local source
law, an infinite uniqueness condition, or another structure that is not
preserved by these interpolating multipliers.

## Surviving strengthened conjecture

A viable obstruction must fail central-scalar invariance. The scalar section
must be generated internally from source two-cells through a non-homogeneous
normalization, curvature, index, resource, or boundary law that detects
central divisor insertion.

Equivalently, the diagram needs a typed determinant-line action and a
source-fixed trivialization sufficiently rigid that multiplying by `h_a`
changes the two-dimensional obstruction class.

The strengthened DPC is:

1. construct the two-cell filler law from labelled theta/Tate operations;
2. construct the scalar section from that same law, rather than attaching it
   afterward;
3. identify the exact non-homogeneous datum fixing its central scalar gauge;
4. prove that the hostile multiplier changes that datum;
5. only then test whether an off-seam zero forces a missing filler.

## Verdict

The naive C2 horn-obstruction conjecture is false. Higher coherence alone is
blind to a common central symmetric multiplier. The route remains alive only
in the stronger form: a source-normalized C2 obstruction theory whose internal
determinant or boundary law detects central divisor insertion.
