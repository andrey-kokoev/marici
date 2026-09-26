# A conditional localized period limit after source-derived recentering

## Result and scope

The preceding joint profile can now be integrated on a compact interior x interval. For the same candidate real reduced-family representative and literal printed normalization, at a fixed regular regulator with0<Re(epsilon)<1, the localized period satisfies

    lim_(E down to0) E^(1-epsilon) P_chi(E) = C_chi(epsilon),

where C_chi is the joint-profile pairing displayed below. This is a written analytic proof using exact finite-E geometry and uniform bounds. It is not a physical cycle identification, a global total-energy residue or regulator removal.

Fix a,b>0, a compact interval J inside(0,a), and a bounded smooth cutoff chi(x,w) supported in J times[0,delta), where delta is sufficiently small. Define P_chi by inserting this cutoff into the candidate real positive-density period used in `triangle-transverse-density.md`. The cutoff is E-independent. All powers use positive real bases with a fixed complex regulator. No owner normalization confirmation is presumed.

## Locate the actual finite-E collision

Set

    ell=a+b-E, g=(a^2+b^2-ell^2)/2,
    d=a-g/a, v=sqrt(H)/(2a), s0=a-x.

The external triangle can be placed at(0,0,0), (a,0,0), (g/a,v,0). Its last edge has length ell, and d^2+v^2=ell^2. The apex coordinates are

    (x,sqrt(w)z,sqrt(w)*sqrt(1-z^2)).

Let eta^2 be its squared perpendicular distance from the line through the last two base vertices. Orthogonal projection gives exactly

    eta^2 = [(d sqrt(w)-v s0)^2
             +2v d s0 sqrt(w)(1-z)+v^2 w(1-z^2)]/ell^2.

All terms are nonnegative. On the chosen compact patch, the collision lies on the segment, not its extension, and occurs at

    w_star=v^2 s0^2/d^2, z=1.

Indeed the two apex distances at this point are ell*s0/d and ell*(d-s0)/d, both positive for small E; their sum is ell. Thus q3=0 exactly, not merely to leading order.

Define lambda_E=w_star/E. Uniformly on J,

    lambda_E → lambda_star=2b(a-x)^2/[a(a+b)] >0.

It is bounded above and away from zero for small E. Use nu=w/(E lambda_E). This pins the moving collision at nu=1,z=1.

## Uniform denominator comparisons from exact geometry

Heron's identity for the triangle with sides s_E,t_E,ell gives

    q3 = 4ell^2 eta^2 /
         [(s_E+t_E+ell)(ell+s_E-t_E)(ell+t_E-s_E)].

For small delta and E, every factor in the denominator is bounded above and below by positive constants on J. Thus q3 is comparable to eta^2, with constants independent of E,w,z.

Put Omega=nu+1-2sqrt(nu)z. Substituting the centered coordinate gives

    eta^2/E = [d^2 lambda_E/ell^2] Omega
                +[v^2 lambda_E/ell^2] nu(1-z^2).

The inequality nu(1-z^2)≤Omega follows from

    Omega-nu(1-z^2)=(sqrt(nu)z-1)^2.

Since d and lambda_E stay nonzero and v^2=O(E), this proves q3/E is uniformly comparable to Omega throughout the cutoff patch.

A second exact identity is

    q23=E+w[1/(r+x)+1/(s_E+s0)].

Hence q23/E is uniformly comparable to1+nu. All other denominators in A_E remain bounded away from zero; choose delta and E small using compactness and their positive w0,E0 values. The six positive terms consequently obey

    E^2 A_E ≤ C / [(1+nu) Omega].

This estimate controls the actual moving singularity, rather than applying pointwise convergence through an untracked pole.

## An E-independent integrable majorant

Write sigma=Re(epsilon). After multiplying P_chi by E^(1-epsilon) and pulling back to nu, its absolute density is bounded by a constant times

    nu^sigma (1-z^2)^(sigma-1/2) /
       [(1+nu)(nu+1-2sqrt(nu)z)].

The remaining factors, including powers of lambda_E, are uniformly bounded on J. Extend the cutoff density by zero outside its nu domain.

This majorant is integrable for0<sigma<1:

- at nu0 it has radial order nu^sigma;
- at infinity it has radial order nu^(sigma-2);
- near nu=1,z=1 its singularity is comparable to
  (1-z)^(sigma-1/2)/[(nu-1)^2+(1-z)], integrable precisely when sigma>0;
- the other angular endpoint requires only sigma>-1/2.

These bounds simultaneously control the moving collision and the growing rescaled tail. They do not address spatial infinity: the original w and x remain localized.

## The integrated compatibility statement

Away from the measure-zero collision, the previously derived profile converges pointwise after this recentering. Dominated convergence applies. Undoing nu to the limiting lambda coordinate yields

    C_chi(epsilon)=2a L h (4a^2)^epsilon
       * integral_J chi(x,0)
          [integral_0^infinity integral_-1^1
             lambda^epsilon (1-z^2)^(-1/2+epsilon)
             W(x,lambda,z) dz d(lambda)] dx,

with h=8ab(a+b), L from the transverse-density note, and W from the joint-profile note.

Thus the boundary functional is derived from the original local density and its geometric change of coordinates. It depends only on the boundary value chi(x,0), not on an arbitrary definition chosen to force equality. For real0<epsilon<1 and the literal positive source normalization, a nonnegative cutoff with nonzero boundary trace gives a positive coefficient: this local boundary observation is nonzero.

The recentered densities converge in L1 by the same domination argument. This is not a claim of total-variation convergence for the original collapsing measures or uniformity over arbitrary original-coordinate tests without regularity control.

## Remaining programme gates

The localization, candidate real representative, branch and printed normalization are essential hypotheses. The other interior interval, x=-b,0,a, and unbounded ends remain untreated. No epsilon→0 limit has been taken; the profile has a regulator singularity that may interact with the source prefactor. An ordinary Laurent residue requires additional analytic information. The physical continuation/normalization owner-input branch remains active.

Next local task: examine the epsilon0 behavior of this proven local coefficient while preserving the distinction between sequential and simultaneous E/regulator limits. Do not promote this local theorem to a physical amplitude identification.

## Verification boundary

`check_triangle_moving_collision.py` checks24 exact rational finite-E collision centers and480 height-decomposition/Heron fixtures, including nonnegativity and the unique collision. Its rational isosceles families approach E0. Receipt: `triangle-moving-collision.json`, with stable source hashes. These fixtures verify arithmetic; the all-parameter comparison and dominated-convergence proof above are written mathematics, not a machine-formalized analytic theorem or owner adoption.
