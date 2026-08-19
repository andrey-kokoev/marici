---
authors:
  - marici.Nima
date: 2026-08-18
---
# 863 — Proper Quartic Rank Losses Lie on Existing Divisor Intersections

## Exact intersection support

Entry 862 excludes a source rank loss at the generic point of
\(\mathcal Q_{uv}=0\).  SageMath exact elimination now locates its proper
intersections with the known diagonal divisors.  For the two nonlinear
letters,

\[
\boxed{
\operatorname{Res}_v(\mathcal Q,D)
=-u^4(u-4)^2(16u^3-57u^2+56u-16)
}
\]

and

\[
\boxed{
\operatorname{Res}_v(\mathcal Q,H)
=u^3(3u^2-6u+1)(u^3-2u^2-5u+8).
}
\]

For the relevant linear letters,

\[
\operatorname{Res}_v(\mathcal Q,u+v-2)=-u^3(5u-8),
\]

\[
\operatorname{Res}_v(\mathcal Q,v-2)=-u^2(u-2)^2.
\]

Thus every candidate special point is already an intersection with a
predeclared diagonal or soft carrier.

## Source-rank census

The complete labelled source system was evaluated at finite-field
representatives of these strata.  The signatures, uniform across both
derivatives and all three quotient generators, are

\[
\begin{array}{c|c|c}
\text{stratum}&\operatorname{rank}M&\text{fixed mask}\\
\hline
\mathcal Q\cap D&116&5\\
\mathcal Q\cap H&116&3\\
\mathcal Q\cap\{u+v-2=0\},\ u=8/5&114&3\\
(u,v)=(2,2)&92&512\\
(u,v)=(0,2)&73&0
\end{array}
\]

The previously observed rank-\(116\) point is therefore not mysterious:
it lies on \(D=0\).  At \(u=4\), both \(D\) and \(\mathcal Q\) restrict to
the same quadratic \(v^2-44v+100\), explaining the squared resultant
factor.

## Narrow conclusion

\[
\boxed{
\text{Every observed proper-}\mathcal Q\text{ rank loss is inherited from
an existing carrier intersection.}
}
\]

No new quartic-only carrier stratum is indicated.  The finite-field census
uses representative rational points; it does not assert identical ranks
at every algebraic conjugate point without an extension-field audit.

The remaining quartic question is consequently coefficient-theoretic or
physical, not a missing generic or proper algebraic carrier discovered by
the source rank matrix.

## Durable verification

- point gate: `research/benincasa/marici-gm/src/bin/nima_marked_extension_q_fiber_gate.rs`;
- packet: `research/nima/quartic-known-divisor-intersections.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-37f576cfdf98175b34f98249`.
