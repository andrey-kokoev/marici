# Falsification attempt: the current cut forgets bath preparation

## Frozen boundary

Contract: `contracts/intrinsic-cut-oscillator-falsifier.v1.json`, written before execution. Cut: the actual two-promoted raw/from/to coefficient presentations with **all** nested member records, labels, endpoint fields, masses and aggregate values. No cone or geometric wrapper. Equivalence for this attack is exact equality of those complete presentations; no source field is stripped to manufacture a collision.

The independently declared target is a *prepared* stationary Markov model: the bath occupation is part of the boundary condition, and added external occupation is a required observation. This is not a claim that two preparations are two different unprepared dynamical laws.

## Exact collision

Use the existing source rates k_external=1, k_internal=4 at resonance. Both preparations have

    r=3/5, q=-4/5, |q|^2=16/25.

Compare vacuum occupation n=0 with thermal occupation n=3/2, both allowed by the source's declared occupation parameter. The complete promoted cut and all recursive members are identical under both existing endpoint policies. The intrinsic raw/from/to triangle commutes without the added cone.

But the existing source law gives

    N_add = |q|^2 n,
    N_add(0)=0,
    N_add(3/2)=24/25.

Therefore no function of **this cut alone** can recover N_add for both preparations. This is a decoder-impossibility argument, not just a failed attempt to implement one: equal arguments must produce equal outputs, while the required outputs differ.

Changing the actual bath coupling and regenerating the entire source changes the cut and its coefficient readout. This control confirms that the test retains the actual nested coefficient data. The missing variable is the bath preparation, not a deleted nested bath coefficient.

## What failed, what survived

**Falsified:** interpreting the current four-coefficient cut as a complete representation of the prepared thermal domain. It determines the transfer coefficients and commutator normalization, not every physical noise prediction.

**Survives:** the intrinsic presentation triangle exists in this example without `ThreeWitnessRetainedCone`, and full recovery of the coefficient-only domain holds. The narrower native-readout and retained-representation theorems are unchanged.

**Not established:** falsity of the existential all-domain conjecture, or impossibility of a different WG cut containing the preparation state. A complete preparation-bearing WG source admission was not constructed in the earlier coefficient test. Consequently this collision cannot silently be promoted into a counterexample satisfying every premise of the universal strong conjecture.

This corrects our earlier shorthand that 'the bath is retained underneath': the bath **transfer channel** is retained; the thermal state/occupation was not in that packet. The claim that the bounded Markov transfer representation was the whole prepared stochastic/quantum domain was too broad.

## No retrospective repair

The frozen cut contract and failed interpretation remain recorded. Occupation is not added to them after the result. Any preparation-bearing successor must independently identify where that state enters the actual source and how its witness is retained; it is a changed contract, not proof that this test passed.

The remaining discriminating question is whether an alleged missing distinction already belongs to the actual source and is lost by the cut, or was never admitted into that source. Only the former directly attacks intrinsic determination for a correctly bound full-domain source. This distinction is needed before declaring the universal conjecture refuted.

## Verification

`uv run --with sympy python research/strominger/checkers/check_intrinsic_cut_oscillator_falsifier.py`, exit zero, execution `structured_command_execution:e_42200_1792524602073650600_57`. Receipt: `results/intrinsic-cut-oscillator-falsifier/verification.json`. The checker verifies the predicted collision and counterexample; its pass status is not a surviving-conjecture verdict. Both endpoint policies were tested. No new physical experiment or Agda compilation.
