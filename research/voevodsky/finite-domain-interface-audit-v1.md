# Finite domain WG: interface audit and actual continuation theorem

Target: `math:finite-domain-wg-example`.
Interface: `research/conjecture_net/contracts/stagewise-mathematical-interface.v1.json`.
Formal addition: `research/voevodsky/agda/FiniteDomainInterfaceAudit.agda`.
Receipt: `research/voevodsky/results/finite-domain-interface-audit-v1.json`.

## Reviewed disposition

Constructed **bounded supplied-operation adapter audit**, not native category-law generation. The local branch node is resolved at this scope with formal outcome left null. This evidence does not resolve the RH example or their common assembly.

The acceptance is met by actual supplied computations, joined/generated histories and the explicit provenance table below. The falsifier excludes the stronger claim that the wrapper generates category laws; no such claim is admitted. The typed negative controls reject invented feedback and request relabelling, rather than treating their failed compilation as a failure of the retained adapter.

## Binding to the frozen interface

| Obligation | Actual pilot binding and limit |
|---|---|
| Objects, types, universes | `Presentation ℓ` supplies `Input : Type ℓ`, `Output : Input → Type ℓ`; the presentation record lies in the successor universe. |
| Source and guards | `compute` is supplied; `Admitted` replaces Input with a dependent pair of input and `Allowed` evidence. The source computation is not inferred from its signature. |
| Stage and phase | `Compile.State` is tagged request or response. A response retains the exact input together with its dependent output. |
| Actual operation | `Compile.run` computes on requests and is idle on responses; its `evaluated`/`idle` relation witnesses certify precisely those operations. |
| Composition | Actual `Histories.join` composes matching witnessed edges. The new audit constructs evaluated-then-idle by this join and proves that its length is two. |
| Continuations/resources | Arbitrarily many finite repetitions of this same WG are allowed. After the first request transition the endpoint is stationary, but generated history length is the supplied natural-number step count. No runtime complexity or infinite execution theorem is asserted. |
| Identity/recovery | Retain the tagged state, exact admitted request and entire history, rather than quotienting histories by endpoint agreement. No task quotient or inverse of compute is claimed. |
| Proof payload | `execute-law` pairs the actual response with its edge and the supplied law at the retained request index. The audit proves recovery of exactly that supplied proof, without proof irrelevance. |
| Dependent transport | Input/output typing and request retention are checked. This pilot does not supply an arbitrary Layer-3 payload action or identify the evaluated relation with paths. Generic Layer-3 transport is not silently instantiated here. |
| Completion | Finite histories only; no analytic completion. The Boolean instance is finite, but a supplied category need not have finitely many objects or arrows. |

## Law provenance, without answer insertion

- `result-beta`, request retention, stationary-response iteration and history-length results are proved from the declared computation/constructor rules.
- Boolean involution is proved by cases in the existing source, then passed into the law compiler. The compiler does not discover it.
- The category operation is the supplied category's actual composition. Unit and associativity proofs come from that same supplied category (`unitL`, `assoc`).
- `LawOrigin.supplied-law-recovered` proves that the certificate's proof is definitionally the supplied `law k`. Consequently, calling this native generation of category laws would fail the branch's falsifier. Calling it a retained, typed supplied-law certificate is supported.
- `same-operation-response` checks that the law package uses the same operation response and request, not an unrelated expected value inserted as a second result seed.

## New substantive continuation result

For every supplied Presentation and every input i, after suc n WG steps the endpoint is `response(i,compute(i))`, while the generated history has length suc n. Thus the old one-edge law-history can be continued honestly by idle transitions; it is not evidence for a chain of new domain computations.

In particular, starting with Boolean false, two WG steps still end at response(false,true). Two untagged Boolean complements would return false. The checker compiles a deliberately wrong endpoint equation and requires its rejection. A second deliberately ill-typed control attempts true = false, the forbidden admission witness when relabelling the computed true value as the request in the false-only pilot.

These controls distinguish actual licensed continuation from an invented feedback operation. They do not furnish multi-step composition across differently indexed category requests. That would require a new explicit scheduling/source interface and corresponding operation-preservation proofs.

## Verification

Run `python research/voevodsky/checkers/check_finite_domain_interface_audit.py`.

Fresh headless `--ignore-interfaces --safe --cubical --guardedness` compilation passed for the new module and its imports. Both negative modules failed with the expected Boolean type mismatch. The existing unused `isPropIsContr` import warning in `TypedGeneratorLayers.agda` remains; no owner source was changed to suppress it.

The receipt records the command, diagnostic tails, negative control bodies and hashes of the direct audit/interface sources. It is not a complete external toolchain lockfile. Re-running the checker recompiles the closure rather than relying on those direct hashes alone.

## Remaining gates

Native category generation, arbitrary payload-action instantiation and multi-request native scheduling remain excluded. The bounded adapter audit does not promise a complete native implementation of every field in the general interface. The RH binding review and the later example-overlap assembly remain independent; shared field names alone do not identify their validity policies or source types.
