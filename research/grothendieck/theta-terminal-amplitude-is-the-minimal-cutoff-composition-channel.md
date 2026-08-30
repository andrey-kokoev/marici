# Theta terminal amplitude is the minimal cutoff composition channel

## Why terminal-zero pencils do not nest

For an interval ([a,b]), write

\[
 F_{a,b}(s)=\int_a^b f(v)e^{sv}\,dv.
\]

The finite pencil of packet 205 uses the terminal slice (G(b)=0). If
(b<c), the solution with terminal condition (G(c)=0), restricted to
([a,b]), generally has

\[
 G(b)=e^{-sb}F_{b,c}(s),
\]

not zero. Therefore restriction does not map the terminal-zero domain at
cutoff (c) into the terminal-zero domain at cutoff (b). The finite
zero-to-kernel pencils are individually canonical but do not form a strict
cutoff system.

## Minimal boundary enlargement

Retain the terminal amplitude

\[
 \beta_b=G(b)
\]

as an independent boundary coordinate. For the forced equation

\[
 G'+sG+cf=0,
\]

define (Y(q)=e^{sq}G(q)). Integration gives

\[
 Y(a)=Y(b)+cF_{a,b}(s).
\]

Thus interval transport acts on the boundary-source pair by the shear

\[
 \begin{pmatrix}Y(a)\\c\end{pmatrix}
 =S_{a,b}(s)
 \begin{pmatrix}Y(b)\\c\end{pmatrix},
 \qquad
 S_{a,b}(s)=
 \begin{pmatrix}1&F_{a,b}(s)\\0&1\end{pmatrix}.
\]

## Exact composition law

Additivity of the source integral yields

\[
 F_{a,c}=F_{a,b}+F_{b,c}.
\]

Consequently

\[
 S_{a,b}(s)S_{b,c}(s)=S_{a,c}(s).
\]

The terminal amplitude is therefore precisely the missing cutoff-composition
channel. It is not an optional correction: deleting it selects a boundary
slice that is not preserved by interval restriction.

Each shear has determinant one. Hence the completed scalar transform is an
off-diagonal transport coefficient of a source-generated unipotent system,
while zeros are intervals on which that coefficient vanishes. This is the
Rosenbrock realization of packet 205 expressed in compositional form.

## Reciprocal and quadrature typing

For complex source amplitudes, realification of the shear uses the universal
quadrature port (e,Je) from packet 200. The place and cutoff labels remain
separate from this two-dimensional port. Reciprocal Fourier--Tate doubling
must act on two such boundary shears before any scalar compression.

The algebraic determinant-one identity does not prove Hermitian
losslessness. A conservative or indefinite-metric colligation theorem would
have to derive its metric from the complete boundary currents. Assuming such
a metric would merely rename the missing RH orientation law.

## Completion gate

The algebraic cutoff limit is now organized by an exact cocycle rather than
by incompatible terminal-zero domains. Analytic completion still requires:

1. convergence of the terminal amplitudes in a source-selected topology;
2. continuity of the primitive, square, seam, and archimedean coordinates;
3. absence of kernel loss or spectral pollution in the completed graph; and
4. identification of the limiting transfer coefficient with the completed
   theta section.

The reciprocal factor (e^{2|\delta|b}) remains the hostile graph-norm test.
The boundary shear solves compositionality, not cutoff-uniform boundedness.

## Falsifier

The minimal-channel claim fails if cutoff restriction closes without a
terminal coordinate or if a smaller source-derived coordinate carries the
same nonzero (F_{b,c}) cocycle. The completed route fails if the exact shear
cocycle has no continuous realization in the boundary-bearing restricted
product or if its limiting transfer coefficient differs from the completed
theta transform.

## Scope

This proves the exact cutoff-composition law and identifies one terminal
amplitude as its minimal missing channel. It does not prove conservative
metric structure, analytic completion, kernel convergence, or RH.
