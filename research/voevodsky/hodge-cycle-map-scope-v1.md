# Hodge iteration 1: cycle-map scope and a descent test for retained coherence

## Scoped result

The `scope-and-cycle-map` obligation is completed as a **typed interface definition and elementary linear descent lemma**. No candidate variety, obstruction or packet-to-algebraic-cycle construction is supplied. The classical Hodge conjecture remains open.

The substantive restriction is:

> A retained-coherence reader that distinguishes two presentations of the same cohomology class cannot itself be the proposed class-level Hodge obstruction. Killing its invisible kernel is necessary, and supplies a unique factor only on the image of the presentation map—not automatically on the whole Hodge-class space.

This does not invalidate witness-sensitive identity research. It identifies a different task interface: Hodge asks existence of some algebraic preimage, not faithful reconstruction of an arbitrary retained witness.

## Source/type/map dictionary

Fix smooth projective X over C and p. All cycle and cohomology coefficients below are rational.

| Object | Meaning | Admitted structure |
| --- | --- | --- |
| Z | Z^p(X)_Q: finite formal sums of codimension-p algebraic subvarieties | Addition and arbitrary rational coefficients, including negative ones |
| R_rat | Subspace of rational equivalences | Quotient relations; not an assumption that every homologically trivial cycle is rationally trivial |
| CH | CH^p(X)_Q = Z/R_rat | Rational cycle classes modulo rational equivalence |
| H | Hdg^p(X,Q) | Rational cohomology classes of type (p,p) |
| P | A possible source-bound retained packet library | Not constructed for algebraic cycles in this iteration |
| R_packet | Free rational linearization Q[P] | A formal arena for the selected Q-linear obstruction route, not a claim that all packet readouts are linear |
| V | An independently defined rational obstruction target | Not yet supplied |

The standard cycle-class map factors as

    Z --q--> CH --cl--> H.

Existence of this map, its rational-equivalence invariance and its Hodge type are imported standard cycle-class facts. We are not deriving them from packet primitives. Hodge asserts surjectivity of cl. It does not assert injectivity, choose a canonical section, or recover cycle histories.

A possible packet construction would additionally supply

    R_packet --a?--> Z --q--> CH --cl--> H
         |                              |
         F?                             O?
         |                              |
         +------------> V <-------------+

Here a assigns an actual algebraic cycle to each licensed packet. Its generation, coverage and compatibility are still the open `packet-coherence-dictionary` obligation. Define s=cl q a only conditionally on a being supplied. No surjectivity of a or s is assumed.

At this scope we admit finite cycle sums, rational scaling, rational-equivalence comparison, cohomology comparison and explicitly mapped transport along isomorphisms. Broader pull/push operations must be separately typed with their hypotheses and degree shifts. No finite library of divisor constructors is identified with all algebraic cycles.

## Descent lemma

Let s:R->H and F:R->V be linear maps of rational vector spaces. Then

\[
\exists!\,\bar F:\operatorname{im}(s)\to V,\qquad
F=\bar F\circ s
\quad\Longleftrightarrow\quad
\ker s\subseteq\ker F.
\]

**Proof.** If F factors, then s(r)=0 implies F(r)=Fbar(0)=0. Conversely define Fbar(s(r))=F(r). If s(r)=s(r'), their difference lies in ker(s), so F(r)=F(r'). Thus the definition is independent of the chosen lift. Linearity follows from linearity of s and F. Every element of im(s) has such a lift, so any factor must agree with this one. No Hodge surjectivity is used.

The unique domain is **im(s)**. Extending to all of H generally requires extra data and need not be unique. A presentation library covering only some cycles can have an image even smaller than im(cl).

Applied first to Z->CH, the criterion is invariance under rational equivalence. Applied to CH->H, it additionally requires vanishing on homologically trivial Chow classes. The first descent does not imply the second.

## Exact representative-sensitive hostile

The checker uses this formal rational model:

\[
s(x,y,z)=(x+z,y+z,0),\qquad
\ker s=\mathbb Q(-1,-1,1).
\]

The two presentations (0,0,1) and (1,1,0) have the same class (1,1,0). The reader F_bad(x,y,z)=z gives different values. It therefore cannot descend to cohomology.

By contrast,

\[
F_{\rm good}(x,y,z)=2x-y+z
\]

kills the kernel and factors on im(s) as (a,b,0) -> 2a-b.

Two full-target extensions are

    O0(a,b,c)=2a-b,
    O7(a,b,c)=2a-b+7c.

They agree on every presented input and disagree on (0,0,1). Even a zero source reader admits both zero and 7c as extensions. Knowledge of every source readout does not by itself select an obstruction away from its image.

These matrices are **not** asserted to be the cycle map of a selected variety. In particular, the third coordinate is not being declared a nonalgebraic Hodge class. Doing so would simply assume the missing conclusion.

The exact checker also tests the kernel/factor equivalence on all 729 pairs consisting of a 2x2 matrix with entries {-1,0,1} and a one-row reader with entries {-1,0,1}. Every accepted factor is checked by direct matrix multiplication. This is a bounded regression for the written general proof, not a replacement for it.

## Annihilation puts a stronger constraint on packet readers

If a packet really produces an algebraic cycle and O annihilates **all** algebraic cycle classes, then

\[
F=O\circ\operatorname{cl}\circ q\circ a=0
\]

on every such packet.

A nonzero coherence defect on a genuine algebraic witness would therefore falsify the claimed necessity/annihilation theorem. A defect that only says one selected packet construction fails would reject that implementation, not the existence of another algebraic cycle representative.

Similarly, defining O by choosing a complement of im(cl) cannot constitute a noncircular construction of a detector. Establishing a nonzero complement already establishes failure of Hodge. We need a detector defined independently on H, not an arbitrary continuation of source-image data.

The earlier Q4 control makes the positive boundary concrete: its two algebraic plane classes span the entire middle Hodge space, so a linear O killing both is zero there. Keeping primitive/non-divisor coherence data does not change that fact.

## What is resolved and what remains

Resolved at this bounded scope:

- the cycle/Chow/Hodge and hypothetical packet types;
- the distinction between surjectivity, equivalence and witness recovery;
- admissible rational operations and the retained-kernel policy;
- a general linear descent lemma and exact representative/extension hostiles.

Not resolved:

- a source-generated packet realization of arbitrary algebraic cycles;
- a candidate X,p,alpha;
- a genuine obstruction O on its full Hodge space;
- vanishing on all algebraic cycles or nonzero detection;
- any mathematical verdict about the Hodge conjecture.

The two next executable nodes are `literature-boundary-audit` and `packet-coherence-dictionary`. The latter is now unblocked by this scope result and the existing controls. It must supply actual algebraic meaning, not just another metadata inventory.

## Reproduce

    python research/voevodsky/checkers/check_hodge_cycle_map_scope.py

Contract: `research/conjecture_net/contracts/hodge-cycle-map-scope.v1.json`.
Receipt: `research/voevodsky/results/hodge-cycle-map-scope-v1.json`.

Nine checks pass. Verification consists of the written elementary proof and exact rational finite controls; no proof-assistant certification or new geometric cycle-class theorem is claimed.
