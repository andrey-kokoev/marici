# The next two-plus-one level is a four-plus-two-plus-one iterated homotopy limit

Owner: marici.Kitaev

## Question

What appears when the \(2+1\) coherence architecture is applied recursively to
two already formed \(2+1\) systems?

## Claim boundary

At the compressed categorical level, the next stage is again \(2+1\):

\[
T_L
\longrightarrow
J
\longleftarrow
T_R,
\]

where \(T_L\) and \(T_R\) are first-level homotopy pullbacks and \(J\) is a
meta-interface.

At the expanded implementation level it is

\[
4+2+1:
\]

- four leaf systems;
- two first-level comparison systems;
- one second-level comparison system.

Thus recursion generates the counts

\[
1,\ 3,\ 7,\ 15,\ldots,
\qquad
N_{k+1}=2N_k+1.
\]

The object is a binary coherence tree, not three symmetric towers.

### First-level objects

Let

\[
T_L
=
\operatorname{Cone}(f_1-g_1)[-1],
\]

\[
T_R
=
\operatorname{Cone}(f_2-g_2)[-1].
\]

A closed state of \(T_L\) is a triple

\[
t_L=(a_1,a_2,h_L),
\]

with

\[
d h_L=f_1(a_1)-g_1(a_2).
\]

Similarly,

\[
t_R=(a_3,a_4,h_R),
\]

with

\[
d h_R=f_2(a_3)-g_2(a_4).
\]

The child states contain both leaf data and the retained local bridge states.

### Second-level object

Let

\[
\Phi:T_L\to J,
\qquad
\Psi:T_R\to J
\]

be source-authorized meta-comparison maps. The root carries a state

\[
k\in J^{n-1}
\]

satisfying

\[
d_Jk=\Phi(t_L)-\Psi(t_R).
\]

The full recursive object is

\[
T_{\mathrm{root}}
=
\operatorname{Cone}(\Phi-\Psi)[-1].
\]

This is an iterated homotopy limit or iterated mapping cone.

The root is coherent only when:

1. both child cone states close;
2. their full typed images in \(J\) differ by an authorized boundary;
3. the root bridge state \(k\) is retained with its own ambiguity and
   observability.

### Scalar cancellation hostile model

Let four leaf defect bits be

\[
x_1,x_2,x_3,x_4\in\mathbb F_2.
\]

The first-level relative syndromes are

\[
s_L=x_1+x_2,
\qquad
s_R=x_3+x_4.
\]

If the root observes only

\[
r=s_L+s_R,
\]

then

\[
s_L=s_R=1
\]

gives

\[
r=0.
\]

The root reports closure while both child pairs are inconsistent.

This is not a computational accident. It is common-mode blindness one level
up: the root comparison detects disagreement between child syndromes, not
their absolute validity.

Therefore a meta-coherencer must not replace the child validity ports by their
difference alone.

### Retaining the whole tower packet

The faithful hierarchical output is at least

\[
(s_L,s_R,r),
\]

with the relation

\[
r=s_L+s_R.
\]

The root coordinate is redundant once both child syndromes are retained. Its
new value is not additional state reconstruction; it is a consistency check on
the inter-level compiler.

If the child bridge states \(h_L,h_R\) carry logical ambiguity, the root maps
must also specify whether they:

- preserve that ambiguity;
- compare it;
- quotient it;
- or ignore it.

A root that reads only \(s_L,s_R\) can be blind to distinct bridge torsor
classes even when every scalar syndrome vanishes.

### Three classes of hidden mode

The recursive architecture has at least three independent kernel mechanisms.

1. **Leaf common mode:** equal faults inside one pair leave its relative
   comparator silent.
2. **Meta common mode:** equal child defects cancel in the root difference.
3. **Bridge-state kernel:** distinct \(h_L,h_R\) have identical child outputs
   and are erased by \(\Phi,\Psi\).

These must be reported separately. Calling all three “top coherence residue”
loses their causal location.

### Interface conservativity

The root comparison should be conservative on every task-visible child class.
Algebraically, the first gate is

\[
\ker\Phi\cap H^*(T_L)_{\mathrm{task}}=0,
\]

and similarly for \(\Psi\), after accounting for classes intentionally
identified by the meta-task.

Quantitatively, the lower gain of the combined map

\[
(\Phi,\Psi)
\]

must remain positive on the task-localized quotient. Exact finite
injectivity is insufficient if this gain collapses under completion.

This is the recursive version of the kernel-reference theorem: the root must be
injective on precisely the child classes not already observed or quotiented
below.

### Iteration order and the next coherence law

There are two distinct ways to alter a four-leaf factorization.

First, one can rebracket a fixed ordered composite. Associators compare these
bracketings. For four ordered leaves there are five binary bracketings, and
their elementary reassociations form the pentagon.

Second, one can change which leaves are paired:

\[
((1,2),(3,4)),
\qquad
((1,3),(2,4)),
\qquad
((1,4),(2,3)).
\]

These are not related by associators alone. Changing pair membership can also
require permutations, swaps, or braidings, depending on the authorized
constructor theory.

Each admissible factorization produces an iterated cone. In a stable
categorical setting, homotopy limits over equivalent diagrams obey canonical
comparison theorems. But the physical/source compiler may not realize those
equivalences, and different resource costs or fault paths may remain.

Therefore the next comparison cells must be typed separately:

- associators for rebracketing fixed ordered composites;
- braids or symmetries for exchanging ordered leaves;
- source-specific intertwiners for changing the comparison diagram itself.

Conflating these operations would import constructor authority that the source
may not possess.

### Bicomplex and spectral-sequence rotation

The two directions of the hierarchy can be arranged as a bicomplex:

- horizontal differential: comparison within each peer pair;
- vertical differential: comparison between the child comparison systems.

The total differential combines them with the appropriate sign. Its square
vanishes only if the horizontal and vertical comparison laws commute up to the
declared cell.

A spectral sequence then separates:

1. defects killed locally at the child level;
2. child cohomology classes seen by the root;
3. extension data invisible until the total complex is assembled.

This is a principled way to locate the first failed rung. It also prevents a
root scalar cancellation from being mistaken for total exactness.

### Control-theoretic rotation

The expanded \(4+2+1\) system is a hierarchical regulator:

- four plants or local realizations;
- two local observers/controllers;
- one supervisory observer/controller.

A supervisor receiving only local residual differences can miss matched local
failures. It needs either the absolute local validity channels or a trusted
model excluding common-mode defects.

Hidden local controller states are analogous to bridge cohomology. Supervisory
stability does not imply internal-state observability.

### What the root actually adds

If every child state and syndrome is retained, the root does not necessarily
add a new independent scalar coordinate. It adds:

- a test that the two child compiler routes inhabit one comparison theory;
- a state \(k\) recording how they are joined;
- a platform for comparing alternative hierarchical factorizations;
- a new fault boundary between local and supervisory coherence.

This supports the view that a higher rung exposes new composition capabilities
rather than merely closing lower residue.

## Disposition

The next \(2+1\) level is best denoted

\[
(2+1)+(2+1)+1
=
4+2+1.
\]

Its audit packet must retain:

- all four leaf states or task-localized classes;
- both child bridge states;
- both child obstruction and ambiguity groups;
- root interface complex \(J\);
- maps \(\Phi,\Psi\);
- root bridge state;
- leaf, meta, and bridge-state kernels;
- alternative grouping comparisons;
- completion-stable lower gains.

The smallest decisive falsifier is

\[
(s_L,s_R,r)=(1,1,0).
\]

It proves that root closure alone does not imply child closure.

The highest-information next calculation is to compare the three pairings of
four leaves. If their iterated cones are algebraically equivalent but their
source-authorized implementations differ, the residual between those
factorizations is the first concrete associator of the \(2+1\) hierarchy.
