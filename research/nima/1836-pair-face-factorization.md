# Pair couplings require more than a face-plane restriction

## Question

Does each 216-arrow bridge between two parent-face sectors of the existing proton-like construction factor through their shared geometric face in the proposed center-to-face tetrahedral subdivision?

## Retained source and tested interface

Use the existing exact L/G/N coefficients and triangle rotations, not rescaled standalone pieces. For two outer faces abc and abd, the proposed constituent tetrahedra Oabc and Oabd share Oab, with O the origin. Its geometric plane is spanned by the two common vertex vectors a,b.

Each sector has nine coordinate ports per stage. A directed cross-sector bridge contains a 9-by-9 G block from local to aligned ports, and a 9-by-9 N block from aligned to raw ports. There are no cross-sector L arrows. Reversing direction supplies the other half of the 216 arrows.

## Exact findings for all six pairs and both directions

| Directed cross-block | Nonzero coefficients | Rank |
|---|---:|---:|
| G | 27 | 3 |
| N | 81 | 1 |

The G block has the native factorization

    x_h -> (1/12) sum_h R_h^T x_h -> (R_g w)_g.

It passes through the three-component common frame. Every entry of this factorization equals the original source coefficient. The N block admits a scalar factorization; exact pivot-row/column multiplication reconstructs every entry.

Because G and N have different stage domains and codomains, retaining them together as one linear map gives diag(G,N), of rank four per direction. Reusing the same coordinate labels must not erase those stage types.

## Face-plane falsifier

A factorization of G through a two-dimensional complex linear interface is impossible because rank(G)=3. There is also an explicit geometric witness: put the normal a cross b into one source triangle slot and zero into the others. Projection of each input vector onto the shared face plane kills this input, while the native G block maps it to a nonzero output. The checker verifies this for every direction.

This tests the ordinary linear face-plane restriction. It does not rule out a richer face record carrying a normal component, stage labels, or higher comparison data. No such native internal-face comparison maps are supplied by the current port graph, so the common-frame factorization must not be renamed a geometric face factorization without them.

## Disposition

The 216 connecting arrows have an exact low-rank structure, but the naive geometric shared-face interface loses data. Per direction, alignment needs three independent coefficient channels and collective feedback needs one; a joint stage-retaining linear interface has dimension at least four. This is an interface requirement, not a quark mass or a proof of the proposed tetrahedral gluing.

## Verification

`python research/nima/checkers/check_1836_pair_face_factorization.py` checks ranks by exact elimination over Q(sqrt(-3)), all common-frame coefficients, scalar factorizations and the explicit face-normal counterexamples. Results: `results/1836-pair-face-factorization.json`. Final invocation: `structured_command_execution:e_32876_1791219380305487000_15`. No publication or commit is claimed.
