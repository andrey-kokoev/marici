# Covariant whole-window lift for the retained R=s^2 photon cut

## Question and bounded disposition

Does the degree-four Ward/Bose tensor admit an off-forward extension of the prescribed twice-subtracted forward window representative, with a genuinely two-variable analytic difference from the logarithmic representative?

[Contract](contracts/photon-window-lift-v1.json) · [checker](checkers/check_photon_window_lift_v1.py) · [tests](checkers/test_photon_window_lift_v1.py) · [receipt](results/photon-window-lift-v1.json).

**Yes, as a conditional mathematical representative.** The explicit construction below completes EF-WB4 at its declared finite-order R=s^2 scope. It selects neither a physical matching polynomial nor a unique off-forward lift. The strongest rival is simple replacement of the logarithm by a window logarithm without the lower-degree polynomial: that gets the cuts right but fails the exact forward Cauchy prescription. The three-dimensional forward-invisible ambiguity remains.

## 1. Explicit lift and exact forward identification

Use the [regular loop tensor](photon-loop-tensor-v1.md), writing pi^2*M_log=sum_x C_x*ell_x, ell_x=Log(-rho*x), rho>0, x in {s,t,u}. Each C_x is a covariant polynomial multilinear in four polarizations, with quadratic coupling coordinates (g^2,g*f,f^2). Put B_a=pi^2*beta_a and define

    A=B11+B13,     B=B12-2*B13,     H=B2/2,
    J_tau=-(tau^2/2)*A*G2-(tau^2/2)*B2*F2-tau*(B11-B13)*G3.

For 0<tau<1 choose

    pi^2*D_lift,tau = sum_x C_x*[ell_x-Log(1-x/tau)-log(rho*tau)] + J_tau.

This is an explicit Ward/Bose/Lorentz tensor: scalar functions multiply the already constructed channel coefficients, and J_tau is a combination of local covariants. No kinematic denominator is introduced. The log combination is independent of rho and equals -I_tau(x), where

    I_tau(x)=Log(tau-x)-Log(-x).

Its discontinuity has support precisely 0<x<tau. Above tau the endpoint and threshold logarithms have the same rim sign and cancel. Reversing the endpoint sign doubles the exterior cut instead. The endpoint is artificial, not a physical threshold.

At t=0, let A_abs be the constant matrix pi*Im(M)/s^4 in (++ , -- , +- , -+) order. The invariant/reduced dictionary gives A_abs=A_archived/16 at the common Born control; the checker verifies this equality, not a fitted normalization. The s- and u-log matrices are -s^4*A_abs and -s^4*Gamma(A_abs); the t-log coefficient vanishes on physical helicities. The forward restriction is the physical-helicity limit: its transverse source coefficients vanish at least as t^2, so t^2*Log(-t) tends to zero; no numerical 0*Log(0) is used. Polynomial division gives exactly

    pi^2*D_tau(z) = A_abs*[tau^2*z^2/2+tau*z^3+z^4*I_tau(z)]
                 +Gamma(A_abs)*[tau^2*z^2/2-tau*z^3+z^4*I_tau(-z)].

The forward G2/F2/G3 restriction of J_tau is precisely the first two powers in this formula. Thus the constructed lift restricts to the **whole prescribed forward function**, not just its discontinuity or degree-four Taylor coefficient. This statement is for the retained homogeneous R=s^2 cut, not the untruncated physical IR inventory.

The checker independently calls the archived Cauchy polynomial-division and rim functions, compares all 4x4 matrix entries, and checks the three coupling coordinates of the forward jet. At tau=1/2 and g=1/4,f=-1/4, the rational local coefficient shifts in pi^2*(D_lift-M_log) are

    delta g2=21/20480, delta f2=-5/6144, delta g3=17/5120.

Omitting J_tau preserves every cut but loses these nonzero coefficients.

## 2. Two-variable analytic difference, not an inference from forward cuts

Subtracting the log representative cancels all three threshold logs algebraically:

    pi^2*(D_lift,tau-M_log)
      = J_tau-log(rho*tau)*[A*G4+B*G4prime+H*F4]
        -sum_x C_x*Log(1-x/tau).

This equality uses the previously established full-tensor common-scale identity, including G4prime. Each endpoint logarithm has the absolutely convergent expansion

    -Log(1-x/tau)=sum_(m>=1) x^m/(m*tau^m),   |x|<tau.

With u=-s-t, take |s|,|t|<=a and 2a<tau. All three series converge uniformly and absolutely on this two-complex-variable polydisc. Multiplication by polynomial C_x preserves convergence and holomorphy. This proves the analytic remainder directly, rather than inferring it from forward equality. For the covariant tensor the same argument is made on compact momentum/polarization charts with |det(q_i+q_j)|<tau; no global trivialization of helicity frames is assumed.

Since every C_x has Mandelstam degree four, the endpoint series starts at degree five. The complete local difference through degree four is therefore

    J_tau-log(rho*tau)*[A*G4+B*G4prime+H*F4].

The higher generated coefficient of degree 4+m is explicitly sum_x C_x*x^m/(m*tau^m). The checker compares eight such forward coefficients against the independently implemented Cauchy analytic coefficients for each coupling coordinate and three windows.

For the five source helicity scalar functions, let

    K=max(||B11||1+||B12||1+2||B13||1, 3||B2||1), r=2a.

After retaining terms through degree N>=4, the coupling-coordinate l1 tail, uniformly on the polydisc, is at most

    K*r^4*(r/tau)^(N-3)/[(N-3)*(1-r/tau)].

This follows by bounding the log-series tail and each degree-four source polynomial. It is a max-helicity-scalar bound in the declared amplitude coordinates, not an operator-norm bound on arbitrarily boosted tensor components or unknown physical matching. The rational certificate at a=1/16,tau=1/2 is stored in the receipt.

## 3. Nonuniqueness and remaining gates

Any retained local combination eta*F3+zeta*H3+xi*G4prime can be added without changing the prescribed forward function or any cut. Their off-forward minor is (144/625)*I3 at the previous exact control. This is freedom of mathematical extension and finite matching, not an instruction to set physical coefficients to zero. Our minimal lower lift is a declared representative choice. All eight local coefficients remain available when forming M-D_lift; their transformed values are not selected by the construction.

The **unsubtracted** massless amplitude is still nonanalytic at the origin. A convergent generated difference does not imply convergence of an arbitrary matching series, exact unitarity, positivity of IR-subtracted jets, physical preparation, global UV assumptions or native dynamics. Earlier incomplete-stage flags are frozen provenance. C1–C12 and the exhausted C12 budget are unchanged.

EF-WB4 is complete only at its stated finite-order scope. A nonredundant next comparison is whether the archived degree-five c0*c1 cut remains compatible with a full crossed Ward/Bose Born tensor for R=s^2+c1*s^3. The degree-four normalization result does not decide this; it requires a new independent partial-wave/cut comparison, not extrapolation of this receipt or a new numerical planner score.

```text
python -S research/nima/checkers/check_photon_window_lift_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_window_lift_v1.py
```
