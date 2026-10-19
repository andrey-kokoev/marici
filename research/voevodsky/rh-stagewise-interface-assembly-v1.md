# Bounded RH stagewise interface: four-witness overlap review

Dictionary: `research/conjecture_net/contracts/rh-stage-dictionary.v1.json`.
Checker: `research/voevodsky/checkers/check_rh_stagewise_interface_assembly.py`.
Receipt: `research/voevodsky/results/rh-stagewise-interface-assembly-v1.json`.

Fresh exact overlap construction: `uv run research/voevodsky/checkers/check_rh_stagewise_interface_assembly.py --replay`.
Normal runs validate the retained review, rerun the four child validators, and check source freshness without repeating scientific source suites.

## Result and scope

The four constructed child witnesses agree on the frozen 19-stage-family, 19-map dictionary. All 14 required comparison cells are covered: six operation cells, three identity/continuation cells and five analytic cells. The two independent-source boundary cells remain explicit exclusions from this bounded assembly.

This supplies `rh-stagewise-interface`: a reviewed bounded mathematical interface, not the separate `rh-math-assembly` witness, the general mathematical interface, a universal dependent-transport construction or a same-source physical/form assembly. The mathematical branch's general interface remains open. No branch or root outcome is imported automatically.

## Actual interface, not a generic simulator

Each stage is represented by the tuple

    (source type and domain, admitted operations, comparison maps,
     task observation/equivalence, retained reconstruction data,
     topology/completion, provenance and supplied conventions).

Each comparison is a typed commuting witness at a declared domain, a scoped rejection excluding that identification, or a boundary pointing to a different open source task. Composition uses actual recorded maps and overlaps, not equality of present scalar readouts.

- Finite coefficient stages use the parity-resolved reducing frame and independently specified source action. The composite reduction is the original P.
- Actual history stages use their inherited sections and retain endpoint-invisible histories. The source operation is native extension M; its continuous generator has the separately specified angular normalization.
- Generic analytic ports use B_a and the two distinct coordinate assignments: J_carrier permutes AD,CA,DB,BC into cyclic order; J_endpoint=TQ^-1 is the full endpoint adapter. Sharing the symbol J in source notes does not make these the same map.
- Additive lattice/torus stages form an independent declared source route. Their real distributions enter the same analytic rigging, but no common source with the carrier is inferred.
- Analytic stages use E_r=U S(R), E_s=V E_r and their strong anti-duals. Endpoints belong to the source-induced rigging; raw combs are not ordinary log-tempered or Hilbert states.
- Riemann specialization is a rank-one task readout. Complete coefficient/history packages remain retained; future-safe equivalence depends on the selected source operations.

## Overlap review

| Overlap | Reviewed convention/witness | Excluded inference |
|---|---|---|
| Finite descent -> generic comb | Same P, source C12/D12 and J_carrier; all Fourier characters retained | Generator-only old frame treated as full-tick transport |
| History -> generic comb | J_endpoint and A_endpoint=sqrt(3) Q diag(A0,0)Q^-1 | Rational A0 silently used as the full angular generator |
| Native history continuation -> analytic image | J_endpoint M J_endpoint^-1 on finite cyclic coefficients, transported by B_a | Native M relabelled as Fourier or a global ambient operator |
| Generic -> radial -> spectral | Actual U, normalized V and G(t) followed by reflection; continuous strong anti-dual transport | Ordinary log-tempered completion or raw-comb Mellin integration |
| Core -> completed analytic image | Bounded dense-core extension plus transported Frechet/anti-dual topology | Finite tests substituted for analytic extension arguments |
| Identity -> specialization | Carrier scalar quotient is stable under C12/D12; native history needs Z=[ell;ell M] | Same scalar readout used as complete identity under all futures |
| Boundary -> theta/xi | delta_0 exchanged with 1; endpoint constant 1/2 and entire-tail argument retained | Zero-removed comb treated as self-Fourier or zeros constrained by reflection alone |
| Lattice -> analytic rigging | Fixed mesh continuity and strong Gaussian/refinement limit | A selected one-dimensional channel or l2-to-L2(R) atom embedding inferred |

### Two normalizations that cannot be suppressed

In the history implementation A0=[[0,2/3],[-2,0]] and A=sqrt(3)A0. The overlap checker verifies D J_endpoint=J_endpoint A_endpoint and verifies failure when sqrt(3) is dropped. Native sections and drift/extension witnesses use that same convention.

The operation child used unnormalized log Fourier M_log. The analytic child uses V=(2pi)^(-1/2)M_log to obtain a unitary Hilbert chart. On ordinary functions the two spectral presentations are related by this explicit scalar bridge; it cancels on both sides of the operator square, so G(t) is unchanged. Their Hilbert metrics are not silently declared equal: unnormalized Plancherel carries the factor 2pi. Completed distributional transport uses the analytic child's anti-dual convention with the corresponding inverse/adjoint on tests, not an unexamined transpose or the same rescaling on both slots of a pairing.

The fixed finite coefficient Gram is still distinct from analytic rigged pairing or an independently specified Green/Weil form. No energy form is repaired by this normalization review.

## A useful extra continuation square

Generic B_a is injective at the declared shifts. On its finite image define the inherited native-history operation

    M_V=(B_a J_endpoint) M (B_a J_endpoint)^-1.

This is uniquely determined on that image by the existing source operation and adapter; there is no assertion of an independently sourced operator on the whole distribution or spectral space. Its cyclic coefficient matrix is X=J_endpoint M J_endpoint^-1. The fresh checker verifies

    X J_endpoint=J_endpoint M,
    X != F_cyc,
    X F_cyc != F_cyc X.

Thus native continuation can be transported to the generic analytic image without pretending it is Fourier. Composing the continuous embeddings U^times and V^times transports this SAME finite-image square to the completed riggings. M_V is continuous on its finite-dimensional image; no arbitrary extension off that image is admitted.

For Z=[ell;ell M] and T=[[0,1],[1,1]], the cyclic-coordinate predictive reader is Z J_endpoint^-1. It satisfies

    (Z J_endpoint^-1) X=T (Z J_endpoint^-1).

The same two-coordinate predictive task therefore survives this analytic chart. In contrast, the single coefficient-sum row is not X-invariant. This supplies the exact overlap between native operation transport, the identity child's equal-present/different-future witness and rank-one analytic specialization. Carrier scalar invariance remains a different, separately verified C12/D12 task.

Nothing here admits added Fourier as a primitive history actuator. The endpoint/analytic Fourier operation and native operation remain separately typed, noncommuting operations; half-phase and ideal-product applicability remain unbound where no source identification exists.

## Fit to the mathematical branch, without premature discharge

The open `stagewise-mathematical-interface` acceptance is reviewed by its actual clauses:

| Clause | Bounded RH realization supplied here | General obligation not discharged |
|---|---|---|
| Validity | Classical mathematical arguments and exact finite witnesses at explicit domains; no answer insertion/RH assumption | Universal validity/axiom policy and formalization of every proof |
| Source rules | Existing carrier action, actual history extension and declared independent lattice rules | One universal native source generating all laws |
| Composition | Cell-indexed actual-map squares and overlap witnesses | Generic composition across arbitrary dependent objects |
| Dependent transport | Inherited/transported history sections and retained coefficient reconstruction for these sources | Universal identity, substitution and higher dependent transport |
| Supplied versus generated laws | Shift, Gram, chart, mesh, Fourier/Gaussian normalization and analytic theorem inputs explicitly marked | Derivation of those choices solely from the finite carrier |

This is a concrete bounded instance organized by the declared branch acceptance, not a proof that the currently open general interface has been frozen or resolved. The branch work-net explicitly permits bounded research before parent formulation closes. The reciprocal contribution remains non-proof-bearing and cannot discharge the branch example or universal parent by itself.

## Preserved boundaries and verification

The separate channel-carrier source map, one-dimensional selection, successor form and Weil comparison remain open. Legacy RH v20 routes and rejected unchanged-Evans candidate are untouched. No physical apparatus, universal foundations result or RH proof is claimed.

All four child validators run freshly. The new exact checks compare actual matrices, not dimensions or spectra alone; the note supplies the analytic overlap/density reasoning already proved in the child witness. Five hostile controls reject angular-factor loss, ambient native/Fourier promotion, log-tempered substitution, general-branch automatic discharge and Weil-form promotion. This is a scoped reviewed assembly with pinned evidence, not a formal compiler closure.
