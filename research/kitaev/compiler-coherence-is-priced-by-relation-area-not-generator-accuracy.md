# Compiler coherence is priced by relation area, not generator accuracy

Owner: `marici.Kitaev`

## Question

If every defining constructor relation is implemented with small error, how
large can the disagreement become between two physical words representing the
same logical operation?

The amplification factor is the relation area of the comparison word. A
primitive relation error of size `epsilon` gives at best an error bounded by
`Area(w) epsilon` on a null word `w`. Uniform generator accuracy therefore
does not imply uniform compiler coherence when the required relation area
grows.

The bound is sharp. For an almost-commuting Weyl pair, the primitive
commutator phase is `phi`, while the rectangular word

\[
[x^m,z^n]
\]

accumulates the phase `mn phi`. In the standard presentation of the integer
lattice its relation area is exactly `mn`.

## Claim boundary

This packet concerns a frozen finite presentation, a bi-invariant metric on
the physical constructor group, and exact evaluation of words in the chosen
physical generators. It does not include stochastic cancellation, active
error correction during the word, or a compiler allowed to replace the word
by an independently synthesized shortcut.

The resulting bound is an adversarial coherence guarantee. A particular
noise model can behave better, but generatorwise calibration alone does not
prove that improvement.

## Presented logical target

Let the target logical group have finite presentation

\[
G=\langle S\mid R\rangle.
\]

Write `F(S)` for the free group on the generator set and

\[
\pi:F(S)\longrightarrow G
\]

for the quotient map.

Choose one accepted physical lift `U_s` for each generator. The assignment
extends uniquely to a homomorphism

\[
\widetilde U:F(S)\longrightarrow E
\]

into the physical constructor group `E`.

Logical relations need not close physically. For every defining relator `r`,
its residual is

\[
\Delta_r=\widetilde U(r).
\]

These residuals lie in the logical kernel only when the physical generator
lifts induce the correct logical generators.

## Relation area

A null word `w` belongs to the normal closure of `R`. Hence it can be written

\[
w
=
\prod_{j=1}^{A}
u_j r_j^{\varepsilon_j}u_j^{-1},
\]

where each `r_j` is a defining relator and

\[
\varepsilon_j\in\{-1,1\}.
\]

The relation area `Area_R(w)` is the least possible number `A` of relator
cells in such a factorization.

This is a property of the frozen presentation and comparison word. Word
length alone does not determine it.

## Relation-area theorem

Let `d` be a bi-invariant metric on `E`. Suppose every defining relation obeys

\[
d(\Delta_r,1)\leq\epsilon.
\]

For any null word `w`, choose a minimum-area factorization. Applying
`U-tilde` gives a product of conjugates of relator residuals. Bi-invariance
implies

\[
d\bigl(
\widetilde U(u_j)\Delta_{r_j}^{\varepsilon_j}
\widetilde U(u_j)^{-1},1
\bigr)
\leq
\epsilon.
\]

The triangle inequality then gives

\[
d(\widetilde U(w),1)
\leq
\operatorname{Area}_R(w)\epsilon.
\]

No commutativity of the physical residuals is needed for this upper bound.
Bi-invariance carries the estimate through conjugation.

## Dehn-function envelope

Define the presentation Dehn function

\[
\delta_R(n)
=
\max
\left\{
\operatorname{Area}_R(w):
\pi(w)=1,
\ |w|\leq n
\right\}.
\]

Every null comparison word of length at most `n` then obeys

\[
d(\widetilde U(w),1)
\leq
\delta_R(n)\epsilon.
\]

Thus the correct worst-case compiler coordinate is the product of local
relation error and relation-area growth.

## Comparison of two compiled words

Suppose words `a` and `b` represent the same logical operation. Then

\[
w=ab^{-1}
\]

is null in `G`. Bi-invariance gives

\[
d(\widetilde U(a),\widetilde U(b))
=
d(\widetilde U(ab^{-1}),1).
\]

Therefore

\[
d(\widetilde U(a),\widetilde U(b))
\leq
\operatorname{Area}_R(ab^{-1})\epsilon.
\]

This is the executable meaning of a coherent rewrite. Two logically equal
programs need not be physically close unless the relation proof connecting
them has controlled area.

## Sharp Weyl-pair family

Use the standard presentation

\[
\mathbb Z^2
=
\langle x,z\mid xzx^{-1}z^{-1}\rangle.
\]

Let physical unitaries `U` and `V` obey

\[
UV=e^{i\phi}VU.
\]

Their primitive commutator residual is

\[
UVU^{-1}V^{-1}=e^{i\phi}I.
\]

For integers `m,n`,

\[
U^mV^n=e^{imn\phi}V^nU^m,
\]

so

\[
U^mV^nU^{-m}V^{-n}
=
e^{imn\phi}I.
\]

The rectangular null word

\[
w_{m,n}=x^mz^nx^{-m}z^{-n}
\]

has relation area

\[
\operatorname{Area}_R(w_{m,n})=|mn|.
\]

Geometrically, a van Kampen diagram must tile an `m` by `n` rectangle with
commutator cells. Algebraically, the central commutator is crossed once for
each ordered generator pair.

With the geodesic phase metric and

\[
|mn\phi|\leq\pi,
\]

the residual distance is exactly

\[
d(\widetilde U(w_{m,n}),1)=|mn\phi|.
\]

The relation-area bound is therefore attained.

## Vanishing primitive error can still fail uniformly

Let a code-size or cutoff family have primitive relation errors

\[
\epsilon_L\longrightarrow0.
\]

Let the admitted compiler compare words of length at most `n_L`. A sufficient
uniform coherence condition is

\[
\delta_R(n_L)\epsilon_L\longrightarrow0.
\]

Primitive convergence alone is insufficient. For the lattice presentation,
choose square words with side `N_L`. Their length is `4N_L` and their area is
`N_L^2`. If

\[
N_L^2\epsilon_L
\]

does not tend to zero, long-word coherence can remain bad even though every
primitive commutator becomes accurate.

A hostile scaling is

\[
\epsilon_L=L^{-2},
\qquad
N_L=L.
\]

The primitive residual vanishes, while the square relation accumulates order
one phase.

## Exact versus approximate obstruction

Three cases must be separated.

### Nontrivial exact class

A fixed nontrivial cocycle, such as the Pauli four-group commutator `-I`,
prevents any strict section at that cutoff.

### Trivial class with inaccurate generators

An exact splitting exists elsewhere in the physical constructor set, but the
chosen generator implementations have small relation residuals. Reselection
or correction may remove them if physically authorized.

### Asymptotically trivial local residual

Primitive defects tend to identity, yet the admitted word family grows fast
enough to retain a nonzero global rewrite defect. This is a failure of uniform
compiler coherence, not necessarily a nontrivial finite-cutoff cohomology
class.

Conflating these cases hides whether the remedy is impossible, requires a new
constructor, or merely needs a stronger scaling bound.

## Relation syndrome

Defining relators act as coherent parity checks on the physical generator
lifts. A generator table supplies local ports; the relation residuals test
whether they compose according to the target semantics.

This resembles a syndrome map, with an important difference. A scalar
relation check sees only the image of the residual in the selected kernel
probe. Faithfulness requires enough kernel-sensitive probes to distinguish
every retained phase, record action, ancilla transformation, and corridor
holonomy.

Checking one scalar trace of every relator does not certify that the relator
operator is identity.

## Compiler design consequence

A robust compiler should emit not only a target word but also a bounded
coherence certificate:

1. the frozen generator presentation;
2. the physical lift of every used generator;
3. the operator- or channel-valued residual of every used defining relation;
4. the relation-area bound for every permitted rewrite;
5. the kernel probes used to certify residual identity;
6. the fault-spread and resource cost of any residual correction.

Normal forms help only when their construction and comparison areas are
bounded. Choosing a canonical word removes ambiguity at the output surface,
but downstream composition can still require large rewrites back to canonical
form.

## Application to topological constructors

Braids, fusion moves, flux ports, and code-deformation corridors are specified
by generator relations. Physical implementations must satisfy those relations
as coherent operations, not merely after scalar readout.

For the `D(S3)` endpoint programme, a microscopic lift of the two flux ports
would open the next audit:

- freeze a presentation of the target projective control group or admitted
  gate subgroup;
- compute physical residuals on its defining relations;
- identify the full invisible kernel of each residual;
- bound the relation area of synthesis and rewrite words;
- require residual size times area growth to remain controlled with code size.

Full endpoint-algebra span and full projective Lie rank provide none of these
coherence bounds.

## Hostile fixtures

### Accurate generators, inaccurate rectangle

Use an almost-commuting Weyl pair with tiny `phi`, then compare
`U^N V^N` with `V^N U^N`. The discrepancy is controlled by `N^2 phi`, not by
`phi` alone.

### Word-length bound substituted for area

Bound each primitive relation and multiply by word length. The square
commutator has length `4N` but relation area `N^2`.

### Canonical normal form without rewrite cost

Give every target a unique canonical word but omit the area needed to reduce a
product of two canonical words back to canonical form.

### Scalar relator closure

Verify the trace or one syndrome coordinate of every relation residual while
a traceless or record-valued kernel component remains.

### Fixed-depth evidence promoted to scalable compilation

Test all words up to one fixed length while the operational word budget grows
with code size or target accuracy.

### Stochastic cancellation used adversarially

Assume independent zero-mean primitive errors cancel without including that
noise law and its confidence bound in the compiler type.

## Falsifiers

- Generator accuracy is claimed to imply word-level coherence without a
  relation-area bound.
- A relator phase is multiplied only by final word length in a presentation
  with superlinear Dehn function.
- Equality of logical words is promoted to physical equality without
  evaluating their null comparison word.
- A vanishing primitive residual is promoted to a uniform limit without
  controlling the admitted word family.
- A canonical normal form is claimed to eliminate composition defects.
- Scalar relation probes are called jointly faithful without a kernel audit.
- A central phase calculation is applied to a noncentral record or holonomy
  residual.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies ordered words, rewriting cells, closed
comparison loops, and relation area. The coefficient lens supplies the metric
on physical residuals, their multiplication law, and the probes that decide
whether a kernel element is operationally visible.

The area amplification theorem is coefficient-independent once a
bi-invariant metric is supplied. The sharp Weyl phase and the distinction
between projective channel and coherent unitary control require the quantum
coefficient lens.

## Disposition

Approximate compositional control is governed by relation geometry. If every
defining relation closes within `epsilon`, a null comparison word closes only
within `Area(w) epsilon` in the worst case. The Weyl-pair rectangle attains the
bound and shows quadratic amplification from a single almost-commuting pair.

For a scalable physical compiler, primitive relation residuals must decay
faster than the relation area of the longest admitted rewrites grows. This is
the quantitative gate between finite projective controllability and uniform
executable coherence.

No checker, build, or Git operation was run for this research-only packet.
