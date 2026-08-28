# Projected critical-seam Euler product requires genus two

## Scope correction

This theorem applies to the projected numerator-only Euler product.  The full
local Tate boundary observer includes the vacuum denominator and makes its
canonical adjacent-cell minor exactly one.  Consequently the genus-two
product below is not the complete finite-place boundary determinant and
cannot carry RH orientation by itself.

## Connected Euler renormalization

For a complex spectral parameter `s`, put `x_p=p^(-s)`.  The genus-`M`
relative local factor is

`E_M(x)=(1-x) exp(sum_(m=1)^M x^m/m)`.

Its logarithm is exactly

`log E_M(x)=-sum_(m>M) x^m/m`.

Thus the first `M` connected Euler grades are retained as explicit
countercurrents rather than erased after completion.

## Convergence wall

The prime product of `E_M(p^(-s))` converges absolutely when

`(M+1) Re(s)>1`.

At the zeta-one boundary, `M=1` suffices.  This is the previously constructed
relative valuation volume.

At the critical seam `Re(s)=1/2`, genus one fails because its first omitted
term is

`-(1/2) sum_p p^(-2s)`,

whose absolute value contains the divergent prime harmonic series.  Genus
two succeeds because its first omitted term has magnitude `p^(-3/2)`.

Therefore two connected countercurrents are necessary and sufficient for an
absolutely convergent projected finite-place Euler product on the open
critical seam:

`E_2(p^(-s))=(1-p^(-s)) exp(p^(-s)+p^(-2s)/2)`.

This is not numerology from tower dimensions.  It follows from the spectral
abscissa and the Euler logarithm.

## General law

For `Re(s)=sigma>0`, the minimum admitted genus is the least integer `M`
satisfying

`(M+1)sigma>1`.

As the spectral chart approaches `sigma=0`, the required connected-grade
tower becomes unbounded.  Finite genus can control a fixed positive
half-plane but cannot complete the imaginary axis.

## Optics apparatus

Encode each local Euler factor as a complex transmission and accumulate its
log amplitude and phase in prime order.  Compare genus one and genus two at
the preregistered seam `sigma=1/2`:

- genus one must show unbounded negative log-amplitude drift;
- genus two must converge as the channel cutoff grows;
- deleting or altering the coefficient `1/2` of the second connected grade
  restores the drift.

The phase must be retained.  An intensity-only product cannot distinguish a
true complex determinant from its modulus and therefore cannot test the
spectral sewing law.

## Consequence

The prime-square normalization at `s=1` is the first member of a projected
spectral countercurrent hierarchy.  The critical seam forces the next
connected grade whenever the Euler numerator is isolated.  Restoring the
full Tate observer cancels this local minor to one, so the result is a chart
regularization law rather than a completed determinant carrier.  The live
scalarization frontier is archimedean.

## Verification

```text
uv run python research/aspect/checkers/check_projected_critical_seam_genus_two.py
```
