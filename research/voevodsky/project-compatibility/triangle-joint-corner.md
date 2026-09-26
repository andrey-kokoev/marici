# Uniform local corner law and the retained completion parameter

## Result and hypotheses

Freshly read the noncommuting-limit result. Keep exactly its candidate real reduced family, literal printed normalization, positive branches and smooth E-independent cutoff chi supported in a compact J inside(0,a) and sufficiently small0≤w<delta. No physical continuation or owner acceptance is added.

For real E,epsilon positive and sufficiently small, the localized period satisfies the joint estimate

    E^(1-epsilon) P_chi(E,epsilon) = B_chi + O(E+epsilon),

where the constant is independent of both parameters and

    B_chi=[4pi*b*(a+b)/3] integral_J chi(x,0)/(x+b) dx.

The proof below supplies the uniformity missing from the previous fixed-regulator theorem. It is written analysis, not a machine-formalized theorem.

## Remove the apparent loss of uniformity by the actual collision coordinate

Use nu=w/(E lambda_E), lambda_E=w_star/E, as in the moving-collision proof. On J, lambda_E extends smoothly to a positive value at E0. At bounded nu near1, every length and every nonvanishing denominator extends smoothly in E,nu,z to E0: square roots have positive bases there, and sqrt(Hw)=E*sqrt((H/E)lambda_E nu).

Write D_E=q3/E. The exact Heron/height formula gives

    D_E = M_E [Omega + delta_E*nu*(1-z^2)],
    Omega=nu+1-2sqrt(nu)z,
    delta_E=v^2/d^2=O(E),
    M_E=[4ell^2/HeronDenominator] * d^2 lambda_E/ell^2.

M_E is smooth and uniformly positive near the fixed collision nu=1,z=1, including at E0. The remaining scaled numerator is

    E^2 A_E = N_E/D_E,
    N_E = E*(complete six-term bracket)/(q1*q2).

N_E is smooth there because q23/E extends to a strictly positive function. This retains all source terms; terms not containing1/q23 simply acquire an explicit factor E.

Consequently, with u=nu-1 and V=1-z, D_E has a positive quadratic/linear normal form with coefficients bounded above and away from zero uniformly in E:

    D_E=k_E*u^2+m_E*V+O(u^3+uV+V^2).

The smooth numerator, cutoff, Jacobian and their required derivatives are uniformly bounded on a fixed neighborhood. No log(E) occurs in these coefficients after the E^(1-epsilon) normalization: powers are of nu, lambda_E and fixed positive constants.

## Uniform local Mellin extraction, including the rest of the domain

Fix epsilon0<1. Outside a fixed neighborhood of the collision, the previously proved majorant

    nu^epsilon (1-z^2)^(epsilon-1/2) / [(1+nu)Omega]

has a bound integrable uniformly for0≤epsilon≤epsilon0. At nu0 use nu^epsilon≤1; at infinity use nu^epsilon≤nu^epsilon0; at the angular endpoints outside the collision use the exponent-1/2. Extend the cutoff integrand by zero beyond its growing nu domain. Thus this entire complementary contribution is uniformly O(1) before multiplication by L=O(epsilon).

Inside the neighborhood, the positive normal form gives a simple Mellin singularity. Freezing its smooth coefficient produces R_E/epsilon. The errors are uniformly integrable: after the u integration, numerator variation and cubic/mixed denominator errors have at worst V^(-1/2)log(1/V) behavior. The same estimates apply to the finite-domain replacement of the full-line quadratic integral. All bounds are uniform because the coefficients and derivatives above extend to E0 on a compact neighborhood.

Smooth epsilon dependence of the frozen coefficient changes R_E/epsilon by only O(1). Therefore, including the regular prefactors and the source zero in L, the normalized observable obeys

    E^(1-epsilon) P_chi(E,epsilon)
       = E*P_chi^0(E) + O(epsilon),

uniformly for small E. The constant term is identified by the independently derived regulator-first formula, not defined to force agreement. This is stronger than merely taking two iterated limits.

## Control the remaining E dependence

The exact regulator-first expression from `triangle-limit-order.md` is

    E*P_chi^0(E)=(2pi H/3)
       integral_J chi(x,w_star)*s_c*t_c*F_E/d dx.

Here H/E, E*F_E, s_c,t_c,d and w_star extend smoothly to E0 on J; q23/E has a nonzero limit. Since chi is smooth and w_star=O(E), this expression equals B_chi+O(E). Combining estimates proves the joint law stated above.

The cutoff and compact x interval are essential. This argument neither extends to the collinear endpoints nor controls spatial infinity.

## Classify simultaneous approaches without choosing one to force a value

Fix any positive reference energy E_ref to make the logarithm dimensionless, and put

    tau=epsilon*log(E_ref/E).

The proven uniform law implies

    E*P_chi = E^epsilon [B_chi+O(E+epsilon)].

Along any joint approach E→0+,epsilon→0+ with tau→c in[0,infinity],

    E*P_chi → exp(-c)*B_chi,

with exp(-infinity)=0. Indeed E^epsilon=E_ref^epsilon*exp(-tau), and E_ref^epsilon→1. Changing the fixed reference energy does not alter c or this boundary value.

Explicit paths:

- E/E_ref=epsilon^p, p>0: c=0, boundary value B_chi.
- E/E_ref=exp(-c/epsilon), fixed0<c<infinity: boundary value exp(-c)B_chi.
- E/E_ref=exp(-1/epsilon^2): c=infinity, boundary value0.

For positive boundary tests, this realizes every value between0 and B_chi. The two previously calculated iterated values are therefore part of a genuine continuum of local corner behaviors, not sufficient data to determine a unique joint completion.

## Programme-level consequence, with the physical gate intact

Collapsing the entire parameter corner to one point loses a nonconstant source-derived observation. Retaining tau as boundary data gives the local extension exp(-tau)B_chi; alternatively a source-prescribed approach can select one value. Neither choice may be declared the physical prescription merely to obtain a desired result.

This establishes a scoped construction–observation compatibility law and a precise obstruction to an order-independent collapsed local completion. It does NOT establish the common physical carrier calculus, the actual continued chain, the correct source normalization convention, a global amplitude or a total-energy residue of the unlocalized period.

The Benincasa/Nima handoff now needs an explicit regulator/energy approach in addition to normalization and chain transport. Other collinear intervals/endpoints and infinity remain independent analysis gates. A source-authorized completion must either select the approach or retain the relevant asymptotic data; the present local calculation does not supply that authority.

Next independent mathematical step: analyze whether the opposite interior interval and endpoint charts admit compatible boundary data, without gluing away the tau dependence. Owner input remains active in parallel.

## Verification boundary

`check_triangle_pilot_closure.py` reruns the seven original exact-checker dependencies plus the independent measure challenge and records fresh hashes and receipts. The latter finds a mismatch with the ordinary Euclidean loop measure under the volume conventions used here; see `triangle-measure-audit.md`. This blocks physical promotion without changing the literal-family hypotheses of this conditional theorem. Those check algebraic identities and finite fixtures, not the uniform analytic estimates. The proof above uses their source-derived geometric identities and supplies the additional uniform Mellin/tail reasoning explicitly. No numerical sampling of paths is presented as proof of the joint law.
