# The eight-plus-four-plus-two-plus-one level tests whether pentagon coherence self-closes the recursion

Owner: marici.Kitaev

## Question

What appears at the recursive level after \(4+2+1\), and does it force another
independent coherence law or reveal that the hierarchy has already
self-closed?

## Claim boundary

The next balanced recursive implementation is

\[
(4+2+1)+(4+2+1)+1
=
8+4+2+1.
\]

It contains:

- eight leaf systems;
- four first-level bridges;
- two second-level bridges;
- one root bridge.

The total number of components is fifteen.

At the compressed level it is again two peer total complexes plus one
state-bearing meta-interface.

### Recursive cone form

Let \(T_L^{(2)}\) and \(T_R^{(2)}\) be two \(4+2+1\) total complexes. Let

\[
\Phi_3:T_L^{(2)}\to J_3,
\qquad
\Psi_3:T_R^{(2)}\to J_3
\]

be the root comparison maps. Then

\[
T^{(3)}
=
\operatorname{Cone}(\Phi_3-\Psi_3)[-1].
\]

A closed state retains:

- all eight leaf states;
- four first-level bridge states;
- two second-level bridge states;
- one root bridge state.

Any scalar root projection is therefore a severe shadow of the full total
state.

### Hierarchical common-mode cancellation

Let the eight leaf defect bits be \(x_1,\ldots,x_8\). Define first-level
syndromes

\[
s_1=x_1+x_2,\quad
s_2=x_3+x_4,\quad
s_3=x_5+x_6,\quad
s_4=x_7+x_8.
\]

Define second-level comparisons

\[
t_1=s_1+s_2,
\qquad
t_2=s_3+s_4,
\]

and root output

\[
r=t_1+t_2.
\]

Then nonzero defects can cancel at every scale. For example,

\[
(s_1,s_2,s_3,s_4)=(1,1,1,1)
\]

gives

\[
(t_1,t_2,r)=(0,0,0).
\]

All supervisory comparisons close while every local pair is inconsistent.

Therefore retaining only the highest surviving scalar at each level produces a
hierarchical common-mode kernel. A valid tower packet must retain lower-level
validity ports or prove independently that their common modes are impossible.

### Difference tree versus invertible transform

A tree that keeps only pairwise differences loses one common mode per
comparison component. It is not an invertible multiresolution transform.

An invertible Haar-like transform retains both:

- a difference coordinate;
- an average or reference coordinate.

Over \(\mathbb F_2\), sum and difference coincide, so a second independently
typed channel is still required to retain the missing common coordinate.

This clarifies the \(+1\) role. A comparator-only node does not preserve the
whole child state. A lossless compiler must pass both relational and reference
information upward.

### Does the next level require a new associativity axiom?

Not necessarily.

In a monoidal constructor theory, the associator

\[
\alpha_{A,B,C}:(A\otimes B)\otimes C
\Longrightarrow
A\otimes(B\otimes C)
\]

is constrained by the pentagon. Mac Lane coherence then implies that all
canonical composites of associators between any two bracketings agree.

Thus once the associator is natural and the pentagon holds, larger recursive
trees do not require one fresh associativity axiom at every depth. The
associativity tower self-closes.

The \(8+4+2+1\) level is therefore a test of closure, not automatically a new
rung.

### What can still prevent self-closure?

The coherence theorem applies only after the source establishes the relevant
monoidal hypotheses. New structure remains possible when:

- pair changes require braiding or symmetry not supplied by associators;
- associators are physical processes with resource- or path-dependent costs;
- the compiler is only partially defined;
- bridge states carry extra torsor labels not preserved by the monoidal
  equivalence;
- completion destroys uniform invertibility of comparison cells;
- the system is \(A_\infty\), higher, or anomalous rather than ordinary
  monoidal;
- physical implementations of canonically equal composites remain
  distinguishable by an authorized environment.

For braided theories, the hexagon joins the pentagon as a closure law.
For symmetric theories, the symmetry and involutivity laws are also required.

### Associahedral rotation

Binary bracketings of an ordered \(n\)-fold composite are vertices of the
associahedron. Elementary reassociations are its edges. Pentagon faces encode
the basic two-dimensional coherence.

At larger \(n\), higher-dimensional associahedra organize all reassociation
routes. In an ordinary monoidal category, the pentagon already forces their
canonical path independence.

In an \(A_\infty\) constructor theory, by contrast, the higher associahedral
cells carry genuine operations and homotopies. The same geometry then
organizes a continuing tower rather than a closed one.

Therefore the next-level question is not “is there an associahedron?” It is:

> Are its higher cells consequences of the pinned pentagon, or independent
> source constructors?

### Alternative pairings remain separately typed

Changing the balanced pairing of eight leaves can require permutations or
braidings. Associativity alone preserves leaf order.

Consequently:

- rebracketing belongs to associator coherence;
- exchanging leaves belongs to braid or symmetry coherence;
- changing the comparison incidence graph belongs to source-specific diagram
  equivalence.

A scalar output may ignore all three distinctions, but the constructor theory
must not.

### Spectral-sequence interpretation

The recursive comparison tree gives a filtration of the total complex by
depth. The associated spectral sequence asks:

1. which defects are removed or detected locally;
2. which child cohomology classes survive to the next supervisor;
3. which extension or bridge classes reach the root.

Self-closure means the sequence stabilizes with no task-visible unresolved
extension. Root scalar zero is not such a criterion.

### Minimal next-level falsifiers

The \(8+4+2+1\) hierarchy falsifies a proposed closure theorem if any of the
following occurs:

- all root and second-level outputs vanish while a retained first-level defect
  is nonzero;
- two canonical reassociation routes disagree despite a claimed natural
  associator and pentagon;
- equality of bracketings is inferred after a leaf permutation without an
  authorized braid or symmetry;
- algebraic coherence holds but comparison inverse costs diverge with depth;
- two bridge-state torsor classes are erased by every supervisory scalar while
  remaining distinguishable by a source-authorized context.

## Disposition

The next recursive level has two possible outcomes.

**Ordinary monoidal outcome:** pentagon, naturality, and the required braid or
symmetry laws force all higher canonical comparisons. The recursion
self-closes algebraically, though conditioning and physical realization remain
open.

**Higher or weak outcome:** bridge fillers retain independent associahedral
state, so larger polytopes carry new operations and the tower continues.

The decisive next audit is therefore not another parity calculation. It is to
take the pinned \(D(S_3)\) fusion constructors and ask whether the known
\(F\)-symbols and pentagon make every authorized \(8+4+2+1\) reassociation
canonical on the chosen task space. If yes, that is a genuine finite example
of unexpected self-closure. If not, the first differing route identifies the
next constructor cell.
