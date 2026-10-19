# Enriched three-pass test: derived duality

## Question

Continue the operator's three-pass attack with actual algebraic support and resolution data, rather than a resource flag or ordinary cohomology conversion. The source operation tested is derived O_X-duality. This does not assert that derived duality is the operator's unique intended main/codimension conversion.

Active SCC obligation: contravariant route and biduality-coherencer compatibility, followed by descent to rational cohomology. No physical process or time is assigned to dualization.

## Source and typed operation

Let X be the fixed smooth projective complex sixfold. For a closed algebraic subvariety Z of codimension p, its structure sheaf O_Z is a perfect object: smoothness makes coherent sheaves locally admit bounded finite locally free resolutions. Put

    D_X(P) = R Hom_{O_X}(P,O_X),
    D_X: Perf(X)^op -> Perf(X).

The derived category (or its stable enhancement) retains differentials and extension data; it is not merely the Chern character. Perfectness gives the natural evaluation equivalence

    eta_P: P -> D_X D_X P.

The triangle law compares the actual maps:

    D_X(eta_P) composed with eta_{D_X P} = id_{D_X P}.

Thus D_X^3 P is canonically equivalent to D_X P. Derived duality is a source-derived enriched realization candidate, but it cannot exhibit a third-pass defect on these objects. These are standard perfect-complex duality theorems, not a newly formalized result.

## Codimension-one versus higher codimension

For a regular closed immersion i:Z -> X of codimension p, a Koszul resolution gives

    D_X(O_Z) = i_*(det N_{Z/X})[-p].

Here cohomological convention is H^k(A[m])=H^{k+m}(A). The only Ext sheaf is in degree p. Codimension changes the degree and normal-determinant twist; it does not break biduality. For singular, non-lci Z the dual can have several cohomology sheaves, but O_Z is still perfect on smooth X and its FULL derived dual still satisfies biduality. Truncating it is a different operation.

In particular even p=1 defeats the underived substitute. On R=Q[t], Hom_R(R/(t),R)=0 since t annihilates the source and not any nonzero element of R. The derived dual instead has Ext^1=R/(t). Discarding the resolution would lose the divisor already on the first pass. Such a loss is not evidence against algebraicity.

## Exact finite cochain control and sign coherence

For a finite cochain complex V, define

    (DV)^n = Hom(V^{-n},Q),
    d_D^n = (-1)^{n+1}(d_V^{-n-1})^t.

Then d_DD^n=-d_V^n. Evaluation must therefore have component eta_V^n=(-1)^n times ordinary double-dual evaluation. It is a chain map, and D(eta_V) eta_DV=id. Omitting this sign fails for a nonzero differential. The companion checker tests these equations, d squared zero, and a deliberately unsigned evaluation on a three-degree exact complex. It also retains a nonexact complex so acyclicity is not used to hide the witness.

These are exact finite linear controls for the signs and triangle; they do not compute the sixfold's sheaves or prove the general derived theorem.

## Relation to the fixed rational Hodge class

For a codimension-p algebraic subvariety Z, the degree-2p component ch_p(O_Z) is its cycle class; lower components vanish. This is the standard Chern-character/fundamental-cycle formula. Rational algebraic cycles are Q-linear combinations of such contributions, not necessarily single sheaves or effective cycles. Negative multiplicities are handled in K_0(X) tensor Q.

For perfect objects, ch_p(D_X P)=(-1)^p ch_p(P). Hence on degree six (p=3), duality acts by minus one, and the third dual gives minus one again. This sign is NOT the native central-i action: agreement of their signs on a selected subspace does not identify the operations.

Crucially, self-duality D(P)=P is not required: the first and third outputs agree, while the original may differ from its first dual. Testing invariance under one dual would falsely exclude ordinary algebraic classes of odd codimension.

There is a direct competing enriched realization for ANY rational even cohomology class. For the underlying compact smooth manifold, the rational topological Chern character is an isomorphism

    K^0_top(X) tensor Q -> direct_sum_p H^{2p}(X,Q).

Thus the selected alpha has a rational virtual topological K-class, with biduality inherited from complex vector bundles. This does not supply an algebraic perfect object. It proves that rational K-theoretic realizability plus repeatable duality alone cannot separate alpha. No integral lift or effective bundle is asserted.

An algebraic K-class with ch_p=alpha would already imply alpha algebraic, since Chern classes of algebraic vector bundles are algebraic and the Chern character is a rational polynomial in them. Conversely algebraic cycles supply that component through their structure sheaves. Merely asking for such a lift restates the missing algebraicity problem; biduality adds no obstruction once a lift exists.

## Issue-level falsification and disposition

Problem: find an algebraic-specific repeatability requirement violated by alpha.
Candidate: resolution-retaining dualization may fail on the third pass beyond codimension one.
Rivals: full perfect duality closes in every codimension; truncated dualization loses real algebraic data; topological duality also closes without algebraicity.
Risky tests: explicit sign-sensitive triangle, underived divisor hostile, rational topological K comparison, and odd-degree Chern-character sign control.
Strongest falsification: the general perfect biduality theorem excludes the proposed failure for this operation, while the topological comparison supplies repeatable rational lifts without deciding algebraicity.
Disposition: reject derived duality ALONE as the detector, not the general sustained-realization proposal. No fixed-alpha nonalgebraicity theorem or new cycle constructor is supplied. Main net and pins remain unchanged.

The unresolved enriched branch now needs an algebraic-specific operation other than duality alone, with a defined domain and universal cycle necessity. Do not replace this missing operation by an arbitrary resource flag, an underived truncation, self-duality, or the unknown algebraic K-image. This packet stops at that missing source operation; it does not proliferate hypothetical successor interfaces.

Sources: hodge-three-pass-realization-v1.md; hodge-cycle-map-scope-v1.md; ledger 4322. Imported mathematical background: perfect duality on smooth schemes, regular-immersion Koszul duality, Chern characters of coherent sheaves on smooth varieties, and rational topological K-theory. No external literature search, independent review or proof-assistant certification is claimed.
