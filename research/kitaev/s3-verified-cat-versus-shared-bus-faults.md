# Verified cat control versus shared-bus faults

Owner: `marici.Kitaev`

Status: exact bit/phase fault split for the control fanout; coherent bus
verification remains unconstructed.

## Bounded question

Does a verified cat control reduce the four-edge single-fault spread of the
lower-arity sector compiler?

It reduces one component but not the combined worst case.  Encode the logical
control into four repetition-cat rails and verify the adjacent parities

\[
Z_0Z_1,\quad Z_1Z_2,\quad Z_2Z_3.
\]

Every single rail `X` error has a nonzero syndrome.  Conditioned on successful
pre-verification, a later rail or transversal controlled-gate fault touches at
most the one data subsystem assigned to that rail.  A rail `Z` fault does not
spread through a diagonal controlled phase, though it may corrupt the logical
record phase.

## Why the global bound does not improve

The centralizer-Fourier compiler still uses shared coherent holonomy and
sector-label buses.  Those buses revisit a causal cone containing all four
data edges.  Cat parity checks say nothing about a bus fault, so an arbitrary
single bus fault can still reach data weight four.

Hence

\[
\max(1\text{ from accepted cat control},4\text{ from shared bus})=4,
\]

and arbitrary recovery still requires distance at least nine.  A global
improvement needs a verified coherent bus or fresh-bus segmentation whose
sector-label coherence and cleanup are proved.  Merely copying the bus and
checking classical equality is not sufficient for arbitrary coherent errors.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_verified_cat_bus_fault_split.py
```

The checker enumerates all four single-rail bit faults, their exact parity
syndromes, and composes the cat and shared-bus light-cone bounds.  Saved output:
`research/kitaev/results/s3-verified-cat-bus-fault-split.json`.

Falsifiers are an undetected single rail-X fault, an accepted transversal
control fault reaching multiple assigned data subsystems, or a source-derived
bus-verification scheme proving a smaller arbitrary light cone.

