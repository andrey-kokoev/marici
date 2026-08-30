# Four-edge support bound for a lower-arity sector bus

Owner: `marici.Kitaev`

Status: exact causal-support lower bound for clean bus architectures; it does
not determine the charge-sensitive overhead.

## Bounded question

Can a lower-arity coherent sector-label gadget avoid touching one of the four
boundary edges?

No.  With oriented holonomy

\[
h=g_0g_1g_2^{-1}g_3^{-1},
\]

for each edge `e_i` there are two basis configurations identical on the other
three edges but having holonomies in different conjugacy classes.  A full
sector label must in particular distinguish flux class, so a circuit whose
causal support omits `e_i` cannot be exact.

Thus every exact sector-label compiler has data support at least four even if
every primitive gate is two-body.  Lowering interaction arity can reduce
fault propagation per primitive, but it cannot shrink the ideal data support.

## Clean-bus baseline

In the standard compute--phase--uncompute architecture, a bus must interact
with all four edges during compute and reverse those interactions to return
clean.  Before any charge-sensitive processing, the serial baseline is

\[
4\text{ forward}+1\text{ phase}+4\text{ reverse}=9
\]

gates.  This matches the existing holonomy compiler and is only a lower bound
for the full sector bus: the previous theorem proves that charge-sensitive
information must be added.

The eight-interaction bound is architectural, not universal over arbitrary
measurement, teleportation, pre-shared entanglement, or destructive gadgets.
Those alternatives require their own resource and fault accounting.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_sector_bus_edge_support.py
```

The checker exhausts all 1,296 edge configurations and produces an omission
witness for every boundary edge.  Saved output:
`research/kitaev/results/s3-sector-bus-edge-support.json`.

Falsifiers are absence of an omission witness, an exact full-sector labeler
with causal support on three edges under the frozen geometry, or a clean
compute--phase--uncompute bus that returns without reversing its information
transfer by some separately declared mechanism.

