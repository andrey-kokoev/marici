# Primitive pullback and rational algebraicity are transported, not solved

## Fresh task and retained data

Execute auxiliary-primitive-pullpush. Let g:M->X be a smooth auxiliary sixfold projection constructed from the graph source, with generic degree d=b^N>0 and polarization ell. The target X and alpha=R remain unchanged. The source calculation proved

    g_*(ell cup H^4(M,Q))=E cup H^4(X,Q).

Also E cup alpha=0, alpha is a rational (3,3) class, and integral_X alpha^2=-32. No finite-flat or etale hypothesis is imposed on g.

## Primitivity follows from the computed adjoint sector

For every eta in H^4(M,Q), projection and the preceding sector formula give

    integral_M (ell cup g*alpha) cup eta
      = integral_X alpha cup g_*(ell cup eta)
      = integral_X alpha cup E cup theta = 0

for some theta in H^4(X,Q). Poincare duality pairs H^8(M) nondegenerately with H^4(M), so

    ell cup g*alpha=0.

Thus g*alpha is primitive in middle degree for the actual auxiliary polarization ell. This is not a general assertion that arbitrary pullbacks preserve primitive classes: it uses the proved sector image for this particular construction. Holomorphic pullback preserves the rational Hodge type (3,3).

## Trace, nonvanishing and positive norm

Proper cohomological pushforward and the projection formula give

    g_*g*alpha=alpha cup g_*1=d alpha.

Since d is nonzero over Q, g* is injective and g*alpha is nonzero. The intersection pairing is

    integral_M (g*alpha)^2=d integral_X alpha^2=-32d.

For primitive type(3,3) on a smooth polarized sixfold, the Hodge-Riemann positive form has the middle-degree sign (-1)^15=-1. Hence

    q_M(g*alpha)=32d > 0.

Both the sign and factor d matter. The pullback is not generally an isometry. Normalizing the trace by 1/d gives a left inverse to pullback; it does not construct a cycle. The same bilinear scaling holds on the pulled-back Weil plane: its cup matrix is -32d times the identity and its positive norm matrix is 32d times the identity.

## Chow pullback does not require g to be flat

Both M and X are smooth. The graph factorization of g is a regular immersion into M times X followed by a smooth projection; this gives the standard refined/operational pullback

    g*:CH^3(X)_Q -> CH^3(M)_Q.

The morphism has virtual relative dimension zero. Proper pushforward has the same codimension here, and the Chow projection formula gives

    g_*g* z = d z.

This is not a claim that the set-theoretic inverse image of every cycle has the expected dimension. Refined pullback handles excess intersections; an effective input need not have the naive effective preimage interpretation.

Compatibility of cycle classes with these maps proves

    alpha algebraic on X  iff  g*alpha algebraic on M.

Forward: pull back any rational cycle representing alpha. Reverse: if a rational cycle B on M represents g*alpha, then (1/d)g_*B represents alpha on X. Rational coefficients are essential for this inverse normalization; no integral Hodge statement is inferred. This equivalence concerns the existence of SOME representative, not a canonical lifting or equality of the two entire Chow groups.

## Pairing with a supplied graph source

If Gamma in M is the graph of f:Y->X, its fundamental class satisfies g_*[Gamma]=f_*(1_Y). Consequently

    integral_M [Gamma] cup g*alpha
       = integral_X f_*(1_Y) cup alpha
       = integral_Y f*alpha.

The auxiliary construction has not forced this scalar to vanish. It is zero for the already checked polarization complete-intersection sources, but that control does not cover every value of the cycle map. If all such source scalars were proved zero, that would be a genuinely new universal necessity argument; neither positive norm nor trace supplies it.

## Disposition and next complete source-reader comparison

The auxiliary operation preserves the nonzero primitive candidate with known positive scaling, and algebraicity is equivalent before and after it. This closes the proposed loophole that a richer auxiliary smooth realization alone could change the Hodge verdict. No cycle representing either class has been constructed.

The next bounded task is to compose the now-constructed interfaces into an actual source-complete Weil reader: for each smooth proper-map source f:Y->X, evaluate the two degree-six pairings integral_Y f*R and integral_Y f*I, and compare them with the normalized Weil coordinates of f_*(1_Y). Check invariance under resolution choice and auxiliary graph construction, and identify precisely the remaining universal vanishing condition. This completes the source/descent audit rather than repeating a scalar norm test or assuming divisor completeness.

Verification combines the written Poincare-duality and Chow arguments with exact degree-scaled Weil matrices, normalized trace and wrong-sign/wrong-degree controls. Standard refined pullback, projection formula and Hodge-Riemann are imported geometry, not proved by the finite checker. No new ambient variety replaces X, and no Hodge verdict or proof-assistant certification is claimed.
