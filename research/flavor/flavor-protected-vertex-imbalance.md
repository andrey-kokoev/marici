# Protected vertex imbalance: WP670

## General protected channel

Lift WP669 to unequal real masses and independent real reciprocal vertices:

\[
\mathcal M=
\begin{pmatrix}
A I&yJ_n\\
zJ_n&B I
\end{pmatrix}.
\]

The exact physical fermion trace is

\[
\begin{aligned}
\operatorname{Tr}(\mathcal M^\dagger\mathcal M)^2
={}&3A^4+3B^4\\
&+4\left[A^2(y^2+z^2)+2AB yz+B^2(y^2+z^2)\right]|n|^2\\
&+2(y^4+z^4)|n|^4.
\end{aligned}
\]

The Dirac supertrace therefore contributes
\(-8(y^4+z^4)|n|^4\). Unequal masses change the quadratic term but not the
quartic erosion coefficient. Flip-even operator support remains closed.

## Constructor fiber

The reciprocal transformation

\[
y\mapsto ty,\qquad z\mapsto z/t
\]

preserves the product \(yz\) but changes \(y^4+z^4\). At fixed product,

\[
y^4+z^4\geq2(yz)^2,
\]

with equality only at balanced magnitudes. The hostile packets \((y,z)=(1,1)\)
and \((2,1/2)\) both have product one, while their erosion sums are two and
\(257/16\).

## Corrected flow variable

Let \(Q_n,Q_m\) sum \(y^4+z^4\) over protected channels. Then

\[
\frac{dD}{dt}=1136-32(Q_n+Q_m).
\]

WP669 is the balanced slice \(y=z\). Tree-product matching alone neither
identifies nor upper-bounds loop erosion: imbalance can grow without bound at
fixed nonzero product.

## Disposition

Protection closes operator support but not constructor identification. A
source-derived vertex-balance law or two independently calibrated threshold
widths is required. Balance would be a new source restriction; matching does
not imply it. No flavor selector follows from the inequality alone.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp670_protected_vertex_imbalance.py

Generated result: results/wp670_protected_vertex_imbalance.json.
