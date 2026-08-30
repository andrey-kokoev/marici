# Two-Prime Moving Seams Compose Through the Shared pq Window

## Two commuting source shifts

For a source \(\phi\), let \(T_p\) and \(T_q\) be the prime shifts

\[
(T_p\phi)(u)=p^{-1/2}\phi(u+\log p),
\qquad
(T_q\phi)(u)=q^{-1/2}\phi(u+\log q).
\]

They commute, and their composite is the \(pq\) shift. Write

\[
F(z)=\int_0^\infty\phi(v)e^{zv}\,dv,
\qquad
r_p=p^{-1/2-z},
\qquad
r_q=q^{-1/2-z}.
\]

For any \(n\), define

\[
B_n(z)=\int_0^{\log n}\phi(v)e^{zv}\,dv.
\]

Endpoint evaluation gives

\[
E(T_p\phi)=r_p(F-B_p),
\qquad
E(T_q\phi)=r_q(F-B_q),
\]

and

\[
E(T_pT_q\phi)=r_pr_q(F-B_{pq}).
\]

## The shared corner is interval concatenation

When the \(q\)-seam is computed after the \(p\)-shift, its native window is

\[
B_{q\mid p}(z)
=\int_{\log p}^{\log p+\log q}\phi(v)e^{zv}\,dv.
\]

The exact composition law is

\[
B_{pq}=B_p+B_{q\mid p}.
\]

Consequently sequential endpoint transport gives

\[
r_q\left(r_p(F-B_p)-r_pB_{q\mid p}\right)
=r_pr_q(F-B_{pq}),
\]

exactly equal to direct \(pq\) transport.

The other order uses

\[
B_{pq}=B_q+B_{p\mid q}
\]

and gives the same result. The comparison square commutes only because the
second boundary window is transported with the first source shift.

## Full depth-one valuation square

For formal amplitudes \(a,b\), the endpoint of

\[
(I+aT_p)(I+bT_q)\phi
\]

is

\[
\begin{aligned}
F_{p,q}={}&F
+ar_p(F-B_p)
+br_q(F-B_q)\\
&+abr_pr_q(F-B_{pq}).
\end{aligned}
\]

The bare Euler product is

\[
(1+ar_p)(1+br_q)F.
\]

Their exact difference is the boundary packet

\[
-ar_pB_p-br_qB_q-abr_pr_qB_{pq}.
\]

The mixed term is not a separately fitted pairwise repair. It is the endpoint
readout of the shared \(pq\) source state.

## Relation to the det3 anomaly

The source square now has two independently derived shadows:

- endpoint evaluation produces the concatenated moving window \(B_{pq}\);
- order-three determinant regularization produces the mixed anomaly carried
  by the same \(pq\) corner.

This does not yet prove that both shadows come from one reciprocal Evans
colligation. It identifies the smallest common source diagram that such a
lift must represent. Deleting the \(pq\) state simultaneously breaks Euler
multiplication, seam concatenation, and the det3 anomaly cancellation.

## Operator target

The next lift should retain the four source states

\[
1,\quad p,\quad q,\quad pq
\]

together with the three interval incidences

\[
[0,\log p],\quad [0,\log q],\quad [0,\log pq].
\]

Its endpoint functor must produce the formulas above, while its determinant
functor must produce the primitive-square counterfactor and the det3 cocycle.
This four-state object is the first finite candidate for the common lift.

## Falsifier

Reject a proposed two-prime lift if:

- it replaces \(B_{q\mid p}\) by the untransported window \(B_q\);
- it omits the \(pq\) state;
- the two addition orders produce different endpoint sections;
- endpoint agreement occurs only after scalar division;
- its determinant shadow does not reproduce the known det3 anomaly cell.

## Scope

This proves exact two-prime endpoint coherence and identifies its shared
source corner. It does not construct the reciprocal operator colligation,
prove Schur–Evans agreement, pass to all primes, or prove RH.
