# Explanation is a double functor, not a single state model

## Two independent directions

The current programme contains two kinds of composition.

1. Interventions act within one declared source system.
2. Source transformations compare different systems, presentations, scales,
   or regimes.

A state-space realization models the first direction. A natural family of
realizations models the second. Explanation requires their compatibility.

## Source--intervention double category

Let \(\mathbb S\) be a double category whose:

- objects are source-typed systems;
- vertical arrows are admitted interventions or dynamics;
- horizontal arrows are source transformations, comparisons, compilers, or
  changes of explanatory level;
- squares witness compatibility between source transport and intervention.

A typical square is

\[
\begin{array}{ccc}
S & \xrightarrow{f} & S'\\
\downarrow u & \Downarrow\alpha & \downarrow u'\\
T & \xrightarrow{g} & T'.
\end{array}
\]

The cell \(\alpha\) states whether applying \(u\) and then transporting agrees
with transporting and then applying \(u'\), strictly or through a declared
coherence map.

## Explanation functor

Let \(\mathbb R\) be a double category of realizations, state transformations,
module-preserving comparisons, and commuting or coherent squares.

A candidate explanation is a double functor or appropriately weak double
functor

\[
\mathcal E:\mathbb S\longrightarrow\mathbb R.
\]

It must preserve:

- vertical composition of interventions;
- horizontal composition of source transformations;
- identity arrows in both directions;
- square composition;
- the interchange law, strictly or by predeclared coherence.

This packages intervention closure, family naturality, modular transport, and
presentation invariance in one object.

## Why an ordinary functor is insufficient

A vertical-only model can predict every command on one plant while giving no
law for perturbation, version change, coarse-graining, or neighbouring source
instances.

A horizontal-only family can transport static invariants across source
instances while providing no ordered intervention dynamics.

The missing explanatory content is exactly the family of squares relating the
two.

## Failure residue

For one square, define the strict comparison residual schematically by

\[
\Theta_\alpha
=
\mathcal E(g)\mathcal E(u)
-
\mathcal E(u')\mathcal E(f)
\]

when the target coefficient type is additive.

In a Product or Endo lens, the comparison must instead use the corresponding
multiplicative or ordered composition law. A subtraction residual is not
universally typed.

A nonzero residual can mean:

- source transport does not preserve the intervention;
- a coherence cell is missing;
- an anomaly or boundary term is present;
- the proposed source comparison is invalid;
- or the implementation fails the abstract law.

The residual becomes explanatory only when its target type was declared before
it was computed.

## Role of the three lenses

The double Carrier specifies what can compose vertically, horizontally, and
by squares. The coefficient lens specifies how the realized effects compose.

- Sum evaluates square defects additively.
- Product evaluates scalar gain, phase, or multiplicative anomaly.
- Endo retains ordered state transformations and noncommuting square data.

The lower lenses are shadows of the Endo-valued double functor only when the
projection maps preserve both compositions and the coherence cells.

## Toric-code instance

For a fixed periodic lattice:

- vertical arrows include Pauli-string actions and local repair composition;
- horizontal arrows include lattice automorphisms and authorized changes of
  cell presentation;
- squares assert covariance of boundary, syndrome, repair, and logical-loop
  action.

The cellular boundary laws are horizontal-natural under lattice
automorphisms. The Pauli coefficient realization adds ordered vertical action.
Primal--dual intersection supplies the scalar phase seen when vertical
operations cross.

Decoder selection is not a square forced by this double category. Adding it
requires a noise/dynamics enlargement of the source-intervention object.

## Software instance

For a software system:

- vertical arrows are commands, retries, state transitions, and repairs;
- horizontal arrows are versions, migrations, compilation, and deployment
  transformations;
- squares express semantic preservation of commands across those changes.

A compiler correctness theorem is a square. A migration that preserves stored
values but changes retry semantics fails an Endo square even if its Sum
payload readout agrees.

## Strictness warning

Demanding strict commutation everywhere is usually too strong. Boundary
residues, phases, asynchronous scheduling, and compiler refinements may require
pseudofunctorial coherence cells.

Weakening is legitimate only when the cell type, composition law, and higher
coherence were declared independently. Adding one custom cell for every
failed square recreates the lookup-table problem one dimension higher.

## Falsifiers

- Only vertical behaviour is modeled; source transport is absent.
- Only horizontal covariance is modeled; interventions are absent.
- Sum agreement is used to assert an Endo square.
- A failed square receives a post-hoc coherence cell.
- Horizontal and vertical composition work separately but violate
  interchange.
- A claimed compiler or duality moves module ports without transporting their
  intervention meaning.
- Strictness is imposed where the source contains a typed anomaly.
- Weak coherence is made unrestricted and therefore unfalsifiable.

## Revised conjecture

A mature explanation is a problem-resolving, proof-carrying double functor
from source variation and intervention into typed realization. Its
load-bearing content is the prospective set of commuting and coherently
noncommuting squares, together with their failure signatures.

The three lenses evaluate the same double Carrier at different levels of
order sensitivity; none supplies the source or physical implementation of the
arrows it evaluates.
