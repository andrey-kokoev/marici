# Traversal step 2: transport the local period, not its old boundary value

## Fixed interface

Freshly resumed after the volume-dictionary step and reread the local joint theorem. Let P_old be exactly the earlier localized printed-family period. Define G_chi by replacing ONLY its loop measure by the independently calibrated Euclidean distance measure. Keep the same rational factor, candidate real reduced-family chain, cutoff, a,b and positive branches. This defines a transparent benchmark, not the author's intended physical continued cycle.

For E>0,epsilon>0 the ratio of measures is independent of the integration variables, so the integral comparison is exact:

    P_old(E,epsilon)=R(E,epsilon)*G_chi(E,epsilon),
    R=H/(3sqrt(pi))*Gamma(epsilon+1/2)/Gamma(epsilon),
    H=16D=E(E-2a)(E-2b)(2a+2b-E).

This is not a normalization chosen to force a desired boundary value: R was obtained independently from the Cartesian Jacobian and the printed coefficient.

## The regulator-first finite value does not survive unchanged

At each fixed positive E,

    R=(H/3)*epsilon+O(epsilon^2).

The independently established old-family regulator limit P_old^0(E) is finite and positive for positive boundary tests. Hence

    lim_(epsilon down to0) epsilon*G_chi(E,epsilon)
       =3*P_old^0(E)/H
       =(2pi/E) integral chi(x,w_star)*s_c*t_c*F_E/d dx.

Thus G_chi has a nonzero1/epsilon divergence, not the old family's finite regulator limit. Here d in the last integrand is the geometric variable a-g/a from the collision calculation, not the spatial dimension.

Multiplying by epsilon extracts a regulator-pole coefficient; it is NOT a supplied physical renormalization prescription. No finite renormalized observable has been defined by this calculation.

## Transfer the proven joint estimate with its correct powers

The old local theorem states

    E^(1-epsilon)P_old=B_chi+O(E+epsilon),
    B_chi=(4pi*b*(a+b)/3) integral chi(x,0)/(x+b) dx.

Let h=8ab(a+b). Since H/E=h+O(E) and

    epsilon*E/R
      = [3sqrt(pi)*epsilon*Gamma(epsilon)/Gamma(epsilon+1/2)]*(E/H)
      =3/h+O(E+epsilon),

the exact comparison yields

    epsilon*E^(2-epsilon)*G_chi
       =Q_chi+O(E+epsilon),
    Q_chi=3B_chi/h
         =pi/(2a) integral chi(x,0)/(x+b) dx.

This is a conditional analytic consequence of the earlier written joint theorem, not a new independent verification of its uniform estimate. The arithmetic of the coefficient transfer is checked separately.

The changed scaling is decisive: the old finite energy-weighted boundary coefficient cannot be renamed the Euclidean loop readout. At fixed regulator the local energy power shifts from E^(epsilon-1) to E^(epsilon-2), and regulator removal leaves a pole.

## Contribution to the project objective

On the regulated interior, the two readouts have an explicit coherent comparison map: multiplication by R. At the corner, that map loses invertibility because R has the leading zero proportional to epsilon*E. Therefore generic equivalence of normalized periods does not by itself descend to equivalent completed observations.

The comparison must retain normalization and regulator-pole information, or a source-authorized prescription must say which object is observed. This is a concrete typed interface issue, not a reason to discard either family or declare the common-carrier programme impossible.

The Euclidean measure benchmark is now independently calibrated. Source formula reconciliation, the actual continued chain and a physical subtraction/readout prescription remain open. Neither Boolean admissibility nor selecting a desired finite coefficient supplies these data.

## Next severe test

Verify the Euclidean regulator-pole coefficient directly in Cartesian/collision coordinates, without using the old printed family's joint theorem. That tests the transported result independently while the source-owner normalization/continuation request remains active. Do not proceed by merely extending the old finite-coefficient interpretation to more boundary strata.

## Verification boundary

`check_triangle_measure_transport.py` passes54 exact coefficient fixtures, including a regular d5 comparison and the limiting Q_chi coefficient. `triangle-measure-transport.json` records stable input hashes. The Gamma and joint-asymptotic steps are written analysis; the checks do not certify a physical renormalization or continued cycle.
