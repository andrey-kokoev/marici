# 1867 — Ninety-Six Nonzero Dihedral Triple-Wall Candidates Remain

## Frozen census

The five-cycle OFPT packet contains 242 free \(C_5\)-orbits of compatible
labelled triple-wall subsets. Compatibility means that all three walls occur
in at least one frozen source term; it does not assert a Landau solution.

## Dihedral geometric reduction

The regular-cone physical slice of Entry 1234 has the full spatial dihedral
symmetry \(D_5\). Reflecting every source label, cut occurrence, and wall
coefficient therefore preserves the scalar Landau eliminant, although it may
change an oriented residue sign.

Exact labelled canonicalization gives

\[
242\ C_5\text{-orbits}
\longrightarrow
138\ D_5\text{-geometric orbits}.
\]

Among these, 34 are reflection-fixed and 104 pair two distinct cyclic
occurrence orbits. This reduction is for scalar elimination only; the paired
occurrences remain distinct in any oriented Cut or residue assembly.

## Forced-zero gate

A compatible subset is confined to \(t=0\) if either:

1. it contains the total-energy wall \(G=5t\); or
2. it contains two connected-region walls with the same cut support but
   unequal cardinalities.

In the second case subtracting the two wall equations gives

\[
(|A|-|B|)t=0,
\]

and the five-cycle's odd cardinality ensures \(|A|\ne|B|\) for complementary
same-cut regions.

This removes 70 cyclic orbits, or 42 dihedral geometric orbits. Therefore

\[
\boxed{
96
}
\]

nonzero dihedral triple-wall candidates remain.

## Narrow result

The exact three-wall elimination workload is reduced from 242 labelled cyclic
representatives to 96 nonzero geometric representatives without forgetting
which cyclic occurrences each representative controls. No new singular
factor has yet been asserted.

## Next falsifier

Construct the stationary ideal for each of the 96 representatives, saturate
by soft, coincident-focus, and vanishing-multiplier components, and compute its
eliminant in \(z=t^2\). Compare every nonconstant factor with Entry 1866's
degree-83 square-free polynomial before enlarging the Picard--Fuchs
denominator bound.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_compatible_landau_subsets.rs`
- `research/benincasa/results/five-site-compatible-landau-subsets.json`
- Entries 1234, 1236, and 1866
- allocator claim: `seqclaim-c889002364e6b3c7c46de388`
