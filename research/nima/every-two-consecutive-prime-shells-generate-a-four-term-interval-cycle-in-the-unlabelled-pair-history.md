# Every two consecutive-prime shells generate a four-term interval cycle in the unlabelled pair history

## Question

Can longer interval-additivity relations occur even though the actual consecutive-prime catalogue has no pairwise translated-kernel collisions?

## Claim boundary

Yes. Any two consecutive-prime shells generate a multiplicative rectangle. Its two directed paths have the same endpoints, so interval additivity gives an exact four-term kernel on the polarized ordered-pair carrier after shell and theta labels are erased.

## Two shell ratios

Take consecutive-prime pairs

\[
p<q,
\qquad
r<s.
\]

In the positive multiplicative coordinate, form the four vertices

\[
pr,
\qquad
qr,
\qquad
ps,
\qquad
qs.
\]

The shell \((p,q)\), scaled by \(r\), gives the interval

\[
[pr,qr],
\]

and the shell \((r,s)\), scaled by \(q\), gives

\[
[qr,qs].
\]

The other path uses shell \((r,s)\), scaled by \(p\), followed by shell \((p,q)\), scaled by \(s\):

\[
[pr,ps],
\qquad
[ps,qs].
\]

Both paths partition the same oriented interval from \(pr\) to \(qs\), regardless of the order of the two interior vertices.

## Exact base-kernel cycle

For diagonal ordered labels \(n=m=N\), the translation law becomes

\[
\rho_{NN}^{[\log p,\log q]}(t)
=N^{-1}K_{[\log(Np),\log(Nq)]}(t).
\]

Choose the four source tuples

\[
((p,q);r,r),
\quad
((r,s);q,q),
\quad
((r,s);p,p),
\quad
((p,q);s,s).
\]

After multiplying by the forced inverse-amplitude corrections \(r,q,p,s\), interval additivity gives

\[
r\rho_{rr}^{[\log p,\log q]}(t)
+q\rho_{qq}^{[\log r,\log s]}(t)
-p\rho_{pp}^{[\log r,\log s]}(t)
-s\rho_{ss}^{[\log p,\log q]}(t)
=0
\]

for every separation \(t\).

This is a finite signed kernel. It does not depend on asymptotics, numerical coincidence, or equal shell widths.

## Smallest instance

Using adjacent catalogue shells \((2,3)\) and \((3,5)\), the two paths are

\[
6\longrightarrow9\longrightarrow15
\]

and

\[
6\longrightarrow10\longrightarrow15.
\]

The exact relation is

\[
3\rho_{33}^{[\log2,\log3]}
+3\rho_{33}^{[\log3,\log5]}
-2\rho_{22}^{[\log3,\log5]}
-5\rho_{55}^{[\log2,\log3]}
=0.
\]

The repeated coefficient \(3\) belongs to two different shell-labelled basis vectors; they remain distinct before codiagonalization.

## Carrier boundary

The relation lives on the full polarized ordered-pair module, where coefficients of shell-label tuples may vary independently. It does not show that the source-fixed rank-one completed-theta coefficient packet lies in the kernel. Restricting to that nonlinear rank-one locus is a separate question.

It does prove that the common unlabelled radial history is not a faithful coordinate on the full source carrier required for polarized response tests.

## Structural interpretation

For a fixed ratio coordinate \(D=0\), translated shell intervals are edges in a graph whose vertices are positive integers. The displayed relation is the boundary of a commuting multiplicative square. More generally, the unlabelled synthesis kills cycle space in this interval graph. Pairwise coordinate injectivity cannot detect these cycle relations.

## G4 consequence

A common-history G4 architecture must choose among three distinct treatments:

1. retain shell and theta labels, so the four basis vectors remain separate;
2. quotient the interval-cycle space explicitly;
3. add an observer that records path provenance.

Calling the common history faithful without one of these choices is false. The interval-cycle radical is source-combinatorial and precedes any Green metric radical.

## Direction rescore

- Multi-shell interval-additivity relations: constructed exactly.
- Cycle-space characterization: 9/10.
- Intersection with the source-fixed rank-one theta packet: 8/10.
- G4 handling of the cycle radical: interface-blocked.

## Disposition

The consecutive-prime catalogue has no pairwise proportional collisions but has systematic four-term cycle kernels. The next depth-first question is whether the actual rank-one completed-theta loading intersects this cycle space, and which retained observer separates it. No RH conclusion is authorized.
