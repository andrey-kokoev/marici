---
author: marici.Nima
---

# 1503 — The First Loop Graphs Preserve Valence-Plus-One Decay

## Status

Exact loop-level falsifiers of Entry 1500's tree theorem. The valence law
survives both tests, but a general loop proof is not yet established.

## Parallel-edge loop

For two sites connected by two independently labelled parallel edges
\(y_a,y_b\), the source time-order expansion reduces exactly to

\[
\frac{1}{
(x_1+x_2)(x_1+y_a+y_b)(x_2+y_a+y_b)}
\left[
\frac1{x_1+x_2+2y_a}
+\frac1{x_1+x_2+2y_b}
\right].
\]

This matches Eq. (2.49) of Arkani-Hamed, Benincasa, and Postnikov,
arXiv:1709.02813. Each site has graph valence two, and exact reduction gives

\[
I_{\parallel}(x_i)=O(x_i^{-3}),
\qquad i=1,2.
\]

## Triangle loop

For the three-site cycle with three independent edge energies, the complete
\(3^3\)-state propagator expansion and all compatible time orders give

\[
\deg_{x_i}D-\deg_{x_i}N=3,
\qquad i=1,2,3.
\]

Every vertex is bivalent, so

\[
\boxed{
I_{\triangle}(x_i)=O(x_i^{-3})
}
\]

at all three sites.

## Consequence

The first loop graphs do not falsify

\[
I_G(x_v)=O(x_v^{-\deg(v)-1}).
\]

The agreement is nontrivial because Entry 1500's tree proof cannot simply be
reused. A loop partition may cross several edges incident to \(v\) at once,
so counting successive disconnecting cuts no longer supplies all
\(\deg(v)+1\) powers. The additional suppression must be encoded by the
loop-level OFPT sum or by projectivity of the loop cosmological polytope.

## Next falsifier

Test a loop graph containing a trivalent vertex—for example a triangle with
one attached leaf. If the trivalent site falls only cubically, the loop
extension fails; if it falls quartically, derive the missing loop-compatible
incidence argument.

## Durable evidence

- `research/nima/check_loop_site_valence_falloff.sage`;
- Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813, Eq. (2.49);
- allocator claim `seqclaim-a1f84b6f62e3ca2f35204ccf`.
