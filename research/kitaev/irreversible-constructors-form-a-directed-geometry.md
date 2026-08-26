# Irreversible constructors form a directed geometry

## Bounded question

What replaces reversible control distance when authorized constructors are
filters, channels, deletions, measurements, or software commands with no
physical inverse?

## Frozen semigroup model

Let \(X\) be a state space and let

\[
\mathcal G=\{G_1,ldots,G_m\}
\]

be a source-authorized constructor family closed under forward composition but
not assumed to contain inverses. Assign each generator a positive cost
\(c(G_j)>0\), extended additively to words.

Define the directed constructor distance

\[
d_\to(x,y)
=
\inf\{c(w):w(x)=y\}.
\]

If no authorized word sends \(x\) to \(y\), set the distance to infinity.

For stochastic or quantum operations, exact endpoint equality may be replaced
by a typed success condition, such as positive target probability or entry into
a target set. The directionality remains.

## Quasi-metric laws

The directed distance satisfies

\[
d_\to(x,x)=0
\]

and the triangle inequality

\[
d_\to(x,z)
\leq
d_\to(x,y)+d_\to(y,z)
\]

whenever the concatenated routes are admitted.

In general,

\[
d_\to(x,y)\neq d_\to(y,x),
\]

and one direction may be finite while the other is infinite. Distinct states
can also have zero separation if zero-cost identifications or quotients are
admitted; with strictly positive generator costs and discrete states this
degeneracy is absent.

Thus the natural object is an extended directed quasi-metric, not a metric.

## Directed robustness to failure

For a failure set \(F\), define

\[
r_\to(x,F)=\inf_{y\in F}d_\to(x,y).
\]

This is the least authorized forward cost of causing failure. It can be
infinite even when the ambient geometric distance to \(F\) is arbitrarily
small.

Recovery has a different cost:

\[
r_\leftarrow(x,F)
=
\inf_{y\in F}d_\to(y,x).
\]

A system can be easy to damage and impossible to restore, or hard to damage but
easy to reset once damaged. One scalar symmetric robustness score erases this
operational asymmetry.

## Reachability preorder

Define

\[
x\preceq y
\quad\Longleftrightarrow\quad
d_\to(x,y)<\infty.
\]

This is a preorder. Mutual reachability,

\[
x\sim y
\quad\Longleftrightarrow\quad
x\preceq y\text{ and }y\preceq x,
\]

is an equivalence relation. Its classes are the strongly connected components
of the constructor graph.

After quotienting by mutual reachability, the induced relation is a partial
order. The quotient DAG separates:

- reversible or cyclic capability inside components;
- irreversible information loss or resource descent between components;
- terminal sinks and forward-invariant barriers.

This factorization is more informative than asking whether each individual map
is algebraically invertible.

## Forward barrier theorem

For a source set \(A\), define its forward orbit

\[
\mathcal O^+(A)=\{w(x):x\in A,\ w\in\langle\mathcal G\rangle_+\}.
\]

If

\[
\mathcal O^+(A)\cap F=\varnothing,
\]

then failure is prohibited by the authorized semigroup and

\[
r_\to(A,F)=\infty.
\]

Conversely, the forward orbit itself is the smallest forward-invariant set
containing \(A\). It is therefore the canonical semigroup barrier certificate
when it misses \(F\).

No backward-invariance claim follows unless adjoint or inverse constructors are
separately admitted.

## Compensation is not inversion

Suppose \(G\) loses information and a later constructor \(C\) restores a chosen
visible output:

\[
R(C(G(x)))=R(x).
\]

This proves equality only after readout \(R\). It does not prove

\[
C\circ G=I.
\]

The hidden state, correlations, causal history, resource balance, or external
side effects may differ. A compensation action is an inverse only if equality
holds on the full typed state and every required interface.

This is the semigroup version of identical scalar effects with different
operator realizations.

## Minimal erasure witness

Let a state be a pair \((a,b)\), and let

\[
G(a,b)=(a,0).
\]

The visible readout \(R(a,b)=a\) is unchanged. A constructor that assigns a
default value,

\[
C(a,0)=(a,b_0),
\]

can restore one preferred representative but not the unknown original \(b\).

For every \(b\neq b_0\),

\[
C(G(a,b))\neq(a,b).
\]

The quotient value is compensated; the source state is not inverted. Any claim
of recovery must type which level is restored.

## Optical filter instance

An ideal polarizer acts by the trace-decreasing map

\[
\rho\mapsto P_\theta\rho P_\theta.
\]

After successful transmission, orthogonal input information has been removed.
Another polarizer can rotate the surviving ray and create nonzero transmission
through a later crossed analyzer, but it cannot reconstruct the discarded
component of the original field.

Therefore the three-polarizer effect is a forward route around a zero
transmission word, not reversal of the first projection. The directed costs
include transmission loss. A formal inverse of \(P_\theta\) on the full input
space does not exist.

This explains how an inserted constructor can make a previously dark endpoint
visible without making the earlier loss unreal.

## Quantum channel instance

Amplitude damping permits the population route

\[
|1\rangle\longrightarrow|0\rangle
\]

with positive probability. The reverse excitation is not supplied by the same
channel semigroup. Adding a preparation or pumping channel creates a new
authorized edge; it does not turn damping into a reversible constructor.

Likewise, a recovery channel that restores code-space populations need not
restore entanglement with a reference. Full quantum inversion must be tested by
the channel action on an extended reference system, not only on selected local
states.

## Software architecture instance

A deletion command followed by recreation of an object with the same API
fields may restore the current representation while losing:

- the original identity;
- audit history;
- causal links;
- external references;
- ordering metadata;
- or authorization provenance.

A saga compensation is therefore a forward constructor producing an acceptable
business state, not generally an inverse transaction. Idempotency, rollback,
and compensation are separate laws.

The SCC quotient of a workflow graph identifies which domain states are truly
mutually recoverable and which transitions are one-way.

## Information monotones

A source-derived monotone

\[
M(Gx)\leq M(x)
\]

for every authorized generator orders the semigroup flow. If source and target
require

\[
M(y)>M(x),
\]

then no forward word reaches \(y\) from \(x\).

Examples can include support dimension, distinguishability, free energy under a
declared thermodynamic model, fault budget, or retained provenance. The
monotone must be proved for the actual constructor family; importing a favorite
entropy or cost function supplies no authority.

A strict monotone also forbids nontrivial cycles between different levels and
therefore helps identify the partial order of SCCs.

## Irreversible order effects

For noncommuting semigroup generators,

\[
G_2G_1\neq G_1G_2.
\]

Order can open or close forward routes even though inverse commutator loops are
unavailable. The correct search is over admitted positive words, not the group
or Lie algebra generated after formally adjoining inverses.

In finite dimension, the reachable-support filtration for completely positive
maps is one exact positive-word method. In finite software state machines,
breadth-first reachability is another. Smooth irreversible systems require
reachable cones, Lie wedges, or semigroup methods appropriate to their typing.

## Directed first failure

There are two non-equivalent first events:

- first forward word reaching failure;
- first recovery budget at which return becomes possible.

The former prices vulnerability; the latter prices recoverability. They may
occur at different word lengths or one may never occur.

A complete resilience report should therefore state the ordered pair

\[
\bigl(r_\to(x,F),\ r_\leftarrow(x,F)\bigr)
\]

along with the state level on which recovery equality is tested.

## DPC: irreversible constructor explanation

The conjecture is:

> An irreversible capability or failure is explained by the directed orbit and
> monotones of the source-authorized constructor semigroup. Recovery claims must
> exhibit a return word on the full typed state; equality of a scalar or API
> projection establishes compensation only at that quotient.

The finite deterministic and CP-support instances are exact. The explanatory
gain is refusing to infer inverse authority from a restored appearance.

## Critics

### Some irreversible maps are invertible on a restricted image

Correct. The domain and image restriction must be typed. A partial inverse may
exist on one invariant subspace without restoring arbitrary source states.

### Noise can make every state mutually reachable

Correct at a positive-probability support level. Costs, probabilities, hitting
times, and robust margins still distinguish directions. Reachability preorder
alone is then too coarse.

### Continuous semigroups need more than graph reachability

Correct. The quasi-metric definition survives, but computing it requires the
appropriate optimal-control or large-deviation machinery.

### A compensation may be all the application requires

Correct. Then the quotient readout is the declared target. The error is calling
that success full inversion rather than quotient-relative recovery.

## Machine-readable certificate

```json
{
  "code": "directed_constructor_robustness",
  "source": "x",
  "target_or_failure": "F",
  "forward_cost": "finite | infinity",
  "recovery_cost": "finite | infinity",
  "forward_witness_word": ["..."],
  "recovery_witness_word": ["..."],
  "strong_component": "component id",
  "restored_level": "full_state | quotient_readout",
  "monotone_barrier": "M or null"
}
```

## Exact falsifiers

- Symmetric distance assumed for a constructor family without inverses.
- A compensation word reported as an inverse after checking only a quotient
  readout.
- A formal inverse or negative-time flow added to the authorized semigroup.
- A claimed forward barrier whose orbit intersects failure.
- A monotone that increases under an admitted generator.
- Local-state recovery called quantum channel inversion without a reference
  system test.
- Recreated software fields called rollback despite lost identity or external
  effects.
- A three-polarizer route described as reconstructing discarded input
  polarization.

## Deutschian explanation

Irreversibility is not merely expensive reversal. It changes the geometry from
an undirected space to a preorder of forward possibilities. Some states remain
inside cyclic islands; others lie downstream across one-way information-loss
edges.

An inserted constructor can create a new downstream route and restore a visible
output without undoing the past. The explanation is the complete directed word
and the level it restores, together with the monotone or missing return path
showing what remains lost.

## Claim boundary

This packet gives the exact abstract semigroup geometry and finite reachability
interpretations. It does not compute continuous stochastic hitting costs or
derive source monotones for a particular physical system.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was a robustness geometry that does not manufacture inverse
authority.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Irreversible constructors induce a directed quasi-metric and SCC partial
order. Compensation, quotient recovery, and full inversion now have distinct
types; optical, quantum, and software examples share the same carrier geometry.
