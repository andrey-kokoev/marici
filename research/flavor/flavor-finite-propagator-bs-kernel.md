# Finite-propagator aligned bs kernel

## Source-side interface

WP519 showed that the WP516 propagating spectrum cannot be inserted directly
into WP511's local WET coordinate. WP520 constructs the missing source-side
object: the exact momentum-dependent aligned \(bs\) current kernel.

In the \(J_3\)-aligned frame, the \(bs\) transition has components along
\(F_6\) and \(F_7\). These lie in the WP508 sectors
\((F_1,F_6,P_1,E_1)\) and \((F_2,F_7,P_2,E_2)\). If their diagonal current
resolvents are \(K_6(z)\) and \(K_7(z)\), then

\[
K_{bs}(z)=\frac{K_6(z)-K_7(z)}{4}.
\]

At spacelike transfer, set \(z=-q^2\). The checker constructs both resolvents
from WP508's exact matrix numerators and denominators without refitting any
pole or residue.

## Contact recovery and finite-momentum falsifier

At zero momentum, the kernel exactly recovers WP513:

\[
K_{bs}(0)=\frac{b^2}{4a^2(a^2+b^2)}.
\]

Define

\[
F(q^2)=\frac{K_{bs}(-q^2)}{K_{bs}(0)}.
\]

The checker proves \(F(0)=1\) and obtains

\[
F'(0)=-\frac{2395516267}{1613760000}\ {\rm GeV}^{-2}.
\]

A single momentum-independent WET coefficient has zero slope, so it cannot
represent this source kernel beyond the contact point.

The following spacelike points are hostile diagnostics, not a calibrated
neutral-\(B\) momentum distribution:

| \(q\) (GeV) | \(F(q^2)\) | Relative contact error |
|---:|---:|---:|
| 0.10 | 0.9854 | 0.0146 |
| 0.50 | 0.70194 | 0.29806 |
| 1.00 | 0.28486 | 0.71514 |
| 5.00 | 0.0000380 | 0.999962 |

The lightest 12 MeV pole has small residue in this current difference; the
checker does not attribute the distortion to that pole alone.

## Typing and remaining gate

- State domain: WP516's aligned propagating source packet.
- Probe: exact spacelike matrix-current resolvent.
- Classification: finite-propagator source kernel and exact falsifier of a
  single momentum-independent contact transport; neither selector nor physical
  instrument.
- Smallest exact falsifier: \(F'(0)\ne0\), whereas a single local coefficient
  has zero momentum slope.

To predict \(\Delta M_s\), this kernel must be convolved with a calibrated
bilocal neutral-\(B\) matrix-element functional, including threshold running
and uncertainties. No diagnostic momentum point may replace that constructor.
