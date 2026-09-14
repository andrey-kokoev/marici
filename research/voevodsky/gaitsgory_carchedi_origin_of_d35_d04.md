# Correspondence and dg-intersection origin of D35/D04

## Mined sources

- Gaitsgory--Rozenblyum, Volume I, Chapter II.2, §§0.1, 2.1, 3.1.
- Gaitsgory--Rozenblyum, Volume I, Chapter V.1, §§0.1, 3.1--3.2.
- Carchedi, *Derived Manifolds as Differential Graded Manifolds*, §§1 and 4.

## Structural conclusion

The geometric ancestor of the labelled targets is not primarily one unmarked complex with two coordinate projections. It is a pair of correspondences through the common conductor, composed by derived fibre products. Applying `IndCoh` sends a correspondence to push--!pull, while Beck--Chevalley supplies coherent base-change equivalences.

For a conductor inclusion `i: Z -> F`, the marked data are conormal line objects
`N_k^vee=(J_k/J_k^2)^vee` on `Z` (or their total spaces `Tot(N_k^vee) -> Z`). The intended schematic correspondences are therefore based over `Z`; one must not postulate a retraction from a first infinitesimal neighbourhood to `Z`. `D35` and `D04` are the two marked coefficient realizations, and reflection exchanges their conormal legs.

This explains why the map `q: omega[2] -> C Pi^vee[3]` is not determined by the objects `omega` and `C` alone. Gaitsgory--Rozenblyum explicitly emphasize that a general base-change isomorphism is additional coherent correspondence data, not a map obtained from an adjunction in either direction. In the Marici model, `q` must be induced by the actual conductor correspondence and its trace/counit.

Carchedi gives the strict computational model once the geometric legs are specified: replace one map by a fibration and take the ordinary pullback. Locally, a derived zero locus is the dg-manifold with Koszul differential

```text
Q = sum_a s_a partial/partial xi_a.
```

Thus a strict `Dk` should arise as the Koszul/dg model of the derived intersection of the bulk trace section with the marked conormal-extension section. Its comparison-homotopy coordinate is the extra Koszul generator. This matches

```text
Dk^n = W^n + E_k^n + T^(n-1),
d(z,e,h) = (dW z, dE e, qz - pi_k e - dT h).
```

## Exact remaining geometric input

To derive the numerical strict `q`, one must specify the actual map of derived spaces (or correspondence leg)

```text
Z -> Spec(omega-model)
```

whose IndCoh trace/counit is `q`, including the polarity trivialization. The normalization--conductor square supplies `Z` and its polarity character, but the current exports give only the induced cohomological attachment signs, not this strict correspondence map in the ordered 50-state model.

Carchedi cannot manufacture that leg: his construction computes a homotopy pullback after its maps/sections are given. Gaitsgory--Rozenblyum likewise organize the required coherent datum but do not select the Marici-specific conductor trace.
