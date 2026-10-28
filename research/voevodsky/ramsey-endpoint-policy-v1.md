# Endpoint selection: transport succeeds, edge-only invariance fails

## Kernel results

For selectors `Edge → Bool`, the endpoint-order-corrected complementary action is involutive. Every selector transports covariantly with the geometric endpoint action.

There is no invariant edge-only deterministic selector. The proof uses edge01, which is fixed as an unoriented edge while its endpoints exchange. A separate geometric formulation rules out choosing the same endpoint vertex equivariantly, rather than relying only on Boolean representation. This is a quantified kernel obstruction, not a finite search failure.

The no-go does not extend to all contextual selectors. A positive control retains the chart: chart0 chooses the first endpoint; chart7 uses the transported choice, flipping on edges01 and23. Twelve chart-aware covariance cells and twelve bindings to actual edge-permit restriction laws are checked. A hostile assertion that the constant-left selector is invariant is rejected.

## Important scope of the positive control

The chart-aware selector acts on each individual chart's edge permit. It does not assert that independently selecting endpoints in two different charts yields a common vertex. On the reversed edges, the chart0 and chart7 selectors choose different endpoints. Therefore this positive control must not be promoted to a coherent single-vertex selection for mixed-chart overlap spans.

Likewise, retaining both endpoints is not the same operation as selecting one invariant endpoint. The existing independent-input diagram can retain the required incidence data without satisfying an edge-only selector premise.

## Next executable check

Audit mixed-chart common-port selection with the chart index retained: compare independent per-chart choices with a shared ordered-pair selector, and test compatibility with reversing the pair. Fixed edges01/23 offer explicit nonempty common-port controls. Any obstruction should be scoped to the requested selection and reversal laws, not to retained two-endpoint correspondences or parent descent.

## Verification

- `fixtures/ramsey-endpoint-policy/RamseyEndpointPolicy.agda`
- `checkers/check_ramsey_endpoint_policy.py`
- `results/ramsey-endpoint-policy-v1.json`
- passing freeze `scc-freezes/ramsey-endpoint-policy-v1.ce27d6f9cc996e27.json`

Fresh safe Cubical positive and hostile checks passed with `--ignore-interfaces`. No owning native operation, scientific verdict, graph event or Git checkpoint changed. Local net revision25 and external admission revision19 remain unchanged; this receipt awaits consolidation.
