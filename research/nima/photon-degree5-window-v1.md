# Regular degree-five R-family logarithmic/window tensor

## Question and bounded result

Can the independently checked R2/R3 interference cut be lifted regularly with odd crossing and the complete twelve-parameter local jet retained?

[Contract](contracts/photon-degree5-window-v1.json) · [checker](checkers/check_photon_degree5_window_v1.py) · [tests](checkers/test_photon_degree5_window_v1.py) · [receipt](results/photon-degree5-window-v1.json).

**Yes for the coefficient lambda_gamma^2*r0*r1.** The construction below has no rational kinematic poles, matches all retained channel/helicity coefficients, and admits a whole-window extension with a derived two-variable analytic difference. It is not a general dimension-ten Born cut inventory or a prediction of finite matching coefficients. The independently checked right cut is signed interference, not a positive channel by itself.

## 1. Regular logarithmic tensor

Use the [twelve local covariants](photon-local-degree5-v1.md) and [independent Born/cut audit](photon-degree5-cut-v1.md). Strip lambda_gamma^2*r0*r1 and write pi^2*M5_log=sum_x C_x*ell_x with ell_x=Log(-rho*x), rho>0. The positive upper rim is log(rho*x)-i*pi, hence pi*Im M5=-C_s. No new normalization factor is introduced.

For each of six subsets I={i,j}, complement {k,l}, let P_I be the mixed chiral pair product, x_I its symmetric pair invariant, and w_I the crossed product as previously defined. The mixed contribution is

    sum_I P_I*[-(9*x_I^3+x_I*w_I)*ell_I/1280
                +sum_(a in I,b in complement I) sab^3*ell_(ab|complement ab)/1536].

For the all-same-chirality sector use

    (13/1536)*[(F4/4)*sum_x x*ell_x
              +(F5/2)*sum_x ell_x+F3*sum_x x^2*ell_x].

These are polynomials times declared logs, not division by S2 or stu. With S2=s^2+t^2+u^2, the identity

    x^5=(S2^2/4)*x+(S2*stu/2)+stu*x^2

and F4=chi*S2^2, F5=chi*S2*stu, F3=chi*stu show that the latter expression has the required projection (13/1536)*chi*sum_x x^5*ell_x. Thus the forward-invisible F3 remains constructively necessary in this regular representation. The single-minus logarithmic section is zero in this chosen family; independent h3 and h5 analytic matching terms remain free.

Every leg appears in one field strength. Complete pair sums, symmetric weights and common channel branches preserve Ward/Bose/Lorentz covariance. The explicit coefficient polynomials introduce no poles; only the declared massless logarithms and later artificial endpoint logs are present. These are algebraic arguments in imported kinematics, not a native-field or proof-assistant construction.

## 2. Odd crossing and full-tensor scale transport

At the physical forward limit, let A=pi*Im(M5)/s^5. Then

    C_s=-s^5*A,    C_u=+s^5*Gamma(A),    C_t=0,
    C_u=-Gamma(C_s).

The odd sign is indispensable. If the even-degree relation were used, the forward O component of common-log transport would be 13/768. No degree-five local all-same-helicity polynomial has such a forward component, so this would fail the retained crossing/local-jet interface.

Holding leading couplings fixed, ell_x -> ell_x+delta gives

    pi^2*Delta M5=delta*[-G5/120+G5prime/320+65*F5/3072].

This follows from y^3+z^3=-x^3+3xyz and sum_x x^5=(5/2)*S2*stu. The checker verifies it on all 256 matrix-unit polarization tuples, including unphysical polarization components of this representative, not only helicities. The compensating local matching shift needed to keep the total amplitude fixed is the negative of this vector divided by pi^2. Its finite integration constants are not selected.

## 3. Derive, rather than copy, the window polynomial

Put I_tau(z)=Log(tau-z)-Log(-z), 0<tau<1. Degree-five division gives

    z^2*integral_0^tau x^3/(x-z) dx
      =tau^3*z^2/3+tau^2*z^3/2+tau*z^4+z^5*I_tau(z).

The left-cut term has alternating signs, in particular -z^5*I_tau(-z). Consequently the lower polynomial is

    J_tau = (11*tau^3/5760)*G2-(13*tau^3/4608)*F2
           +(tau^2/240)*G3+(11*tau/1920)*G4-(13*tau/3072)*F4.

Define

    pi^2*D5_lift=sum_x C_x*[ell_x-Log(1-x/tau)-log(rho*tau)]+J_tau.

Its forward restriction equals the whole twice-subtracted Cauchy representative for the retained homogeneous interference density. The checker compares the polynomial-division functions, higher analytic coefficients and both rims against the archived implementation, with no redefinition of its coefficients. Physical forward limits use vanishing transverse coefficients times threshold logs, not numerical 0*Log(0).

The endpoint and threshold discontinuities cancel outside the window. This is a mathematical artificial window, not a new physical threshold or an exhaustive physical IR subtraction.

## 4. Analytic difference and retained matching

Subtracting M5_log cancels threshold logs algebraically:

    pi^2*(D5_lift-M5_log)
      =J_tau-log(rho*tau)*[-G5/120+G5prime/320+65*F5/3072]
        -sum_x C_x*Log(1-x/tau).

The final term is sum_(m>=1,x) C_x*x^m/(m*tau^m). Since C_x has degree five, it starts at degree six. For u=-s-t and |s|,|t|<=a with 2a<tau, these series converge absolutely and uniformly, proving two-variable analyticity of the **generated difference**, not the unsubtracted massless amplitude. The covariant statement holds on compact momentum/polarization charts with all pair invariants inside the window.

For the five source helicity scalars, a conservative coefficient bound is K*r^5 with K=13/512, r=2a. After degree N>=5 the generated tail is at most

    K*r^5*(r/tau)^(N-4)/[(N-4)*(1-r/tau)].

This is not a bound on unknown physical matching or arbitrarily boosted tensor components. The lower polynomial plus the displayed common-log polynomial is the exact retained local difference through degree five.

All twelve local coefficients remain independent matching directions. The chosen lower extension has zero additional forward-invisible coefficients by convention; arbitrary allowed kernel additions are not forbidden or predicted away. The complete amplitude may also contain the already constructed degree-four sector. No r1^2 degree-six cut, general leading h3 sector, UV completion, physical preparation or native dynamics is derived here. C1–C12 and C12's exhausted budget are unchanged.

## Next independent question

The fixed R family ties f2=-g2, f3=-3*g3 and sets leading h3=0. Next compute the general degree-two/degree-three Born interference with independent g2,f2 and g3,f3,h3. Retain the six bilinear coupling monomials and physical off-diagonal Bose partial waves, especially single-minus h3. The present zero single-minus cut does not decide that larger inventory. This is a separate bounded compatibility/construction question, not an unearned extrapolation or planner forecast.

```text
python -S research/nima/checkers/check_photon_degree5_window_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_degree5_window_v1.py
```
