# Fourier exchanges two cyclic valuation towers

## Question

Ledger 3864 retyped the square observer as a cyclic two-copy evaluation. Does
the additive Fourier operator act on that cyclic tower as an endomorphism?

## Normalized dilation reversal

On the real additive carrier, use the unitary dilation

\[
(U_qf)(x)=e^{q/2}f(e^qx).
\]

For the standard Fourier convention, direct change of variables gives

\[
\mathcal F U_q=U_{-q}\mathcal F.
\]

For a prime `p`, the positive valuation generator corresponds to
`q=log p`. Fourier sends it to `-log p`, which is not in the positive
valuation monoid.

This obstruction survives at every cyclic arity:

\[
\mathcal F^{\otimes k}U_q^{\otimes k}
=U_{-q}^{\otimes k}\mathcal F^{\otimes k}.
\]

Fourier preserves cyclic word length `k`, but reverses valuation orientation.
It therefore exchanges the primitive, square, and connected-tail grades of
two opposite towers; it does not act within either unilateral tower.

## Minimal Fourier-stable completion

Let

\[
M=\bigoplus_p\mathbb N
\]

be the free commutative prime-valuation monoid. Its positive cone records
ordinary integer labels. The smallest dilation label object closed under
Fourier reversal is its Grothendieck group

\[
M^{\mathrm{gp}}=\bigoplus_p\mathbb Z.
\]

Equivalently, integer dilations must be enlarged to positive rational
dilations. The two cones

\[
M_+=M,
\qquad
M_-=-M
\]

meet at the vacuum and are exchanged by Fourier.

The correct cyclic source is consequently not one tower but a sewn pair

\[
\operatorname{Cyc}(M_+)
\underset{\mathcal F}{\longleftrightarrow}
\operatorname{Cyc}(M_-).
\]

At cyclic grades one and two, Fourier has the types

\[
\mathcal F_1:C_1(M_+)\to C_1(M_-),
\qquad
\mathcal F_2:C_2(M_+)\to C_2(M_-).
\]

Thus a purported Fourier endomorphism of the positive Euler determinant
packet is ill-typed unless it has already forgotten valuation orientation.

## Relation to unilateral boundary defects

On the full scale line, reversal is invertible and the paired construction is
flat. Choosing the physical half-line is a polarization. Translation then
becomes a unilateral shift, and the missing inverse creates the known moving
window projection.

The boundary defect is therefore not an imperfection of the bilateral cyclic
source. It is the incidence data of the inclusion

\[
M_+\hookrightarrow M^{\mathrm{gp}}
\]

after polarization. This explains why primitive and square currents must be
retained at the interface: they are the first two cyclic grades of the data
lost when the opposite cone is omitted.

## Consequence for observer naturality

The earlier target

\[
J\mathcal F=\mathcal F_{\mathrm{Tate}}J
\]

must be replaced by a comparison square whose right side changes objects:

\[
J_-\mathcal F_A
\Longrightarrow
\mathcal F_{+-}J_+.
\]

Here `J_+` and `J_-` land in opposite cyclic valuation towers, while
`F_+-` is the source-derived sewing equivalence. Only their relative
determinant lines may subsequently be compared. Literal equality inside one
positive Euler target would silently identify the two cones.

## Smallest falsifier

At one prime, let `e_r` denote valuation `r`. Positive Euler transport has
`r>=0`. Fourier reversal requires

\[
e_1\longmapsto e_{-1}.
\]

Any proposed one-tower Fourier operator that returns an element with
nonnegative valuation has either discarded orientation or inserted an
unrecorded projection. At square grade the same witness is

\[
e_1\odot e_1\longmapsto e_{-1}\odot e_{-1}.
\]

No larger cutoff is needed.

## Result

The missing Fourier action on the cyclic observer tower does not exist as an
endomorphism of the positive Euler carrier. Fourier requires the bilateral
group completion of the prime-valuation monoid and exchanges two polarized
cyclic towers. The next construction is their relative sewing correspondence,
including the boundary incidence of each cone, rather than a single-tower
naturality equation.
