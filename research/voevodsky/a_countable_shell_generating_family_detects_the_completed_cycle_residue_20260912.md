# A countable shell-generating family detects the completed cycle residue

## Question

Can one replace growing polynomial-moment depth by one fixed countable family that detects every completed cycle?

## Claim boundary

Yes mathematically. Modulate shell \(j\) by \(t^j\) and record the differential common history at a countable set of parameters accumulating inside \((0,1)\). The resulting family is jointly faithful on the completed cycle space. This does not establish physical access to the parameterized modulation.

## Generating modulation

For \(0<t<1\), define the diagonal source modulation

\[
D_t(e)=t^{j(e)},
\]

where \(j\geq1\) is the consecutive-prime shell index, and define

\[
A_t=BD_t.
\]

Choose a countable set, for example

\[
t_n=\frac12+\frac1{n+3},
\qquad n\geq0,
\]

which lies in \((0,1)\) and accumulates at \(1/2\).

## Analytic separation

For a completed cycle \(z\), consider

\[
F_z(t)=\partial D_tz
=\sum_{j\geq1}t^j\partial z_j,
\]

where \(z_j\) is the subchain supported on shell \(j\). Since \(z\in\ell^1\) and \(|t|<1\), this is a distribution-valued analytic function on the unit disk.

If \(A_{t_n}z=0\) for every \(n\), completed history injectivity on interval synthesis gives \(F_z(t_n)=0\). The identity theorem, applied after pairing with every finitely supported vertex test, gives

\[
\partial z_j=0
\]

for every shell \(j\).

## One-shell acyclicity

For fixed consecutive primes \(p_j<q_j\), shell-\(j\) edges are

\[
kp_j\longrightarrow kq_j.
\]

At each vertex there is at most one outgoing and at most one incoming edge of this shell type. Directed edges strictly increase the positive integer vertex. Hence each shell subgraph is a disjoint union of paths and has zero cycle space. Therefore

\[
\partial z_j=0\implies z_j=0.
\]

Thus \(z=0\), proving

\[
\bigcap_{n\geq0}
\ker(A_{t_n}|_{\mathcal Z})
=\{0\}.
\]

## Bounded direct-sum readout

Let \(\alpha_n=2^{-n-1}\) and define

\[
\mathcal A z=(\alpha_nA_{t_n}z)_{n\geq0}.
\]

Because \(|t_n^{j(e)}|\leq1\), every \(A_{t_n}\) obeys the same projective-to-Hilbert bound as \(B\). Since \((\alpha_n)\in\ell^2\), the direct-sum map is continuous. Every \(\alpha_n\) is nonzero, so joint faithfulness is retained.

## Relation to moment channels

At a finite cutoff with \(s\) shell values, evaluations at \(s\) distinct parameters form a Vandermonde system and recover the shell-resolved boundary coefficients. Polynomial moments are finite jets of a related generating construction; their required depth can grow, whereas the fixed countable evaluation family does not change with cutoff.

## Physical acceptance test

A physical realization must implement a reproducible one-parameter attenuation whose action on shell \(j\) is verified to be \(t^j\), preserve separate readouts for several \(t_n\), and measure their joint noise covariance. Without that map, the generating family is only a mathematical detector.

## Disposition

The completed route residue now has a fixed countable jointly faithful probe design with a continuous Hilbert direct-sum readout. Covariance becomes measurable if the shell-generating modulation is physically admitted and calibrated; no finite channel count is asserted.
