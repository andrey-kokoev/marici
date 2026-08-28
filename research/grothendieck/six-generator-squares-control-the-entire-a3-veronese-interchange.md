# Six Generator Squares Control the Entire A3--Veronese Interchange

## The combined object

Let the directed sewing stages form the chain

```text
V_0 -> V_1 -> V_2
```

with adjacent maps `f_01` and `f_12`. Suppose every `V_i` is a graded module
over Strominger's Cartan algebra

\[
\mathcal C=\operatorname{Sym}(H_1)/(q),
\qquad \dim H_1=3.
\]

The directed stage algebra and the symmetric grade algebra coexist precisely
when both adjacent maps are graded `C`-module homomorphisms.

## Finite generation theorem

Choose a basis `x,y,z` of `H_1`. It is sufficient to test

\[
f_{i,i+1;l+1}C_{i,l}(g)
=C_{i+1,l}(g)f_{i,i+1;l}
\]

for:

- the two adjacent arrows `i=0,1`;
- the three generators `g=x,y,z`;
- every grade at which the source construction is defined.

These are six families of elementary interchange squares. Once they commute,
interchange for every ordered monomial follows by induction. Since the
generators commute, it then depends only on the symmetric tensor. Since each
stage action already factors through the relation `q`, the equality descends
to the even Veronese quotient.

The long stage composite requires no new primitive check:

\[
(f_{12}f_{01})C_0(g)
=f_{12}C_1(g)f_{01}
=C_2(g)(f_{12}f_{01}).
\]

The same calculation iterates to every Cartan monomial. Thus the two adjacent
arrows, three generator directions, and one quadratic relation generate the
entire cross-coherence tower.

## Concrete Veronese chart

Use the conic presentation

\[
\mathcal C\cong
\mathbb C[u^2,uv,v^2],
\]

with generators

\[
x=u^2,\qquad y=uv,\qquad z=v^2
\]

and relation

\[
xz-y^2=0.
\]

The grade-`l` piece has basis

\[
u^{2l},u^{2l-1}v,\ldots,v^{2l}
\]

and dimension `2l+1`. Multiplication by `x,y,z` shifts the exponent by zero,
one, or two. This gives an exact integer model for testing the six squares.

## Hostile defect

A stage map may preserve the dimensions and the directed `A3` flag while
failing one generator square. For example, changing one weight inside the
middle-grade map makes transport depend on whether grade change occurs before
or after stage movement. The discrepancy is a typed interchange anomaly; it
cannot be repaired by checking only the final long composite.

This is the precise place where the Veronese proposal can fail without
invalidating either the `A3` tower or the Cartan tower separately.

## Application to completed theta sewing

The theorem does not yet identify theta control operators with the Cartan
generators. It supplies the finite compilation target if such operators are
derived:

1. construct three source-native grade-changing controls on each of source,
   operator-symbol, and spectral-output stages;
2. prove the common quadratic relation at every stage;
3. test the six adjacent-arrow generator squares before scalar compression;
4. obtain long-composite and higher-grade coherence formally.

The moving-seam channel must be included in the stage maps. If it is omitted,
a commuting quotient diagram does not establish interchange for the completed
source object.

## Meaning

The correction and the Veronese insight now coexist cleanly. The stage index
is directed `A3`; the grade index is symmetric Veronese. Their relationship is
neither identification nor analogy but a distributive law witnessed by six
generator squares.

## Falsifier

One nonzero commutator on any adjacent arrow and any of the three source
generators falsifies the tensor-product/interchange architecture. Agreement
only after the long composite, scalar readout, or cutoff limit is insufficient.
