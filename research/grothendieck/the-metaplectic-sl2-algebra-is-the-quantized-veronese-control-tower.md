# The Metaplectic sl2 Algebra Is the Quantized Veronese Control Tower

## Theta-native three-generator system

Let `Q` denote multiplication by the additive coordinate and let `P` denote
differentiation, with

\[
[P,Q]=1.
\]

The three quadratic operators

\[
E=\frac{Q^2}{2},
\qquad
F=-\frac{P^2}{2},
\qquad
H=\frac{QP+PQ}{2}
\]

are source-native metaplectic controls. They generate dilation, quadratic
phase, and Fourier-conjugate quadratic transport. Direct Weyl-algebra
calculation gives

\[
[H,E]=2E,
\qquad
[H,F]=-2F,
\qquad
[E,F]=H.
\]

Thus the missing three-control object is not an invented copy of Strominger's
axis space. It is the standard `sl2` triple already carried by the theta
phase-space representation.

## Veronese as the classical symbol

Replace `Q,P` by commuting classical coordinates `q,p`. The principal symbols
are

\[
e=\frac{q^2}{2},
\qquad
f=-\frac{p^2}{2},
\qquad
h=qp.
\]

They obey

\[
h^2+4ef=0.
\]

This is a nondegenerate complex conic after a linear change of coordinates.
Its coordinate ring is the even Veronese algebra of the two-dimensional
phase-space spinor `(q,p)`.

Therefore Strominger's Cartan conic and the theta metaplectic triple are not
identified by a dimension coincidence. They are related by symbol and
quantization:

```text
commuting quadratic symbols -> Veronese conic
Weyl quantization             -> metaplectic sl2 operators.
```

## Quantum correction

The classical zero relation is replaced by a central Casimir value. In the
polynomial oscillator representation,

\[
\Omega=H^2+2H+4FE
\]

acts as

\[
\Omega=-\frac34 I.
\]

The fixed scalar is the ordering correction. It is not a defect to subtract;
it records that the operator tower is a quantization of the conic rather than
the commutative coordinate ring itself.

This is the precise extra datum that the raw Veronese model omits. At symbol
level there is one quadratic relation. At operator level there are the three
`sl2` commutators and one fixed central character.

## Corrected A3 interchange theorem

Let source, operator-symbol, and spectral-output stages carry compatible
metaplectic modules. A stage arrow intertwines the full control algebra if it
commutes with `E,F,H`. Hence the earlier six-square compiler survives in
quantized form:

- three `sl2` generators;
- two adjacent `A3` arrows;
- six primitive intertwining squares.

Commutation with the generators forces commutation with the universal
enveloping algebra. The long stage composite follows automatically. The
Casimir value must agree at all three stages; otherwise a map can commute at
the classical-symbol level while failing to lift to the quantum source.

## Why the seam remains decisive

On the full Schwartz space the metaplectic operators are canonical. The RH
construction uses half-line tails, endpoint traces, and completed reciprocal
sewing. Restricting `P` or `P^2` to a half-line produces boundary terms.
Consequently, the stage arrows must include the moving-seam channel before
the six commutators are evaluated.

A symbol-level commuting diagram is insufficient. The exact target is a
boundary-bearing metaplectic intertwiner from the prime-labelled stable source
through the completed readout to the spectral section.

## Explanatory gain

The recent structures now fit without conflation:

- `A3` explains directed source-to-symbol-to-output composition;
- the Veronese conic explains the classical three-control symbol;
- `sl2` explains its noncommutative theta quantization;
- the Casimir records the unique ordering correction;
- six generator squares test the distributive law with directed transport.

This is the sought post-factum rigid structure behind the apparent `6x6`
coincidence.

## Falsifier

The route fails if the completed source arrows do not intertwine any one of
`E,F,H`, if their Casimir characters differ, or if the commutator closes only
after erasing the boundary/seam channel. A convenient finite oscillator matrix
with the right abstract commutators is not source authority.
