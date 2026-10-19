# Source-complete Weil reader: coverage and descent, not universal vanishing

## Fresh task and fixed data

Execute source-complete-weil-reader-audit. Retain X, its K=Q(i) action, the fixed basis (E^3,R,I) of rational Hodge classes and alpha=R. The exact cup matrix is diag(2160,-32,-32). The previously constructed projector O is independently defined by the K-endomorphism correspondence and equals projection onto W=QR plus QI on this Hodge space.

## A reader defined on every algebraic cycle generator

Let S be the free rational vector space on supplied pairs (Y,f), where Y is a smooth connected projective threefold and f:Y->X is a morphism. Define

    s:S -> Hdg^3(X,Q),   s(Y,f)=f_*(1_Y),
    F(Y,f)=(-1/32)(integral_Y f*R, integral_Y f*I) in Q^2.

Extend both maps rationally to finite signed sums. Projective resolution and the proper pushforward degree rule proved in the preceding turn give im(s)=im(cl:CH^3(X)_Q->Hdg^3(X,Q)). Thus the source covers all algebraic generators, including singular supports; it is not merely the divisor library. Coverage is a theorem of existence, not an effective enumeration of every source map or its periods.

If s(v)=a E^3+bR+cI, the projection formula and exact pairing give

    F(v)=(b,c),
    R F_1(v)+I F_2(v)=O(s(v)).

This gives the commutative source-bound diagram S --s--> Hdg --O--> W, with F followed by the basis identification Q^2->W on the other side. The coordinate vector depends on the marked basis; the reconstructed W-valued map is the intrinsic retained projector. No unknown cycle-image quotient was used to define the reader.

## Descent and choice checks

- If s(v)=s(w), then F(v)=F(w). Thus ker s is contained in ker F. In particular rational-equivalence changes and homologically trivial changes of the cycle presentation do not affect F.
- Two resolutions of the same irreducible support push to the same fundamental class, so their readers agree. No claim that the resolutions' other cohomology groups agree is made.
- For a proper generically finite h:Y'->Y of degree e between smooth projective threefolds, F(Y',f h)=e F(Y,f). Dividing the source generator by e gives the same rational cycle value. Without normalization this is covariance, NOT invariance.
- If dim f(Y)<3, the fundamental-class pushforward and both reader components are zero.

The ambient linear reader exists on the entire fixed Hodge space by the displayed pairings. One must not claim that source completeness proves the unknown equality im(s)=Hdg. Here it only means im(s)=the algebraic cycle image.

## The full auxiliary graph/envelope comparison

For any source f choose the constructed graph Gamma in an auxiliary smooth sixfold M with g:M->X of degree d. Then

    integral_Gamma g*R = integral_Y f*R,
    integral_Gamma g*I = integral_Y f*I.

There is NO degree d factor in these equations, since g restricted to Gamma is the supplied map f. This proves independence of the chosen graph embedding and sufficiently positive auxiliary cuts at the reader-value level.

By contrast, for a pulled-back class g*beta,

    integral_M g*beta cup g*R = d integral_X beta cup R,

and similarly for I. A reader applied to two pullbacks needs normalization -1/(32d), not -1/32. These two situations are not interchangeable.

Now construct a general high-degree nodal envelope D_M of Gamma inside M. The smooth-center theorem applies to any smooth projective sixfold (its proof used only the stated dimension and standard Lefschetz/blowup facts), and gives

    im(H^6_(D_M)(M)->H^6(M)) = ell H^4(M) + Q[Gamma].

The explicit auxiliary sector calculation therefore yields

    g_* im(H^6_(D_M)(M)->H^6(M))
       = E H^4(X) + Q f_*(1_Y).

Modulo E H^4(X), the entire additional image is the single line spanned by O(s(Y,f)). The singular-envelope construction transports the supplied generator's unknown Weil component; it neither annihilates it nor creates an independent one. Taking rational spans over all source maps recovers precisely O(im(cl)), not a different obstruction space.

## The universal equation is the old open gate

The proposed all-cycle necessity is now an entirely typed equation:

    F(Y,f)=(0,0) for EVERY smooth projective threefold map f:Y->X.

By coverage and the exact formula, this is equivalent to O(im(cl))=0. On this fixed source it is equivalent to alpha being nonalgebraic, by the existing f0=2+i correspondence: for nonzero z=bR+cI,

    det[z,f0*z]=-44(b^2+c^2) != 0.

The projector preserves algebraic classes, and z together with f0*z spans W. Thus any nonzero reader value would supply an algebraic alpha via the already constructed rational combination; no nonzero value has been found on the fixed X. Conversely algebraic alpha would itself give nonzero value (1,0).

The squared positive readout 32(F_1^2+F_2^2) is merely the norm of O(s). Passing source coverage, descent, trace, or norm checks does not prove its universal zero. The actual algebraic product-fiber R gives value (1,0) in that other fiber, refuting a family-uniform vanishing shortcut, not deciding the fixed-X equation.

## Scoped dispositions

The tested higher-cycle, support, nodal-envelope and auxiliary-realization route is now source-complete at the classical cycle-image interface. Its proposed extra obstruction is MERGED with the base all-algebraic-cycles-annihilation gate; there is no new independent necessity theorem. The tested Deligne nonliftability route is rejected, the complete-intersection nodal residue route has zero extra ambient image, and the general smooth/proper-map route retains exactly the source class's primitive component. The broader existential conjectures remain open; none is declared universally disproved by this audit.

Do not continue extending this same diagram merely to rediscover O(im(cl)). The next independent bounded geometric test is deformation of the actual known-algebraic product-fiber witness: choose an allowed infinitesimal Weil-family direction, test the divisor factors' linearized (1,1) condition, and compare it with the determinant class's preserved (3,3) type. This tests whether the supplied witness can be transported, while distinguishing failure of those chosen factors from nonexistence of every algebraic witness. It is not a request for the operator to provide an all-cycle theorem.

Verification: exact source pairing, degree normalizations, correspondence determinant and algebraic-image rival-model controls, alongside the written composition of already constructed geometric maps. Finite models do not assert additional actual cycles or a theorem about all period values. No proof-assistant certification or Hodge verdict is claimed.
