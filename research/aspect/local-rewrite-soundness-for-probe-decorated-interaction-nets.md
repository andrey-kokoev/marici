# Local rewrite soundness for probe-decorated Interaction Nets

## Question

When does a local Interaction Net rewrite preserve probe-configuration semantics rather than merely preserve its unprobed output?

## Claim boundary

This packet states and tests a finite local criterion. It does not prove confluence or normalization for an entire Interaction Net system, nor does it identify semantic equivalence with physical equivalence.

## Boundary-indexed semantics

Let a redex \(R\) and reduct \(R'\) expose the same typed boundary configuration category \(\mathsf B\). Assign constraint presheaves

\[
\mathcal K_R,\mathcal K_{R'}:\mathsf B^{\mathrm{op}}\to\mathcal C.
\]

A rewrite witness is a natural transformation

\[
\alpha:\mathcal K_R\Longrightarrow\mathcal K_{R'}.
\]

For every boundary inclusion \(c\subseteq d\), naturality requires

\[
\rho'_{d,c}\alpha_d=\alpha_c\rho_{d,c}.
\]

The rewrite is strongly probe-sound when every \(\alpha_c\) is an isomorphism. Equality only at \(c=\varnothing\) is insufficient: a rewrite can preserve the unprobed response while changing unary or joint constraints.

## Residual-bearing rewrites

If \(\mathcal C\) supplies an admitted notion of fiber, cofiber, kernel, cokernel, or comparison span, a noninvertible component may be retained as a typed residual. The residual kind must be declared; a generic category does not provide a canonical subtraction. A rewrite without componentwise isomorphism or an explicit residual witness is semantically lossy.

## Minimal finite witness

Take boundary configurations \(\varnothing,\{p\},\{q\},\{p,q\}\). The redex joint constraint is the equality relation

\[
J=\{(0,0),(1,1)\}.
\]

The reduct uses the complemented coordinates

\[
J'=\{(1,1),(0,0)\}=J.
\]

Let \(\alpha_p\) and \(\alpha_q\) flip their respective bits and let \(\alpha_{p,q}\) flip both coordinates. These maps are bijections and commute with both joint-to-unary restrictions. They therefore constitute a strongly probe-sound rewrite even though representatives change.

A hostile mutation flips both joint coordinates but leaves the unary maps unchanged. The unprobed object and joint relation remain setwise equal, yet the naturality squares fail. A second hostile mutation collapses the joint relation to one point; naturality can be arranged on a restricted image, but invertibility fails and the erased branch must remain as a residual.

## Rewrite certificate

A local certificate must record:

1. common typed boundary ports and configurations;
2. redex and reduct constraint objects;
3. every component \(\alpha_c\);
4. naturality checks for generating boundary inclusions;
5. componentwise invertibility or a typed residual;
6. source paths and conventions;
7. nonclaims concerning global confluence and physical realization.

## Falsifiers

1. Agreement only at the empty configuration does not establish probe soundness.
2. Equal joint cardinalities do not establish naturality.
3. A representative relabelling is sound only when unary and higher components transform coherently.
4. A noninvertible component cannot be called equivalent because selected readouts agree.
5. Local soundness does not compose globally without interface compatibility and rewrite-overlap coherence.

## Disposition

Local probe soundness is natural isomorphism of boundary-indexed constraint presheaves. Residual-bearing rewrites are a strictly weaker, explicitly typed class. The finite checker distinguishes coherent relabelling from a joint-only mutation and from lossy collapse.
