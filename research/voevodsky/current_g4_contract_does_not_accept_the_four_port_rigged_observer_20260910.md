# The current G4 contract does not accept the four-port rigged observer

## Question

Does the canonical materialized G4 interface identify the retained four-port observer with `conservative_green_complex`?

## Claim boundary

No. The only materialized contracts are versions 1 and 2 of Aspect's interaction-net state. Version 2 declares a corrected three-port Hilbert/graph model and leaves `conservative_green_complex` open. The retained four-port rigged observer disagrees with that interface in port count and topology, and canonical arithmetic loading remains unspecified. This is a contract mismatch, not evidence against the internal observer.

## Problem

The external identification role requires equality of typed interfaces, not agreement of scalar formulas or dimensions. The current contract declares `g4_common` with:

- complex Hilbert and graph-norm source objects;
- declared source graph completions;
- source graph norm and Hilbert target norm;
- no undeclared quotient;
- source-derived comparison maps only.

It labels the model generation `corrected_G4_three_port_evans_green` and makes `conservative_green_complex` depend on `three_port_source_separation`.

## Bold conjecture

The retained four-port system can be admitted under the existing `g4_common` descriptor without changing the G4 contract.

## Named rivals

1. A new interface version must replace three-port separation by the four-port joint trace and replace one Hilbert target by a multi-rung rigging.
2. Seam flux is redundant and can be quotiented away under the existing no-undeclared-quotient rule.
3. Distributional primitive and square rows can be represented by Hilbert vectors, preserving the current target descriptor.

## Exact comparison

| G4 v2 field | Retained observer | Status |
|---|---|---|
| `radial_history_carrier` | weighted second-order bilateral relative graph | compatible refinement |
| `first_order_differential_and_domain` | first derivative plus second-order graph control required for flux trace | topology mismatch |
| `zero_separation_trace` | complete four-port trace \((P,Q,M,J)\) | port-count mismatch |
| `moving_shell_endpoint_traces` | exact metric-natural endpoint transport | constructed |
| `function_valued_wronskian_incidence` | retained odd graph and source-reached seam flux | constructed internally |
| `forward_shell_synthesis` | rigged covariant synthesis \(U_4\) | constructed, not bounded below |
| `hermitian_adjoint_and_analytic_transpose_returns` | Hilbert adjoint only on middle rung; primitive and square use distributional transpose rungs | topology mismatch |
| `polarized_green_metric` | positive joint graph plus four-port symplectic boundary form | constructed on retained chain |
| `arithmetic_loading_and_codiagonal` | several admissible convergent loadings, no canonical G4 selection | open |
| `all_jet_compatible_laplace_readout` | not established by the observer packets audited here | not verified |

## Strongest falsification attempt

The existing contract prohibits undeclared quotients. Therefore the fourth port cannot be removed merely to satisfy `three_port_source_separation`.

The primitive row also cannot be represented in the fixed Hilbert Green transpose range: finite interpolant norms grow at least as \((\log p_X)/C_{\rm cut}\). Therefore the multi-rung topology cannot be collapsed to the declared Hilbert target without losing a source current.

These two independent obstructions reject the bold conjecture.

## Required successor interface

A compatible successor contract must declare at least:

1. the four-dimensional joint trace \((P,Q,M,J)\);
2. the weighted second-order relative graph domain;
3. the projective source, labelled Hilbert observation rung, and strong/distributional dual rungs;
4. graph-valued synthesis with zero Hilbert lower margin;
5. contragredient transpose rather than universal Riesz adjoint;
6. primitive and square dual-rung maps;
7. connected trace-class/nuclear coordinate;
8. Gaussian Mellin line attachment;
9. a selected arithmetic loading and codiagonal;
10. an all-jet Laplace readout if still required.

This successor must preserve version 2 as immutable history rather than rewriting it.

## Disposition

External G4 identification fails against the current canonical contract. The earliest mismatch is structural: three ports versus the source-required four-port joint trace. The second is topological: one Hilbert target versus a necessary rigged transpose architecture. Even after those are repaired, canonical arithmetic loading and the all-jet readout require explicit witnesses. The retained observer remains internally complete; it is not yet an implementation of the materialized G4 formal slot.
