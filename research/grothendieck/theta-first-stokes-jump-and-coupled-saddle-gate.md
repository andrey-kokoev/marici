# First Stokes jump and the coupled-saddle gate

## Refined event

Along \(z=1/2+ib\), the physical saddle becomes phase-aligned with a persistent
competitor at

\[
\boxed{b_{\mathrm S}\approx5.988285289982947.}
\]

The saddles are

\[
u_{\mathrm p}\approx0.08401358911356424
                   +0.38179499285876844\,i,
\]

\[
u_{\mathrm c}\approx-0.05825544402510956
                   +0.4629646570392176\,i.
\]

Their action imaginary parts agree to approximately \(1.1\times10^{-15}\);
the bisection bracket has width \(1.43\times10^{-14}\). Their real-action
difference is

\[
\Re(\mathcal S_{\mathrm p}-\mathcal S_{\mathrm c})
\approx0.06304481360798686.
\]

In the Pick coordinate,

\[
t_{\mathrm S}\approx-35.60956071422615
                    +5.988285289982947\,i,
\qquad
|t_{\mathrm S}|\approx36.10956071422615.
\]

This is earlier than the first observed saddle collision at
\(|t|\approx92.86\), but beyond the certified disk \(|t|\leq8.5\).

## Upward-flow topology

Upward thimbles were traced using

\[
\frac{du}{ds}=
\frac{\overline{\mathcal S_z'(u)}}{|\mathcal S_z'(u)|}.
\]

At \(b=5.95\), neither upward branch of the competitor intersects the original
real-\(u\) contour. At the event, the physical and competitor branches meet
the real contour near \(u=0.0352796\). At \(b=6.03\), one competitor branch
intersects near \(u=0.0346241\).

The below/above result is unchanged for step sizes
\(0.002,0.001,0.0005\). The above-event crossing agrees to better than
\(6\times10^{-8}\).

This is strong numerical evidence that the competitor intersection number
changes. Flow enclosures and the orientation sign remain open.

## What is falsified

A globally single-thimble explanation is false. The physical saddle chart
undergoes a Stokes jump by approximately \(|t|=36.11\).

The correct object after the jump is a canonical coupled thimble block.
Discarding the new saddle would violate contour covariance.

## First coupled-saddle positivity diagnostic

At leading saddle order, the logarithmic barycenter is \(\log x=2u\). With the
exact cone coefficients at the event,

\[
C_{\mathrm p}\approx2.7846252504>0,
\qquad
C_{\mathrm c}\approx-0.4855429975<0.
\]

The new saddle is not separately positive. The action magnitude ratio is

\[
\exp\Re(\mathcal S_{\mathrm c}-\mathcal S_{\mathrm p})
\approx0.9389013972.
\]

For the canonical plus-paired block, the leading weighted cone proxy is

\[
\boxed{C_{\mathrm p+c}\approx1.2010658485>0.}
\]

Thus coupled positivity survives the first Stokes event at leading order,
despite failure of the competitor individually.

At this leading stage the orientation sign and fluctuation integrals were not
yet established; the next section supplies their numerical post-jump audit.

## Relative-cycle geometry and exact post-jump quadrature

The zero-directed downward branches from both saddles converge to the same
simple zero of the analytically continued completed source,

\[
u_\star\approx0.6388300536005935\,i,
\qquad |\Phi'(u_\star)|\approx259.1968.
\]

This is a zero of the Mellin amplitude, not a zero of Xi. The other downward
branches run into the decaying sectors at positive and negative real infinity.
Thus the two thimbles form a relative cycle from \(-\infty\) to \(u_\star\)
to \(+\infty\).

Above the jump, both upward intersections with the positive real contour have
the same oriented sign; their imaginary flow components are approximately
`-0.9996`. This selects the plus pairing under the consistent local
orientation.

At \((a,b)=(0.5,6.03)\), direct quadrature along the two downward thimbles,
closing their short terminal segments at \(u_\star\) and suppressing the
infinite tails by 30 action units, gives

\[
\mathcal M_{\rm pair}
\approx0.0567852346+0.5942293851i,
\]

and the exact-path cone diagnostic

\[
\boxed{C_{\rm pair}\approx1.2796779868>0.}
\]

The individual exact thimble barycenters give

\[
C_{\rm p}^{\rm exact}\approx5.80829,
\qquad
C_{\rm c}^{\rm exact}\approx-3.74368.
\]

Thus fluctuation corrections do not make the competitor positive. Positivity
is genuinely coupled at exact-thimble level. Above the wall, the full thimble
integrals also carry different phases (approximately `-0.4461` and `0.9000`
radians), despite action-phase equality on the wall. Therefore a
common-positive-phase convexity theorem is too restrictive after the jump;
the required theorem must control the oriented complex sum directly.

An independent real-contour transform gives

\[
\mathcal M_{\mathbb R}
\approx0.0567317697+0.5942837022i.
\]

The paired integral agrees with the real-contour integral to relative error
`4.67e-4`; the barycenters differ by `7.62e-5`. These errors are consistent
with non-certified path step and tail truncation. This strongly supports both
the plus orientation and exact contour reconstruction, but is not yet a
directed enclosure.

## Next theorem and falsifier

The next target is a two-thimble coupled positivity theorem:

1. certify the jump coefficient and orientation;
2. express both thimble moments with their source-derived oriented phases;
3. retain principal and competitor as one source-canonical block; and
4. prove the exact block barycenter remains in the cone.

The falsifier is the first parameter where the oriented exact paired block
crosses the cone boundary.

The denominator-free expansion is now isolated in
theta-oriented-two-thimble-coupled-positivity-theorem.md. At \(b=6.03\), the
principal self numerator is \(0.125852\), while the negative competitor and
cross defect totals \(0.069302\), giving principal-dominance safety factor
about \(1.816\).

Continuation finds that this two-thimble block remains the complete
original-contour block until a third saddle joins at
\(b\approx9.6439257771\). Four exact-path samples across the chamber pass the
oriented dominance gate, with the defect ratio decreasing toward the far
wall. See `theta-first-two-thimble-chamber-reconnaissance.md`.

Artifacts:

- checkers/theta_completed_saddle_stokes_scan.py
- results/theta-completed-saddle-stokes-scan.json
- checkers/theta_stokes_upward_thimble_trace.py
- results/theta-stokes-upward-thimble-trace.json
- checkers/theta_complex_source_zero_endpoints.py
- results/theta-complex-source-zero-endpoints.json
- checkers/theta_stokes_paired_cycle_crosscheck.py
- results/theta-stokes-paired-cycle-crosscheck.json
