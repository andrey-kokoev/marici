# Cross-method test of comparison-slot normalization

## Question

If 137 is an abstract comparison normalization and carrier realization modifies it, what must the same modification do in atomic-recoil and electron-magnetic-moment determinations?

Use alpha_0 = 1/137 as the proposed baseline. Write alpha = alpha_0/(1+epsilon). The hypothesis is a shared epsilon, not equal raw residuals in different apparatuses.

## Atomic recoil

The determination uses the dimensionless product

    Q = (2 R_infinity / c) (m_atom / m_e) (h / m_atom) = alpha^2.

The three measured input factors are obtained independently; the two occurrences of m_atom do not mean that a single experiment directly measures h/m_e. The baseline predicts Q_0 = alpha_0^2. A shared correction requires

    Q/Q_0 = 1/(1+epsilon)^2,
    epsilon_recoil = sqrt(Q_0/Q) - 1.

This is a shift of the assembled input product relative to the proposed baseline, not a claim that an atom-recoil experiment has an unexplained systematic error of that size. The product alone does not allocate a hypothetical carrier correction among recoil, spectroscopy, or mass-ratio inputs.

## Electron magnetic moment

The measured frequency comparison determines a_e = (g-2)/2. The theoretical relation is a_e = F(alpha), with QED radiative terms and small other contributions; its leading term is alpha/(2*pi).

A shared correction requires

    a_e = F(alpha_0/(1+epsilon)),
    epsilon_magnetic = alpha_0 / F_inverse(a_e) - 1.

The inverse is understood on the physical local branch, with all other inputs fixed and their uncertainties propagated. To first order,

    a_e - F(alpha_0) = -alpha_0 F_prime(alpha_0) epsilon + O(epsilon^2).

At leading QED order this is -alpha_0 epsilon/(2*pi). A precision test must use the full F, not only that term. The magnetic anomaly itself is not the .036 residual.

## Numerical scale using the quoted rubidium result

Use alpha^-1 = 137.035999206 only to express the empirical target; it is not predicted here.

- Relative alpha shift from 1/137: -0.00026269889816255.
- Relative shift of Q from (1/137)^2: -0.0005253287856139544.
- Leading-term magnetic-anomaly shift: -3.0518122764496634e-7.

The last value compares alpha/(2*pi) at the two couplings, not full predicted electron anomalies. No independent magnetic-moment dataset was evaluated in this calculation.

## Test and outcome

The shared-normalization hypothesis requires epsilon_recoil and epsilon_magnetic to agree within independently propagated uncertainties, without fitting a different carrier coefficient to each route. The known disagreement between rubidium and caesium recoil extractions must also remain visible in such a comparison.

This establishes how one normalization residual would appear in the two experiments: recoil reads its square, while the magnetic anomaly is linear at leading order and nonlinear at higher orders. It does not determine the residual from carrier geometry. Agreement between independently extracted alpha values tests their common physical parameter; by itself it cannot distinguish this carrier explanation from other explanations of that parameter.

A carrier prediction must supply epsilon before these observed values are used, then propagate it through both formulas. The prior 137.036195933608 toy-model result is not accurate enough to match the precision recoil values; matching the rounded .036 tail is not that test.

## Fixed prediction versus quoted precision

Executable: research/nima/checkers/check_fine_structure_cross_method_target.py. Exact rational calculations compare the unchanged toy prediction with the quoted inverse-coupling determinations:

| Determination | Inverse-coupling difference (toy minus observed) | Difference / quoted measurement uncertainty |
|---|---:|---:|
| Rb 2020: 137.035999206(11) | +0.000196727608 | 17884.3 |
| Cs 2018: 137.035999046(27) | +0.000196887608 | 7292.1 |

These are measurement-uncertainty units, not a full statistical significance calculation: no theoretical uncertainty budget exists for the toy model. As a fixed exact prediction it fails both targets. Relative to the rubidium-inferred coupling, it predicts an alpha-squared product smaller by about 2.871175 parts per million and a leading magnetic term smaller by about 1.435589 parts per million. The latter is a propagated comparison, not an independent magnetic-moment measurement test.

## Explicit reference amplitude and intensity calculation

The assembly checker now has a readout extension: research/nima/checkers/check_comparison_reference_readouts.py. It uses identity reference d=I and the Euclidean matrix inner product <A,B>=Tr(A^T B)/2. These choices define a concrete two-dimensional linear prototype.

For C=d+R, define amplitude A=<d,C>, intensity J=<C,C>, and residual power V=<R,R>. Since <d,d>=1:

    A = 1 + <d,R>,
    J = 1 + 2<d,R> + V.

Thus reference interference and residual power contribute separately. V is the power of a deterministic residual in these tests. It becomes a noise statistic only after a stochastic ensemble and centering are specified.

Let H have its only nonzero entry H_12=1. Change one incoming arrow leg to I+uH and one outgoing arrow leg to I+vH^T. Their eleven-by-eleven compositions and the sixteen unchanged state composites give

    C = I + (11uH + 11vH^T + uv H^T H)/137.

The resulting scalar readouts are

    A = 1 + uv/274,
    V = [121(u^2+v^2) + u^2 v^2]/(2*137^2),
    J = 1 + uv/137 + V.

The uv term is the actual product of the two modified legs. It arises in their single intersecting composition slot. Its sign reverses when one leg reverses. A one-leg perturbation (v=0) changes intensity through residual power while leaving reference amplitude unchanged. Equal and opposite incoming perturbations cancel in the assembled comparison, as verified separately.

Outcome: exact readout and two-leg product identities pass. The prototype supplies a concrete route from relationship-valued residual to scalar amplitude and intensity. Carrier dynamics still have to determine u,v, the metric, and which readout enters electromagnetic normalization. These identities contain no value selected from the measured alpha and produce no numerical fine-structure prediction.

## What could identify the carrier mechanism?

A single universal shift of alpha is experimentally indistinguishable from specifying alpha itself unless the carrier independently predicts that shift or another observable. Re-expressing two existing extractions in terms of epsilon does not construct that prediction.

In the typed assembly prototype, R = C-d is a map A->B, whereas epsilon is a scalar. The missing object is a carrier-specified scalar readout and feedback law, not a further numerical adjustment. If d is invertible in a linear realization, d^-1 R is an endomorphism and its normalized trace is one possible basis-invariant readout. But it need not be the physical one: the checker's off-diagonal perturbation H has zero trace while remaining nonzero. A norm-squared readout detects H, requires an inner product, and is quadratic rather than linear in the perturbation. These readouts predict different signs and sensitivities.

Thus the next source-derived decision is what the reference measures: a coherent amplitude, an intensity, or another specified invariant. An integer slot count cannot decide between these. The current cross-method calculation rules out the frozen toy prediction at precision scale and locates the missing mathematical operation; it does not supply a replacement coefficient.
