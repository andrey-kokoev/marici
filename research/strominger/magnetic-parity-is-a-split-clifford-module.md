# Magnetic parity is a split Clifford module

Let

\[
\mathrm{Cl}_{1,0}
=
\mathbb R[\varepsilon]/(\varepsilon^2-1)
\]

act on the sheet packet by identifying \(\varepsilon\) with the
reflection-helicity involution \(Q\). Its primitive idempotents are

\[
e_E=(1+\varepsilon)/2,
\qquad
e_M=(1-\varepsilon)/2.
\]

They are exactly the electric and magnetic projectors. For a packet
\(u=A+\varepsilon B\),

\[
e_Eu=(A+B)e_E,
\qquad
e_Mu=(A-B)e_M.
\]

The individual parity kernels are annihilator ideals of the split algebra's
zero divisors. Joint algebraic faithfulness is the identity
\(e_E+e_M=1\).

## Two kernel mechanisms remain distinct

At a reflection-fixed orbit carrying only the trivial representation, the
magnetic ideal is absent. Multiplication by \(e_M\) is zero on the entire
orbit. This is the Clifford form of a tower zero column.

On a free orbit, both ideals exist. A collision circuit occurs when a nonzero
sheet combination lies in the complementary electric ideal and is therefore
annihilated by the magnetic projector. The selected ideal is available; the
source image is aligned away from it. This is not the fixed-orbit mechanism.

| Class | Clifford diagnosis |
|---|---|
| tower | selected ideal absent from the orbit module |
| collision circuit | selected ideal present, source vector lies in its annihilator |
| transport loss | kernel before the Clifford projection; excluded here |

## Exceptional circuits are visible in the complementary ideal

The exact sheet calculation gives, for both exceptional grade-two circuits,

\[
A(E_i)=B(E_i)\neq0.
\]

Consequently,

\[
M(E_i)=0,
\qquad
E(E_i)=2A(E_i)\neq0.
\]

Thus \(E_1\) and \(E_2\) predict a nonzero electric signal exactly where
the magnetic port reports zero. For \(E_1\),

\[
A(E_1)=\frac{40(z+\bar z)}{(1+z\bar z)^3}.
\]

The dependency-free exact Laurent-rational replay verifies seven gates for
\(E_1,E_2\): both sheets are nonzero, the sheets agree, and the electric sum
equals twice either sheet.

## Complementary-port theorem

Let the one-sheet map \(A:D\to W\) be injective, let
\(B:D\to W\) be its reflected partner, and define

\[
E=A+B,
\qquad
M=A-B.
\]

Over any coefficient ring in which \(2\) is not a zero divisor,

\[
E\vert_{\ker M}\text{ is injective},
\qquad
M\vert_{\ker E}\text{ is injective}.
\]

Indeed, if \(d\in\ker M\), then \(A(d)=B(d)\), hence
\(E(d)=2A(d)\). If also \(E(d)=0\), then \(A(d)=0\), and injectivity of
\(A\) gives \(d=0\). The other statement is symmetric.

This lifts the explicit \(E_1,E_2\) calculation to every magnetic kernel
class, including all towers and collision circuits. Once membership in
\(\ker M\) is known, the electric port alone separates its elements. No
simultaneous electric-magnetic acquisition is needed for that restricted
classification problem.

The qualification matters: this does not reconstruct an arbitrary element of
\(D\) from one parity port. Arbitrary-state reconstruction uses both ideals
and still requires a provenance-correct jointly executable refinement.

## The full source symmetry

Chart parity \(P\) and helicity conjugation \(\sigma\) commute and square
to one. Their algebra is

\[
\mathrm{Cl}_{1,0}\otimes\mathrm{Cl}_{1,0}
\cong
\mathbb R[\mathbb Z_2\times\mathbb Z_2]
\cong
\mathbb R^4.
\]

It is not \(\mathrm{Cl}_{2,0}\): two standard Clifford generators would
anticommute, whereas \(P\sigma=\sigma P\). The physical involution is the
diagonal product \(Q=P\sigma\), which combines the four primitive sectors
into two parity ideals.

## Operational boundary

Clifford completeness proves that the two ideal components reconstruct the
sheet state. It does not construct a jointly executable instrument.
Preparation provenance still requires a pullback, and acquisition
compatibility still requires a primitive joint refinement or separate
nondestructive-reuse authority.

Replay:

`python research/strominger/checkers/magnetic_split_clifford_checks.py`
