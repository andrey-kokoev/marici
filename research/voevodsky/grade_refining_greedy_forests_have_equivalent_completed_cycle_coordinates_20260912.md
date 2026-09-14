# Grade-refining greedy forests have equivalent completed cycle coordinates

## Question

Do different cutoff-natural greedy forest presentations define equivalent completed cycle ports?

## Claim boundary

Yes when both total orders refine the same proper arithmetic grade. The transition maps are continuous in both directions for the projective exponential topology. This does not cover arbitrary forests whose paths may use edges of unboundedly larger grade than their chords.

## Grade-controlled fundamental cycles

Let \(T\) be produced by Kruskal's greedy rule from a total order refining \(W\). When a chord \(e\) of grade \(w\) is rejected, its endpoints are already joined by a tree path consisting only of edges processed earlier. Hence every edge in its fundamental cycle has grade at most \(w\).

For another grade-refining greedy forest \(U\), the \(U\)-chord coordinates of that represented cycle are a subset of its edge coefficients. Each coefficient is \(0\), \(1\), or \(-1\), and every nonzero target coordinate has grade at most \(w\).

## Arithmetic counting bound

For the symmetric all-ratio grade

\[
W(a,b;j,k)=\log(abkp_jp_{j+1}),
\]

the number \(N(w)\) of edges with grade at most \(w\) obeys the crude bound

\[
N(w)\leq e^{5w}.
\]

Indeed each of the five positive integer labels \(a,b,k,p_j,p_{j+1}\) is at most \(e^w\); coprimality, primality, and consecutiveness only reduce the count. No asymptotic prime theorem is required.

Therefore one source chord coordinate of grade \(w\) contributes at most

\[
e^{5w}e^{\delta w}=e^{(\delta+5)w}
\]

to the target \(q_\delta\) seminorm. Summing columns gives

\[
q_\delta^U(C_{U\leftarrow T}z)
\leq
q_{\delta+5}^T(z).
\]

Exchanging \(T\) and \(U\) gives the inverse estimate. Thus the integral forest-change map extends to a bicontinuous linear isomorphism between completed chord targets.

## Consequence

Within the class of grade-refining greedy orders, the completed augmented observer is presentation independent up to a canonical continuous forest-change isomorphism. No one forest is selected as ontologically or physically preferred.

The estimate is intentionally coarse. A sharper edge-counting theorem could lower the seminorm shift, but the projective topology only requires some finite shift.

## Hostile boundary

An arbitrary spanning forest need not satisfy the path-grade condition. It can connect endpoints of a low-grade chord through arbitrarily high-grade edges, so its coordinate transition need not be continuous for this projective topology. Visibility of a finite forest at every cutoff does not imply uniform completed continuity.

## Disposition

The completed forest-presentation independence gate is closed for the source-relevant grade-refining greedy class. The remaining cycle-sector question is physical covariance, not coordinate coherence or observer faithfulness.
