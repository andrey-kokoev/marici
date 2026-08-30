# The graph intersection of Euler and theta metrics does not repair compact incidence

## Result

Taking the graph intersection of the intrinsic Euler completion and the theta-sampling pullback completion does not restore a lower bound for the Euler-to-theta incidence.

Because the theta norm is weaker than the Euler norm, the intersection is just the Euler object with an equivalent graph norm. The sampling map remains compact and not bounded below.

Thus the three candidate domains reduce to two genuinely different choices:

- retain the Euler topology and accept compact non-coercive incidence;
- pass to the theta pullback topology and give up bounded inverse reconstruction.

## Abstract setup

Let

\[
H_E
\]

be the Euler half-density Hilbert space, and let

\[
S_\theta:H_E\to H_A
\]

be the diagonal theta-sampling incidence. In an Euler-normalized prime basis,

\[
S_\theta e_p=\eta_pe_p,
\qquad
\eta_p\ne0,
\qquad
\eta_p\to0.
\]

The pullback seminorm is

\[
\|x\|_\theta=\|S_\theta x\|_{H_A}.
\]

Since \((\eta_p)\) is bounded,

\[
\|x\|_\theta
\le
M\|x\|_E
\]

for some finite \(M\).

## Graph intersection

Define the proposed common graph object by

\[
H_\cap
=
H_E\cap H_\theta
\]

with norm

\[
\|x\|_\cap^2
=
\|x\|_E^2+\|x\|_\theta^2.
\]

Every \(x\in H_E\) has finite theta norm because \(S_\theta\) is bounded. Hence, as sets,

\[
H_\cap=H_E.
\]

Moreover,

\[
\|x\|_E
\le
\|x\|_\cap
\le
\sqrt{1+M^2}\|x\|_E.
\]

Therefore the graph-intersection topology is equivalent to the original Euler topology.

It introduces no new completion object and no stronger control of inverse sampling.

## Lower-bound hostile survives

For the normalized prime basis,

\[
\|e_p\|_\cap^2
=
1+|\eta_p|^2
\longrightarrow1,
\]

while

\[
\|S_\theta e_p\|_{H_A}
=
|\eta_p|
\longrightarrow0.
\]

Consequently,

\[
\inf_{x\ne0}
\frac{\|S_\theta x\|_{H_A}}
{\|x\|_\cap}
=
0.
\]

The graph intersection does not give closed range, a bounded inverse, or a completion-uniform observer margin.

## Graph norm of the inverse

One might instead attempt to use

\[
\|x\|_{\mathrm{inv}}^2
=
\|x\|_E^2
+
\|S_\theta^{-1}x\|^2.
\]

But this expression is typed on the analytic range, not on the Euler source. In prime coordinates it inserts weights \(|\eta_p|^{-2}\), producing a much stronger domain.

That domain contains only Euler vectors satisfying

\[
\sum_p|\eta_p|^{-2}|c_p|^2<\infty.
\]

It is a source restriction, not an intersection of the two original metrics. Because \(|\eta_p|^{-1}\) grows superexponentially, the restriction is severe and requires explicit constructor authority.

## Closed range theorem

For a bounded operator between Hilbert spaces, the following are equivalent on the orthogonal complement of its kernel:

- the range is closed;
- the operator is bounded below;
- the Moore--Penrose inverse is bounded on the range.

Here the kernel is zero, but the singular values \(|\eta_p|\) tend to zero. Therefore

\[
\operatorname{ran}S_\theta
\]

is not closed in the unweighted analytic target whenever infinitely many prime fibers are admitted.

This is an exact completion obstruction, not merely failure to find a convenient estimate.

## Legitimate architectures

Three coherent architectures remain.

### Compact correspondence

Keep \(H_E\) as the arithmetic source and treat

\[
S_\theta:H_E\to H_A
\]

as compact injective incidence. Do not demand inverse reconstruction or an odd coercivity margin from this arrow alone.

### Pullback object

Complete the algebraic prime packet in \(\|\cdot\|_\theta\). Then \(S_\theta\) is isometric onto the closure of its range. This is a new typed object and its relation to Euler operations must be proved constructor by constructor.

### Restricted source

Use the strong inverse-weighted domain on which analytic sampling has a bounded inverse. This admits only a proper rapidly decaying Euler subspace and needs direct source authority.

The graph intersection with the weaker theta metric is not a fourth solution.

## Consequence for the five-margin programme

A compact incidence arrow cannot contribute a positive global observability margin on the full infinite Euler source. Therefore either:

- Euler observability is supplied by another port before theta sampling;
- global coercivity is formulated only after passing to the theta-control object;
- or the admitted source is restricted.

This distinction must be fixed before assembling the normalized Birman--Schwinger defect. Otherwise a vanishing singular sequence is hidden inside a change of topology.

## Next gate

The source architecture must now answer:

> Is theta sampling intended as a compact forward incidence, an equivalence after changing objects, or a restriction to an inverse-weighted domain?

The existing constructor evidence supports the first interpretation most directly. Any stronger interpretation requires a new authority theorem.
