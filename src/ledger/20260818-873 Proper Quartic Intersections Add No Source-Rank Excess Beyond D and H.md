---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 873 — Proper Quartic Intersections Add No Source-Rank Excess Beyond D and H

## Question

Entry 863 found rank (116) on both

\[
\mathcal Q\cap D
\qquad\text{and}\qquad
\mathcal Q\cap H.
\]

After Entry 871 excluded an intrinsic generic \(\mathcal Q\)-residue, the
remaining source-matrix question was whether imposing \(\mathcal Q=0\) creates
an additional rank defect on either existing divisor.

## Generic divisor census

Using the complete labelled (132\)-equation, (372\)-unknown source system,
we evaluated generic points of

\[
D=-4+12u-6uv+4v-9u^2+4u^2v-v^2=0
\]

and

\[
H=-2-3u+2uv+v-u^2v+u^3=0
\]

away from \(\mathcal Q=0\) and deeper soft loci.  Across two independent
large primes the generic signatures are

\[
\begin{array}{c|c|c|c}
\text{divisor}&\operatorname{rank}M&\text{fixed mask}&\text{pivot hash}\\
\hline
D&116&5&8576889687366901377\\
H&116&3&8576889687366901377.
\end{array}
\]

These are exactly the rank and fixed-mask signatures reported by Entry 863
at \(\mathcal Q\cap D\) and \(\mathcal Q\cap H\).

## Narrow conclusion

\[
\boxed{
\mathcal Q\cap D\text{ and }\mathcal Q\cap H
\text{ add no source-rank excess beyond the generic }D,H\text{ defects.}
}
\]

Thus the rank-(116) intersections are inherited from the existing carrier
divisors in the literal sense: imposing \(\mathcal Q\) does not lower the
source rank further.

This does not prove that the supported nearby-cycle or physical comparison
is trivial.  Equal ranks and masks do not exclude an extension class with
unchanged rank.  Any surviving \(\mathcal Q\)-phenomenon at these intersections
must therefore be sought in a typed coefficient/physical specialization map,
not in an additional source-rank defect or carrier stratum.

The deeper points \((u,v)=(2,4)\in D\) and \((2,0)\in H\) were excluded from
the generic census; their ranks (92) and (82) belong to deeper existing
support.

## Durable verification

- checker: `research/benincasa/marici-gm/src/bin/marked_extension_known_divisor_excess.rs`;
- packet: `research/benincasa/marked-extension-known-divisor-excess.json`;
- primes: (2305843009213693951) and (2305843009213693723);
- allocator claim: `seqclaim-7985ae12ce63c85ac40626a0`.
