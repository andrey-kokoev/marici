# The history graph energy canonically dominates causal oddness but gives only a non-strict margin

## Source-derived positive companion candidate

Let \(H=H_+\) be the closed forward history operator on its graph domain. Its canonical graph energy is

\[
S_{\mathrm{gr}}
=
\frac12(I+H^{*}H)
\]

as a closed positive quadratic form. The causal odd operator is

\[
T_{\mathrm{hist}}
=
\frac{H-H^{*}}{2}.
\]

For every graph-domain vector \(x\),

\[
\langle x,iT_{\mathrm{hist}}x\rangle
=
-\operatorname{Im}\langle x,Hx\rangle.
\]

Cauchy–Schwarz and the arithmetic-geometric mean inequality give

\[
\left|
\langle x,iT_{\mathrm{hist}}x\rangle
\right|
\le
\|x\|\,\|Hx\|
\le
\frac12
\left(
\|x\|^2+\|Hx\|^2
\right)
=
\langle x,S_{\mathrm{gr}}x\rangle.
\]

Thus

\[
-S_{\mathrm{gr}}
\le
iT_{\mathrm{hist}}
\le
S_{\mathrm{gr}}
\]

as forms. Both reciprocal blocks

\[
D_\pm=S_{\mathrm{gr}}\pm iT_{\mathrm{hist}}
\]

are nonnegative.

This domination uses the actual history graph and does not require positivity of the cosine transform.

## Why this does not yet give completion coercivity

The bound is non-strict. Equality is possible only when both inequalities saturate, which requires

\[
\|Hx\|=\|x\|
\]

and

\[
Hx=\pm i x
\]

in the exact case. For approximate sequences, loss of the auxiliary margin occurs when \(H\) has approximate graph modes behaving like multiplication by \(+i\) or \(-i\).

Therefore strict auxiliary coercivity is equivalent to a quantitative exclusion of these imaginary unit modes in the graph-normalized numerical range.

## Multiplier model

If \(H\) is normal with multiplier \(m(\xi)\), then the normalized odd contraction has scalar magnitude

\[
\kappa(\xi)
=
\frac{
2|\operatorname{Im}m(\xi)|
}{
1+|m(\xi)|^2
}.
\]

The elementary identity

\[
1+|m|^2-2|\operatorname{Im}m|
=
(\operatorname{Re}m)^2+
(|\operatorname{Im}m|-1)^2
\]

shows

\[
\kappa(\xi)\le1,
\]

with equality exactly at

\[
m(\xi)=+i
\quad\text{or}\quad
m(\xi)=-i.
\]

A uniform auxiliary margin is therefore

\[
\operatorname*{ess\,sup}_{\xi}
\frac{
2|\operatorname{Im}m(\xi)|
}{
1+|m(\xi)|^2
}
\le
1-\varepsilon.
\]

This is weaker and more natural than demanding that \(m\) remain inside the sector \(|\arg m|<\pi/4\).

## Exponential hostile revisited

For

\[
m(\xi)=\frac{1+i\xi}{1+\xi^2},
\]

the symmetric-part energy failed to dominate strictly. But the graph-energy ratio is

\[
\kappa(\xi)
=
\frac{2|\xi|}{\xi^2+2}.
\]

Its supremum is \(1/\sqrt2\), attained at \(|\xi|=\sqrt2\). Thus this hostile fails for the symmetric-part energy but has a uniform graph-energy margin. The obstruction is specifically approach to the imaginary unit points, not large causal frequency by itself.

The important lesson is that changing \(S\) changes the exact obstruction from sector angle to distance from the imaginary unit points.

## Source-authority qualification

The graph energy is canonical for a closed operator, but it is source-authorized for the Adams auxiliary block only if the declared Green construction includes both:

- the history output energy \(\|Hx\|^2\);
- the domain or wall energy \(\|x\|^2\) with the stated coefficient.

The identity term cannot be inserted merely to force positivity. It may plausibly be supplied by the independently retained coefficient-wall identity residue, but that intertwining theorem remains to be proved.

## Relation to the full seam Gram

Grothendieck's full seam-history Gram supplies \(H^{*}H\) and is positive. It retains energy invisible to endpoint traces. The missing comparison is whether the coefficient-wall carrier supplies the \(I\) summand in the same typed auxiliary fiber. If so, the canonical graph energy closes non-strict positivity automatically.

## Revised next gate

Prove the source identity

\[
S
=
\frac12(I_{\mathrm{wall}}+H_+^{*}H_+)
\]

on the reduced tail/PV carrier, with correct normalization. Then establish uniform exclusion of approximate modes

\[
H_+x_n\approx\pm i x_n
\]

over primes, cutoffs, and compact off-seam regions. This is the exact strict-margin theorem for the history-based auxiliary block.
