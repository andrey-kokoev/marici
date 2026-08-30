# The comoving scale-valuation cell has two boundary charts

## Why one comoving coordinate is insufficient

For valuation depth \(j\), the adjacent scale cell is

\[
\alpha_{p,j}(q)
=
W_{(j+1)L}(q)-W_{jL}(q),
\qquad
L=\log p.
\]

Its support is a widening annulus with two moving fronts, near

\[
q=jL
\quad\text{and}\quad
q=(j+1)L.
\]

A coordinate centered on only one front sends the other to infinity. The
proper scale-observation blowup therefore has two charts.

## Inner-front chart

Set

\[
u_-=q-jL.
\]

At fixed \(u_-\) and \(L\to\infty\), the adjacent cell converges to

\[
\alpha_{p,j}(jL+u_-)
\longrightarrow
H(u_-)-1
=-H(-u_-).
\]

This chart sees the entrance into the negative plateau: it is zero before
the front and negative one after it.

## Outer-front chart

Set

\[
u_+=q-(j+1)L.
\]

At fixed \(u_+\),

\[
\alpha_{p,j}((j+1)L+u_+)
\longrightarrow
-H(u_+).
\]

This chart sees the exit from the plateau: it is negative one before the
front and zero after it.

## Transition and fifth wall

The two limiting profiles are complementary:

\[
\bigl(H(u)-1\bigr)+\bigl(-H(u)\bigr)=-1.
\]

Their transition is therefore the constant carrier already identified as the
fifth wall. The two charts do not describe two independent bulk states. They
are localizations of one oriented interval cell, glued through its constant
interior plateau.

Fourier transport sends that overlap carrier to the delta boundary. Hence
the constant–delta plane is also the Čech overlap datum of the two comoving
front charts.

## Geometric interpretation

The adjacent valuation cell is a one-dimensional cobordism between two
fronts:

- the inner face creates the plateau;
- the outer face annihilates it;
- the plateau is their shared relative object;
- reflection exchanges entrance and exit;
- Fourier transport exchanges the plateau overlap with its delta incidence.

This is a literal realization of two complementary localizations. The raw
single function \(\alpha_{p,j}(q)\) had hidden them by projecting both moving
faces into one observation coordinate.

## Constructor typing

The correct comoving correspondence retains

\[
(p,j,u_-,u_+)
\]

with incidence relation

\[
u_+-u_-=-L.
\]

The two coordinates are not simultaneous independent positions; they are
charts related by the source scale. Pushforward to \(q\) identifies them and
recreates the traveling window.

Thus the source object is naturally a two-chart groupoid or Čech object over
prime scale, not a single function space in \(u=q-\log p\).

## Effect on weighted aggregation

In either chart the profile is stationary as \(p\to\infty\). The primitive
and square growth now lies entirely in the measure on the scale variable
\(L\), rather than being mixed with moving support. This cleanly separates:

1. universal front geometry, supplied by the Gaussian tail;
2. arithmetic multiplicity, supplied by prime density and Mellin weight;
3. overlap incidence, supplied by the fifth wall.

The primitive exponential wall and square constant plateau are therefore
pushforwards of the same two-front cell with different scale measures.

## Remaining gate

The next theorem is a relative pushforward on this two-chart groupoid. It
must pair the two front currents before integrating over \(L\), retain the
constant–delta overlap, and determine whether primitive valuation degree
turns the scale measure into the square remainder without leaving an
unmatched front.

The finite falsifier is an uncancelled coefficient of either limiting profile
\(H(u)-1\) or \(-H(u)\) after the primitive-to-square incidence is applied.

## Result

The comoving blowup of an adjacent scale/valuation cell has two complementary
boundary charts, not one. Their limiting profiles are \(H(u)-1\) and
\(-H(u)\), and their overlap is exactly the fifth-wall constant. The hidden
two-sector structure is now an explicit Čech atlas for the traveling prime
cell.
