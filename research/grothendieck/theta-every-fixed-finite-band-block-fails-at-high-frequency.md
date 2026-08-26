# Every fixed finite theta band block fails at high frequency

## Bounded question

Can a larger but fixed canonical regrouping of consecutive oscillation bands
repair the two-lobe obstruction?

## Canonical finite block

Fix an integer \(m\ge1\). With \(L=\pi/b\), retain the first \(m\) complete
oscillation periods. The aggregate block is

\[
I_m(a,L)
=
\beta I_{J,m}(a,L)+\alpha I_{W,m}(a,L),
\]

where

\[
I_{J,m}(a,L)
=
\int_0^{2mL}J_a(r)\cos(\pi r/L)\,dr,
\]

and

\[
I_{W,m}(a,L)
=
\int_0^{2mL}rW_a(r)\sin(\pi r/L)\,dr.
\]

The endpoint \(2mL\) is fixed before inspecting the source sign and is
covariant under regrouping complete consecutive phase periods.

## Universal fixed-block asymptotics

For fixed \(m\), smooth evenness at the origin gives

\[
J_a(r)=J_a(0)+\frac12J_a''(0)r^2+O(r^4),
\qquad
W_a(r)=W_a(0)+O(r^2).
\]

The required elementary moments are

\[
\int_0^{2mL}\cos(\pi r/L)\,dr=0,
\]

\[
\int_0^{2mL}r^2\cos(\pi r/L)\,dr
=
\frac{4mL^3}{\pi^2},
\]

and

\[
\int_0^{2mL}r\sin(\pi r/L)\,dr
=
-\frac{2mL^2}{\pi}.
\]

Consequently,

\[
I_{J,m}(a,L)
=
\frac{2mJ_a''(0)}{\pi^2}L^3+O_m(L^5),
\]

and

\[
I_{W,m}(a,L)
=
-\frac{2mW_a(0)}{\pi}L^2+O_m(L^4).
\]

## Physical port map

For the actual angular coefficients,

\[
\beta=\frac{2\pi}{L}+O(L),
\qquad
\alpha=2a+O(L^2).
\]

Therefore

\[
I_m(a,L)
=
\frac{4m}{\pi}
\left[J_a''(0)-aW_a(0)\right]L^2
+O_m(L^4).
\]

The larger block multiplies the same source gate by \(m\); it does not change
its orientation.

## Strict source obstruction

The preceding packet proved that, for the completed theta source,

\[
J_a''(0)-aW_a(0)<0
\]

for all sufficiently small positive \(a\). Hence, for every fixed
\(m\ge1\) and every such \(a\),

\[
I_m(a,L)<0
\]

for all sufficiently small positive \(L\), equivalently for all sufficiently
large \(b\).

## Result

No fixed finite regrouping of complete consecutive phase periods can prove the
outer theta angular inequality. The one-block failure is not repaired by two,
three, or any preassigned finite number of blocks.

The quantifiers matter. This theorem does not control a block count
\(m=m(L)\) that diverges as \(L\to0\). Once \(mL\) remains macroscopic, the
local Taylor reduction is no longer valid and the full global source geometry
can enter.

Thus the surviving mechanisms are sharply reduced to:

1. a genuinely nonlocal block whose number of bands grows with \(b\);
2. the undecomposed full oscillatory integral;
3. a source operation before phase-band projection.

## Explanation

Finite band regrouping was hiding a locality assumption. At high frequency,
every fixed finite block collapses onto the same infinitesimal germ of the
source and therefore inherits the same strict Hardy orientation. Global
modular information cannot appear until the block spans a nonvanishing source
scale. The missing explanation is necessarily nonlocal in band number.

## Sharp falsifier for the surviving route

For a proposed growing block \(m(L)\), compute the first regime in which
\(m(L)L\) has a nonzero limit. If its exact source integral remains negative,
the entire consecutive-band transport route closes and only a pre-projection
source identity survives.
