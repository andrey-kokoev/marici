# Real/complex neutron arrows to existing native coefficients and energy

## Actual new connection

`checkers/check_neutron_arrow_native_bridge.py` passes the source inferred from `inputs/neutron-real-complex-arrows.json` through the unchanged common geometric assembler and prior geometric-to-native bridge. It does not just recount an unrelated stored fixture.

In an isolated temporary input tree, the existing bridge reads the newly inferred neutron action in place of `mode-neutron.json`. It reconstructs all eighteen native ordered triangle modes from the generated six-panel geometry, verifies their intrinsic 36-coordinate numerators against the existing packet, rebuilds the rank-one return, reconstructs the native phase/alignment Hamiltonian entry by entry, and rebuilds all 21 admitted seam projectors. The existing proton bridge remains an independent control in that replay.

The wrapper then reconstructs the retained intrinsic three-sector L/G/N protocol from those verified numerators and compares all coefficients with the stored operators. It uses the prior metric-aware numerator representation; it does not misread it as an ordinary Euclidean matrix. Source content roots, geometry hashes and source files are bound, and shared stores remain unchanged.

## Coefficient-network results

| Stage | Nonzero coefficient transfers |
|---|---:|
| L: sector-local selection | 432 |
| G: sector alignment | 108 |
| N: global return | 1296 |
| Total | **1836** |

There are 36 complex coordinates and a rank-one return. All 1296 closed three-stage cycles have positive exact weights; their sum is one, and their union covers every transfer. Exact serialization recovery passes.

This is the existing intrinsic **three paired-face sectors, twelve coordinates per sector** protocol. The eighteen local triangle modes and their geometric origin are retained, but the sector-wide selection is an explicit native protocol choice. It is not a mere relabeling of the older 54-coordinate ambient belt protocol. Conversion to that old interface carries separately counted costs in the prior research.

Therefore 1836 here is a protocol transfer count. It is not a neutron mass result or evidence that proton and neutron are identical. The count happens to agree with the prior proton protocol, while stage supports, modes, seams and geometry differ.

## Energy results, kept separate from transfer counts

Fresh isolated execution of the prior seam occupation checker verifies:

- Native formation-constraint energy on the return: **zero**.
- Geometric shared edges among subdivided triangles: **24**.
- Seam projectors admitted by the native grouping: **21**.
- Each seam projector annihilates the return; its satisfied-interface complement fixes it.

For the already declared neutral-register occupation law

    h_e = epsilon n_e + J(n_e-S_e)^2 - g X_e,
    S_e = c-P_e,

its existing zero-mixing fixture has epsilon=1/4, J=1/2, kappa=1, g=0. Each of the 21 matched seam registers contributes 1/4 relative to the inactive reference, giving **21/4 in the declared energy unit**. The two prior nonzero-mixing trials are also freshly replayed and retained in the receipt.

This is conditional on the supplied occupation Hamiltonian and its parameters. Coupling occupation to defects P_e instead yields no such increment on the return. Thus neither complex coordinates nor phase persistence alone forces stored occupation energy.

**Do not add 21/4 to 1836:** one is an operator energy in a declared unit; the other counts staged nonzero coefficients. No conversion between them or physical mass calibration has been derived.

## Scope of the single process

The common geometry/cycle process now feeds an existing native coefficient and energy adapter. That adapter still supplies ordered corners and character, frame/plane decoding, paired-face sector grouping, alignment and the occupation law. These are named inputs, not silently derived from six bare arrows.

No new particle-specific weights or doublet-selection rule were invented. This does not yet make one arrow-only coefficient constructor for every particle; it establishes a tested end-to-end neutron branch through already admitted machinery.

## Reproduction

```sh
python research/strominger/checkers/check_neutron_arrow_native_bridge.py
```

Fresh run passed. Complete coefficient packet, native reconstruction report, exact occupation certificate and source hashes:

`research/strominger/results/neutron-arrow-native-bridge.json`.

Predecessors: `neutron-real-complex-arrows.md`, `research/voevodsky/geometric-phase-energy-bridge.md`, `research/voevodsky/checkers/check_belt_three_by_twelve.py`, and `research/voevodsky/checkers/check_seam_occupation_energy.py`.
