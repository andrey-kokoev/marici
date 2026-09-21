# Relative Green currents descend through balanced factorizations

## Finite-cutoff result

Combining the source collision-current constructor with the balanced seam normal form gives a relative paired descent for nonminimal associated-layer factorizations. At a fixed free finite source, common capacity, and the prescribed multiplicative memory weights, let N be normalization from external seam records to the balanced seam target. Then

    q_external + T_N = N^* q_balanced.

Here T_N is constructed by enumerating new matches of typed record shapes and assigning the existing tail-flux pairings. It is NOT defined by subtracting the two sides of this equation. The corrected form descends through balancing because its independently constructed expansion equals the normal-form pullback.

For the seven-event triple layer this applies to the presentation with 55440 coefficient directions and its 20160-dimensional balancing kernel. The resulting 35280-dimensional associated-layer corner remains faithfully embedded in the balanced function-valued target. This does not assert that its restricted self-pairing is nondegenerate.

Inputs:

- `../grothendieck/relative-green-sewing-is-generated-by-slot-collisions-and-tail-flux.md`
- `../nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`

## 1. Normalization is an admitted memory-slot coarsening

In the bottom three-seam term an external coordinate consists of three actual seam edges and their marked letters, together with six memory buffers:

    (u0 | edge1 | v0), (u1 | edge2 | v1), (u2 | edge3 | v2).

N retains all three edges and replaces the buffers by

    u0, v0 u1, v1 u2, v2.

It removes only the two artificial factorization cuts inside the joined buffers. The seam edges determine the endpoints of the four remaining buffers. No feature crosses a seam letter. Ordered features are unchanged. With one common capacity at least the packet length, none of these source records overflows.

Thus N is exactly a composition of the memory-slot operations admitted by the relative-current theorem. Memory weights multiply; seam weights remain separately fixed. The root factor is retained once where appropriate. These statements are coefficientwise and do not replace the full seven-event receiver by copies of a root corner.

## 2. Construct the correction before comparing forms

A fine shape records all factorization cuts, seam edges, vacuum/feature seam sectors, and separate memory lengths. For every ordered pair of different fine shapes whose normalized shapes coincide, include its pairing in T_N.

Vacuum pairs contribute the prescribed incidence coefficient. Feature pairs contribute the independently derived divided tail current, retaining their own spectral variables and denominator. Multiple feature slots use the labelled product current with independent spatial variables. Signature-transformed observer channels use their existing prescribed coefficient matrices. Keep bulk and forcing channels distinct.

This recipe depends only on N, the existing forms on the normal-form factors, and the source current. It does not use a relation Gram inverse, a numerical spectral rank, or a fitted positive metric.

For equal fine shapes, N is an ordered tensor reassociation at fixed memory lengths; its pairing is unchanged. Different fine shapes with different images contribute zero. The remaining pairs are exactly the constructed new matches. Expanding arbitrary vectors proves

    q_external(u,v)+T_N(u,v)=q_balanced(Nu,Nv).

## 3. Descent and its precise sign

For any balancing vector k, Nk=0. Therefore for every external vector v,

    q_external(k,v)+T_N(k,v)=0,
    q_external(v,k)+T_N(v,k)=0.

The SUM q_external+T_N descends to balanced normal forms. Neither summand need descend separately. Equivalently the balanced pullback minus its retained correction recovers the external form. Confusing these two uses would put the correction on the wrong side.

In particular, moving an extra arrow across either relation-factor interface leaves the corrected observation unchanged. Nima's kernel theorem identifies the entire multiplication kernel with these balancing relations, not just the 32 tested examples. Its coefficientwise analytical embedding then transfers this conclusion to the fixed function-valued balanced target.

On a restricted source image there may still be additional radical directions of the self-form. They are not quotiented here. Faithful layer injection and detection by ambient paired observers remain separate from self-pairing nondegeneracy.

## 4. Coherence

For consecutive permitted normalizations N1,N2 the new matches split disjointly into those first created at step one and those first created at step two. Hence

    T_(N2 N1)=T_N1+N1^* T_N2.

The two buffer mergers in the three-seam normal form consequently produce the same total correction in either order. No new triangle or suspension phase is chosen. Existing cochain and reversal conventions remain unchanged.

The associated-layer cycle and its shifted connecting observation are still the previously constructed balanced maps. The relative pairing construction does not alter their differential or manufacture a nonzero higher Tor group over the hereditary source.

## 5. What this positively closes

At finite cutoff the factorization-balancing operation now has both a faithful analytical associated-layer map and a source-generated relative paired comparison. The earlier fixed-form isometry obstruction is respected, not evaded: the original external form is not said to descend unchanged. Its collision current is retained explicitly.

This is a relative comparison in the prescribed rich records, not an isometry of the original unbalanced and balanced carriers. No new arithmetic boundary generator is claimed beyond the supplied tail currents. It also does not establish uniform packet estimates, arbitrary weight-changing or truncating operations, or a completed receiver.

## Verification

Fresh checks:

- `uv run --with sympy python research/grothendieck/checkers/check_source_relative_green_sewing.py`
- `uv run python research/nima/checkers/check_seven_event_factorization_descent.py`
- `uv run python research/voevodsky/checkers/check_balanced_relative_green_descent.py`

The new checker tests all 32 seven-event balancing moves, 128 relative pairing comparisons, and 64 nonzero collision fixtures. It constructs collisions from differing fine shapes with matching normalized shapes, rather than defining them by a Gram difference. The non-diagonal feature matrix is an exact regression fixture, not an actual Clark evaluation. The general function-valued statement follows from the two input theorems and the explicit identification of N above.

The complementary ordinary checker `check_ordinary_collision_port_sewing.py` also passes on all 2160 ordinary columns with 864000 coordinate regrouping checks. It verifies slot order, separate weights, the full forgotten-sector discrepancy, and the existing within-partition formal anomaly. Neither numerical fixture supplies a new positivity claim.
