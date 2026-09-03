# Forward–backward adjunction and mate coherence

## Question

Is backward attachment transport derived from forward realization by adjunction, and what is the exact boundary of that explanation?

## Claim boundary

This packet treats functors, profunctors, finite posets, and finite discrete categories. It does not assert that every attachment correspondence has an adjoint realization functor.

## Companion and conjoint

For a functor

\[
F:\mathcal C\to\mathcal D,
\]

its companion and conjoint profunctors are

\[
F_*(c,d)=\operatorname{Hom}_{\mathcal D}(Fc,d),
\qquad
F^*(d,c)=\operatorname{Hom}_{\mathcal D}(d,Fc).
\]

They satisfy

\[
F_*\dashv F^*
\]

inside the bicategory of profunctors.

Suppose an attachment lift profunctor has the form

\[
P_f(E,D)=\operatorname{Hom}(F_fE,D).
\]

If \(F_f\) has a right adjoint \(f^*\), then

\[
P_f(E,D)
\cong
\operatorname{Hom}(E,f^*D).
\]

Thus backward pullback is the representable shadow of the conjoint exactly on the adjoint sector.

## Composition and mates

For realization arrows

\[
R\xrightarrow{f}S\xrightarrow{g}T,
\]

left adjoints compose in realization order:

\[
F_gF_f.
\]

Right adjoints compose in the reverse categorical direction:

\[
f^*g^*.
\]

A forward comparison

\[
\alpha:F_gF_f\Longrightarrow F_{gf}
\]

has a mate

\[
\alpha^*:(gf)^*\Longrightarrow f^*g^*.
\]

If \(\alpha\) is invertible, its mate is invertible and may be reversed to give the usual pullback compositor. Beck–Chevalley is the assertion that the relevant mate of a realization square is invertible.

## DPC cycle

### Governing conjecture

Forward and backward coherence are adjoint shadows on the companion/conjoint sector, while general correspondence transport is more primitive. The mechanism is hard to vary: adjunction converts hom-sets and sends forward comparison cells to direction-reversed mates.

### Rivals

1. Every backward attachment functor is the right adjoint of a forward realization functor.
2. Every lawful attachment correspondence secretly comes from an adjoint pair.
3. Forward and backward compositors are unrelated structures.
4. Adjunction and mates explain the representable sector, while deletion, branching, and some representable pullbacks remain outside it.

### Risky consequences

The conjecture predicts exact reversal of right-adjoint composition in a finite poset. It also predicts a representable backward functor between discrete categories that has no left adjoint, plus a branching relation that is lawful under relational composition but is not representable by a backward function.

### Falsification attempt

The checker constructs two monotone maps between finite chains, verifies each adjunction exhaustively, and verifies that the right adjoint of their composite is the reverse composite of right adjoints. It then enumerates every candidate forward function for a constant backward function between two-object discrete categories; none satisfies the adjunction hom-set equation. A branching relation remains composable but fails unique representability.

### Residual

The finite checks do not implement general 2-cell mate formulas or noninvertible Beck–Chevalley squares. The displayed mate statement is a standard direct consequence of the adjunction hom-set bijections.

### Disposition

Rivals 1, 2, and 3 are rejected. Rival 4 is provisionally retained. Adjoint pullback is explanatory but restricted; profunctor correspondence remains the general transport object.

## Explanation

The opposite directions are not independent coincidences. A right adjoint necessarily reverses the order of a composite. Coherencers cross from the forward side to the backward side by the mate construction. The explanation fails exactly if the correspondence lacks a companion/conjoint representation or the required adjoint.

## Disposition

Use adjunction and mate calculus on the representable adjoint sector. Retain correspondence-valued transport outside that sector; do not fabricate forward realization functors from backward or branching data.
