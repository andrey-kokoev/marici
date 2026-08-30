# Falsification of two-tower exhaustiveness

## Claim under attack

The proposed exhaustion said that second-level closure is completely generated
by presentation invariance `I`, executable composability `C`, and their mixed
mate `M`.  It excluded higher-nerve coherence from counting as a falsifier.

That exclusion makes the exhaustion claim non-predictive: a higher coherence
class is precisely evidence that the proposed list is incomplete.

## Minimal hostile source

Let the source labels form the group

\[
G=\mathbb Z/2=\{0,1\}.
\]

Take presentation changes and executable compositions to be the group law.
Every object and every binary composite exists, and choose the binary mixed
mate to be the identity.  Thus

\[
I=C=M=1
\]

on every object and every composable pair.

Now equip triple composition with the normalized phase

\[
\omega(a,b,c)=(-1)^{abc}.
\]

It obeys the pentagon cocycle identity, so this is a coherent
source-authorized system.  But

\[
\omega(1,1,1)=-1.
\]

The phase cannot be removed by any normalized binary rephasing.  Indeed, for
every normalized two-cochain \(\beta\),

\[
(\delta\beta)(1,1,1)=1.
\]

Hence \(\omega\) represents the nonzero class in
\(H^3(\mathbb Z/2,U(1))\).

## Verdict

The strong exhaustiveness conjecture is false.  Pairwise invariance,
composability, and mate closure do not determine coherent triple pasting.
They require an additional associator class

\[
A=[\omega].
\]

Calling this a “higher-nerve issue” does not save the conjecture; it identifies
the missing constructor.  The corrected minimal architecture is therefore

\[
(I,C,M,A),
\]

where `A` may vanish in strict sectors but is not constructively guaranteed by
the first three entries.

This does not yet prove an infinite hierarchy.  It does prove that the number
of lower axes and pairwise fillers cannot by itself bound the next coherence
depth at two.  A source may carry a nontrivial ternary class even when every
binary test passes.

## Next risky conjecture

A defensible replacement is degree-sensitive:

> Closure through arity \(n\) consists of source-authorized cells through
> degree \(n\); closure at lower degrees does not imply vanishing of the next
> obstruction class.

Its next falsifier is constructive: find source hypotheses that force
\([\omega]=0\), rather than assuming strict associativity or declaring the
class out of scope.
