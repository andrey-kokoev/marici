# Arithmetic Loewner kernel completion is the current Deutsch--Popper target

Let `K_F(x,y)=(F(y)-F(x))/(y-x)`, where
`F(t)=(4t-1) Xi'(s)/((2s-1)Xi(s))` and `t=(s-1/2)^2`.

## Conjecture

There is a source-defined map `R(x)` into one Hilbert space, constructed from
the completed prime--theta correspondence without using Xi zeros, such that

\[
 K_F(x,y)=R(x)^*R(y)
\]

throughout the natural positive source domain. Its minimal kernel completion
carries a canonical positive self-adjoint resolvent generator. After integer-
residue multiplicity amplification, its symmetric regularized determinant is
completed Xi and its trace identity is the prime-power explicit formula.

This explains all finite positivity inequalities as compressions of one
correspondence. Loewner theory then reconstructs self-adjointness from source
positivity rather than assuming it from a zero-derived operator.

## Direct falsifiers

The conjecture fails if a finite Loewner minor is negative, source
factorizations disagree under compression, the induced relation is not
closable, its closure is not canonically self-adjoint, the determinant has the
wrong zero divisor or multiplicities, or the trace formula misses any gamma or
prime-power term.

Global Loewner positivity is RH-equivalent under the established pole
identification. The source-factorization requirement is the added explanatory
content: it forbids reconstructing the Hilbert space retrospectively from a
zero list. Positivity through rank six is now certified on the entire central
interval `[0,0.01]`. Rank seven and higher, extension beyond the central
interval, the zero-free source factorization, and operator completion remain
open; RH is not proved.

## Source-measure no-go boundary

Positivity and evenness of an upstream theta-type measure cannot by themselves
produce the conjectured Gram kernel. An exact symmetric four-atom measure has
positive `F'(0)` but violates the first coupled diagonal condition

\[
 2F'(0)F'''(0)-3F''(0)^2\ge0.
\]

This strengthens the earlier scalar theta-cumulant no-go: the obstruction
survives the boundary transformation `F(t)=(4t-1)ell'(t)` and reaches local
Loewner positivity itself. See
`positive-even-measure-loewner-curvature-falsifier.md`.

Therefore the explanatory bridge must establish something genuinely stronger,
such as an order-two Stieltjes representation for `F'`, from the special
arithmetic structure of completed Xi. Assuming its spectral poles on the
negative real axis would merely import RH and is not an admissible derivation.

## Preferred rank-uniform attack

The Pick inequality has a simple geometric equivalent. If

\[
 X(t)=\Xi(\tfrac12+\sqrt t),\qquad
 t=\tfrac14+r e^{i\theta},
\]

then

\[
 \operatorname{Im}F(t)=-4\,\partial_\theta\log|X(t)|.
\]

Thus the preferred universal target is: on every upper semicircle centered at
`t=1/4`, the modulus of `X` is nonincreasing as the angle runs from zero to
pi. This is equivalent to the Pick gate, but exposes a possible source proof
through a theta modular rotation-comparison principle. It also has the
smallest possible hostile test: a single strict modulus increase between two
angles falsifies the conjecture. See
`quarter-centered-angular-modulus-pick-equivalence.md`.

Theta positivity already proves that every such arc stays below its initial
modulus and that its terminal modulus is no larger than its initial modulus.
Hence the remaining obstruction is exactly an interior rebound below a
decreasing positive-theta envelope. Equivalently, one must control the rate at
which the modulus of a tilted theta characteristic function can regain phase
coherence while the real tilt decreases along the arc.

The complex region is now certified through `|t|<=17/2`: throughout its upper
half, `Im F(t)>0` with directed margin exceeding `0.00840024 Im(t)`. Positive
normalized theta coefficients simultaneously prove source analyticity through
`|t|<=9`. This uses no zero locations. See
`central-complex-pick-radius-seventeen-halves-certificate.md`.

This disk closes the hostile inner cone in the two-copy theta decomposition
and continues through the outer annulus `1/4<|t|<=17/2`. In the remaining
outer region, both geometric coefficients are nonnegative. It is therefore
sufficient there to prove the first-quadrant property `Re(B'/B)>=0` and
`Im(B'/B)>=0` directly from the theta source.

The first proposed source transport for that outer theorem has now been
falsified: fixed-`S`, fixed-label adjacent shifting by `pi/b` fails locally on
the `S=0` fiber. The failure does not touch the Pick inequality. The surviving
canonical test integrates the exact labelled conditional law `S|D` first and
then tests adjacent whole-band residuals; it is a distinct conjecture, not a
repair inferred from the desired scalar sign.

That conditional adjacent-block mechanism is itself now enclosed strictly
below zero on the exchange orbit `{(1,2),(2,1)}` at `a=1,b=11` by the exact
A/B source-reflection reduction and directed-binary64 boxes. The remaining
formal gaps are explicit: certified transcendental rounding, exact `pi`
partition endpoints, and a checked analytic tail bound. A canonical
larger-block scan stays negative on the same orbit, even though the dominant
`(1,1)` channel and total scalar direction remain positive. This preserves the
faithful-transport lesson: scalar positivity does not identify a unique
labelwise cancellation law. The initially proposed negative large-frequency
coefficient was checked and retracted.

The high-frequency replacement is now source-derived. The labelled two-copy
kernel factors exactly through one-copy transforms `Z_n(z)`. Individual folded
labels carry nonzero odd boundary jets and therefore spurious algebraic
Fourier tails; the full modular label sum cancels every odd jet at the sewing
point. A 70-decimal audit verifies these cancellations through odd order nine
at relative scale about `1e-68`. Consequently, high-frequency estimates must
resum the complete theta source before folding, taking absolute values, or
integrating by parts. See `theta-modular-jet-sewing-mechanism.md`.

At rank four, the naive continuum box loses correlations, but exact Newton
divided differences certify all 330 quadruples on the central `0.001` grid.
The grid plus a directed global derivative bound now proves continuum rank
four on `[0,0.01]`. Rank five is the next finite-rank gate.

At rank five, degree 29 resolves the high-derivative tail and structured
Newton--`LDL*` certifies all 462 distinct central grid quintuples. The
continuum rank-five interpolation is now the active gate.

All 3003 confluent and separated rank-five anchors now pass. Direct
determinant transport is provably too coarse by four orders; differentiated
`LDL*` pivot transport is the remaining central rank-five gate.

At the weakest anchor, differentiated pivot transport has safety factor above
72,000. Extending that derivative enclosure from the anchor to its whole cell
is now the precise remaining step.

Natural interval propagation across that cell is falsified as an efficient
route: it loses about five orders in the fifth pivot. A centered affine/Taylor
`LDL*` model is required.

The centered model through degree five displays stable `~5e-6` decay per
degree and preserves essentially the full pivot margin. Directed coefficients
and an all-order remainder majorant are now the concrete target.

The degree-five coefficients are now directed for the complete degree-29
source polynomial. The analytic source tail is also injected through Taylor
degree five, leaving margin `6.6650083764e-26`. The sole remaining central
rank-five obligation is an all-orders majorant beginning at degree six.

The all-orders majorant is now closed on the weakest endpoint cell, leaving
uniform extension over the remaining ordered cells as the only central
rank-five obligation.

A complete numerical anchor sweep finds all 15,015 fifth-pivot coordinate
derivatives negative. Proving this coordinatewise monotonicity would reduce
uniformization to the certified upper endpoint cell and is now the preferred
rank-five theorem target.

## Thimble transport is removed from the proof contract

The modular sewing audit now proves that the completed real Mellin contour is
the faithful source object. Superexponential decay makes

\[
Z(z)=\int_{\mathbb R}e^{zu}\Phi(u)\,du
\]

entire in \(z\), with every parameter jet obtained on that same fixed contour.
Complex thimbles are optional coordinate decompositions.

Inside any theta analyticity strip

\[
\left|\Im u-k\pi\right|<\frac\pi4,
\]

endpoint incidence uniquely determines a relative path: the strip is simply
connected, source zeros are not punctures, and every Mellin-jet one-form has a
primitive. Integral Picard--Lefschetz mutation therefore changes only the
presentation of a period. It supplies no additional global obstruction or
positivity mechanism.

Accordingly, the preferred rank-uniform attack should no longer accumulate
wall-by-wall thimble reconstructions. The live explanatory question is
strictly:

\[
\boxed{
\text{which special property of the completed positive real theta source
forces the quarter-centered angular energy to decrease?}
}
\]

Any successful answer must act on the undecomposed real-source integral or
its exact Loewner kernel. Component signs, saddle counts, and fitted
cancellation paths are diagnostics only.
