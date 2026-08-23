# First two-thimble chamber reconnaissance

## Chamber topology

On \(z=1/2+ib\), the first competitor joins the real Mellin contour at

\[
b_1\approx5.988285289982947.
\]

A third saddle creates phase walls at

\[
b_{2a}\approx9.544332180951134,\qquad
b_{2b}\approx9.643925777107869.
\]

Upward-flow tracing shows that the third saddle misses the real contour at
\(b=9.53\) and \(9.60\). At \(b=9.66\), after the second wall, one branch
intersects with oriented sign \(-1\).

Therefore the first genuine two-thimble chamber on this ray is numerically

\[
\boxed{5.98828529\lesssim b\lesssim9.64392578.}
\]

The first later phase equality changes the saddle basis but not the
original-contour intersection census. The second admits the third contributor.

## Oriented defect scan

Write

\[
\mathcal N=N_{11}+N_{22}+N_{12},\qquad
\delta=-\frac{N_{22}+N_{12}}{N_{11}}.
\]

Exact-path diagnostic quadrature gives

\[
\begin{array}{c|rrrr}
b&7&8&9&9.6\\ \hline
\delta&0.43441&0.33058&0.26193&0.24436\\
\text{paired cone}&1.57867&1.96435&2.48796&2.91817.
\end{array}
\]

Every sample has \(\delta<1\), with increasing safety toward the far wall.
At \(b=9.6\), the paired-thimble cone \(2.9181731\) agrees with the independent
real-contour value \(2.9184614\) to about \(2.9\times10^{-4}\).

The observed worst defect is near chamber entry, not near the third-saddle
wall.

The second logarithmic moments give the Gauss--Manin derivative directly:

\[
\begin{array}{c|rrrr}
b&7&8&9&9.6\\ \hline
\delta'&-0.11510&-0.08936&-0.04537&-0.01289.
\end{array}
\]

Thus every sampled point satisfies the proposed local monotonicity inequality
`D'A-DA'<=0`. This is evaluated from the exact moment-transport identity, not
from finite differences between the displayed defect values.

## Selected conjecture

For fixed \(a=1/2\), throughout the first two-thimble chamber,

\[
\delta(b)<1,
\]

and \(\delta\) is nonincreasing after a short entry layer.

The desired proof should derive a differential inequality for the oriented
defect under parameter transport within the chamber. Its falsifier is a point
where \(\delta=1\), or where the proposed differential sign fails.

The chamber derivative is now expressed exactly by Gauss--Manin moments:
\(\partial_bM_k=iM_{k+1}/2\). Consequently \(\delta'\leq0\) reduces to a
finite inequality involving only thimble moments through order two. See
theta-thimble-gauss-manin-defect-flow.md.

## Limitations

- Phase walls and flow intersections are not interval-certified.
- Path quadrature uses step \(0.001\) and 30 action units of tail decay.
- Only the ray \(a=1/2\) has been followed.
- Beyond the far wall, a three-thimble theorem is required.

That next mutation has now been resolved numerically. A second simple source
zero appears at

\[
u_{\star,1}\approx
0.2556475134765196+0.6955398322128286i,
\]

and the post-wall contour is the incidence-forced chain

\[
-\infty\longrightarrow u_{\star,0}
\longrightarrow u_{\star,1}\longrightarrow+\infty.
\]

At \(b=9.66\), its three edges reconstruct the direct real contour to relative
error \(5.16\times10^{-4}\), and its cone is
\(2.96772133898>0\). Thus the far wall ends the two-thimble basis but does not
end the source-derived positivity mechanism. See
`theta-first-three-thimble-chain.md`.

Artifacts:

- checkers/theta_first_two_saddle_chamber_trace.py
- results/theta-first-two-saddle-chamber-trace.json
- checkers/theta_third_saddle_stokes_trace.py
- results/theta-third-saddle-stokes-trace.json
- checkers/theta_two_thimble_chamber_defect_scan.py
- results/theta-two-thimble-chamber-defect-scan.json
- checkers/theta_first_three_thimble_block.py
- results/theta-first-three-thimble-block.json
