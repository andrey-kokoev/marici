# Limiting conditioning distorts the mode metric beyond scalar or commuting compensation

**New batch, iteration 10 of 10.**

**Strength:** exact algebraic pullback, rational strict bounds and a real-centralizer congruence obstruction. Not a no-go for arbitrary noncommuting controls or physical mechanisms.

[Previous survival analysis](SURVIVAL-TRANSFER.md) · [Checker](check_limiting_mode_metric.py) · [Receipt](results/limiting-mode-metric.v1.json)

## 1. Fresh limiting pullback

The exact backward survival profile h is nonconstant and satisfies Kh=rho*h, with 3/5<rho<5/8 and 32rho^5-rho-2=0. For the symmetric terminal seed, q_n/rho^n tends to c*h with c>0.

Pull this profile back through the boundary-initialized synchronized two-plane E. Exact polynomial arithmetic gives

    Gh=E^t diag(h) E = [[A+B,B],[B,B]],
    A=4+1/(2rho^2)+1/rho^3,
    B=rho+1/(2rho).

Hence E^t diag(q_n) E / rho^n tends to c*Gh. The original counting pullback is G0=[[9,1],[1,1]], while the reference step T preserves Gref=diag(3,1). These two starting metrics are not interchangeable.

Coarse rational interval bounds already prove

    0<2B<A<8B.

Gh is positive definite because its determinant is AB>0. It is not a scalar multiple of G0: scalarity would require A=8B. Thus the finite depth-three scalar exception from the earlier audit does not become an asymptotic scalar law.

## 2. Compensation commuting with T cannot restore either target metric

The unchanged reference step has minimal polynomial lambda^2+lambda+1. Every real map commuting with it has the form

    C=aI+bT.

For any nonzero such map,

    C^t Gref C=k Gref,
    k=a^2-a*b+b^2>0.

The checker verifies the polynomial coefficients of this identity exactly. The corresponding inverse-metric identity implies that commuting congruence preserves

    det(G) / trace(Gref^-1 G)^2.

For G0 this invariant is 1/2. For Gh it is

    9AB/(A+4B)^2 > 1/2,

since 18AB-(A+4B)^2=-(A-8B)(A-2B)>0. Therefore no invertible real C commuting with T can satisfy C^t Gh C equal to a positive scalar times G0.

Gh is also not invariant under T; its invariance defect is checked algebraically. If a commuting invertible C carried Gh to a scalar multiple of Gref, invariance would transfer back to Gh, a contradiction. Thus compensation preserving the unchanged reference-step representation cannot restore the invariant reference metric either.

This is a scoped centralizer obstruction, not a claim about every change of basis or intervention.

## 3. Noncommuting whitening exists, but is another operation

Any positive Gh admits Cholesky factorization Gh=U^t U. Then

    C=U^-1 diag(sqrt(3),1)

satisfies C^t Gh C=Gref. This construction needs algebraic state-dependent coefficients and generally further square roots. It cannot commute with T by the preceding obstruction.

Used as a coordinate change, it requires conjugating the step as well; it cannot keep the same T and repair the metric simultaneously. Used as an actual filter, it is a new intervention whose source authorization remains missing. Mathematical availability is not physical preparation.

Likewise, diagonal h weighting preserves graph reflection but not the original selected plane. Rows 0 and 2 of E must remain opposite; h0=1 differs from h2=1/(4rho^2). A sqrt(h) amplitude filter has the same non-preservation issue. Reflection-compatible filtering does not by itself retain the reference two-mode representation.

## 4. Ten-turn batch checkpoint

This batch has made the preparation/measurement gap more explicit:

- Positive forward native operations cannot generate nonzero odd payloads from nonnegative inputs; signed data and observer subtraction remain allowed.
- A retained orbit observer gives exact even/odd records, but odd*odd concatenation is even; neutral-even successor continuation is a different operation.
- Supplied controller contexts are jointly reflection-covariant, while fixed event labels leak system parity.
- Explicit event registers preserve joint parity, not conditional system oddness; label sums and differences retain different system-parity channels.
- Initial-plane combined norm completeness is possible in a fitted positive metric, but labelled closure reaches fourteen dimensions and contains a two-dimensional endpoint kernel.
- Predecessor-preserving event histories repair that kernel with exact decoders and history-dependent fiber metrics.
- Those controlled weights differ from native accepted weights by products of available-choice counts; retained first rejects account for the missing norm.
- Survival decays uniformly and has a nonconstant algebraic limiting profile. Its mode distortion cannot be removed by scalar or reference-step-commuting compensation.

These results construct and test conditional finite/algebraic bookkeeping. They do not provide native controller policy, coherent odd preparation, event-register recombination, physical metric or independently emitted photons. No formal root outcome is admitted.

## 5. Nonredundant continuation

Advance the independently open atlas/seed source-correspondence branch. Compare exact source claims and admitted operations against the now-explicit requirements: dictionary/control policy, odd correlation preparation, retained event-label recombination and algebraic/state-dependent filtering.

The spectral/accounting constructions must stay separate from physical-channel admission. Broader source-authorized interventions are not excluded by this batch. Completing ten turns is not completing the scientific objective; its root remains null and executable source-correspondence work remains.

Existing pinned work-net and downstream contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_limiting_mode_metric.py
python research/scattering/seed-composition/check_limiting_mode_metric.py --check
python research/scattering/seed-composition/check_survival_transfer.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact rational interval bounds and polynomial remainders verify the pullback and centralizer identities. Their interpretation uses the explicit linear-algebra arguments above, not a new machine-formal admission. Prerequisites are recomputed; only this checker's receipt is written and `--check` is read-only.
