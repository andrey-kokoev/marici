# Single pair: a=P, b=E, ab=N as a marked interface

## Local result

The interpretation works for the tested native boundary fixture, including all eight retained context frames:

- `a`: the marked P endpoint;
- `b`: the marked E endpoint;
- `ab`: their compatible interface, mediated by one native N;
- `ba`: the same interface read from the opposite endpoint;
- `aa`, `bb`: self-comparison channels, not extra particle species.

The P and E bodies share an edge. Independently enumerate the actual face-neighbours of each endpoint: their intersection contains exactly one primitive body. Completing its marked reader produces the native neutron. Thus the middle body is reconstructed from the endpoint geometry rather than supplied as a desired answer.

This is a fixture-local statement under the existing native marking, subdivision and PN/NE laws, not a theorem about arbitrary P/E placements or a physical P+E=N reaction.

## Full coefficient condition

Let A be the native PN coefficient map and B the native NE map. A compatible boundary satisfies

```
N = A(P) = B^{-1}(E).
```

Reading `ab` starts from A(P) and checks against the E endpoint. Reading `ba` starts from B^{-1}(E) and checks against P. Both must reconstruct all five complex coefficients, the same body and the same occurrence origin.

The product notation `ab` therefore denotes a compatible interface here, not multiplication or addition of endpoint amplitudes. The two endpoints are constrained by E=B A(P); they are not ten freely chosen complex coefficients.

Visible P/E active faces alone are insufficient. The checker constructs two full states with identical active P and E face coefficients but different retained neutron states. The complement must remain available.

## In-place polarity reversal and positive confirmation

`reverseInPlace` changes only the flow orientation and records a pending reversal. It does not clone the bank, alter coefficients, swap particle identities, or grant confirmation automatically.

`confirm` reconstructs the interface starting from the now-leading endpoint and checks geometry, occurrence and all five coefficients against the retained state. Only success appends a positive-confirmation record. An inconsistent endpoint is rejected and remains pending.

A second confirmed reversal returns the orientation and retained state while keeping all four action records. This tests a flow-orientation involution, **not** an Artin braid generator or a claim that a braid's square is trivial. Flow polarity here is not electric charge conjugation.

Native E still has no outgoing move. Reading its interface backwards is not an invented E-to-N growth operation.

## Verification

```
node research/strominger/checkers/check_single_pe_pair.mjs
```

**9 check groups pass**: unique native middle body, opposite readings, explicit confirmation, retained double-reversal history, refusal of inconsistent endpoints, active-face insufficiency, all five coefficient basis vectors, all eight context frames, and absence of native reverse growth.

- Model: `single-pe-pair-model.mjs`
- Receipt: `results/single-pe-pair-v1.json`

No 14-stage continuation is guessed. The omitted stage and general word-growth rule still need definition before extrapolating this local pair to the proposed 28-step bank. The viewer and previous schedules are unchanged.
