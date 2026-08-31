# Ratio translation of the completed pair kernel produces an exact oriented Laplace boundary cocycle

## Question

How does the exact ratio translation \(t\mapsto t+\log(m/n)\) act after the
one-sided Laplace readout defining the ordinary Evans shell?

## Claim boundary

It produces a Mellin character times a translated base transform, together
with a finite oriented correction over the interval between zero and the ratio
shift. This correction is a canonical candidate source for an ordered linking
term. No identification with the existing G4 linking port is asserted.

## Base shell transform

For a translated shell \([A,B]\), define

\[
 K_{[A,B]}(w)
 =\int_A^B\Phi_1(v)\Phi_1(v+w)\,dv
\]

for every real \(w\), and define its positive-separation Laplace transform

\[
 H_{[A,B]}(z)
 =\int_0^\infty e^{-zw}K_{[A,B]}(w)\,dw.
\]

The superexponential source decay makes the required oriented finite intervals
and positive tail well defined, with entire dependence on \(z\).

## Ordered-pair readout

Let

\[
 d_{nm}=\log\frac mn,
 \qquad
 A_n=a+\log n,
 \qquad
 B_n=b+\log n.
\]

The product--ratio identity gives

\[
 \rho_{nm}^{[a,b]}(t)
 =(nm)^{-1/2}K_{[A_n,B_n]}(t+d_{nm}).
\]

Therefore its Laplace transform is

\[
 R_{nm}^{[a,b]}(z)
 =(nm)^{-1/2}e^{zd_{nm}}
 \int_{d_{nm}}^\infty
 e^{-zw}K_{[A_n,B_n]}(w)\,dw.
\]

The character factor is

\[
 e^{zd_{nm}}=\left(\frac mn\right)^z.
\]

## Oriented finite correction

Define

\[
 J_{[A,B]}(z;d)
 =\int_0^d e^{-zw}K_{[A,B]}(w)\,dw,
\]

with the standard oriented-integral convention when \(d<0\). Then

\[
 \int_d^\infty e^{-zw}K_{[A,B]}(w)\,dw
 =H_{[A,B]}(z)-J_{[A,B]}(z;d).
\]

Hence

\[
 R_{nm}^{[a,b]}(z)
 =(nm)^{-1/2}
 \left(\frac mn\right)^z
 \left[
 H_{[A_n,B_n]}(z)
 -J_{[A_n,B_n]}(z;d_{nm})
 \right].
\]

The ordinary Evans contribution is \(-R_{nm}^{[a,b]}\).

## Meaning of the two terms

The first term is the full positive-separation base response transported by the
product half-density and ratio Mellin character. The second is a finite
oriented segment created because one-sided Laplace readout is not invariant
under separation translation.

Thus ratio transport does not act by a scalar character alone. The truncation
boundary produces an additional source cocycle.

## Swap behavior

Swapping \((n,m)\) sends

\[
 d_{nm}\longmapsto-d_{nm}
\]

and reverses the oriented finite interval. The product coefficient is
unchanged. The shell translation simultaneously changes from \([A_n,B_n]\) to
\([A_m,B_m]\), so the swap law includes both orientation reversal and base
transport.

A formula retaining only \((m/n)^z\) misses this finite correction.

## Candidate linking interpretation

The correction

\[
 (nm)^{-1/2}
 \left(\frac mn\right)^z
 J_{[A_n,B_n]}(z;d_{nm})
\]

has the structural features expected of an ordered linking contribution:

- it vanishes on the diagonal \(n=m\);
- it changes orientation under ratio reversal;
- it is entire in \(z\);
- it is additive under subdivision of the oriented ratio interval;
- it is fixed before Xi zeros are inspected.

These features make it a comparison target, not an authorization to identify
it with the wall/incidence polarization.

## Exact test for the G4 port

A proposed ordered linking response should be pulled back to the completed
pair carrier and compared with this finite ratio-segment section. The test must
also retain the translated shell \([A_n,B_n]\). Equality only of the Mellin
character or diagonal labels is insufficient.

## Disposition

The one-sided Evans readout converts ratio translation into a character plus a
canonical oriented boundary cocycle. This isolates an explicit source section
that may account for part of the missing linking response. Its typed comparison
with the G4 linking port and the remaining diagonal base response are open. No
RH conclusion is authorized.
