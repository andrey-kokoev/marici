# The completed odd residue classifier is formal on any common Hausdorff topological packet

## Question

Does the finite identity

\[
\ker\rho_N=\{(r,-r,0)\}
\]

survive completion when primitive, square, and connected strata carry different topologies?

## Claim boundary

This packet proves the completed kernel theorem for any common Hausdorff topological vector packet on which the three observer channels are copies and the declared readout is continuous. It does not prove that the existing plus-tail, minus-tail, and seam constructions have already been identified with those copies or that their record-labelled update maps extend.

## Completed packet

Let

\[
V=V^{(1)}\oplus V^{(2)}\oplus V^{(3)},
\]

where:

- \(V^{(1)}\) is the primitive distributional packet;
- \(V^{(2)}\) is the square Hilbert packet;
- \(V^{(3)}\) is the connected trace-class packet.

Each summand may have its own Hausdorff locally convex topology. Equip the finite direct sum with its product topology. Completeness of every summand implies completeness of \(V\), but completeness is not needed for the algebraic kernel equality.

Define

\[
\mathcal M=V\oplus V\oplus V,
\qquad
\mathcal O=V\oplus V,
\]

and

\[
\rho(P,Q,M)=(P+Q+M,M).
\]

Finite addition is continuous in every topological vector space, so \(\rho\) is continuous.

Let

\[
\mathcal R=V,
\qquad
h(r)=(r,-r,0).
\]

Then \(h\) is continuous and injective. Its inverse on its image is the continuous first-coordinate projection.

## Exact completed kernel

If \(\rho(P,Q,M)=0\), its second component gives

\[
M=0.
\]

The first component then gives

\[
P+Q=0,
\qquad
Q=-P.
\]

Therefore

\[
(P,Q,M)=h(P).
\]

Conversely,

\[
\rho h(r)=\rho(r,-r,0)=0.
\]

Hence

\[
\operatorname{im}h=\ker\rho
\]

as topological vector subspaces. Since \(\mathcal O\) is Hausdorff and \(\rho\) is continuous, \(\ker\rho\) is closed. The map

\[
h:V\xrightarrow{\sim}\ker\rho
\]

is a topological isomorphism.

This result is insensitive to the different internal regularity classes because no cross-stratum identification is performed. The equations hold componentwise in \(V^{(1)},V^{(2)},V^{(3)}\).

## Extension prism

Suppose each cutoff inclusion

\[
i_N:V_N\to V_{N+1}
\]

is continuous and the completed object is formed from a compatible directed system. Define inclusions componentwise on \(\mathcal M_N\), \(\mathcal O_N\), and \(\mathcal R_N\). Then

\[
i_N^{\mathcal M}h_N=h_{N+1}i_N
\]

and

\[
\rho_{N+1}i_N^{\mathcal M}=i_N^{\mathcal O}\rho_N
\]

hold strictly by coordinate calculation. Any admitted limit functor preserving these finite products carries the prism to the limit.

## Strongest hostile

The theorem fails to apply if the observer channels do not inhabit copies of one common packet. For example, if \(P\in V_+\), \(Q\in V_-\), and no source-derived comparison embeds both into a common Hausdorff packet \(V\), then the expression \(P+Q\) is not typed. Likewise, if \(M\) lands in a quotient or different completion, the formula

\[
\rho(P,Q,M)=(P+Q+M,M)
\]

already assumes the missing comparison.

A second hostile occurs if the limit topology does not preserve the declared finite product or if the readout exists only on a dense core and is unbounded. Then the finite kernel theorem does not define a closed completed classifier.

## Disposition

The topological kernel calculation itself is closed conditionally:

> Whenever the three completed observer channels are source-identified with one common Hausdorff topological packet \(V\) and the readout is the continuous map \((P,Q,M)\mapsto(P+Q+M,M)\), the reciprocal-odd classifier is a closed topological isomorphism onto the full readout kernel and is natural under every componentwise cutoff inclusion.

The remaining construction gate is earlier than kernel analysis: verify a source-derived common-packet comparison for the actual plus tail, minus tail, and seam channel, stratum by stratum. Update lineage remains a separate instrument-level obligation.
