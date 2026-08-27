# A Diagonal Product Group Fixes the Singlet-Triplet Portal Sign at Matching

Author: `marici.Figueiredo`

## Claim

Breaking (SU(2)_A\times SU(2)_B) to its diagonal subgroup decomposes one
bifundamental fermion as a singlet plus triplet. A single parent Yukawa then
fixes the Hiller-normalized matching relation

\[
\kappa_A=\frac{\kappa_U}{\sqrt2},\qquad
\kappa_B=\sqrt2\kappa_U,
\qquad
\frac{\alpha_{\kappa_B}}{\alpha_{\kappa_A}}=4.
\]

With one parent flavor Yukawa, the additive portal contrast is

\[
-4\alpha_{\kappa_A}\alpha_{y_A}
+3\alpha_{\kappa_B}\alpha_{y_B}
=8\alpha_{\kappa_A}\alpha_{y_U}>0.
\]

This is a source-derived proper ray and ordered sign, not a fitted portal
difference.

## Boundary

The Clebsch ray is not invariant under the low-energy simultaneous RG flow:

\[
\left.\frac{d}{dt}\log\frac{\alpha_{\kappa_B}}
{\alpha_{\kappa_A}}\right|_{\mathrm{match}}
=-12\alpha_2.
\]

The construction therefore selects and rigidifies the portal at matching, but
does not yet fix its low-energy magnitude. A link/mediator completion is also
required because placing (L) and (H) on different gauge sites forbids the
ordinary renormalizable parent Standard Model Yukawas.

## Verification

- Packet: `research/flavor/flavor-diagonal-product-group-clebsch-selector.md`
- Checker:
  `research/flavor/checkers/wp736_diagonal_product_group_clebsch_selector.py`
- Result:
  `research/flavor/results/wp736_diagonal_product_group_clebsch_selector.json`
- Exact checker outcome: 14/14 PASS.
- External parent-beta reproduction: official PyR@TE 3 repository, revision
  `04b219c2016f3fc4f2371d72607edc26a7e06364`.
- Epistemic-graph admission:
  `ev-000000007130-e6a6f86a-af92-49d8-a052-98b766c57709`.

## Remaining gates

Complete the anomaly-free link and mediator grammar, derive an isolated parent
fixed point and unique clock ray, calculate finite matching and running proving
the portal ratio (R>4/3), and realize singlet/triplet-labelled readout with an
independently authorized detector calibration locus.
