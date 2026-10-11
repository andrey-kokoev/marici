# Testing future potential as a dual continuation

## Stronger hypothesis

The previous test showed that an unexecuted parallel path does not acquire opposite phase character merely by changing its execution tag. This turn tests a different type: an effect or continuation consuming a state to produce an answer.

Fresh inspection of `WholePackageSigmaPi.agda` confirms that its retained universe already represents map types with El(maps Q R)=El(Q)->El(R). This supports the type of construction, but does not select a complex-linear functional, a nonzero continuation or an electromagnetic action.

Distinguish:

    Effect = V -> R,
    Future = (V -> R) -> R.

A future computation in continuation-passing form has the second type. These two objects must not be conflated when interpreting charge.

## A positive selection theorem

Supply equivalences e on states V and h on answers R. Requiring evaluation covariance

    transformed(f)(e x) = h(f x)

for every x uniquely forces

    transformed(f) = h composed f composed e^-1.

The inverse is derived from compatibility of evaluation, not assigned to an unexecuted flag. `ContinuationPhaseTransport.agda` proves both this covariance and uniqueness for arbitrary supplied equivalences and function types.

In a separately declared complex-linear functional sector, let V have scalar phase weight q and R weight r. The induced effect character is then r-q. With a neutral answer, r=0, it is -q.

**This is a real positive result for the refined intuition:** a linear continuation into neutral answers naturally transforms oppositely to its argument. It is the ordinary contragredient action, now explicitly checked at the retained type interface. It is not yet evidence of a new matter particle.

## The sharper controls

### The answer representation matters

Holding state weight q=1 fixed gives effect weights -1, 0 and +1 when the answer weights are 0, 1 and 2 respectively. Neutral output must therefore belong to the intended observable contract, not be inferred solely from the word future.

### A bare function type is not a linear dual

With weight-one input and neutral output, the same function type contains:

| Function sector | Induced character |
|---|---:|
| f(x)=x, complex-linear | -1 |
| f(x)=x^2 | -2 |
| f(x)=conjugate(x), antilinear | +1 |
| f(x)=absolute-square(x) | 0 |

The inverse-input transport law applies to all four. It does not make the whole function space a single negative-charge representation. The source must select the linear sector before the weight -q conclusion applies.

The exact finite phase controls are regressions; the stated character weights follow symbolically from the monomials/conjugation and are not inferred only modulo three.

### Continuation-passing a state does not reverse its charge

Define present(x)(f)=f(x). The induced action on Future satisfies

    transform(present(x)) = present(e x).

This naturality is proved in Agda. In the double-linear sector its character is r-(r-q)=q: the original weight returns. For general function spaces the theorem concerns the embedded present states; it is not a claim that every possible nonlinear Future has one character.

Thus putting a present state into continuation form does not produce an oppositely charged state. The negative character of a dual effect is paired with its argument in evaluation, yielding the declared answer character. It does not require a charge-flipping matter transition.

## Retention and native boundary

The module uses the existing retained universe to keep the original state beside its continuation presentation. It proves the active-value identity. It does not claim that a native seed executor selects an actual nonzero effect, that all alternatives must be effects, or that this is a field-coupled particle birth operation.

The generic transport theorem is formally checked. The U(1), complex linearity and charge interpretation are explicit representation hypotheses checked separately by exact character calculations. This is not an Agda formalization of electromagnetism or verified extraction of complex arithmetic.

## Outcome

The original status-only proposal failed. Its dual-continuation refinement has a precise mathematical success: inverse phase response is forced by evaluation covariance in the neutral-answer linear sector.

The physical gap is now more specific. Why would the proposed source select that sector and instantiate a persistent independently interacting object in it, rather than merely store a functional describing how to read another state? No electron mass, conserved matter-charge current, statistics or dynamical coupling has been derived. Relabelling a bra/effect as an electron would bypass exactly this question.

## Fresh verification

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ContinuationPhaseTransport -Fresh` passed, with safe Cubical/guardedness checking, ignored interfaces and stable inputs.
- Receipt: `results/agda-ContinuationPhaseTransport.json`.
- `python research/nima/checkers/check_continuation_charge_character.py` passed 225 linear evaluation controls, additional function-sector controls, exact integer-character identities, and source-digest agreement with the formal receipt.
- Results: `results/continuation-charge-character.json`.

No prior source law or owner artifact was changed. No new ledger entry, physical charge derivation or publication is claimed.
