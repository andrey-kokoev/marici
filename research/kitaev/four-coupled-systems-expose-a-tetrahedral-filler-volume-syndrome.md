# Four coupled systems expose a tetrahedral filler-volume syndrome

Owner: marici.Kitaev

## Question

When does adding a fourth coupled system reveal a genuinely new coherence rung,
rather than merely adding redundant triangle checks to the three-system torsor
model?

## Claim boundary

For ordinary abelian vertex-frame data, it does not reveal a new rung. If all
triangle curvatures vanish on a filled simplex, the edge differences integrate
to vertex frames up to common mode.

A new obstruction appears only when the triangle fillers themselves retain
typed choices.

Let the four vertices of a tetrahedron be \(0,1,2,3\). Suppose every triangular
boundary admits a filler. Let

\[
a_{ijk}\in\mathbb F_2
\]

label the \(C_2\)-torsor choice of filler on oriented face \(ijk\). The
tetrahedral residual is

\[
\Omega_{0123}
=
a_{123}+a_{023}+a_{013}+a_{012}.
\]

Over \(\mathbb F_2\), orientation signs coincide. With general abelian
coefficients, the alternating boundary signs must be retained.

The value \(\Omega_{0123}\) is the coboundary

\[
\Omega=\delta a.
\]

It asks whether the four face fillers assemble into a coherent volume
3-cell.

### Facewise closure does not imply volume closure

Each triangular face can have:

- matching boundary paths;
- an authorized invertible filler;
- zero edge-level triangle syndrome.

Nevertheless, the four chosen face fillers can have

\[
\Omega_{0123}=1.
\]

Then no authorized tetrahedral 3-cell can contract their combined boundary in
the strict \(C_2\) model.

This is the smallest exact witness in which every lower face is individually
closed but the assembled surface retains a higher obstruction.

### Gauge invariance

Let an edge-level 1-cochain \(b_{ij}\) change the local references used to label
face fillers. Then

\[
a\longmapsto a+\delta b.
\]

The tetrahedral residual is unchanged:

\[
\delta(a+\delta b)
=
\delta a+\delta^2b
=
\delta a.
\]

Thus \(\Omega\) cannot be repaired by changing edge frames. It is a genuine
higher relational syndrome.

A face-reference change not induced from edge data can change the individual
\(a_{ijk}\), but its admissibility must itself be typed as a 3-dimensional
gauge constructor. One cannot erase \(\Omega\) by silently expanding the gauge
group.

### Detection is again not correction

A nonzero tetrahedral syndrome detects an odd number of flipped face reports.
It does not identify the erroneous face. All four single-face flips produce
the same residual.

Overlapping tetrahedra can localize face faults through a higher syndrome
complex, but a preferred correction still requires decoder authority,
reliability weights, or a trusted reference.

The hierarchy therefore repeats:

- triangle syndrome detects inconsistent edge comparisons;
- tetrahedral syndrome detects inconsistent face fillers;
- neither syndrome chooses a repair representative.

### Minimal exact complex

Let

\[
C^1
\xrightarrow{\delta_1}
C^2
\xrightarrow{\delta_2}
C^3
\]

be simplicial cochains on the tetrahedron with \(\mathbb F_2\) coefficients.

- \(C^1\) labels six edges.
- \(C^2\) labels four faces.
- \(C^3\) labels the one volume.
- \(\delta_2\delta_1=0\).

If \(a=\delta_1 b\), then \(\Omega=\delta_2a=0\). Conversely, on the full
contractible tetrahedron, every face assignment with \(\Omega=0\) lies in the
image of \(\delta_1\). Hence zero volume syndrome is exactly the integrability
condition for the face labels in this finite abelian model.

Removing the interior 3-cell changes the topology. A zero or nonzero boundary
class can then be retained as surface data rather than declared fillable. The
Carrier geometry determines whether the volume filler is present; the
coefficient lens determines its value.

### Ordered nonabelian successor

For nonabelian filler automorphisms, the four face transports must be composed
in a specified order with whiskering and associators. The residual is not the
unordered product of four labels.

The appropriate law has the form

\[
\Omega
=
A_4A_3A_2A_1
\]

after transporting all face automorphisms to one common base and parenthesized
frame. Changing that frame conjugates \(\Omega\) or acts through a higher
gauge law.

Pentagon coherence is the canonical example: several associator fillers
between the same composite boundary must themselves compose consistently.
The scalar \(C_2\) tetrahedron is only its parity shadow.

### Why this is not Pfaffian volume

The tetrahedral syndrome is a coboundary obstruction. It tests whether face
fillers integrate to a volume cell.

A Pfaffian is instead the top exterior coefficient of an alternating bilinear
form. It tests nondegeneracy of pairwise relational directions.

Both first become naturally four-indexed in small examples, but their laws are
different:

- tetrahedral coherence uses an oriented boundary sum or ordered face product;
- Pfaffian volume uses signed pair partitions.

They can vary independently. A system can have \(\Omega=0\) and degenerate
skew volume, or \(\Omega\ne0\) with a nondegenerate pairwise skew form.

Any proposed unification must derive a map between these structures; matching
arity four is not evidence.

### Self-closure criterion

The scalar \(C_2\) tetrahedron self-closes at this rung when:

1. every required face filler is typed;
2. \(\Omega=0\);
3. the full tetrahedral 3-cell is authorized;
4. no task-visible choice of 3-cell remains after the declared localization.

Condition 2 alone is insufficient. It proves existence of an integrable face
assignment in the finite complex, not physical authority for the volume
constructor or uniqueness of its filler.

If multiple 3-cells fill the same tetrahedral boundary, they form the next
torsor and the tower continues.

## Disposition

The fourth system has now separated two cases that were previously blurred.

If the previous rung retains only abelian edge differences, triangles already
give complete integrability on a simplex and the fourth vertex adds
redundancy.

If triangle fillers retain their own torsor choices, the tetrahedral
coboundary is a genuinely new, gauge-invariant higher syndrome.

The exact first falsifiers are:

- changing \(\Omega\) by an edge-reference transformation;
- claiming facewise closure implies \(\Omega=0\);
- inferring a preferred bad face from one nonzero tetrahedral syndrome;
- treating \(\Omega=0\) as authority for a physical 3-cell;
- identifying tetrahedral coboundary with Pfaffian volume solely because both
  first appear naturally on four labels.

The next experiment should compare two tetrahedra sharing a face. It will test
whether overlapping volume syndromes can localize one corrupted face and
whether their shared-face cancellation is the first finite model of
higher-dimensional fault-tolerant coherence.
