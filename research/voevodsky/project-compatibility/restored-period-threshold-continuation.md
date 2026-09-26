# Restored period: an endpoint-inclusive threshold continuation

## Frozen family and scope

Fresh input is the positive-sheet L1 theorem and the restored density D. Keep fixed noncollinear external momenta with positive lengths, fix X1,X3>0, and vary only X2 as an analytic site coefficient. The focal distances are a=y12 and b=y23, separated by P=|p2|. The third norm w=y31 has its center off the focal segment. Put

    delta=X2+P,
    I(delta)=integral_R3 1/[a b w ell1 ell3 (delta+a+b-P)] d3l,
    ell1=X1+a+w, ell3=X3+b+w.

At X2=+P, delta=2P and this is the previously studied positive-sheet germ. The entire positive real delta interval is nonsingular on the fixed real cycle. This is a specific restored representative, not the full graph sum, coupling transform or a chosen physical i0 prescription.

## Exact prolate reduction includes the endpoints

Choose the focal axis coordinate u and transverse radius rho. Set

    v=a+b-P>=0, z=a-b in[-P,P],
    a=(P+v+z)/2, b=(P+v-z)/2,
    u=P/2+(P+v)z/(2P),
    rho^2=[(P+v)^2-P^2](P^2-z^2)/(4P^2).

The exact measure identity is

    d3l=(a b/(2P)) dv dz dphi.

It cancels both explicit focal denominators, including their apparent endpoint singularities. Therefore

    I(delta)=integral_0^infinity B(v)/(delta+v) dv,
    B(v)=1/(2P) integral_-P^P integral_0^(2pi)
          1/(w ell1 ell3) dphi dz.

No interior segment cutoff is required.

## Threshold coefficient and regularity

At v0 the transverse radius vanishes and u=(P+z)/2. Thus

    B0=B(0)=(2pi/P) integral_0^P
        du/[w(u)(X1+u+w(u))(X3+P-u+w(u))] >0.

The third center is a positive distance from the compact segment. Near v0 all remaining denominators are uniformly nonzero. Azimuthal averaging removes odd transverse powers; the remaining expansion is smooth in rho^2, hence B(v)=B0+O(v), uniformly through z=+-P. This justifies including both endpoints in the coefficient.

Choose a small v0>0. The tail v>=v0 is holomorphic for |delta|<v0/2: there the threshold density is bounded by a constant times the integrable positive-sheet density. Splitting B(v)=B0+[B(v)-B0] on[0,v0] yields, in closed angular sectors of the slit plane,

    I(delta)=-B0 Log(delta)+C0+O(delta Log(delta)).

Thus this restored period has a genuine logarithmic threshold. The former positive-sheet Taylor/integration theorem is not contradicted: its center delta=2P is not this endpoint.

## Continuation and discontinuity

The Stieltjes representation defines the analytic continuation from delta>0 to C minus the negative real axis. It fixes the real logarithm for positive delta. At delta=-s, s>0 sufficiently small, the two boundary values obey

    I(-s+i0)-I(-s-i0)=-2pi i B(s)
                      =-2pi i B0+O(s).

The sign follows from1/(v-s+i0)=PV1/(v-s)-i pi delta_D(v-s). Both boundary choices are displayed; neither is designated the physical one without source contour evidence.

The source normal is

    nu=P^2-X2^2=2P delta-delta^2.

Near the negative threshold, delta=nu/(2P)+O(nu^2); the leading logarithmic coefficient in nu is also-B0. At the positive branch X2=+P the same nu0 is regular. Retaining nu without its sheet loses precisely this distinction.

For the signed response -8 L_ext I with fixed external factor, the leading logarithm is +8 L_ext B0 Log(delta). This does not settle other graph-sector cancellations or conventions in a full physical observable.

## Research result and next test

We have now joined the positive-sheet integral to a negative-threshold nonanalyticity for the SAME restored family, with an explicit approach and endpoint-inclusive coefficient. The proof is written analytic work, supported by exact geometry and kernel controls below.

Next compare this energy-threshold logarithm with the dimensional regulator pole at delta0, retaining the same density and normalization. Any proposed common boundary readout must preserve the sheet and order/prescription of these operations. Physical contour selection, the uncontracted operator lift and global graph assembly remain open.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_restored_threshold_continuation.py` verifies focal identities, the exact Jacobian cancellation, the normal-coordinate relation, the logarithmic model integral and the sign of its discontinuity. The full analytic integral theorem is not machine-formalized and B0 is an explicit remaining one-dimensional integral, not a numerically fitted constant.
