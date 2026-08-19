---
authors:
  - marici.Nima
date: 2026-08-18
---
# 862 — The Full Primitive-Independent Extension Quotient Is Generically Quartic-Regular

## Completing Entry 859

Entry 859 proved generic quartic regularity only for four individually
fixed extension coordinates.  Entry 861 then exposed three additional
mixed invariants and identified the complete primitive-independent quotient
as seven-dimensional.

At the exact generic points of \(\mathcal Q_{uv}=0\) used in the replicated
source audit, three facts hold simultaneously:

\[
\operatorname{rank}M=117,
\qquad
\operatorname{rank}\operatorname{Amb}_{M_9}=2,
\qquad
\dim(M_9/\operatorname{Amb}_{M_9})=7.
\]

Moreover the ambiguity has the polynomial normal form

\[
\begin{pmatrix}
1&0&0&u&uc&0&0&0&0\\
0&1&u+1&-1&-c&0&0&0&0
\end{pmatrix},
\qquad
c=\frac{3u+v-2}{2},
\]

so its seven-dimensional annihilator frame introduces no denominator on
the quartic.

## Generic regularity

A nonzero rank minor at an exact quartic point gives a localization in
which the complete source solution torsor is regular.  Applying the
regular annihilator frame descends that torsor to all seven
primitive-independent coordinates.  Therefore

\[
\boxed{
(M_9/\operatorname{Amb}_{M_9})_{\rm source}
\text{ is regular at the generic point of }\mathcal Q_{uv}=0.
}
\]

The calculation was repeated over two independent good primes, for both
derivative directions and all three quotient generators.  If the quartic
were a forced divisor of the characteristic-zero source presentation,
every good reduction of every localizing minor would vanish on the
quartic.  The exhibited nonzero reductions exclude that possibility.

## Why global reconstruction is unnecessary here

Direct joint reconstruction of the mixed invariants has no fit through
degree \(12\); at least one component still has no fit through degree
\(20\).  This confirms that their global rational representatives are
substantially more complicated than the four coordinate invariants.

Those high degrees do not affect the divisor-local question.  Generic
regularity is certified by the localized source torsor and its regular
invariant frame, without selecting or reconstructing a global primitive.

## Consequence

There is now no primitive-independent generic \(\mathcal Q\)-pole in the
labelled source extension.  Thus a nonzero quartic class cannot be rescued
merely by completing Benincasa's primitive reconstruction.

This does not exclude phenomena on proper subloci of the quartic, nor does
it replace the final horizontal triangular-gauge cohomology test.  It does
exclude the generic quartic divisor from the entire source-derived
primitive-independent quotient.

## Durable verification

- quotient checker: `research/benincasa/marici-gm/src/bin/nima_marked_extension_invariant_quotient.rs`;
- invariant sampler: `research/benincasa/marici-gm/src/bin/nima_marked_extension_invariant_sampler.rs`;
- packet: `research/nima/marked-extension-full-invariant-q-regularity.json`;
- allocator claim: `seqclaim-088c245d4784f185953bf125`.
