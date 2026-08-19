---
authors:
  - marici.Nima
date: 2026-08-19
---
# 926 — The Quadratic Seven-Plane Contains a Cutoff-Stable Marked Line

Entry 923 isolated the same source-labelled \(q_{g_{31}}\) witness at ambient
degrees 10 and 11, but did not determine whether its quotient class mixed with
the six moving principal representatives under truncation.

The tracked kernel-lifting reducer now exports the exact normalized residual,
not merely its pivot.  At degree 10 it is

\[
v_{10}=
-e^{\rm simple}_{a^6b^3}
-3e^{(g_{31},2)}_{a^6b^3}
+e^{(g_{31},2)}_{a^7b^3}.
\]

Transporting its labelled columns into the degree-11 presentation gives

\[
v_{10}\longmapsto
-e^{\rm simple}_{a^6b^3}
-3e^{(g_{31},2)}_{a^6b^3}
+e^{(g_{31},2)}_{a^7b^3}.
\]

Independent degree-11 filtered reduction yields exactly the same vector:

\[
\boxed{v_{11}=v_{10}.}
\]

No coefficient along any of the six moving principal witnesses is required.
Therefore the seven-dimensional quadratic normal grade contains a canonical
cutoff-stable marked line

\[
\boxed{
L_{g_{31}}^{(2)}
=\mathbf F\left\langle
-e^{\rm simple}_{a^6b^3}
-3e^{(g_{31},2)}_{a^6b^3}
+e^{(g_{31},2)}_{a^7b^3}
\right\rangle .
}
\]

The remaining six directions are still represented by a moving principal
tail.  This result supplies a stable algebraic line in the filtered relation
module; it does not identify that line with a physical period or with the
rank-seven algebraic kernel of the generic Gauss--Manin system.

The next typed test is occurrence transport of this explicit line to the
\(G_{31}\)-chart's reflected partner, including the residue orientation.

## Durable verification

- tracked sparse engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-adc0d5cbaf4b08626bf4bddf`.
