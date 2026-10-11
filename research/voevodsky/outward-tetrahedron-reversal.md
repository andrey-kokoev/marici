# Outward tetrahedral construction: an incidence-reversal candidate

## Construction to test

The operator asks for the electron to do something in reverse and for its new tetrahedron to build outward from its own barycenter. The proposed precise interpretation here is reversal of tetrahedral flag incidence, not reversal of a shrinking animation.

```text
Inward flag:   vertex → edge → face → body
Outward flag:  body → face → edge → vertex
Spatial view: body barycenter → face center → edge midpoint → vertex
```

The outward construction starts at one root, branches to four face centers, then to three edge midpoints per face, then to two endpoints per edge. This generates 4×3×2 = 24 labelled paths. Shared edges and vertices remain shared: the four layers contain 1, 4, 6, and 4 distinct nodes, not 1, 4, 12, and 24 distinct spatial points.

Each complete flag supplies the same four corners of one barycentric small tetrahedron as before, but its construction order and arrows are reversed. Together the 24 small tetrahedra fill the new tetrahedron. Their outer vertices have the original tetrahedron's scale.

This is branching, not recovery of a unique predecessor from an unlabeled center. The root is supplied with the tetrahedral incidence data. Retaining a flag distinguishes its route through the shared nodes.

## What remains fixed

Choose the new tetrahedron's coordinates and attachment of its barycenter once. Reveal its incidence layers in the order above. Existing points never move; there is no radial contraction or expansion of an already built solid. The host geometry is not involved in the layer-generation rule.

The display can place the root at the selected host attachment vertex. This placement alone does not specify a pullback: the attachment maps must still be supplied. The incidence calculation below deliberately does not manufacture host-side layers, a belt, or an isotope difference.

## Algebraic distinction

For the oriented simplex, the outward signed incidence is the usual boundary operator:

```text
C3 → C2 → C1 → C0.
```

Its transpose gives the inward coboundary on the dual cochain spaces. Reversing the incidence relation is involutive; the boundary operator is not an inverse of the coboundary. Boundary-squared cancellation is an identity of signed sums, not deletion of the separately retained traversal histories.

This gives an exact meaning of reversal for the flag construction. It does not yet establish that the proton's full typed coefficient protocol reverses in the same way. In particular, reversing the selected projector cannot mean taking its inverse: it has a nonzero kernel, as checked in `fold-coefficient-attachment.md`.

## Check

```text
python research/voevodsky/checkers/check_outward_tetrahedron_reversal.py
```

Twelve checks pass: node and arrow counts, all 24 reversed paths, involutive reversal, branching, strictly increasing barycenter radii along outward incidences, unchanged terminal scale, and the oriented boundary identity. These test the candidate construction, not its identification with an electron.

## Consequence for the next visualization

Show construction stages, not a shrinking tetrahedron. Draw the host unchanged and generate the new tetrahedron from its attached root. The hydrogen/deuterium distinction needs its own specified additional structure; incidence reversal by itself provides no difference between those two cases.
