# Encounter sector: metric embedding exists, existing cycle operation does not match

## Verdict

The narrower bridge fails at the **existing source-operation gate**, before channel transport. All four native chirality/doublet cases have a nontrivial fifth-order pair cycle. The only simultaneous S4 relabellings preserving Strominger's actual eleven-arrow interface square to identity. Neither can carry that cycle through an injective encounter embedding.

An abstract eight-real-dimensional metric/dynamical embedding does exist. It is explicitly constructed below, so this failure is not a repetition of the full-state spectral obstruction. No arbitrary new target symmetry, response mixing or channel vertex was installed to force a pass.

## Fresh source state and scope

[Contract](contracts/scattering-encounter-operation-gate.v1.json); [checker](checkers/check_scattering_encounter_operation_gate.py); [result](results/scattering-encounter-operation-gate.json).

SCC obligation: source-operation compatibility before channel attachment transport. The declared target library is existing vertex relabellings preserving the native selection, plus a separately tested same-clock free-flow interpretation. It is not every possible operator in the ambient matrix algebra.

Fresh communication/read: Strominger's [shared-leg controllability audit](../strominger/shared-leg-controllability-audit.md) reports conditional scalar energy regulation, not independently writable coefficient coordinates or arbitrary encounter controls. Its preparation variations and common-gain law do not supply the desired target cycle. That audit is read, not independently replayed here.

The first execution correctly refused a changed observer-note pin. Fresh inspection found its added controllability follow-up. This new test explicitly pins that reviewed revision, records both old/new hashes and keeps the prior result unchanged. All computational predecessor pins remain enforced; a later unreviewed narrative revision is refused too.

## Positive control: one exact embedding

Reconstruct the137-row generator A from the actual S4 constructor. Let P_low be its squared-frequency32 projector. Select the first nonzero projected coordinate and normalize it to v. Set

    omega=sqrt(32), w=A v/omega, E=[v,-w].

Exact checks give

    E^T E=I2,
    A E=E omega J,
    E^T (A^T A/2) E=16 I2,
    E^T (A/2) E=(omega/2)J,
    J=[[0,1],[-1,0]].

Use one identical plane in each of the four independent matrix-response columns. B=I4 tensor E has eight orthonormal real columns and realizes four complex scalar-energy amplitudes. The full rational/radical vectors are saved, not merely a rank count.

For native scalar encounter energy e, matching the evolution requires declared rate omega/e. In the explicitly stated native Hessian convention e I8, the target Hessian needs a separate factor16/e. These are mathematical conversions, not selected physical clock/energy units. The construction does not prove that arbitrary states in this plane can be prepared as products of the actual shared legs.

## Exact cycle obstruction

Enumerate all24 existing vertex permutations. Preserving the eleven-arrow list with ordered AB omitted forces A and B individually fixed. Only identity and interchange of C,D remain. Their induced137-slot simultaneous-leg matrices U both satisfy

    U^2=I, UA=AU.

They act identically on response-column labels; adding a new action on those labels is outside this source library.

For every native doublet/chirality case, reconstruct

    D_pair=D tensor conjugate(D).

The existing adapter gives, and this test verifies,

    D_pair^5=I, D_pair^2!=I,
    D_pair P_scalar=P_scalar,
    [D_pair,P_vector]=0.

If an injective realified encounter map B carried the operation, U B=B D_pair would imply B(D_pair^2-I)=0, a contradiction. This excludes **any** injective B for these target relabellings, not just the convenient plane constructed above.

A free-flow replacement also fails: a scalar-energy encounter evolves by one common complex phase. The native pair cycle fixes the scalar subspace but acts nontrivially on the vector subspace, so it is not a scalar phase.

A further algebraic consequence, not a separately preregistered numerical test: because both target relabellings commute with A, their compositions with free flows reduce to exp(tA)U. On an invariant scalar-frequency encounter subspace, squaring a proposed cycle again forces D_pair^2 to be a scalar phase. Its fixed scalar vector forces that phase to one, contradicting D_pair^2!=I. These compositions do not repair the gate.

## Channel check and stopping boundary

Existing encounter scalar/vector projectors, two-output vertex and vector-three-output vertex were loaded from the pinned native channel result. Their support identities and vertex-Gram covariance under all four native cycles pass exactly. The original Grams are stored without silently normalizing the vertices. No new scattering solve was performed.

Those checks validate the source side only. Because the target cycle cannot be carried, the test deliberately does NOT define B-dependent target vertices and claim an existing channel correspondence. A formal construction such as vertex*B^T would add target structure by design; it would not discover an admitted source operation. The scalar orbital-record triple vertex and all asymptotic flux maps remain downstream, untransported.

## Decision

Continue physical-scattering research on the existing native-pair/orbital model without identifying it with Strominger's coefficient law. Reopen this bridge only for a specified additional source operation/representation on the target, or a separately declared weaker task that does not require the native cycle. Changing that requirement changes the task and must remain explicit.

The full96-complex-dimensional native complement remains under its own source dynamics. Neither this selected embedding nor software provenance realizes the previously excluded full-state map. No universal no-go for nonlinear, controlled, enlarged or otherwise sourced bridges is asserted.

## Reproduction

```text
uv run --with sympy python research/nima/checkers/check_scattering_encounter_operation_gate.py
uv run --with sympy python research/aspect/scc/scc.py check scattering-encounter-operation-gate-v1
```

Use structured-command. Exact finite algebra, not a new kernel proof or physical apparatus admission. Owner source files and producer receipts are untouched; no commit/push authorized.
