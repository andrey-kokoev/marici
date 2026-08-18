---
id: 451
date: 2026-08-17
title: The Soft Newton Polygon Forces the Weighted Rees Ideal (u,a2)
---

# The Soft Newton Polygon Forces the Weighted Rees Ideal \((u,a^2)\)

Entry 448 inferred that the first Gauss--Manin correction has a simple
\(a\)-pole and proposed the ordinary blowup of \((u,a)\). Before pulling the
full exact complex, the complete Cayley--Menger Newton polygon gives a stricter
geometric test.

The lowest terms have weights \(\mathrm{wt}(a)=1\),
\(\mathrm{wt}(u)=2\) and form the perfect square
\[
K_{\rm in}
=a^4+u,a^2(1-b^2)+\frac{u^2}{4}(1-b^2)^2
=\left(a^2+\frac u2(1-b^2)\right)^2.
\]
Thus the source-derived Rees ideal is \((u,a^2)\), not \((u,a)\).

Indeed, on the ordinary chart \(u=as\), the total transform has exceptional
order two and exceptional equation
\[
\frac{s^2}{4}(1-b^2)^2.
\]
It loses the balance between \(a^4\), \(ua^2\), and \(u^2\), so the ordinary
blowup is not adapted to the controlling Newton face.

On the weighted chart \(u=a^2s\), division by \(a^4\) gives exceptional
equation
\[
\left(1+\frac{s}{2}(1-b^2)\right)^2.
\]
For generic \(b^2\ne1\), the reduced exceptional section is
\[
s=-\frac{2}{1-b^2},
\]
but it occurs with multiplicity two. The double structure cannot be discarded:
it is the natural candidate support for the mixed quartic/Euler deformation
seen in Entry 450. The directions \(b=\pm1\), where the first
Kodaira--Spencer class vanishes, require separate charts or a further blowup.

This corrects Entry 448's proposed modification without changing its pole
theorem. The next gate is to pull the complete exact complex to the weighted
Rees space, retain the doubled exceptional section, and assign filtration
weights from total-transform orders before recomputing flatness.

The executable audit is
research/voevodsky/check_soft_axis_weighted_newton_blowup.py.
