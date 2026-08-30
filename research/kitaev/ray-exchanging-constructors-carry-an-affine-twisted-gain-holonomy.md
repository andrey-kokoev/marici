# Ray-Exchanging Constructors Carry an Affine Twisted-Gain Holonomy

When every constructor preserves the ordered repair and drift rays, relative
gain is multiplicative. A constructor exchanging the two rays inverts the
safety factor, so the correct coefficient group is not \(\mathbb R_{>0}\)
alone.

Write

\[
x=\log M.
\]

Represent a constructor by \((\ell,\varepsilon)\), where

\[
\ell=\log\gamma,
\qquad
\varepsilon\in\{+1,-1\}.
\]

Its action is

\[
x\longmapsto\varepsilon x+\ell.
\]

Here \(\varepsilon=+1\) preserves the rays and \(\varepsilon=-1\) exchanges
them.

## Composition law

If \((\ell_1,\varepsilon_1)\) acts first and
\((\ell_2,\varepsilon_2)\) second, their composite is

\[
(\ell_2,\varepsilon_2)
\circ
(\ell_1,\varepsilon_1)
=
(\ell_2+\varepsilon_2\ell_1,
 \varepsilon_2\varepsilon_1).
\]

This is the affine group

\[
\mathbb R\rtimes C_2,
\]

equivalently \(\mathbb R_{>0}\rtimes C_2\) before logarithms.

Two exchanging constructors compose as

\[
(\ell_2,-1)\circ(\ell_1,-1)
=(\ell_2-\ell_1,+1).
\]

Thus their net relative gain is

\[
\frac{\gamma_2}{\gamma_1},
\]

not \(\gamma_2\gamma_1\). Equal exchange gains cancel exactly.

## Loop classification

For a loop \(C\), its holonomy is an affine map

\[
x\longmapsto\varepsilon_Cx+\ell_C.
\]

There are two independent cases.

### Even loop

If \(\varepsilon_C=+1\), the loop preserves the ordered rays and translates
the log margin by \(\ell_C\). A globally flat ordered frame requires

\[
\ell_C=0.
\]

### Odd loop

If \(\varepsilon_C=-1\), the loop returns with the two rays exchanged. No
single-valued ordered polarization exists around that loop, regardless of
\(\ell_C\). The affine reflection has fixed point

\[
x_C^*=\frac{\ell_C}{2},
\]

but this supplies only an unordered or twisted frame.

Therefore the first obstruction is the \(C_2\) parity holonomy. After passing
to the orientation double cover that kills odd loops, the remaining
obstruction is the ordinary additive log-gain holonomy on even loops.

## Gauge transformation

Changing the relative log frame at a vertex by \(q\) conjugates loop
holonomy. For an even loop, \(\ell_C\) is unchanged. For an odd loop,
\(\ell_C\) shifts by twice the frame change, while \(\varepsilon_C=-1\)
remains invariant.

Hence:

- even-loop translation is a genuine gain invariant;
- odd-loop displacement depends on origin;
- odd-loop parity is the invariant obstruction to ordered polarization.

## Tail recurrence

Along an infinite constructor path, the correct completion recurrence is

\[
x_{n+1}=\varepsilon_nx_n+\ell_n.
\]

Completion stability requires the resulting affine orbit to remain bounded in
the normalization sense appropriate to the source. Simple products of gains
are valid only when every \(\varepsilon_n=+1\).

For a repeated exchange with fixed \(\ell\),

\[
x_{n+1}=-x_n+\ell,
\]

so

\[
x_{n+2}=x_n.
\]

The orbit is bounded even though naively multiplying \(e^\ell\) at each stage
would predict exponential drift. Conversely, alternating exchanges with
unequal \(\ell_1,\ell_2\) produce a genuine translation
\(\ell_2-\ell_1\) every two steps and can diverge.

## Source-authority boundary

The compiler classifies the possibilities but cannot decide whether
Fourier--Tate transport preserves or exchanges the repair and drift
characters. The source must provide \((\ell_e,\varepsilon_e)\) for every
admitted constructor and the exact composition ordering.

## Falsifiers

- Multiplying gains across an exchanging edge without inversion.
- A loop with odd parity under a claimed global ordered polarization.
- A nonzero even-loop log translation under a claimed flat frame.
- Treating the origin-dependent displacement of an odd reflection as an
  invariant number.
- Using a product test instead of the affine recurrence on a mixed tail.
- Silently passing to the orientation double cover without typing that change.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to finish the gain compiler when source constructors may
exchange the two sheet characters.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The obstruction splits exactly into parity holonomy and even-loop
translation, with a complete affine recurrence for the tail.
