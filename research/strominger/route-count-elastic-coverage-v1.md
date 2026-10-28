# Route-count attachment: full elastic-domain coverage refuted (-+)

The explicit attempt in `contracts/route-count-elastic-coverage-probe.v1.json` tries to reject full-domain coverage by the existing calibrated route-count attachment. The target is the independently specified full real two-body momentum plane, not merely the two-point prepared orbit.

The native observer has type Nat x Nat. The existing positive-mass mechanical map B_m is invertible, and its fixed gain lambda is positive. Consider

    p*=B_m lambda (1,-1).

For positive square-root masses a,b, this is

    p*=sqrt(2/(a^2+b^2))*a*b*lambda*(1,-1).

It is an admissible counter-moving state with total momentum zero and positive kinetic energy lambda^2. Its unique possible count preimage is (1,-1), which cannot belong to Nat x Nat. The impossibility does not depend on enumerating source comparisons. At unit masses and gain, the target is simply (1,-1).

**Outcome: -+.** This fixed attachment is not surjective onto the full elastic domain. Its previous **++** remains valid: native route exchange intertwines with the elastic action on the represented sector, and the twice-exchange effect equation holds. The control (1,2)->(2,1) still passes in the new checker.

This is a source-image admission obstruction, not a loss of already represented records or a failure of action coherence. Appending history metadata cannot produce a missing signed amplitude under the unchanged readout. Allowing signed inputs, offsets, different observations or a different source would be a new contract, not a repair of this frozen claim.

The whole-domain identification is therefore not completed by promoting the current observer binding. A different actual source/state interface is needed if the intended target is the full elastic domain. The existing generalized recoil construction already has continuous source coordinates, but that does not identify them with native route lengths or prove their full native admission. Do not create a third compatible mechanical model or retrofit a target answer to the count source.

Verification: `uv run --with sympy python research/strominger/checkers/check_route_count_elastic_coverage.py`, exact symbolic pass. Receipt: `results/route-count-elastic-coverage/verification.json`. The written range argument supplies the universal preimage exclusion. No fresh Agda or physical experiment; no refutation of all WG presentations or of the governing tower-cut conjecture.
