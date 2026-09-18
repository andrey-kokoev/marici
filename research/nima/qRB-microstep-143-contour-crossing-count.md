# qRB microstep 143: contour-crossing count

For the translate-Gram continuation, the contour displacement is

$$
\eta=\frac{d}{4\sigma}.
$$

An upward shift crosses precisely those poles

$$
2k+\frac12<\eta,
\qquad k=0,1,2,\ldots
$$

so the number of crossed poles is

$$
 r(\eta)=\max\left(0,\left\lceil\frac{\eta-1/2}{2}\right\rceil\right),
$$

away from pole-alignment values. At alignment, the continuation requires a prescribed indentation or principal-value convention.

Thus the continued gamma channel is piecewise analytic in `d`, with residue corrections changing only when `|d|` crosses the corresponding pole threshold.

Status: crossing count specified; alignment convention remains to be fixed.
