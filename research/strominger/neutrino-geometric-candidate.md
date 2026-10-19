# Adding a neutrino candidate to the relative geometric catalogue

Date: 2026-10-11
Status: exploratory exact construction; no physical identification.

## Proposed fourth carrier

Use an oriented equilateral triangle as a **candidate internal carrier**, not as a claim that a physical neutrino is a planar object. It is the two-dimensional simplex member beside the existing tetrahedral and four-simplex presentations. This is a new modeling choice; the existing sources do not force it.

| Label | Intrinsic geometry | Vertices | Admitted boundary facets | Center-cone cells |
|---|---|---:|---:|---:|
| Proton | tetrahedron, dimension 3 | 4 | 4 | 4 |
| Neutron | triangular belt, dimension 3 | 6 | 6 (two caps reserved) | 6 |
| Electron | four-simplex, dimension 4 | 5 | 5 | 5 |
| Neutrino candidate | triangle, dimension 2 | 3 | 3 | 3 |

These are geometric counts, not constituent numbers, masses or generations. The comparison checker reconstructs all four using Voevodsky's unchanged `assemble_relative_geometry.py`. No active Voevodsky contract, ledger or source is edited.

## Source and exact construction

Source: `inputs/relative-neutrino-candidate.json` in this directory.

In affine coordinates choose

    G = [[8,4],[4,8]],
    T(u,v) = (1-u-v,u),
    seed = (0,0).

The seed orbit is `(0,0), (1,0), (0,1)`. Every squared edge length is eight. The order-three, orientation-preserving affine isometry fixes the center `(1/3,1/3)`. The shared constructor derives three supporting edges and cones them to the center, with positive oriented area determinants. Interior radial edges cancel in the chain boundary, leaving the outer triangle; its boundary has zero boundary.

A declared attachment-pole mark selects the opposite edge. Deleting that mark preserves the triangle but removes its attachment designation: the port is extra source data, not forced by shape.

## Spin and neutrality decoration

Attach a two-component internal space with the exact unitary lift

\[
U=\operatorname{diag}\left(\frac{1+\sqrt{-3}}2,
                           \frac{1-\sqrt{-3}}2\right).
\]

Then `det U=1`, `U^3=-I`, and `U^6=I`. Its adjoint transverse rotation has an order-three phase, matching the triangle cycle up to orientation convention. The two coordinate projectors commute with the lift and provide two possible spin-axis sectors. Neither is selected as physical neutrino helicity. A finite cyclic lift does not by itself supply a full rotation representation, Lorentz covariance, a Weyl equation or fermionic statistics.

Declare the external electric charge operator `Q=0`. This gives an explicitly neutral decoration, but **neutrality is not inferred from the triangle**. The same geometry could instead be decorated by a charged action. Likewise, the candidate does not explain why weak production selects a chirality. For massive neutrinos, chirality and helicity must not be identified indiscriminately.

Three vertices are NOT three neutrino flavors. No sterile-neutrino, seesaw, dark-matter or Gram-sector claim is imported from other research.

## Checks and controls

Fresh execution passes 19 exact checks, including:

- orbit, metric, center, supporting-edge and oriented chain identities;
- unitary spin lift and its three-/six-step returns;
- rejection of a non-isometric metric perturbation;
- failure of spanning when the cycle generator is deleted;
- rejection of injected target-cell lists;
- attachment-role deletion control.

Arithmetic uses rational numbers and the exact quadratic field `Q(sqrt(-3))`, with no floating-point tolerance or external algebra dependency.

Run from the repository root:

```sh
python research/strominger/checkers/check_neutrino_geometric_candidate.py
```

Result: `research/strominger/results/neutrino_geometric_candidate.json`, containing the full candidate geometry, source hashes, spin decoration and reconstructed four-model catalogue.

## Next discriminating construction

The useful next test is an explicit retained, charge-preserving weak-transition interface for a candidate channel such as

\[
n\longrightarrow p+e^-+\bar\nu.
\]

This notation states a proposed comparison target, not a constructed reaction. It needs sector identification, tensor-product input/output spaces, charge assignments, an actual intertwining vertex, spin/angular-momentum and energy accounting, and a conjugate-partner contract. Vertex-count arithmetic cannot substitute for that map.

Other open gates: source selection of this carrier/metric; propagation and physical chirality; mass/mixing; Dirac versus Majorana character; and empirical admission. The current contribution is a checked fourth **geometric candidate**, not a neutrino theory.
