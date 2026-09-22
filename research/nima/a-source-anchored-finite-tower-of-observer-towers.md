# A source-anchored finite tower of observer towers

## Result

The two-index proposal has a working exact prototype:

- jet depth `m=0,1,2,3`, with carrier dimensions `1,4,7,8`;
- coherence/nerve dimension `n=0,1,2,3,4`.

At every jet depth there are four explicit rational coordinate realizations. Their comparisons, composition triangles and higher compatibility cells form a strict realization groupoid's nerve. Truncating jet depth commutes with these comparisons and their faces and degeneracies.

This is a finite **tower of coherently related observer-realization towers**, anchored to the actual forgotten source products. It is not an infinite verification, nor four new layers of measurement hardware.

## 1. The source anchor

On the eight forgotten block paths, let Z be the interaction transform

`Z[t,b] = 1 if b contains t, otherwise 0`.

The checker independently verifies all 64 coefficients against actual ordered Fox rows. The depth-m carrier retains the moments indexed by subsets of size at most m.

Choose four invertible realization matrices A_i: identity, a triangular shear, a degree scaling with another shear, and their composite. The shears/scaling do not all commute. Each output moment of degree d depends only on input moments of degrees at most d.

Consequently these matrices descend to every truncated jet carrier. The source anchors and comparison maps are

`E_i^m = A_i^m Z_m`,

`F_ji^m = A_j^m (A_i^m)^(-1)`.

The exact identities checked are

`F_ji^m E_i^m = E_j^m`,

`F_kj^m F_ji^m = F_ki^m`,

`P_mq F_ji^m = F_ji^q P_mq`.

The last equation ties the two tower directions together. It would be insufficient to build an unrelated coherence structure at each depth.

## 2. What the higher towers contain

Here coherence dimension is indexed starting with observer realizations:

| Dimension | Data |
|---|---|
| 0 | realized jet carriers |
| 1 | comparisons between realizations |
| 2 | composition triangles |
| 3 | compatibility among their boundary triangles |
| 4 | the next compatibility among boundaries |

A simplex is an ordered sequence of realizations. Faces remove a vertex and compose the neighboring comparisons; degeneracies insert an identity comparison. The checker verifies the simplicial identities and agreement of each composed route with the direct comparison.

Per jet depth, the numbers of labelled cells are `4,16,64,256,1024`, including repeated-frame degeneracies. These counts do not measure new information. The higher cells are forced by strict composition; they are not independently chosen higher homotopies.

## 3. The source product still controls the construction

For compatible packets, moments multiply by the ordered tensor product. The actual source multiplication is checked on the interaction bases.

At realization i, the transported product is

`B_i = A_i^(n+k) ((A_i^n)^(-1) tensor (A_i^k)^(-1))`.

The checker verifies that changing realization commutes with this product and that the product descends to truncated jet levels.

It also compares two three-factor product routes with different intermediate realizations. All 256 tested mixed-realization cubes commute as exact rational matrices. This connects the higher comparisons to source productization, rather than leaving them as formal diagrams with no source meaning.

## 4. Evidence follows the same comparisons

An observer constraint is pulled back along the source anchor to a constraint on compatible histories. Expressing that constraint in another realization gives the same source fiber.

The checker compares 128 pairs of entire rational affine fibers, while preserving the previous terminal evidence. These are coordinate presentations of the same evidence, not newly acquired facts. Actual evidence refinement is the separate intersection operation developed in `four-coherence-roles-on-the-forgotten-residual-cube.md`.

## 5. The important failure case

Consider the invertible full-data change

`new_m_empty = old_m_empty + old_m_123`,

with every other coordinate unchanged.

It is a valid invertible change on retained full data. But it does NOT descend to the declared terminal-only view. The hidden source `H tensor H tensor H`, with `H=Q-P`, has old terminal value zero and new terminal coordinate one.

Thus there can be no terminal-only comparison producing that new coordinate. One must use the retained residual, enrich the view, or change the declared filtration. Simply asserting another coherencer cannot fix the missing information.

A second negative control corrupts one comparison matrix. Its carrier dimensions remain correct, but a composition triangle fails.

## 6. Interpretation for the lane

The prototype shows how to organize a tower of towers without inventing unrelated observers at every level. Source anchors induce the comparisons, and coherent truncation connects the depth levels.

It also exposes the key assumption: these four realizations describe the SAME jet information at a fixed depth. Their comparisons are invertible. Our historical sixteen-private and matched observer enrichments change source kernels and are nonsplit; they must not be inserted into this groupoid as if they were coordinate changes.

Extending the construction to those actual views requires retaining their noninvertible comparisons and compatible-source ambiguity. Neither the existence of this strict nerve nor its higher cells supplies a section of those restrictions.

Depth truncation remains lossy throughout. Exact symbolic use must retain omitted interactions as typed residuals. Unknown-source use must preserve the corresponding ambiguity. The coherence hierarchy itself is not storage for discarded source values.

## Reproduction

`python research/nima/checkers/check_residual_tower_of_towers.py`

All checks pass, including both negative controls. The report includes 5,456 higher route checks, 160 depth/comparison squares, 256 mixed-realization product cubes, and the face/degeneracy identities.

Artifact:

`research/nima/results/residual-tower-of-towers.json`

It exports the source anchors, realization matrices, and all comparison matrices at each jet depth. Scope is the exact finite forgotten packets and illustrative rational coordinate realizations—not noisy acquisition, arbitrary marked-source actions, completed-source reconstruction, nontrivial weak higher coherence, or the outstanding selected-observer comparison certificate.
