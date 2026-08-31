# G3 coercivity can control only the Xi defect complement, not the full G4 pencil

## Divisor compatibility

A G4 pencil whose determinant section is

\[
E(s)\xi(s)
\]

must fail invertibility at every nontrivial Xi zero.  Since such zeros lie in
the critical strip, no uniform positive lower bound can hold for the full G4
pencil on a parameter set containing them.

## Overcoercivity test

Suppose a positive Gram estimate gave

\[
\|C(s)\psi\|
\ge c\|\psi\|,
\qquad c>0,
\]

for the entire proposed G4 pencil throughout the closed strip.  Then

\[
\ker C(s)=0
\]

there.  If the index is zero, \(C(s)\) is invertible and its determinant
section is nowhere zero.  It cannot equal \(E\xi\) with \(E\) a unit.

Therefore applying all five strict G3 margins to the full divisor-bearing
pencil is a type error.

## Required defect splitting

The admissible local normal form is

\[
C(s)
\sim
\begin{pmatrix}
a(s)\tau_s&*\\0&C_Q(s)
\end{pmatrix},
\]

where:

- \(\tau\) is the theta Mellin dual section;
- \(a(s)\) is nowhere zero;
- \(C_Q(s)\) is the complement pencil;
- only \(C_Q\) is uniformly coercive across the seam.

At a simple Xi zero, the defect block loses rank while the complement remains
invertible.  At a zero of order \(m\), the local module length of the defect
block is \(m\).

## Correct role of the five margins

The retained arithmetic, analytic, glue, coherent-diagonal, and mixed margins
may prove:

\[
\|C_Q(s)q\|
\ge c_Q\|q\|.
\]

They may also control the triangular elimination that isolates the defect
line.  They cannot be imposed on the theta defect coordinate itself.

Thus “full vector before scalarization” means all retained physical ports of
the complement are present.  It does not mean that the divisor-bearing
cohomology line is assigned positive energy and eliminated.

## Projection must be source-derived

One cannot define the defect projection from the Riesz projection of a known
Xi zero.  The splitting

\[
H=i(\mathcal L_\theta)\oplus Q
\]

must come from the source incidence map \(i\), with a bounded projection
constructed before zero inspection.  Its reciprocal transport must preserve
the theta line and the complement.

Without this projection, a G3 estimate on an abstract positive Gram does not
identify which part of the G4 pencil it controls.

## Relation to the strict Cayley no-go

The same-sign Cayley--Weyl system applied its strict impedance gap to every
source direction, including the would-be defect line.  It was therefore
zero-free on the seam and could not carry Xi.

A valid architecture must instead have:

- a lossless or rectangular theta defect channel where the gap may close;
- a strictly passive/coercive complement controlled by G3;
- a divisor-preserving coupling between them.

## Revised G3-to-G4 arrow

The correct arrow is not a similarity between the full analytic return and a
positive G3 Gram.  It is a complement estimate after the chain map

\[
K_\tau\to C
\]

has split off the Xi defect block.  In symbols:

\[
G3
\Longrightarrow
C_Q^{-1}\text{ bounded},
\]

not

\[
G3
\Longrightarrow
C^{-1}\text{ bounded on the seam}.
\]

## Disposition

The five G3 margins remain useful only as complement-control candidates.  They
cannot close the full G4 pencil without contradicting the required Xi divisor.
The missing source defect projection and triangular normal form are now
explicit prerequisites.  No RH conclusion is authorized.
