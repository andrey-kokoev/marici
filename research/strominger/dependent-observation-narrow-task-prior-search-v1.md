# Prior search: global based-path transport and nontrivial loop observation

Status: source inspection only in this search; no new proof or compiler run. Earlier fresh verification of SeedGeometricResponseState remains a separate recorded action.

## Result

The narrower task is largely reuse and assembly, not a new mathematical existence problem. My previous claim that global transport binding and nontrivial loop observation were substantive missing constructions overstated the gap.

### Exact library theorem for the proposed global family

`C:/Users/andrey/tools/cubical-agda/cubical-0.9/Cubical/Foundations/Transport.agda`, lines 194–202, defines `substInPathsL`:

    subst (lambda x -> a = x) p q = q followed by p.

This is exactly the required transport/concatenation equation for O(x)=(node A=x), not just a related result. The same module supplies `substComposite`, `substRefl` (via imported foundations), `substEquiv`, `substInverse`-style recovery through `subst⁻Subst` and `substSubst⁻`. Specializing these laws does not require a new generic transport theorem.

### Existing global family / native response squares

`research/nima/agda/SeedGeometricResponseInterpretation.agda` already defines a family on the actual realized HIT using ua of edge equivalences. Its `primitive-square`, `inverse-square`, `route-square`, and `native-square` bind geometric transport to primitive, arbitrary-word and actual native execution.

Its edge equivalences are inputs. Instantiating them with `SeedGeometricResponseState.edge-equiv` removes a free action-table choice at that instance. This ua-built family is not definitionally the literal based-path family; if equality/equivalence of the two presentations is required, it needs its own explicit comparison. Do not manufacture that extra comparison requirement if the chosen observation contract only needs one presentation.

### Nontrivial dependent loop observation already assembled

`research/strominger/agda/TransportObservationPartialCorrespondence.agda` and `transport-observation-partial-correspondence-v1.md` supply:

- `short-reading`: actual compiled AB;BA reads true;
- `long-reading`: actual compiled AB;BC;CA reads false;
- `edge-reading`, `step-reading`, `run-square`: transport/update binding;
- `native-parity`: agreement of native readout with an independent parity interpreter for all A-to-A directed words;
- `parity-accepted`: a certified observation factor retaining the actual executions;
- `no-forgotten-factor`: refusal for the constant summary.

The underlying `ReturnProbe` is a genuine family over the realization, flipping across BA. Since transport at the empty loop preserves false, the AB;BA computation already exhibits nontrivial observable monodromy. It also detects that AB;BA is not the constant based path. Combining that fact with `substInPathsL` gives nonidentity transport of refl in the based-path family. This last packaged specialization was not located as a named theorem in the searched sources; its ingredients are present.

### An even stronger finite observer already exists

`research/nima/seed-joint-parity-response.md` and `agda/SeedJointParityResponse.agda` combine AB and BA Boolean families, prove primitive/word/native squares, and recover both seam choices on the four-corner domain. A single-bit observer is therefore not the current upper bound of prior work. The finite observer does not reconstruct arbitrary histories and its task is explicitly chosen.

### Related, not exact-source replacements

`research/voevodsky/agda/ClosureDependentRefinementRegression.agda` has a circle cover with flip monodromy; `ClosureGluingTreeRegression.agda` uses it to prove a surviving loop nontrivial. These confirm reusable techniques, but the same-source ReturnProbe results above are the closer evidence. No proof from a different circle source is needed here.

## Corrected remaining scope

For the declared extension-based interpretation, use a small common-witness assembly specializing existing transport laws and source/native theorems; do not rebuild the constructions or present them as a new existence breakthrough.

The genuinely unresolved distinctions are stronger requirements, not this elementary binding:

1. Execution in the unchanged original twelve-rule calculus, rather than the already explicit unary transport extension.
2. Independent selection/classification of the observation task, rather than declaring the based-path or parity task.
3. Broader observation-language, anchor/source-mode and product comparisons, as already listed in the prior partial-correspondence packet.

No choice among those stronger objectives is made by this search. The proposed conjecture should be reassessed for redundancy before expanding its proof program.
