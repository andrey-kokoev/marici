# Xi-torsion lift iteration 20: final disposition—the two strict-range theorems do not form the claimed Xi-torsion equivalence

## Objective 1: proved in the correctly typed graph category

Let `zeta` be the Xi spectral parameter and `xi` the Fourier observer variable.
For the translated-theta common-history codiagonal,

\[
\widehat{J_\theta c}(\zeta,\xi)
=
\widehat\Phi(\xi)F_c(\zeta,\xi).
\]

Retaining `F_c` on two complex `xi`-lines gives the tame inverse

\[
q_{K,j,\delta}(c)
\le
K_{R-\delta-1/2}S_{K,j,R}(F_c),
\qquad R>\delta+\frac32.
\]

The converse estimate also holds. Hence `J_theta` is a strict topological
embedding onto a closed range in the deconvolved Fourier--Köthe graph category,
with compact-open/Silva control in `zeta`.

It is spectrally horizontal:

\[
\partial_\zeta J_\theta c
=J_\theta(\partial_\zeta c).
\]

Qualification: descent of the deconvolved observer to an ordinary raw-history
topology still requires controlled division by `widehat Phi`. The graph theorem
is unconditional only when the deconvolved channel is retained as part of the
target.

## Objective 2: proved only in its separate bordered source category

The actual factor is

\[
H_{a,b,c}(\zeta)
=T_{PB}^{\rm rig}
(e^{\zeta\cdot}\otimes K_{1,c}).
\]

It is a four-chart bordered packet, not a translated-theta common history.
Prime loading gives a canonical labelled lift. Opposite Fourier charts invert
the Clark cells by a finite Hadamard transform, and the endpoint channel has
distinct outgoing/reflected arithmetic frequencies.

Accordingly:

- superexponential Euler--theta loading gives all-order coefficient recovery;
- mixed `p^(-3/2-sigma)` loading gives finite-strip mean-square Bohr recovery;
- shellwise, `H_border` belongs to the labelled bordered synthesis range by its
  source construction.

This does **not** prove

\[
H_{\rm border}\in\operatorname{im}J_\theta,
\]

because the two maps have different targets and use different exponential
variables. No strict horizontal comparison square between them is declared.

## Objective 3: the claimed equivalence is false

There are three distinct statements:

1. the labelled Evans identity
   \[
   \Delta^{\rm lab}=\tau H^{\rm lab};
   \]
2. possible torsion in a scalar holomorphic codiagonal cokernel;
3. the Hermitian relative-Haar fiber value
   \[
   (1-p^{-2\operatorname{Re}\zeta_0})E_p(b_{\zeta_0}).
   \]

The first is proved shellwise. The second has no common source-defined cokernel
linking `J_theta` and `J_B`; moreover scalar `O`-module saturation destroys
label injectivity. The third is not holomorphic cokernel torsion at all.

In the reduced physical Xi fiber, the energy defect is exactly

\[
[\delta_p]_{\rm red}
=
(1-p^{-2\operatorname{Re}\zeta_0})E_p(b_{\zeta_0}).
\]

Its vanishing is equivalent to critical-line confinement because the energy is
positive. Strictness ensures that this class is not a completion artifact; it
does not force the class to vanish.

## Final theorem boundary

The completed investigation establishes two useful but separate strict-range
theorems:

- strict horizontal recovery for translated-theta common histories;
- labelled/four-chart recovery for the independent bordered Clark factor.

It refutes the assertion that these are equivalent to excluding an RH-bearing
Xi-torsion class. The only torsion-free module available directly is the
labelled Evans module, whose divisibility closes the identity edge already
known. The relative-Haar obstruction remains a nonzero Hermitian reduced-fiber
class unless an independent metric conservation law is proved.

## Nonredundant successor problem

A future programme should no longer optimize the scalar codiagonal topology.
It must construct one of:

1. a prime-diagonal metric localization map from the bordered Evans carrier to
   the relative-Haar carrier;
2. a source-derived Green identity whose reduced Xi-fiber readout is
   `delta_p`;
3. finite Schur certificates proving that readout vanishes on every Xi state.

Any of these would address the remaining obstruction directly. None follows
from objectives 1--2 alone.