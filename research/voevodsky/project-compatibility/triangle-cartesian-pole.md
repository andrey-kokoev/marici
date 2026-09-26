# Independent Cartesian derivation of the local Euclidean regulator pole

## Independence and scope

Fresh input is the measure-transport claim. This derivation does NOT use the old printed normalization, its finite regulator limit or its joint energy theorem. It uses the Euclidean loop measure and the actual local denominator q3=s+t-ell on the same candidate real reduced-family domain. E is fixed positive and small; x stays in a compact interval J inside(0,a).

Let ell=a+b-E. The two distance centers defining s,t are the endpoints of a segment of length ell. Write the loop point in line-normal coordinates

    loop=A+u*e+eta, 0<u<ell, rho=|eta|.

Then s=sqrt(u^2+rho^2) and t=sqrt((ell-u)^2+rho^2). The exact rationalization

    q3=rho^2[1/(s+u)+1/(t+ell-u)]

gives q3=k(u)rho^2+O(rho^4), with k=ell/[2u(ell-u)]. All other source denominators stay nonzero on the fixed-E compact segment. Let F_E denote the complete six-term source factor divided by q1*q2, evaluated on that segment. The integrand is F_E/(E*q3) to leading transverse order.

## The radial pole comes from Euclidean geometry

For spatial dimension3+2epsilon, the line-normal dimension is2+2epsilon. Use standard rotational dimensional continuation, defined by angular sphere area

    S_(1+2epsilon)=2*pi^(1+epsilon)/Gamma(1+epsilon).

This does not assert existence of a literal fractional-dimensional Cartesian manifold. The leading local angular integrand is constant, so this sphere factor fixes the relevant continuation unambiguously for the pole calculation.

The Cartesian radial measure gives

    d^d loop=du*dOmega*rho^(1+2epsilon)d(rho),
    integrand times measure ~ (F_E/(E*k))*rho^(-1+2epsilon).

Since integral_0^delta rho^(-1+2epsilon)d(rho)=delta^(2epsilon)/(2epsilon), and S→2pi, the regulator-pole coefficient in u coordinates is

    (2pi/E) integral chi_line(u)*u*(ell-u)*F_E/ell du.

Smooth angular/prefactor variations are O(rho) and leave an integrable remainder at epsilon0. Away from the collision the localized integral is regular. These estimates are uniform along the fixed-E compact segment; no joint E,epsilon uniformity is needed here.

## Compare in the previous x coordinate only after deriving the pole

With dgeom=a-g/a, the segment is parametrized by

    x=a-(dgeom/ell)u, |du/dx|=ell/dgeom,
    u=s_c, ell-u=t_c, chi_line=chi(x,w_star).

Thus the independently derived result is

    G_chi(E,epsilon)=A_chi(E)/epsilon+O(1),
    A_chi(E)=(2pi/E) integral_J
        chi(x,w_star)*s_c*t_c*F_E/dgeom dx.

It agrees with the transported coefficient exactly. For a positive cutoff with nonzero trace on the collision segment, A_chi(E)>0. The loop-measure regulator pole is therefore confirmed independently, not merely propagated from the old-family theorem.

## Decision point

Freeze this local mathematical result. It does not determine a finite renormalized physical observable. The old finite boundary value is a normalization-weighted pole coefficient, not automatically a finite part of G_chi. Further boundary charts are not the next priority. The next test is whether that coarse boundary value contains enough data to recover any proposed finite readout, and which source prescription selects such a readout.

`check_triangle_cartesian_pole.py` passes54 exact coefficient/Jacobian fixtures. The dimensional continuation and Mellin argument are written analysis, not machine-formalized proofs. Physical continuation, other strata and source normalization intent remain outside this local benchmark.
