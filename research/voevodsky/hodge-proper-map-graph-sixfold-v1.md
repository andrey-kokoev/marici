# Proper-map sources embedded in a controlled auxiliary sixfold

## Fresh task and supplied source

Execute proper-map-graph-sixfold-reduction. Let f:Y->X be any supplied morphism from a smooth connected projective threefold to the fixed sixfold X. This includes the resolutions covering every irreducible cycle generator; it does not assume that alpha has such a realization.

Choose a projective embedding j:Y->P^N, increasing N if needed so N>=2. The graph i=(f,j) embeds Y as a smooth threefold Gamma in T=X times P^N. Write p:T->X, h=c1(O_(P^N)(1)), and also E for p*E. The ambient has dimension6+N and the graph has codimension N+3, independent of the rank or injectivity of f.

## N positive hypersurfaces through the graph really can be smooth

Choose A=H^a external O(b), with a,b positive and sufficiently large along a common ample ray, and I=I_Gamma. Serre vanishing/generation ensures that

    H^0(T,I tensor A) -> H^0(Gamma,N*_(Gamma/T) tensor A|Gamma)

is surjective, and that the target bundle B and I tensor A are globally generated. Thus N independent choices of defining sections give an arbitrary generic tuple of normal derivative sections in the rank-(N+3) bundle B.

At a fixed graph point the bad matrices are the (N+3) by N matrices of rank at most N-1. This determinantal locus has codimension

    ((N+3)-(N-1)) (N-(N-1)) = 4.

Fiberwise evaluation from the tuple parameter space is surjective. The incidence of rank failure over Gamma therefore has codimension at least4-3=1 in the parameter space. Since Gamma is projective, its image is closed; a general tuple avoids it everywhere. This is the actual base-locus calculation. Genericity at one point would not have sufficed.

Consequently the N normal derivatives are independent at every graph point. Each successive partial intersection is smooth there. Away from the graph, the system is base-point-free, so successive Bertini supplies smooth complete intersections there as well. The resulting M, cut out by N sections of A, is a smooth projective sixfold containing Gamma as a smooth codimension-three center. All these conditions hold simultaneously on a nonempty generic open parameter set. Ample complete-intersection connectedness makes M connected.

This construction differs from trying to place a threefold in one smooth divisor of a sixfold: here the remaining normal rank is three and the rank-drop codimension is FOUR, greater than the graph dimension. There is no contradiction with the earlier forced-node calculation, whose rank-three normal section on a threefold has expected zeros.

## Projection degree and the unchanged target

Let q:M->T be inclusion and g=p q:M->X. In cohomology

    [M]=(aE+b h)^N,
    g_*(1_M)=p_*[M]=b^N.

Fiber integration extracts the coefficient of h^N. The positive coefficient shows g is dominant and generically finite of degree b^N; it is not asserted finite or unramified everywhere. Restricted to Gamma, g is exactly the original f. Thus

    g_* cl_M(Gamma)=f_*(1_Y).

M is an auxiliary source ambient, not a replacement Hodge candidate. The final target and the fixed class alpha remain on X.

## Compute the entire auxiliary Lefschetz-sector pushforward

Put ell=c1(A|M). Successive weak Lefschetz applies to the smooth ample complete intersections and identifies H^4(M,Q) with H^4(T,Q). Since N>=2, every class there has a unique expression

    beta4 + beta2 h + beta0 h^2,

with beta4 in H^4(X), beta2 in H^2(X), beta0 in H^0(X). No assumption about the much larger middle Hodge space of M is made.

Using the projection formula and [M]=(aE+b h)^N,

    g_*(ell q*(beta4+beta2 h+beta0 h^2))
      = (N+1) a b^N E beta4
        + binomial(N+1,2) a^2 b^(N-1) E^2 beta2
        + binomial(N+1,3) a^3 b^(N-2) E^3 beta0.

Every term lies in E cup H^4(X). Conversely the first coefficient is nonzero, and beta4 is arbitrary, so over Q

    g_*(ell cup H^4(M,Q)) = E cup H^4(X,Q).

This is equality of subspaces, not identification of their elements or a claim that g_* is injective on the auxiliary sector.

Consequently g_* induces a well-defined quotient map

    gbar_*: H^6(M)/(ell H^4(M)) -> H^6(X)/(E H^4(X)),

and it sends the quotient class of Gamma to the quotient class of f_*(1_Y). The unknown primitive component of a supplied cycle has not been set to zero by embedding its source.

## Controls and limitations

The construction works even if f contracts exceptional loci or has image dimension less than three. In the latter case the dimension-three cycle pushforward is zero despite the graph being an honest embedded smooth center in M. This illustrates why source embedding and ambient pushforward must remain separate maps.

The finite checker verifies the determinantal codimension, all three coefficient extractions, projection degree and a nonsquare-rank hostile. These are arithmetic controls for the written geometric argument, not explicit global sections or equations for M. Serre generation, Bertini, complete-intersection connectedness, weak Lefschetz and projective-bundle integration are imported standard facts. No numerical positivity threshold is asserted.

## Next executable comparison

Now test transport of the FIXED candidate class through g. Determine whether g*alpha is primitive for ell, calculate its polarized self-pairing and trace back to X, and type the pull-push comparison on Chow classes. This must decide whether the auxiliary construction genuinely changes the algebraicity question or merely transports it. The already computed equality of Lefschetz sectors supplies the required adjoint-pairing input; no new algebraic representative is assumed.

No universal all-cycle annihilation, proof-assistant certification or Hodge verdict is established.
