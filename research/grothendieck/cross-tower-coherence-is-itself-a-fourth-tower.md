# Cross-tower coherence is itself a fourth tower

## Operator correction

The previous architecture treated input, output, and control as three towers
and their required compatibility as one horizontal cell. That truncation is
not justified. The comparison has its own successive typing and coherence
requirements.

The fourth tower is not a fourth physical sector. Its objects are
relationships among the other three towers.

## Rung 0: common comparison carrier

For every finite cutoff (X), construct a typed defect object
(mathcal D_X) capable of retaining:

- integer and prime labels;
- valuation grade;
- endpoint and seam incidence;
- operator or quadratic-form structure.

Scalar determinant lines are quotients of this carrier, not the carrier
itself.

## Rung 1: independently sourced lifts

Lift the input and boundary data into the common carrier:

\[
\widetilde W_X:C_X\longrightarrow\mathcal D_X,
\qquad
\widetilde B_{X,s}:Y_{X,s}\longrightarrow\mathcal D_X.
\]

The operator-valued boundary lift (K_{p,s,X}) belongs here. Equality of
scalar traces does not establish this rung.

## Rung 2: state-level comparison cell

On the source-admissible state pullback, construct a comparison or homotopy

\[
\eta_{X,s}:
\widetilde W_X(c)
\Longrightarrow
\widetilde B_{X,s}(y).
\]

This is stronger than declaring their difference zero after scalarization.
The cell must identify every typed component and expose any central anomaly.

## Rung 3: naturality under source transport

For every authorized source operation (T), the comparison must commute with
transport:

\[
T_{\mathcal D}\eta_{X,s}
=
\eta_{X,T(s)}T_{\mathrm{state}}.
\]

This rejects a comparison fitted only in one frame, one Clark sheet, or one
endpoint presentation.

## Rung 4: cutoff and braid coherence

For (X\subset Y), restriction must preserve the entire comparison cell, not
only its scalar value. For two incomparable authorized operations, the two
transport paths must agree up to a named higher cell whose residual is typed.

Thus the fourth rung contains both cutoff naturality and repair-compiler braid
coherence.

## Rung 5: completion descent

The compatible finite comparison system must descend through restricted
product completion. Contracting partners, boundary coordinates, and anomaly
cells may not escape to infinite norm or disappear into a scalar quotient.

This is where finite exactness can fail to become completed exactness.

## Independence of the rungs

The hierarchy is not decorative. Small countermodels separate its levels.

### Scalar equality without operator lift

The matrices

\[
A=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
B=\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]

have equal trace but act on different channels. Scalar agreement does not
produce rung 1.

### One-cutoff equality without naturality

A comparison may hold at cutoff (X) and be extended at (Y) by a new
component whose restriction changes the old port. Rung 2 does not imply rung
4.

### Finite coherence without completion descent

The exact complexes

\[
\mathbb C\xrightarrow{\varepsilon_X}\mathbb C,
\qquad
\varepsilon_X\longrightarrow0,
\]

have finite contractions but no uniformly controlled limiting contraction.
Rung 4 does not imply rung 5.

## Geometric interpretation

The three physical towers form the vertices of a triangle. Pairwise
comparison lifts are its edges. The triple compatibility is its filled face.
Transport, cutoff, and completion coherences are higher cells above that
face.

The operator-valued boundary lift is therefore not the whole missing theorem.
It is the first nontrivial arrow of the fourth tower.

## Current RH target

The desired terminal composite is:

\[
\text{completed triple coherence}
\Longrightarrow
(2\operatorname{Re}s-1)N_s=0,
\qquad
N_s>0.
\]

The next finite task remains construction of the prime-two operator lift, but
its acceptance contract now includes all higher destinations: comparison,
transport naturality, cutoff coherence, and completion descent.

