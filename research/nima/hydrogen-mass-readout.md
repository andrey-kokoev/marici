# A conditional mass-valued readout for the hydrogen composite

## Question

Build the missing explicit readout object for hydrogen while distinguishing constituent count, atom mass and the closed-system mass. Active obligation: retained-source recovery and conservation-compatible physical readout. The primitive masses and hydrogen binding remain supplied rounded reference inputs; constructing this map does not derive them from WG.

## Construction

The immutable source record holds proton rest energy, electron rest energy, binding B=13.5984 eV and occurrence weight two. The output retains that exact source object, the atom rest energy, and separate outgoing atom and photon four-momenta. A certificate checks source recovery, energy/momentum conservation, the atom mass shell and the photon null mass shell.

With c=1, let I be the incoming proton-plus-electron rest energy and F=I-B the atom rest energy. In a declared one-photon final channel at initial center-of-momentum threshold,

\[
E_\gamma=B-\frac{B^2}{2I},\qquad
P_H=(I-E_\gamma,-E_\gamma),\qquad
P_\gamma=(E_\gamma,E_\gamma).
\]

Thus P_H+P_gamma=(I,0), P_H squared=F squared, and P_gamma squared=0. The direction is a chosen one-dimensional kinematic presentation; no radiation transition amplitude or threshold capture rate is inferred.

The subsystem mass is obtained from its invariant four-momentum. Composing systems requires adding four-momenta before taking the invariant; simply adding subsystem rest masses is not equivalent when radiation or relative motion is retained.

## Results and controls

Using the prior rounded inputs gives hydrogen mass 1837.152646388595 electron masses. The corresponding photon energy is approximately 13.598399901512668 eV and atom recoil approximately 9.84873317073e-8 eV. The closed atom-plus-photon system retains invariant mass 1837.152673 electron masses, equal to the initial proton-plus-electron system. The atom's mass deficit is not destruction of total closed-system energy.

The aggregation weight remains two and is not the physical mass. Three supplied binding values, zero, half the reference and the reference, yield three different atom masses with the same count and valid conservation certificates. A control that sends all B into a photon while omitting atom recoil is rejected. A photon has zero rest mass but positive energy, so discarding it on the basis of zero rest mass also breaks the conservation readout.

## Disposition and verification

An explicit witness-retaining hydrogen mass map now exists in the executable model. It is a conditional physical adapter, not an independently predicted mass. No native derivation of the input masses, binding or electromagnetic channel is claimed. The next missing source law is unchanged; this readout does not manufacture it from the aggregation count.

`python research/nima/checkers/check_hydrogen_mass_readout.py` passed via `structured_command_execution:e_32876_1791228745591088900_53`. Results: `results/hydrogen-mass-readout.json`. No commit or publication is claimed.
