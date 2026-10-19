# Port closure is not reversible response descent

## Result

The source/final-occurrence quotient is sound for the existing arrival task and composes with the retained path constructor. It is not automatically a carrier for the full numerical response.

A new native theorem proves a precise gate:

> If every primitive effect action is injective, and the FULL interpreted effect of each positive path factors through its typed source/final-occurrence port, then every pair of positive parallel paths has the same effect.

In particular, both direct/indirect seam effect pairs agree, so all four return effects agree. The full reversible mixed response therefore cannot be preserved by that quotient when it is nonzero.

Injectivity is weaker than invertibility. No primitive matrices or physical laws are chosen in this theorem.

## Why the gate follows from the actual source

Let p,q:s->t be positive parallel paths. The actual seed has an outgoing occurrence e at every vertex t.

Appending that SAME e gives paths with identical source and final occurrence:

    port(p e)=port(q e).

If full effects factor through ports, then

    act(e)(run(p,a)) = act(e)(run(q,a)).

Injectivity of act(e) cancels the final action, giving

    run(p,a)=run(q,a).

The formal proof uses the existing path interpreter and its composition law. It does not assert p=q in the free path type. The original histories remain distinct.

For the actual seam this produces

    run(AB)=run(AD DB),
    run(BA)=run(BC CA).

The existing conditional comparison-square constructor then supplies the four equal return effects. Any reader of those equal current effect states gives equal values. In a linear matrix realization this annihilates the mixed rectangle.

## Crucial scope: full effects versus observations

The hypothesis is factorization of the ENTIRE interpreted effect state, for every input, not merely factorization of a nonseparating scalar observation of a larger state.

A hidden reversible state may still have an arrival-only observable. That does not let us cancel an equality of observed scalars through its primitive action. This theorem does not forbid that architecture.

Likewise the actual arrival update is noninjective: it overwrites the current arrival with the supplied occurrence. Its successful port quotient does not contradict the gate.

Thus a source port interface can be a good routing/observation layer while remaining insufficient as the full response carrier.

## Exact comparison with the existing numerical target

The existing end-to-end shared-leg preparation chain and its eight support checks were freshly rerun. No new fixture was introduced.

Use its actual arrow legs at indices0 and1:

    X0=I, X1=I+H/3,
    Y0=I, Y1=I+K/5.

All four have determinant one. With Cij=Yj Xi,

    C11-C10-C01+C00 = (Y1-Y0)(X1-X0)
                     = [[0,0],[0,1/15]].

Its trace is exactly1/15. Subtracting the existing common reference2I at every corner does not change the contrast. The existing trace preparation with declared gain1/4 has contrast1/60 on the corresponding actual four record slots.

This is an exact nonzero response target already present in the repository. It is not a new physical measurement or a newly generated source amplitude.

No map identifying these four fixture slots with the seed paths is supplied here. The conclusion is conditional: a proposed binding preserving that nonzero mixed rectangle cannot simultaneously satisfy the native gate's injective-action and full-effect-through-port hypotheses. A numerical dimension match or the earlier port-composition square does not discharge that requirement.

## Structural disposition

Keep the successful port quotient, but do not promote it to the full response state by relabelling.

The nonredundant architecture now has separate obligations:

1. **Routing and arrival observation:** the source/final port summary, with exact composition and contextual closure already proved.
2. **Response-sensitive state:** retained distinctions sufficient for the intended reversible mixed effect, not erased merely because arrivals coincide.
3. **Source response interpretation:** an actual operation on that finer state, with its observation binding to the numerical target.

This does not mean storing all history is proved minimal or physically necessary. It means that the tested arrival quotient cannot itself be the full reversible mixed-response carrier under the stated hypotheses. A noninjective response law or a different target observation is also mathematically possible, but changing either is an explicit contract change.

The intended T9/J4 binding remains open. The new result explains exactly why the successful arrival-level square alone cannot complete it, and tests this against an existing nonzero target rather than another invented response model.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedPortResponseDescentGate -Fresh
    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_seed_port_response_descent_gate.py

Fresh safe Cubical/guardedness closure passed with ignored interfaces and stable inputs.12 native/fixture checks pass; all eight supporting instrument audits are freshly executed by the unchanged end-to-end checker. The Agda theorem is universal over the stated typed effects; the matrix checks use exact rational arithmetic. The imported instrument dynamics retain their original numerical tolerance.

Artifacts:

- `agda/SeedPortResponseDescentGate.agda`
- `results/agda-SeedPortResponseDescentGate.json`
- `checkers/check_seed_port_response_descent_gate.py`
- `results/seed-port-response-descent-gate.json`

No existing update law, physical calibration, primitive source map or rung reader was modified.
