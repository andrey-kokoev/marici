# Benincasa five-sector cover obstruction

## Question

Do the five local residue sectors and cyclic relabellings define a sector-overlap nerve or a new coherence-pyramid Carrier?

## Claim boundary

The audit uses the frozen five-site region-pair soft-overlap gate. It preserves local residue and cyclic-equivariance results but does not infer overlap maps from relabelling symmetry.

## Available local data

The source provides:

- five residue sectors;
- cyclic relabelling isomorphisms;
- sector-local double-Leray germs;
- an occurrence-forgetting incidence map.

This defines an equivariant family of local objects. It does not define their pairwise overlaps.

## Missing overlap interface

A Čech nerve would require, at minimum:

- coefficient objects on each pairwise overlap;
- restriction maps from both local sectors;
- a source-derived Čech differential;
- descent or colimit assembly.

All four are absent. The missing maps are undefined, not zero. Cyclic covariance acts on the direct sum of local sectors and does not supply gluing.

## Nerve consequence

Five named local vertices exist, but no nondegenerate overlap edge is typed. Therefore the intended five-cycle cannot yet be assigned cycle rank: the overlap incidence object itself is undefined. This differs from an admitted discrete five-vertex nerve with cycle rank zero.

The occurrence-forgetting rank-34 kernel records incidence redundancy only. It is not overlap cohomology and cannot replace the missing Čech differential.

## Physical pairing boundary

The related transverse-pair gate also lacks integration chains, contour orientation, denominator regulator, and relative-boundary maps. Its physical pairing is undefined, neither zero nor nonzero. Hence physical pairing cannot supply the missing overlap interface.

## Disposition

The Benincasa data form a typed local-sector family but not an admitted coherence-pyramid sector vertex or overlap nerve. The first reopening object is a source-derived pairwise-overlap correspondence with its two restriction maps. Until then, cyclic relabelling and local residue computations must remain separate from descent.

## Verification

- `research/voevodsky/checkers/check_benincasa_five_sector_cover.py`
- `research/voevodsky/results/benincasa_five_sector_cover.json`
