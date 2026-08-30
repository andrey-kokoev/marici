# 1817 — The Physical Five-Site Current Activates Every Active Transverse Gysin Line

## Correction to the source gate

Entry 1816 correctly shows that `five-cycle-ofpt-packet.json` alone does not
contain a physical chain. It does not exhaust the frozen five-site source
objects. Entries 1216--1217 independently construct:

- the oriented Euclidean current \(d^3\ell\);
- its external-Gram Kummer density;
- the physical positive sheet \(y_i\ge0\).

Those objects legitimately supply the missing Betti input without importing
an ad hoc regulator hierarchy.

## Local intersection calculation

At each active threshold point, orient the two-dimensional Morse tangent plane
by the ambient physical current and its threshold normal. For an ordered wall
pair \((A,B)\), let

\[
J_{A,B}=n\cdot(\nabla_Tg_A\times\nabla_Tg_B).
\]

Exact rational interval arithmetic evaluates \(J_{A,B}\) for:

\[
22\ \text{active pairs}
\times
2\ \text{physical sheets}.
\]

All 44 intervals exclude zero.

The real-chain intersection index is

\[
\operatorname{sgn}J_{A,B}.
\]

Entry 1813's residue orientation line transforms by the same sign. Their
pairing therefore has source-normalized value

\[
\boxed{+1}
\]

for every labelled local occurrence.

## Result

The physical five-site current activates all 22 local transverse Gysin lines,
and hence all 110 members of their free cyclic assembly. The activation is
canonical at local Betti/de Rham intersection level.

This supersedes only Entry 1816's global stopping conclusion. Its narrower
statement about the insufficiency of the OFPT denominator packet remains
valid.

No claim is made here about global analytic-continuation monodromy away from
the Euclidean physical chamber.

## Architectural consequence

The full mechanism is now source-derived:

\[
\text{physical current}
+\text{transverse carrier incidence}
+\text{oriented Gysin line}
\longrightarrow
\text{nonzero physical coefficient pairing}.
\]

No new carrier generator or fitted regulator is required.

## Next falsifier

Combine the local intersection pairing with the exact source residue
coefficients and cyclic transitions to construct the rank-110 supported
physical coefficient object. Test its specialization at the constant-field
threshold node and its compatibility with the external-Gram Kummer density.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_physical_intersections.py
- research/benincasa/results/five-site-g5-transverse-pair-physical-intersections.json
- Entries 1216, 1217, 1813, and 1816
- allocator claim: seqclaim-9d6f6af2cd1ad1a22062dac4
