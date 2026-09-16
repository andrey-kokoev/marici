# The central complex Pick certificate extends from 8.5 to 8.9

The existing directed elementary-anchor argument has additional margin beyond its previously recorded radius \(17/2=8.5\).

A radius sweep gives the directed lower bounds

\[
\begin{array}{c|c}
R&\inf_{|t|\le R}\operatorname{Re}F'(t)\\
\hline
8.5&0.0084002481\ldots\\
8.6&0.0065389944\ldots\\
8.7&0.0046462986\ldots\\
8.8&0.0027215736\ldots\\
8.9&0.0007642184\ldots\\
9.0&-0.0012263825\ldots
\end{array}
\]

The final negative number means only that this particular majorant no longer closes at radius nine.

## Directed certificate

The checker

`research/grothendieck/checkers/central_complex_pick_radius_eight_point_nine_certificate.py`

uses the same directed coefficient intervals, elementary anchor

\[
C(81)<13,
\]

and zero-free source disk as the radius-8.5 proof.

It certifies

\[
\boxed{
\operatorname{Re}F'(t)
>
0.0007642184015665901748429326719
\qquad
(|t|\le8.9).
}
\]

Since the normalized source is already certified nonzero through \(|t|\le9\), vertical integration from the real boundary gives

\[
\boxed{
|t|\le8.9,
\quad
\operatorname{Im}t>0
\Longrightarrow
\operatorname{Im}F(t)>0.
}
\]

The durable result is

`research/grothendieck/results/central-complex-pick-radius-eight-point-nine-certificate.json`.

## Remaining central annulus

The previously unresolved annulus

\[
8.5<|t|\le9
\]

is reduced to

\[
\boxed{
8.9<|t|\le9.
}
\]

Closing the final width \(0.1\) requires either a sharper treatment of the degree-seven tail, an additional elementary anchor, or direct Arb boxes on this compact annulus.

## Scope

This is genuine complex-interior Pick positivity on a disk, not merely real-boundary monotonicity. It remains local in \(t\) and does not establish the global Pick property or RH.
