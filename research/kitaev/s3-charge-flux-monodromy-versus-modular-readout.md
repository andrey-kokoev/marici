# Mixed charge--flux monodromy versus scalar modular readout in `D(S3)`

Owner: `marici.Kitaev`

## Bounded question

Does a scalar modular entry faithfully represent the underlying mixed-sector
braid operator?

No.  Pure charge `pi` transported around a flux basis state labelled by
`g` acts by the representation matrix `pi(g)`.  On a full conjugacy-class
flux space the monodromy is therefore

\[
M_{\pi,C}=\bigoplus_{g\in C}\pi(g).
\]

This operator is source-derived from the electric representation and flux
label.  Its normalized trace is the modular readout:

\[
\operatorname{tr}M_{a,b}=\mathcal D S_{ab},\qquad \mathcal D=6.
\]

## Zero scalar, invertible operator

For the two-dimensional standard charge `C` around transposition flux
`D` or `E`, the monodromy is the direct sum of the three reflection
matrices.  It has

\[
\chi_M(x)=(x-1)^3(x+1)^3,\qquad
\mu_M(x)=x^2-1,
\]

trace zero and determinant minus one.  It is invertible and non-scalar, while
the modular entry is exactly

\[
S_{CD}=S_{CE}=0.
\]

The zero is cancellation between three plus and three minus eigenvalues, not
absence of braid response.  This is an exact non-Abelian analogue of a coarse
scalar readout erasing a faithful operator-level distinction.

For `C` around three-cycle flux `F,G,H`, the characteristic and minimal
polynomials are

\[
\chi_M(x)=(x^2+x+1)^2,\qquad \mu_M(x)=x^2+x+1,
\]

with trace `-2=6(-1/3)`.  Thus transposition and three-cycle flux families
are distinguished by their operator spectra even before resolving the
centralizer charge.

## Capability kernel

A pure-electric monodromy probe sees the flux element through `pi(g)` but
does not act on the flux sector's centralizer irrep.  It therefore gives the
same operator for `D` and `E`, and likewise for `F,G,H`.  Resolving those
anyon labels requires additional probes carrying magnetic/dyonic coefficient
data.  The scalar modular trace is coarser still: it can vanish on an
invertible non-scalar action.

## Carrier and coefficient allocation

Carrier geometry supplies an oriented linked pair and the conjugacy-class
flux basis.  The quantum coefficient lens supplies the charge representation
matrix, direct-sum internal space, and trace/eigenvalue readouts.  Intersection
alone says that winding occurred; it does not determine the block matrices or
their cancellations.

## Verification

`uv run --with sympy python -u research/kitaev/checkers/check_s3_charge_flux_monodromy.py`
passes seven aggregate gates.  It constructs the exact standard
representation from generators, verifies the group law, audits all six
charge/family pairs, proves invertibility, verifies both minimal polynomials,
and checks `tr M=6S` against the independently frozen modular matrix.

## Claim boundary

This packet derives full monodromy, not elementary exchange `R` maps.  It
does not resolve centralizer irreps within a fixed flux class and does not
choose mixed fusion bases or verify mixed hexagons.  Equality of the `D/E`
operators here is a probe kernel, not equality of those anyons.

The charge--flux action is the finite-group quantum-double mechanism of
[Kitaev](https://arxiv.org/abs/quant-ph/9707021); the open-ribbon representation
spaces are typed in [Cowtan and Majid](https://arxiv.org/abs/2107.04411).  The
trace comparison uses the exact finite-group modular transform of
[Koornwinder et al.](https://arxiv.org/abs/math/9904029).

## Falsifiers

The result fails if the generated standard matrices violate the `S3` group
law, either monodromy is singular, the stated minimal polynomials fail,
`tr M != 6S`, or the zero-entry witness becomes scalar or zero.
