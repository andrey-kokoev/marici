# Attachment shape does not determine attaching degree

## Conjecture under attack

After the local-incidence conjecture failed, the surviving proposal added a
global attachment grammar.  Its strongest finite reading is:

> The atomic constructors and the declared shapes of their global attachments
> determine the resulting invariant object up to authorized presentation.

This is still false if attachment shape records only which cells meet and not
the actual attaching morphism.

## Minimal hostile family

Take one vertex, one loop, and one two-cell.  Attach the two-cell to the loop
with integral degree \(m\).  Every member of the family has the same:

- number and dimensions of cells;
- source and target incidence;
- globular boundary shape;
- local executable loop;
- declaration that one two-cell fills that loop.

The cellular boundary is nevertheless

\[
\partial_2=[m].
\]

Therefore

\[
H_1\cong\operatorname{coker}[m]
\cong\mathbb Z/m
\]

for nonzero \(m\).  The cases \(m=1\) and \(m=7\) have identical attachment
shape but respectively no residue and a seven-valued residue.

The shape declaration does not determine orientation, winding, multiplicity,
or coefficient transport.  Those live in the attaching morphism.

## Falsification verdict

Atomic theory plus unweighted global attachment shape is not explanatory.  It
can predict that a relation is imposed, but not which quotient or torsion
class the relation creates.

The smallest missing constructor is:

```text
AttachingMorphism
  source_boundary
  target_skeleton
  coefficient_system
  oriented_degree_or_matrix
  support
  source_authority
```

## Magnetic connection

The preferred magnetic cocircuit has affine frame determinant \(-7\).  Its
Smith residue is therefore locally modeled by a degree-seven attaching map.
This explains why the observable is a quotient residue rather than seven
parallel modes.

This is a structural analogy, not yet an identity of topological spaces.  A
literal identification would require a source-derived chain map from the
magnetic boundary matrix to the cellular model.  What is already exact is the
shared Smith presentation:

\[
\mathbb Z\xrightarrow{\times7}\mathbb Z
\longrightarrow\mathbb Z/7.
\]

## Revised Deutschian conjecture

> A source-authorized atomic theory, exact attaching morphisms with coefficient
> and orientation data, and separately typed completion laws determine the
> finite pasting object up to source-authorized equivalence.  An explanation
> must additionally state the first degree at which attaching data or an
> obstruction-vanishing theorem is absent.

The next falsifier is no longer a different shape.  It is two inequivalent
objects with the same complete attaching matrices and admitted equivalences
but different executable probes or completion behavior.
