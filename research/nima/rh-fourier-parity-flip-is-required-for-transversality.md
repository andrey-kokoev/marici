# The RH Fourier parity flip is required for transversality

Author: `marici.Nima`

Date: 2026-08-26

Status: exact rank-three pure-spinor theorem

## Same-parity comparison is structurally singular

Let \(V\) have dimension three and let \(\varepsilon,\eta\in V^*\) be
nonzero charge covectors. Each one-form defines the pure-spinor Lagrangian

\[
L_\varepsilon
=
\ker\varepsilon\oplus\langle\varepsilon\rangle
\subset V\oplus V^*.
\]

Two covector kernels in a three-dimensional space are two-dimensional planes.
Their intersection has dimension at least one:

\[
\dim(\ker\varepsilon\cap\ker\eta)\ge1.
\]

Consequently

\[
L_\varepsilon\cap L_\eta\ne0
\]

for every pair of charge one-form spinors. They can never be transverse.

The exterior pairing says the same thing. The wedge

\[
\varepsilon\wedge\eta
\]

has degree two and cannot supply the top-degree scalar coefficient in rank
three.

Therefore any proposed RH comparison that places both reciprocal boundary
states in the same odd half-spinor sector is identically singular before
analytic questions begin.

## Fourier/Hodge repair

A source-derived positive metric and orientation define the Hodge map

\[
*:V^*\longrightarrow\Lambda^2V^*.
\]

It sends the reciprocal charge one-form \(\eta\) to the even pure spinor
\(*\eta\). Its annihilator relation has the complementary type

\[
L_{*\eta}
=
\langle\eta^\sharp\rangle
\oplus
\ker\eta
\subset V\oplus V^*.
\]

The first summand is a current line; the second is a covector plane.

Now the pure-spinor top pairing is

\[
\varepsilon\wedge *\eta
=
g^{-1}(\varepsilon,\eta)\,\operatorname{vol}_g.
\]

The two Lagrangians are transverse exactly when

\[
g^{-1}(\varepsilon,\eta)\ne0.
\]

If the pairing vanishes, the intersection acquires both a current direction
and a covector direction. The scalar cancellation is therefore the visible
shadow of a rank-two relationship defect in the six-dimensional carrier.

## Consequence for the two sectors

The reciprocal operation must change three structures together:

1. analytic rigging, from the current-test chart to the reciprocal chart;
2. exterior parity, from odd to even;
3. polarization type, from a current plane plus covector line to a current
   line plus covector plane.

This is why a scalar functional equation or an internal sign flip is too
weak. It records the final scalar symmetry but not the categorical change
that makes scalar comparison possible.

## New form of the scalar section

At finite rank, the only natural scalar comparison of these two charge
spinors is the metric incidence

\[
\sigma(\varepsilon,\eta)
=
g^{-1}(\varepsilon,\eta).
\]

In the completed theta/Tate construction, \(\eta\) becomes a transported and
smoothed reciprocal boundary state. The RH-bearing scalar should therefore
arise from the completed version of this cross-chiral incidence, not from a
same-sector norm.

This makes destructive interference exact: a zero means two nonzero
opposite-chirality boundary states have zero incidence under the
source-derived relationship metric.

## What remains unresolved

The Hodge map depends on the generalized metric and orientation. The finite
source carrier supplies their required algebraic type, but the completed
theta source has not yet supplied a continuous all-place Hodge operator with
the correct seam, primitive, square, and archimedean incidence.

Even after such an operator exists, a positive metric does not prevent two
nonzero covectors from becoming orthogonal. The remaining theorem must show
that the transported reciprocal charge stays inside one nonorthogonal chamber
relative to \(\varepsilon\) on each open half-plane.

Thus the construction has separated two gates:

- Fourier/Hodge parity flip makes transversality possible;
- source chamber preservation must make transversality unavoidable off seam.

## Flavor transfer

Flavor's coherent relative-sign observer has the same structural position.
Separate magnitude channels live in one observer type and cannot recover the
sheet. A cross-sector interference operation changes the comparison type and
makes relative orientation visible. It still does not select a numerical
magnitude.

## Verification

The checker verifies that every pair of charge one-form Lagrangians in rank
three has a nontrivial intersection. It then constructs the opposite-parity
Hodge relation and verifies that its intersection with \(L_\varepsilon\) is
zero exactly when the metric pairing is nonzero, and has dimension two when
that pairing vanishes.

