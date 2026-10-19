# Eight-sector transport of the anchored PN discrepancy

## Frozen task and boundary

Test Strominger's four eight-sector charts against Nima's saved anchored PN packet. Preserve its rank-two native C3 route difference and exact source data. Owner files remain read-only. This experiment does not assign fields to four actual neutron reader contexts, construct a geometric seam, or admit a new native operation.

The original N field has 36 internal components in three native sectors. The eight-sector workspace is a **different, outer tensor index**, not a relabelling of those three sectors. The workspace metric is I8 tensor M_N. P's field and anchor are unchanged.

## Explicit choices

Embed one complete N field as `f_s = profile_s n`, using two declared unit-norm profiles:

1. One native-diagonal coarse average slot, split into its two fine sectors.
2. The cube parity profile `sx sy sz / sqrt(8)`.

Neither choice is claimed canonical or an independently authorized physical preparation. These restricted separable embeddings test the interface algebra and the actual PN obstruction, not arbitrary independent four-reader data.

For each imported chart H use `weights=H profile/sqrt(2)`. Transitions use the actual retained `H_target H_source^T/2`. Source charts, metrics, marked reader origins and provenance remain part of the type.

## Operator representation

The transported packet is explicitly **factored**, retaining the original 900 anchored operator-comparison blocks plus the profile and chart weights. No additional original field is stored. Expanded N/N blocks are `w_t conjugate(w_s) C_NN`; N/P and P/N blocks have the appropriate single factor. P/P is unchanged. Every workspace N summand uses the original source metric.

This is a sufficient representation on the declared separable image, not a compressed encoding of arbitrary eight-sector fields. Source recovery validates every core block. Expanded anchor columns independently recover the actual workspace field. Full expanded block matrices are compared against independently computed workspace outer products, for every source block type at a nonzero sector pair. Orthogonality of the profile supplies the left inverse and preserves all original comparisons.

## Decisive checks

For both profiles and all four charts, recover both competing routes for both contrast inputs. Compute their full workspace difference and its weighted Gram. Require exactly `3 I2`, hence rank two. Test full-packet chart identities, round trips and composition triangles.

The averaging hostile uses the actual PN discrepancy in the parity profile. All four charts' average-only projections kill that profile and hence erase the rank-two residual; full chart data retain it. This is a declared comparison embedding demonstrating loss, not a claim that the native NN chain populates that mode.

Reject missing differences, chart-label-only changes, source-origin drift, missing neutron sectors, forged cross comparisons and profile corruption. Verify imported receipt freshness and all input hashes unchanged at completion.

## Measured result

The exact checker passes: 32 source-packet recoveries, 28,800 expanded-block checks, eight identity/round-trip cases, 128 complete-packet composition triangles and eight residual Grams equal to `3 I2`. All six corruption controls reject. The fresh anchored-PN closure check also passes. Both source profiles retain the discrepancy; all four average-only parity-profile readouts erase it.

The implementation and SCC manifest are Nima-owned. Imported source receipts passed their direct-hash freshness gate, and all read inputs remained unchanged.

## Reproduction

```sh
python research/nima/checkers/check_anchored_pn_contact.py
python research/nima/checkers/check_eight_sector_pn_transport.py
python research/aspect/scc/scc.py check eight-sector-PN-transport
```

The first command provides a fresh Nima-owned closure audit of the source packet; the second consumes pinned Strominger chart evidence without rerunning his output-writing checkers. Receipt: `results/eight-sector-PN-transport/verification.json`.

A passing result supports faithful read-only tensor-chart transport of the failed PN square. It does not repair that square or establish a reader-incidence/locality lift. The next gate would be a sourced assignment to actual reader summands and transport of their native operations, preserving the same obstruction test.
