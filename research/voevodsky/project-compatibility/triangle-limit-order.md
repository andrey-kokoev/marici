# Noncommuting local energy and regulator limits

## Scope and observable

Freshly read the finite-energy collision geometry and sequential regulator-coefficient result. Continue the SAME localized candidate real period P_chi(E,epsilon), literal printed normalization, positive branches, a,b>0 and compact x interval J inside(0,a). The E-independent cutoff chi(x,w) is supported at small w and may have nonzero trace at w0.

This note compares two orders for the SAME observable E*P_chi(E,epsilon). It is not a comparison of differently normalized quantities. The result remains conditional on this representative and normalization, not an identification of the full physical period.

## Extract the regulator singularity at fixed positive E

Use ell,d,v,H,w_star from the moving-collision note. At the exact q3 collision define

    s_c=ell*(a-x)/d, t_c=ell*(d-a+x)/d,
    r_c=sqrt(x^2+w_star), z=1.

The complete remaining six-term factor, evaluated at these lengths, is

    F_E = [ (1/q23+1/q31)/(E+r_c)
           +(1/q31+1/q12)/(E+t_c)
           +(1/q12+1/q23)/(E+s_c) ]/(q1*q2),

where q1=r_c+a+s_c, q2=r_c+b+t_c, q12=a+b+s_c+t_c,
q23=E+r_c+s_c-a and q31=E+r_c+t_c-b. All are positive at fixed small E on J. In particular F_E does NOT contain1/q3. No term is discarded in this fixed-E expression.

Set u=w-w_star and V=1-z. The exact height formula and Heron's identity yield

    q3=k*u^2+m*V+O(u^3+uV+V^2),
    Kq=ell/(2s_c*t_c),
    k=Kq*d^2/(4w_star*ell^2), m=Kq*2w_star.

The angular coefficient m includes BOTH contributions from the height identity:2d^2*w_star/ell^2 and2v^2*w_star/ell^2. Their sum is2w_star. Dropping the second because it vanishes as E→0 would give the wrong finite-E coefficient.

Since

    2km=[d/(2s_c*t_c)]^2,

the local angular/radial Mellin singularity is

    integral dw dz (1-z^2)^(-1/2+epsilon)/q3
       = [2pi*s_c*t_c/d] * 1/epsilon + O(1)

after localization equal to1 at the collision. The coefficient follows by integrating du/(k*u^2+m*V) over the real line, then using (1-z^2)~2V.

For each fixed E this expansion is uniform on J. Smooth prefactor variations and the cubic/mixed remainder leave integrable errors, of at worst V^(-1/2)log(1/V) after u integration. Away from the unique collision the integral stays bounded as epsilon→0+. No uniform-in-E remainder is asserted at this stage.

## The regulator-first local period

The source-derived density before regulator removal is

    2a L (H/E) (4a^2)^epsilon
       chi(x,w) w^epsilon (1-z^2)^(-1/2+epsilon) A_E dx dw dz.

At fixed E, w_star>0. Therefore w_star^epsilon→1, and the previously sourced L/epsilon→1/(6a) cancels the regulator divergence. The resulting finite regulator-first period is exactly

    P_chi^0(E) := lim_(epsilon down to0) P_chi(E,epsilon)
      = [2pi H/(3E)]
          * integral_J chi(x,w_star) [s_c*t_c/d] F_E dx.

Regular parts vanish against the simple zero in L. This formula retains the full finite-E source bracket and the actual collision location.

## Take the energy limit of this expression independently

Uniformly on J, w_star→0, s_c→s=a-x, t_c→t=x+b, d→a+b and H/E→h=8ab(a+b). The exact collision geometry or its Taylor expansion gives

    q23/E → a*t/[x(a+b)],
    E*F_E → (a+b)/(4a*s*t^2).

Only now, after retaining all terms at finite E, may the1/q23 terms be selected as the energy-leading terms. Their limits imply

    lim_(E down to0) E*P_chi^0(E)
      = B_chi
      := [4pi*b*(a+b)/3] * integral_J chi(x,0)/(x+b) dx.

This agrees with the earlier energy-first E^(1-epsilon)-normalized coefficient calculation, but was derived independently from the fixed-E regulator singularity.

## A genuine order obstruction for one observable

The fixed-regulator local theorem already implies E*P_chi(E,epsilon)→0 for every fixed real0<epsilon<1. Consequently

    lim_(E down to0) lim_(epsilon down to0) E*P_chi = B_chi,
    lim_(epsilon down to0) lim_(E down to0) E*P_chi = 0.

For a nonnegative cutoff with nonzero boundary trace, B_chi>0. Thus this localized source-derived candidate family has noncommuting energy and regulator limits. There can be no jointly continuous extension of this observable to the parameter corner that agrees with both iterated values.

This is a concrete completion-order obstruction, not merely missing documentation. It does NOT refute a prescribed physical order, a richer boundary object retaining asymptotic data, or a properly specified regularized observation. It also does not settle the unlocalized physical period: other sectors, endpoints, infinity, the continuation path and normalization convention remain separate gates.

## Next discriminating step

Determine whether recentering gives regulator-uniform control of the normalized local family. That would distinguish simultaneous approaches to the corner instead of relying only on iterated limits. Do not infer a joint asymptotic from the two iterated limits alone. The owner-input branch must still specify the actual physical regulator/continuation prescription.

## Verification boundary

`check_triangle_limit_order.py` passes24 rational finite-energy fixtures with exact collision lengths and all six source terms, plus9 general limiting-coefficient fixtures. It checks the angular coefficient directly, the quadratic coefficient by differentiation, and detects the erroneous omission of the finite-E angular term. `triangle-limit-order.json` binds unchanged source snapshots. The Mellin extraction and sequential-limit proof are written analysis, not machine-formalized analytic theorems or physical owner acceptance.
