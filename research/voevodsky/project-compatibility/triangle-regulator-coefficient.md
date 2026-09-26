# Regulator cancellation in the localized boundary coefficient

## Order and scope

Freshly inspected the proven localized limit and the primary-source eq:constant in cosmologicalintegrals.tex. Retain the candidate real reduced family, literal printed normalization and compact x interval J inside(0,a). The order here is strictly

    first E→0 in E^(1-epsilon)P_chi(E),
    then real epsilon→0+ in its coefficient C_chi(epsilon).

No regulator-first or simultaneous period limit is asserted.

## Extract the profile's regulator singularity

Write I_x(epsilon) for the lambda,z integral of the profile in the preceding local theorem. Use s=a-x, t=x+b, A=bs/(at), B=(a+b)/(2st), lambda_star=A/B, and

    Q_star=D23(lambda_star)=a*t/[x(a+b)].

Only the collision lambda=lambda_star,z=1 produces a divergence as epsilon→0+. Contributions away from that collision remain bounded uniformly for epsilon in a small positive interval: the lambda0 and infinity powers and the other angular endpoint have an integrable majorant there.

One can isolate the singularity without treating the moving square root as constant. Put

    v=1-z, y=sqrt(B lambda)-sqrt(A), xi=y+sqrt(A)v.

The exact identity is

    D3=xi^2+A*v*(2-v),
    1-z^2=v*(2-v).

At the collision, d(lambda)/d(xi)=2sqrt(A)/B and the remaining reciprocal denominator is1/(4xst Q_star). Integrating the leading xi kernel uses

    integral_R dxi/[xi^2+A*v*(2-v)]
       =pi/[sqrt(A)*sqrt(v*(2-v))].

The remaining local Mellin integral is proportional to integral v^(epsilon-1)dv. Its coefficient gives

    I_x(epsilon)=pi/[4xst Q_star B] * 1/epsilon + O(1)
               =pi/[2a(x+b)] * 1/epsilon + O(1).

This expansion is uniform on J. To justify the bounded remainder, insert a smooth cutoff equal to1 at the collision. Variation of the smooth prefactor is O(|xi|+v); its xi integral gives at worst log(1/v), which is integrable against v^(-1/2). The finite-xi-domain correction to the full-line kernel is bounded under the same angular weight. The epsilon-dependent smooth coefficient at the collision differs from its epsilon0 value by O(epsilon), contributing only O(1) after the simple Mellin singularity. No global analytic-continuation theorem is needed for this real one-sided asymptotic.

## Retain the source zero instead of substituting epsilon0 early

The literal source formula, with n_s=n_e=3,L=1,d=3+2epsilon, gives

    C(d)=48*pi^epsilon*3^(2epsilon-3)/Gamma(epsilon).

Since Gamma(epsilon)^(-1)=epsilon+O(epsilon^2),

    C(d)/epsilon →16/9.

The transverse prefactor was

    L=C(d)*16^(epsilon-1)*(576a^2)^(1/2-epsilon)/(16a^2),

hence L/epsilon→1/(6a). Setting the source zero to zero before integrating would miss its product with the profile divergence.

Combining these limits with h=8ab(a+b) yields the finite, source-normalized sequential coefficient

    lim_(epsilon down to0) C_chi(epsilon)
      = [4pi*b*(a+b)/3] * integral_J chi(x,0)/(x+b) dx.

It is nonzero for a nonnegative cutoff with nonzero boundary trace. This is a derived cancellation, not a fitted counterterm or an arbitrary normalized test.

## Why this is not yet the ordinary energy residue

The established theorem gives E*P_chi(E)=E^epsilon[C_chi(epsilon)+o(1)] at each fixed real0<epsilon<1. Therefore

    lim_(epsilon down to0) lim_(E down to0) E*P_chi(E)=0.

The nonzero result above uses the DIFFERENT energy normalization E^(1-epsilon). Comparing these expressions alone is not a theorem about exchanging two limits of the same function. Nor does it identify the Laurent residue of a regulator-removed physical period.

To test limit order properly, derive the regulator-first finite-E local limit independently and then evaluate its E behavior. Uniformity as epsilon→0 was not supplied by the fixed-regulator dominated-convergence theorem. The factor E^epsilon itself makes such uniformity a substantive issue.

## Remaining gates and next step

Next local task: extract the regulator singularity directly at the exact finite-E collision, including the complete six-term source factor, and compare the resulting regulator-first local observable with the energy-first one. The other interval/endpoints, spatial infinity, physical continuation, normalization confirmation and global amplitude identification remain open.

## Verification boundary

`check_triangle_regulator_coefficient.py` passes27 exact Fraction coefficient fixtures for the collision quadratic coefficients, Q_star, the profile singular coefficient, the source-zero slope and the combined boundary density. Receipt: `triangle-regulator-coefficient.json`; inventoried source bytes stayed unchanged. The Mellin/Gamma asymptotics and uniform remainder argument are written analysis, not machine-formalized results. Physical convention and owner acceptance are not inferred from the arithmetic.
