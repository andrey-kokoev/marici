# The Three Sewing Roles Form an A3 Path Algebra, Not a Veronese Generator Space

## Correction to the six-channel proposal

The conditional Segre--Veronese gate remains mathematically correct, but
Aspect's recursive architecture does not presently supply its hypothesis.
The three labels in the sewing problem are stage types, not exchangeable axis
generators.

The native diagram is

```text
source -> operator symbol -> spectral output.
```

Its elementary incidence algebra has:

- three identity cells;
- two adjacent arrows;
- one length-two composite.

This is the six-dimensional path algebra of the directed chain `A3`,
equivalently the algebra of upper-triangular `3x3` matrices.

## Exact algebraic distinction

Let `e_0,e_1,e_2` be the vertex idempotents, `a:0->1`, `b:1->2`, and
`c=ba:0->2`. These six elements form a basis. The arrow radical satisfies

\[
J=\langle a,b,c\rangle,
\qquad J^2=\langle c\rangle,
\qquad J^3=0.
\]

The algebra is noncommutative: a vertex idempotent can act nontrivially on an
incident arrow from one side and annihilate it from the other. By contrast,
Strominger's Cartan algebra

\[
\operatorname{Sym}(H_1)/(q)
\]

is commutative, and its three degree-one directions are permutation-compatible
axis generators. The two algebras cannot be identified merely because both
start from a three-component presentation.

## Correct six-channel carrier

If every stage carries a two-dimensional sector pair, the finite carrier is

\[
V=V_0\oplus V_1\oplus V_2,
\qquad \dim V_i=2,
\qquad \dim V=6.
\]

The source operator is then naturally a representation of the `A3` quiver
with dimension vector `(2,2,2)`. In a stage-adapted basis, admissible transport
is block triangular and retains the two adjacent maps and their composite.
It need not factor as `A tensor B`, and the three stage blocks need not be
permutable.

This explains the `3+2+1` part structurally: it is the nerve of a compositional
chain, not a Veronese Hilbert count.

## Where Veronese can still enter

The even Veronese algebra may govern a second, independent grade or control
index inside each stage. The correct combined object would then be a module
carrying two commuting actions:

The path algebra `C A3` governs directed stage transport. Independently, the
Cartan algebra

\[
\mathcal C=\operatorname{Sym}(H_1)/(q)
\]

governs symmetric grade change.

Only a source-derived interchange law can justify combining them as a tensor
product action. In that case Veronese manages repeated control-grade changes,
while the `A3` path algebra manages source-to-symbol-to-output composition.
Neither replaces the other.

An associated-graded Veronese interpretation is another possibility. It would
require a filtration whose extension data records the directed arrows and
whose graded pieces acquire the symmetric Cartan action. The extension data
must remain explicit; passing to the associated graded cannot silently erase
the moving-seam defect.

## Consequence for Aspect's `6x6` matrices

The six requested source basis functions should first be typed by their
actual source construction. If they form three stage-local pairs, the first
matrix gate is preservation of the stage flag and both directional
composites, not rank-one Kronecker reshuffling.

The Segre--Veronese gate from ledger 3634 becomes applicable only if a second
theorem identifies the three-dimensional factor with exchangeable Cartan
directions. Without that theorem, rejecting a valid block-triangular source
map for failing pure-tensor factorization would be a false negative.

## Falsifiers and promotion gate

Promote the Veronese interpretation only if the source supplies all of:

1. a common three-dimensional generator object at the three positions;
2. permutation covariance of those generators;
3. the unique quadratic relation `q`;
4. compatibility of `q` with forward and reverse sewing;
5. interchange between grade action and directed stage transport.

Until then, the native theorem is the `A3` path-algebra typing with a possible
independent Veronese module action.
