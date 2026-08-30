# Shortest constructor route or invariant barrier

## Bounded question

Given source and target sectors and a frozen finite constructor family, what is
the minimum number of constructors needed to open a nonzero transition, and
what exact certificate proves that no such word exists?

## Frozen linear model

Let \(S\) be a finite-dimensional vector space. Let \(A\subseteq S\) be the
source subspace and let \(P_B:S\to B\) be the target projection. Let

\[
\mathcal G=\{G_1,\ldots,G_m\}
\]

be the finite source-authorized constructor family.

A word

\[
w=G_{i_k}\cdots G_{i_1}
\]

opens the route when

\[
P_BwA\neq0.
\]

No constructor outside \(\mathcal G\) is admitted by the theorem.

## Filtered reachable subspaces

Define

\[
R_0=A
\]

and recursively

\[
R_{k+1}
=
R_k+\sum_{G\in\mathcal G}GR_k.
\]

Then

\[
R_k
=
\operatorname{span}
\{wA:|w|\le k\}.
\]

This follows by induction: applying one generator to every word of length at
most \(k\) produces every word of length at most \(k+1\), while retaining
\(R_k\) includes shorter words.

## Constructor distance

Define

\[
d_{\mathcal G}(A,B)
=
\min\{k:P_BR_k\neq0\}.
\]

If no such \(k\) exists, set

\[
d_{\mathcal G}(A,B)=\infty.
\]

The equality

\[
P_BR_k\neq0
\]

holds exactly when at least one word of length at most \(k\) has nonzero
source-to-target action. If every individual word vanished after \(P_B\), every
linear combination would vanish as well.

Thus the first filtration stage meeting the target gives the exact shortest
constructor length.

## Route-or-barrier theorem

Exactly one of the following occurs.

### Finite route

For some \(k\),

\[
P_BR_k\neq0.
\]

Then a word of minimum length \(d_{\mathcal G}(A,B)\) is a finite witness.

### Invariant barrier

The ascending chain stabilizes at

\[
R_\infty
=
\operatorname{span}\{wA:w\in\langle\mathcal G\rangle\}.
\]

This subspace contains \(A\), is invariant under every \(G\in\mathcal G\), and
satisfies

\[
P_BR_\infty=0.
\]

It is therefore a complete prohibition certificate: every authorized word
keeps the source inside a target-dark invariant subspace.

Conversely, any subspace \(R\) satisfying

\[
A\subseteq R,
\qquad
GR\subseteq R
\]

for every authorized generator, together with

\[
P_BR=0,
\]

certifies that no authorized word opens the route.

The canonical \(R_\infty\) is the smallest common invariant subspace containing
the source.

## Finite stopping bound

The filtration can strictly increase at most \(\dim S-\dim A\) times. If

\[
R_{k+1}=R_k,
\]

then \(R_k\) is already invariant and no later stage can grow.

Therefore the finite algorithm either finds a route or certifies prohibition
after at most \(\dim S-\dim A\) strict dimension increases.

When \(A\) is initially target-orthogonal and \(B\) has positive dimension, any
finite route has a witness before the reachable filtration exhausts the
target-dark ambient subspace. The elementary uniform bound

\[
d_{\mathcal G}(A,B)
\le
\dim S-\dim A
\]

is sufficient for the declared audit.

## Dual barrier

Assume an inner product and an orthogonal target projector. Let

\[
D_\infty=R_\infty^\perp.
\]

Since \(R_\infty\) is invariant under every \(G\), its annihilator is invariant
under every adjoint \(G^*\). If the route is prohibited, the target subspace lies
inside \(D_\infty\).

Thus prohibition has two equivalent certificates:

- a forward-invariant source-reachable subspace missing the target;
- a backward-invariant dual subspace containing the target and annihilating all
  reachable source states.

This is the finite control-theoretic duality behind a selection rule.

## Weighted constructor cost

Assign each generator a positive source-authorized cost \(c(G)>0\), extended
additively to words. Define

\[
d_c(A,B)
=
\inf\{c(w):P_BwA\neq0\}.
\]

For a finite alphabet with costs bounded below away from zero, only finitely
many words lie below any fixed budget. A least-cost route therefore exists when
the feasible cost set is nonempty and closed under the declared discrete cost
typing.

The unweighted dimension bound does not by itself identify the least-cost word.
A longer word made from cheap generators can beat a shorter word containing an
expensive generator. Cost optimization must retain the filtered word data, not
only the stabilized reachable subspace.

## Unauthorized bridge no-go

If arbitrary linear constructors are allowed, every nonzero source and target
pair is trivially connected by a rank-one bridge. Such a bridge has no
explanatory force.

Route synthesis must optimize only over:

- the frozen constructor family;
- a source-derived enlargement declared before testing;
- or a parameterized admissible class with independently fixed constraints.

Adding the desired map after seeing the target is authority laundering, not an
explanation.

## Polarizer instance

Take the finite family

\[
\mathcal G_0=\{P_0,P_{\pi/2}\}.
\]

Starting from the horizontal ray, the reachable subspace remains horizontal
until an orthogonal projection kills it. No word has nonzero vertical output.
The horizontal source ray is the invariant barrier.

Enlarge the family in advance to

\[
\mathcal G_\theta
=
\{P_0,P_\theta,P_{\pi/2}\},
\qquad
0<\theta<\frac{\pi}{2}.
\]

Then

\[
P_{\pi/2}P_\theta P_0\neq0.
\]

The route has two angular transitions and one inserted constructor. The old
barrier is no longer invariant under the enlarged family because
\(P_\theta P_0\) leaves the horizontal ray.

This is how a source enlargement legitimately destroys a prohibition
certificate: it breaks the exact invariant used by the old theorem.

## Toric-code instance

Let the authorized generators be local Pauli operations of unit support cost.
On a code space, a nontrivial logical transition requires a Pauli word in the
normalizer but outside the stabilizer. The minimum support of such a word is the
code distance.

Thus code distance is a least-cost route-opening invariant:

- below the distance, local words cannot connect distinct protected logical
  sectors without detectable syndrome or leaving the code space;
- at the distance, a logical word supplies the first nontrivial protected
  transition.

The exact cost is support weight rather than sequential word length, so this is
the weighted group version of the route theorem. The source-authorized local
Pauli family and stabilizer quotient must remain frozen.

## Software-workflow instance

Let states be domain configurations and generators be admitted commands. A
missing event is route-deficient when some command word reaches a configuration
emitting it. It is prohibited when a preserved domain invariant places every
reachable configuration in an event-dark region.

The linear theorem does not automatically apply to nonlinear software state
machines. Its exact finite-state analogue uses breadth-first reachable sets
instead of linear spans. The same route-or-invariant logic survives, while the
coefficient machinery changes.

## Robust route quality

Nonzero reachability does not imply a useful route. For each budget \(B\), define

\[
\Gamma(B)
=
\sup_{c(w)\le B}\|P_BwP_A\|.
\]

The constructor distance asks when \(\Gamma(B)\) first becomes nonzero. Robust
capability asks whether it exceeds a declared lower margin. Executable control
also prices noise, loss, timing, locality, and fault propagation.

The lossy polarizer chain demonstrates the separation: algebraic route quality
can improve with refinement while physical transmission collapses.

## Critics

### Linear span can use unphysical cancellation

The span is used only for the zero/nonzero existence test. If its target
projection is nonzero, at least one constituent word has nonzero projection.
The span does not authorize implementing arbitrary linear combinations of
words.

### Positive-state reachability is not linear reachability

Correct. For channels, cones, or stochastic systems, one must compute the
appropriate reachable cone or set. The present theorem classifies structural
linear capability.

### A shortest word can be physically worst

Correct. Word length is one algebraic cost. Weighted cost and robust performance
are separate optimization layers.

### A barrier can disappear after adding constructors

Correct. Prohibition is relative to the frozen family. A legitimate enlargement
must identify which invariance law it breaks and why the new constructor is
source-authorized.

## Exact falsifiers

- A word shorter than the reported constructor distance with nonzero target
  projection.
- A claimed barrier subspace not invariant under every authorized generator.
- A target vector lying in the claimed reachable-dark barrier.
- Filtration growth after a declared fixed point \(R_{k+1}=R_k\).
- A prohibition claim made before exhausting the finite reachable filtration.
- A route synthesized only by an unauthorized rank-one bridge.
- Promotion of nonzero algebraic reachability to robust or executable control
  without a margin and cost theorem.

## Deutschian explanation

The explanation of a forbidden transition is the invariant barrier that makes
every authorized composite fail for the same reason. The explanation of a
route-deficient transition is the shortest source-authorized word that breaks
that barrier, together with the exact intermediate reachable subspaces it
creates.

These are dual and incompatible accounts:

- the witness word shows where the old route family becomes insufficient;
- the invariant subspace shows why no witness word can exist without enlarging
  the family.

The theory is hard to vary because any proposed new route must either remain
inside the barrier and fail or identify the precise generator that violates its
invariance.

## Claim boundary

This is an exact finite linear theorem. It does not grant physical authority to
the generators, identify a laboratory cost metric, solve positive-cone
reachability, or prove completion-stable control.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was a primal shortest-route witness or a dual invariant
barrier certificate without admitting arbitrary bridges.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The reachable filtration gives both the exact constructor distance and
the canonical smallest invariant barrier; toric code distance becomes its
weighted protected-sector instance. Positive and executable reachability remain
separate.
