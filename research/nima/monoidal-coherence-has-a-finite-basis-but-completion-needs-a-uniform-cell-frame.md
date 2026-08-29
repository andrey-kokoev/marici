# Monoidal coherence has a finite basis but completion needs a uniform cell frame

## Finite arity closure

If the intended arithmetic-analytic constructor system is monoidal, independent finite-arity escalation stops at four atoms. Mac Lane coherence reduces all finite reassociation diagrams to a finite basis:

1. binary assembly;
2. associator naturality;
3. left and right unitors;
4. triangle identity;
5. pentagon identity.

Higher bracketings create no new independent reassociation axioms once these cells are established.

If exchange is admitted, add braiding and the hexagons. If dagger, reversal, or duality is admitted, add compatibility with associators, unitors, evaluation, coevaluation, and involution.

These extensions are conditional on source authority. Symmetry or dagger structure cannot be inferred from a scalar observer.

## Cohomology qualification

For a phase-valued associator
\[
\alpha_{a,b,c}=\omega(a,b,c),
\]
the pentagon condition is
\[
\delta\omega=1.
\]
A nontrivial coherent class
\[
[\omega]\in H^3
\]
may be a genuine coefficient lens. It is not a defect and need not be removable in the frozen skeletal presentation.

An authorized rephasing by a two-cochain \(\eta\) changes
\[
\omega\mapsto\omega\,\delta\eta.
\]
Only a coboundary can be eliminated by such gauge. The checker must therefore report separately:

- pentagon failure;
- coherent nontrivial class;
- authorized coboundary rephasing;
- unauthorized attempted strictification.

## Restricted-product completion

Let \(\mathcal C_X\) be the finite-cutoff monoidal constructor categories, with authorized inclusions
\[
I_{X,X'}:\mathcal C_X\to\mathcal C_{X'}.
\]
Let \(\widehat{\mathcal C}\) be the restricted-product completion selected by source energy and the projective exponential topology.

The completion theorem must construct continuous limiting cells
\[
\widehat\alpha,\qquad
\widehat\lambda,\qquad
\widehat\rho
\]
from the finite associators and unitors, and prove that the triangle and pentagon remain valid after completion.

Pointwise validity of every finite diagram does not prove this.

## Three completion failures

### Continuity loss

The finite associators exist and satisfy every identity, but their operator norms or relevant projective seminorm constants diverge. No continuous associator acts on the completed restricted product.

### Authority drift

The finite associators are source-authorized at each cutoff, but the authority witnesses are incompatible under inclusion. The limit arrow exists formally yet has no durable source authorization.

### Frame loss

The cells remain continuous individually, but their inverses become ill-conditioned. A coherent finite rebracketing can then become asymptotically noninvertible in the completed topology.

The completion needs both forward and inverse control.

## Uniform cell frame

For each projective seminorm \(p_j\), require a controlled target seminorm \(p_{k(j)}\) and constants \(C_j,c_j>0\), independent of cutoff, such that
\[
p_j(\alpha_Xv)
\le
C_j\,p_{k(j)}(v),
\]
and
\[
p_j(v)
\le
c_j^{-1}\,p_{k(j)}(\alpha_Xv).
\]
Analogous bounds are required for unitors and any admitted braiding, duality, or dagger cells.

In a Hilbert realization, this reduces to uniform condition-number control:
\[
\sup_X\|\alpha_X\|\,\|\alpha_X^{-1}\|<\infty.
\]

For unitary phase associators the norm is automatically one, but type-fiber transport, changing source energy, and nontrivial target topology still require compatibility. A bare modulus-one scalar does not prove continuity between varying fibers.

## Compatibility with cutoff inclusions

The finite cells must be natural under completion maps:
\[
I_{X,X'}\alpha_X
=
\alpha_{X'}I_{X,X'}
\]
with the correctly parenthesized inclusion functors. The same is required for unitors and optional coherence cells.

If equality holds only up to a higher cell, that higher cell must itself be source-authorized and uniformly controlled.

## Completion of the \(H^3\) class

A finite coherent class \([\omega_X]\) must form a compatible inverse/direct system under cutoff. The completion cannot select representatives independently at each \(X\).

Three questions are distinct:

1. do the cocycles \(\omega_X\) transport compatibly?
2. does their class stabilize in the frozen coefficient system?
3. does a continuous limiting associator realize the limiting class?

Class stabilization without a continuous representative is insufficient. Continuous representatives with authority drift are also insufficient.

## Hostile: coherent phases with no continuous limit

Let each finite associator be multiplication by a phase in its own fiber and satisfy the pentagon exactly. Conjugate it through fiber identifications \(T_X\) whose condition numbers diverge:
\[
\alpha_X=T_X^{-1}U_XT_X,
\qquad
\|T_X\|\,\|T_X^{-1}\|\to\infty.
\]
Each finite \(\alpha_X\) is an isomorphism and all coherence diagrams commute. Yet the transported associators need not have a bounded limit on the completed topology.

This is completion failure without finite coherence failure.

## Optional braiding gate

If a braiding
\[
\beta_{a,b}:a\otimes b\to b\otimes a
\]
is source-authorized, verify both hexagons and uniform completion bounds. Symmetry further requires
\[
\beta_{b,a}\beta_{a,b}=1.
\]
No exchange law is introduced merely because scalar multiplication commutes.

## Optional dagger and duality gate

If dagger or reversal is admitted, require
\[
\alpha^\dagger=\alpha^{-1}
\]
in the appropriately reversed typing, together with unitors and evaluation/coevaluation compatibility. Reciprocal-sheet and Real involutions must be placed in this gate only if their source constructors actually supply the relevant anti-monoidal or dagger structure.

## Completion theorem target

> The finite arithmetic-analytic constructor system has the source-authorized monoidal coherence basis; its cells are compatible under cutoff; they extend to continuous, continuously invertible cells on the restricted-product completion; and all triangle, pentagon, and conditionally admitted hexagon or dagger identities persist.

This closes obligation one at the constructor level. Only then does the completed common nine-operation domain exist for the five-margin coercivity theorem.

## Next executable audit

For each finite cutoff, record:

- cell digests for associator and unitors;
- triangle and pentagon outcomes;
- optional hexagon/dagger outcomes;
- source-authority references;
- cutoff naturality;
- seminorm/operator bounds for cells and inverses;
- compatible \(H^3\) class data.

The completion audit then takes the uniform envelopes of those bounds and rejects continuity, authority, or frame loss before any Green margin is computed.
