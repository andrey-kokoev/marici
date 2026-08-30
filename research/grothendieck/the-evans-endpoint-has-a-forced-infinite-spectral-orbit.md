# The Evans Endpoint Has a Forced Infinite Spectral Orbit

## Prolonged source tail

For a test source \(f\), define the tail moments

\[
G_k(q,z)
=\partial_z^kG_0(q,z)
=\int_q^\infty (v-q)^k f(v)e^{z(v-q)}\,dv,
\qquad k\ge0.
\]

Their scale equations are

\[
\partial_qG_0=-zG_0-f,
\]

and, for \(k\ge1\),

\[
\partial_qG_k=-zG_k-kG_{k-1}.
\]

Spectral differentiation is the upward shift

\[
\partial_zG_k=G_{k+1}.
\]

Thus the source-native vertical generator is regular before scalar
projection, but it acts on an infinite moment prolongation.

## Dual orbit of endpoint evaluation

Let \(\ell_k\) evaluate the \(k\)-th tail moment at the fixed endpoint:

\[
\ell_k(f)=G_k(0,z)
=\int_0^\infty v^k f(v)e^{zv}\,dv.
\]

Then

\[
\partial_z\ell_k=ell_{k+1}.
\]

The orbit of \(\ell_0\) is not rank one. More strongly, it has no finite
rank on the test-source space. If

\[
\sum_{k=0}^N c_k\ell_k=0
\]

for every compactly supported smooth source, then

\[
\int_0^\infty
\left(\sum_{k=0}^Nc_kv^k\right)f(v)e^{zv}\,dv=0
\]

for every such \(f\). The fundamental lemma forces the polynomial to vanish
identically, hence every \(c_k=0\).

Therefore no regular scalar connection

\[
\ell_0'+\ell_0A=a(z)\ell_0
\]

can close universally on the endpoint line. Endpoint nullity is one
coordinate cancellation inside a forced infinite observable orbit.

## Prime transport of the full orbit

For a prime \(p\), put \(L_p=\log p\), \(r_p=p^{-1/2-z}\), and

\[
B_{p,j}(z)=\int_0^{L_p}v^j f(v)e^{zv}\,dv.
\]

The \(k\)-th endpoint moment of the shifted source is

\[
\ell_k(T_pf)
=r_p\sum_{j=0}^k
\binom{k}{j}(-L_p)^{k-j}
\bigl(\ell_j(f)-B_{p,j}(z)\bigr).
\]

This is simply the binomial expansion of \((v-L_p)^k\) after moving the
lower endpoint back to the fixed chart.

Spectral differentiation commutes with prime transport only for this complete
formula. Differentiating the right-hand side gives the \((k+1)\)-st formula:

\[
\partial_z\ell_k(T_pf)=\ell_{k+1}(T_pf).
\]

The derivative of \(r_p\) supplies one factor \(-L_p\), while derivatives of
\(\ell_j-B_{p,j}\) raise \(j\). Pascal's identity combines them into the next
binomial row.

## Exact obstruction

The mixed arithmetic–spectral square closes, but only on the infinite tower

\[
(\ell_0,\ell_1,\ell_2,\ldots)
\]

together with all seam jets

\[
(B_{p,0},B_{p,1},B_{p,2},\ldots).
\]

Every finite truncation fails at its top component because spectral
differentiation produces the next moment and the next seam jet. This is not a
numerical completion problem; it is an algebraic nonclosure theorem.

Consequently the hoped-for regular rank-one endpoint connection does not
exist on the full source category. A viable vertical bridge must instead be:

- an infinite jet/pro-object with a source-selected topology;
- a quotient justified by an independently proved source recurrence; or
- a different observable carrying finite spectral closure.

The theta source does not presently supply such a finite recurrence.

## Relation to the common lift

The four-state arithmetic square \(1,p,q,pq\) is finite horizontally, but
each of its endpoint ports carries an infinite vertical moment tower. The
common lift is therefore not a finite matrix object. It is a horizontally
finite, vertically pro-valued diagram. Its determinant and Evans shadows may
still be finite scalar sections, but the comparison authority lives before
that compression.

## Falsifier

Reject any proposed finite-rank spectral lift if:

- it identifies \(\ell_{N+1}\) with lower moments without a source-derived
  recurrence;
- it omits \(B_{p,N+1}\) after differentiating the transported \(N\)-th
  moment;
- it obtains a scalar connection by using \(F'/F\);
- prime transport commutes only after endpoint aggregation.

## Scope

This proves forced infinite spectral rank and exact prime covariance of the
complete moment-seam tower. It does not construct its completed topology,
reciprocal Schur colligation, determinant comparison, zero confinement, or
RH.
