# A 3-crossed module tests whether volume comparison self-closes

Owner: marici.Kitaev

## Question

Does the 2-crossed-module rung self-close, or can two valid comparison routes
agree in every lower projection while differing by a task-visible fourth-level
constructor?

## Claim boundary

The published hostile-test object is a 3-crossed module

\[
K \xrightarrow{\partial_3} L
\xrightarrow{\partial_2} H
\xrightarrow{\partial_1} G.
\]

Arvasi, Kuzpinari, and Uslu prove that these are equivalent to simplicial groups
whose Moore complex has length three and model connected homotopy 4-types:

<https://arxiv.org/pdf/0812.4685>

This is a requirement language, not evidence that the toric-code or
\(D(S_3)\) compiler supplies a nontrivial \(K\)-level.

### The naive ladder is false

The next rung is not one new binary lifting. The published definition contains:

- actions of \(G\) on \(K,L,H\);
- actions of \(H\) on \(K,L\);
- an action of \(L\) on \(K\);
- the lower lifting \(H\times H\to L\);
- three distinct liftings \(L\times L\to K\);
- two distinct liftings \(H\times L\to K\);
- one lifting \(L\times H\to K\);
- eighteen compatibility laws in the cited convention.

Thus \(K\) compares several inequivalent ways in which lower Peiffer liftings,
actions, and boundaries interact. One scalar fourth-dimensional residual would
erase which mixed composition failed.

### Residual sectors

The homotopy sectors are

\[
\pi_1=G/\operatorname{im}\partial_1,
\qquad
\pi_2=\ker\partial_1/\operatorname{im}\partial_2,
\]

\[
\pi_3=\ker\partial_2/\operatorname{im}\partial_3,
\qquad
\pi_4=\ker\partial_3.
\]

Adjoining \(K\) can repair part of the former \(\pi_3=\ker\partial_2\), because
boundaries from \(K\) identify some old \(L\)-comparisons. At the same time,
closed \(K\)-constructors create the new sector \(\pi_4\).

Going up therefore does two things:

1. closes some residue from the preceding rung;
2. may expose ambiguity among the repairs used to close it.

### Smallest survival fixture

For an abelian group \(A\), take

\[
A\longrightarrow1\longrightarrow1\longrightarrow1
\]

with trivial boundaries, actions, and liftings. Then

\[
\pi_1=\pi_2=\pi_3=1,
\qquad
\pi_4=A.
\]

With \(A=C_2\), every edge, face, and volume-comparison output is identical,
yet one fourth-level logical bit survives. This falsifies universal
self-closure after the 2-crossed-module rung. It does not prove that a physical
source realizes the fixture.

### Repair and self-closure fixtures

For

\[
A\xrightarrow{\mathrm{id}}A\longrightarrow1\longrightarrow1
\]

one has

\[
\pi_3=0,\qquad\pi_4=0.
\]

The \(K\)-constructor fills the old \(L\)-residue without introducing a new
closed ambiguity.

More generally, for a homomorphism \(f:K\to L\) of abelian groups with trivial
lower groups,

\[
\pi_3=\operatorname{coker}f,
\qquad
\pi_4=\ker f.
\]

This gives the sharp finite shadow:

- surjectivity closes every old \(L\)-residue;
- injectivity prevents a new \(K\)-logical sector;
- bijectivity gives complete closure;
- failure of surjectivity leaves an old obstruction;
- failure of injectivity creates a new ambiguity.

The next rung self-closes in this shadow exactly when \(f\) is an isomorphism.

### What the abelian fixture cannot prove

The fixtures establish logical possibility but erase why seven lifting types
are required. A genuine nonabelian audit must distinguish:

- alternative \(L\)-\(L\) comparisons;
- left and right mixed \(H\)-\(L\) comparisons;
- compatibility with the lower \(H\times H\to L\) lifting;
- transport under the \(G,H,L\) actions.

A candidate with only an undifferentiated map into \(K\) is merely the
chain-complex shadow. It cannot certify 3-crossed-module coherence.

### Geometric and compiler interpretation

The next closed geometric audit composes four-dimensional comparison cells
around a 5-simplex boundary. Its explicit ordered word is
convention-sensitive and must be derived from a frozen simplicial group.

The safest compiler starts from the Moore complex

\[
NG_3/\partial_4(NG_4\cap D_4)
\longrightarrow NG_2\longrightarrow NG_1\longrightarrow NG_0.
\]

For Moore length three, the higher term vanishes. The Peiffer liftings are then
derived from simplicial degeneracies and commutators instead of fitted to a
desired cancellation.

Closure through this rung requires:

1. every task-visible old \(L\)-residue lies in
   \(\operatorname{im}\partial_3\);
2. \(\ker\partial_3\) is trivial or task-invisible;
3. all distinct lifting types satisfy one frozen convention;
4. comparison is constructor-faithful, not merely scalar-faithful;
5. the 5-simplex composition is coherent;
6. the source authorizes every action, boundary, and lifting.

For the full algebraic sector, the simple condition is

\[
\ker\partial_2=\operatorname{im}\partial_3
\quad\text{and}\quad
\ker\partial_3=1,
\]

together with the complete 3-crossed-module laws.

### Hostile falsifiers

Reject at the first applicable case:

1. either consecutive boundary composite is nontrivial;
2. an action fails to respect a boundary;
3. distinct lifting types are collapsed into one scalar;
4. \(\pi_3\) is declared closed despite a surviving quotient class;
5. a nonzero element of \(\ker\partial_3\) is silently contracted;
6. the abelian shadow is presented as nonabelian coherence;
7. a 5-simplex word mixes conventions;
8. a physical \(K\)-port is inferred from algebraic availability;
9. scalar cancellation substitutes for constructor equality;
10. the hierarchy continues without a task-visible residual.

## Disposition

The hostile test defeats universal self-closure: the pure fixture

\[
C_2\to1\to1\to1
\]

has trivial lower sectors but nontrivial \(\pi_4\).

It does not authorize a fourth physical rung in the current programme.
Neither the toric-code carrier nor the \(D(S_3)\) endpoint algebra has yet
exhibited two source-derived fourth-dimensional constructors that agree at
\(G,H,L\) while remaining operationally distinct.

The strongest result is therefore the repair criterion

\[
\pi_3=\ker\partial_2/\operatorname{im}\partial_3,
\qquad
\pi_4=\ker\partial_3.
\]

A fourth coefficient level is earned only when it repairs a named,
task-visible \(L\)-residue. It self-closes when that repair is exhaustive and
has no task-visible kernel.

The next bounded move should freeze one small nonabelian simplicial group of
Moore length three, derive all seven lifting types, and test its 5-simplex
closure rather than append a fifth coefficient group.
