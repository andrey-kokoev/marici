# Distinct shell endpoints make the entire projective diagonal source codiagonally faithful

## Question

Can the late-shell projective faithfulness theorem be extended across the finitely many early and transition shells?

## Claim boundary

Yes when shell lower endpoints are distinct and every shell is nontrivial. A transition zero of the completed-theta atom changes only the endpoint prefactor order, not the decisive double-exponential scale. The smallest active endpoint still has the slowest separation tail. Combining finite endpoint-germ asymptotics with the late projective majorant proves faithfulness for the entire ordered diagonal shell family.

## Endpoint germ at an arbitrary shell

Let

\[
\rho_{a,b}(t)
=
\int_a^b\Phi(u)\Phi(u+t)\,du,
\qquad a<b.
\]

The completed forcing \(\Phi\) is real analytic and not identically zero. At the lower endpoint \(a\), let \(r_a\ge0\) be its finite vanishing order:

\[
\Phi(u)
=(u-a)^{r_a}\gamma_a(u),
\qquad
\gamma_a(a)\ne0.
\]

For large positive \(t\), the shifted completed-theta factor is controlled by its first theta label and contains

\[
\exp\left[-\pi e^{2u}e^{2t}\right].
\]

Watson endpoint localization at \(u=a\) therefore gives

\[
\rho_{a,b}(t)
=B_{a,b}(t)
\exp\left[-\pi e^{2a}e^{2t}\right]
\left(1+o(1)\right),
\]

where \(B_{a,b}\) is nonzero for all sufficiently large \(t\) and differs from the generic late-shell prefactor by a finite power determined by \(r_a\). A zero at \(a\) changes this finite power but not the coefficient \(e^{2a}\) in the double exponential.

## Strict endpoint ordering

For two nontrivial shells with \(a<c\),

\[
\frac{\rho_{c,d}(t)}{\rho_{a,b}(t)}
=
\frac{B_{c,d}(t)}{B_{a,b}(t)}
\exp\left[
-\pi\left(e^{2c}-e^{2a}ight)e^{2t}
\right]
\left(1+o(1)\right)
\longrightarrow0.
\]

No finite endpoint vanishing order can compensate for the displayed scale separation.

## Projective family

Let \(a_1<a_2<\cdots\) be all shell lower endpoints, including the finite early and transition portion, and let \(c_j\) be projectively exponentially summable. If the loaded codiagonal vanishes, then

\[
\sum_j c_j\rho_j(t)=0.
\]

A nonzero packet has a least active index \(j_0\). The finitely many endpoints below the late regime cause no summability problem. For the infinite late tail, the previously proved majorant

\[
C_{j_0}e^{Ma_j}
\exp\left[-c_Te^{2a_j}ight]
\]

is summable against \(|c_j|\). Dominated convergence after division by \(\rho_{j_0}(t)\) yields

\[
c_{j_0}=0,
\]

a contradiction. Hence every coefficient vanishes.

## Result

For the full projective diagonal shell source with distinct lower endpoints,

\[
\ker(DJ_{\rm or})
\cap
\mathcal A_{\exp}^{\rm diag}
=\{0\}.
\]

Early shells and transition zeros introduce no new codiagonal radical.

## Strength boundary

The endpoint scale distinguishes shells, not internal labels at the same endpoint. The unresolved classes are now narrower:

- repeated lower endpoints with different theta-label or ordered-pair content;
- off-diagonal pair histories;
- later G4 metrics or codiagonals that differ from the source map.

Those require internal incomplete-gamma asymptotics rather than endpoint ordering alone.

## G4 consequence

The entire diagonal arithmetic source survives the source radial codiagonal, including signed projective completion. A G4 radical cannot remove a nonzero diagonal packet while claiming to use only this codiagonal. It must identify an additional metric null direction, gauge relation, or compression.

## Direction rescore

- Full projective diagonal shell faithfulness: completed for distinct endpoints.
- Early and transition shells: absorbed by endpoint-germ asymptotics.
- Repeated-endpoint internal labels: 8/10.
- Ordered off-diagonal packets: 7/10.
- G4 radical comparison: interface-blocked.

## Disposition

The diagonal codiagonal-kernel audit is complete at source level for distinct shell endpoints. The next depth-first source question is internal separation at a fixed endpoint, where theta-label and ordered-pair exponents replace shell position as the asymptotic discriminator. No RH conclusion is authorized.
