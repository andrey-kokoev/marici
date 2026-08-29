# An integral lattice needs a determinant functor, not a chosen order

## Correction

An integral source lattice can preserve primitivity and expose torsion, but it
does not by itself choose a Real orientation. If two source labels are
independent and equally authorized, exchanging their presentation order changes

\[
e_1\wedge e_2\longmapsto e_2\wedge e_1=-e_1\wedge e_2.
\]

Thus a chosen ordered basis merely relocates the orientation torsor into the
presentation convention.

## Correct object

Let \(C_X^\bullet\) be the finite, typed integral source complex at cutoff
\(X\). Its determinant line is

\[
\operatorname{Det}(C_X^\bullet)
=
\bigotimes_j
\left(\bigwedge^{\mathrm{top}} C_X^j\right)^{(-1)^j}.
\]

The needed source law is a determinant functor carrying:

1. the typed parity of every source port;
2. the Knudsen--Mumford comparison for every authorized exact sequence;
3. the Koszul sign for every authorized interchange;
4. a primitive integral generator compatible with cutoff extension;
5. a Real structure whose fixed ray agrees with that generator.

The ordering problem is then not suppressed. It is absorbed by declared
coherence maps whose signs are determined by grades.

## Finite obstruction

Take a rank-two degree-zero lattice with basis \(a,b\). The swap has
determinant \(-1\), so no orientation can be invariant under it.

Now place \(a\) in degree zero and \(b\) in degree one. The determinant line
is \(a\otimes b^{-1}\). Its comparison under a typed interchange is governed
by the determinant-functor convention, not by an untyped permutation of a
single basis.

Therefore one of the following must hold:

- the source actually distinguishes an order;
- the label swap is not an authorized symmetry;
- the determinant functor supplies a graded comparison cell;
- or no canonical orientation has been constructed.

## Theta/Tate gate

The theta/Tate programme must not report a source-fixed determinant sign from
prime ordering alone. It must construct the finite source complex and answer:

- which prime, seam, endpoint, square, and archimedean ports occupy which
  degrees;
- which label permutations are authorized;
- what comparison sign each authorized permutation induces;
- whether cutoff inclusions preserve a primitive generator through the exact
  determinant-line comparison;
- whether the completion retains that compatible system.

The smallest falsifier is an authorized source relabelling whose induced
determinant comparison is \(-1\) while all scalar readouts remain unchanged.

## Decisive conclusion

Saturation solves the integral primitivity problem. A determinant functor solves
the presentation problem. Both are required before an integral source anchor
can orient the Real determinant line.

