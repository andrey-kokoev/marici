# Cohomological classification of compositor twists

## Question

Which automorphism-valued changes of attachment compositors are removable choices of representatives, and which obstruct strictification?

## Claim boundary

This packet treats a group of system-map labels acting trivially on a central abelian automorphism group. Noncentral coefficients require nonabelian coherence rather than the ordinary second cohomology group used here.

## Setup

Let \(G\) label composable system-map symmetries and let \(A\) be a central automorphism group of the representing attachment. A normalized compositor twist is a function

\[
c:G\times G\to A,
\qquad c(e,g)=c(g,e)=0.
\]

The pentagon is exactly the cocycle equation

\[
c(g,h)+c(f,gh)=c(f,g)+c(fg,h).
\]

Changing each representative comparison by a normalized one-cochain \(b:G\to A\) changes the twist by

\[
(\delta b)(f,g)=b(g)+b(f)-b(fg).
\]

Consequently, coherent twists modulo representative gauge form

\[
H^2(G,A)=Z^2(G,A)/B^2(G,A).
\]

The zero class is strictifiable by a gauge. A nonzero class is a residual obstruction: every member is coherent, but none can be gauged to the identity compositor.

## DPC cycle

### Governing conjecture

The cohomology class \([c]\), rather than the raw twist or pointwise representative, is the exact invariant of central compositor coherence under changes of presentation. The mechanism is hard to vary: the pentagon defines cocycles and representative changes define precisely coboundaries.

### Rivals

1. Every coherent compositor can be strictified by choosing different representatives.
2. Distinct raw cocycles always describe distinct attachment semantics; quotienting by coboundaries discards physical structure.
3. Only witness counts or pointwise automorphism groups matter, so the composition group contributes no obstruction.

### Risky consequences

With trivial \(C_2\) coefficients, the conjecture predicts different behavior for two composition groups despite identical coefficient and pointwise attachment data:

- \(H^2(C_3,C_2)=0\), so every coherent twist is gauge-removable;
- \(H^2(C_2,C_2)\cong C_2\), so one coherent class is not strictifiable;
- distinct cocycles in the same coboundary orbit must be classified together.

Rival 1 predicts no nonzero class for \(C_2\). Rival 2 predicts one class per cocycle. Rival 3 predicts no contrast between \(C_2\) and \(C_3\).

### Falsification attempt

The checker exhaustively enumerates every normalized two-cochain and one-cochain for both finite groups, filters cocycles by every pentagon equation, constructs all coboundaries, and computes translation orbits. It also verifies that the nontrivial \(C_2\) cocycle is coherent and absent from the coboundary set.

### Residual

The result assumes trivial central action. It does not classify noncentral attachment automorphisms, varying coefficient systems, or bicategorical modifications not expressible as group cochains.

### Disposition

All three rivals are rejected in the finite fixtures. The cohomological classification is provisionally retained for central trivial-action compositor twists: strictification exists exactly for the zero class.

## Computed classification

For \(C_2\) with \(C_2\) coefficients, there are two normalized cocycles, one normalized coboundary, and two cohomology classes. The cocycle with \(c(1,1)=1\) represents the nonzero obstruction.

For \(C_3\) with the same coefficients, there are four normalized cocycles and four coboundaries, forming one cohomology class. Raw twists differ, but every one is a representative-gauge change.

## Disposition

Central compositor twists are classified up to coherent gauge by \(H^2(G,A)\). Pointwise representability and the coefficient automorphism group do not decide strictifiability; the composition law and cocycle class are essential.
