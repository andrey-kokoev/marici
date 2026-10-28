# Prepared oscillator cut v2: repair the missing source input

The old four-coefficient cut and its collision test are unchanged. This is a new, explicitly versioned adapter, not a retrospective claim that the frozen test passed.

## Source change

Aspect's independently specified Markov source already declares bath occupation n and the observation N_add=|q|^2 n. The old adapter omitted n. Contract `contracts/prepared-oscillator-cut.v2.json` now admits it before promotion as a fifth, typed scalar source record:

- four existing transfer-coefficient rows;
- one occupation row with a dedicated bath-state role and port.

The preparation record is not a transfer edge. The existing `incoming_promotion`, `indexed`, `unindex` and `leaves` definitions are unchanged. All five records participate in both promotions. Mixed-role aggregate means are transport summaries, never interpreted as physical amplitudes.

## Readout

`checkers/check_prepared_oscillator_cut.py` exposes a source adapter and a `readout(raw)` function. The readout takes only the current cut; it recovers and validates the typed leaf records, computes r and q from the four transfer edges, and consumes n from the recovered preparation row. There is no saved source model or external occupation parameter at readout time.

The supplied analytic law yields, for positive real g,h, real detuning delta and nonnegative n,

    N_add = 4 g^2 h^2 n / (4 delta^2 + (g^2+h^2)^2).

The source variables and physical law remain explicitly supplied inputs. No claim of a new native WG derivation is made.

## Checks

- Exact symbolic recovery and noise identity through raw/from/to presentations at depths 0, 1 and 2.
- Both existing endpoint policies; record counts 5→3→3 (inherited) and 5→3→1 (common).
- Vacuum n=0 and thermal n=3/2 now produce different complete cuts, with added occupations 0 and 24/25.
- Changing the nested recovered occupation to 2 changes the readout to 32/25 even when outer summaries remain unchanged. This hostile checks the readout's dependency, not validity of the deliberately inconsistent aggregate summaries.
- Missing, duplicate, negative and wrongly typed preparation records are rejected; no vacuum default.
- The old coefficient-only collision remains a passing counterexample regression.

Run:

```
uv run --with sympy python research/strominger/checkers/check_prepared_oscillator_cut.py
uv run --with sympy python research/strominger/checkers/check_intrinsic_cut_oscillator_falsifier.py
```

Receipt: `results/prepared-oscillator-cut/verification.json`.

## Follow-up attack: collisions within the declared source family

The checker now reconstructs all four independently declared inputs from the cut. Write the recovered transfer coefficients as `(a,b,c,d)=(g chi,h chi,-g,1)`. Then

    g = -c
    chi = a/g
    h = b/chi
    delta = i (1/chi - (g^2+h^2)/2)
    n = recovered occupation record.

The source assumptions g,h>0 and real delta ensure g and chi are nonzero. Substitution proves that this reconstruction composed with the source constructor is the identity on `(g,h,delta,n)`. Retained leaf recovery extends that identity through both promotion policies and all three presentations. Thus equal complete labelled cuts cannot encode different tuples in this declared family. This does not settle arbitrary, unspecified notions of geometric triangle equivalence.

The symbolic checker verifies the reconstruction and source re-encoding at every tested depth/presentation. A phase-sensitive hostile uses delta=+3 versus delta=-3: added occupations coincide, but the cuts differ and the reconstructed signs are correct. Four malformed-coefficient controls (wrong direct term, zero susceptibility, wrong coupling sign, imaginary recovered internal coupling) are rejected by source-family admission. The readout now performs that admission check before evaluation. This validates recovered source leaves; it does not certify every outer aggregate of an arbitrarily tampered promotion tree.

This is an algebraic left-inverse argument with exact symbolic execution, not a new Agda theorem. No source fields or physical scope were added during this follow-up attack.

## Claim boundary

This fixes the adapter for the declared occupation-only prepared Markov response/noise interface. It is not an encoding of arbitrary bath states, squeezed/correlated baths, all admissible physical operations or full fluctuation-dissipation. Intrinsic determination and universal source coverage remain open. The old counterexample shows why full source admission matters; the v2 result demonstrates a bounded repair with the missing datum physically justified before its use, rather than attaching a desired answer.
