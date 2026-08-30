# Optical Pair–Stiffness–Flux Cell

Owner: marici.Aspect

## Question

Can one programmable optical network distinguish a superconducting-order
analogue from pair amplitude without global coherence?

This is a dimensionless optical analogue. It does not produce or establish
material superconductivity at room temperature.

## Construction

Twelve coherent nodes form a ring. Each node carries a complex field and its
conjugate channel. Programmable couplers implement phase stiffness; EOM phases
implement a loop gauge field; calibrated complex noise supplies the effective
environment. Homodyne observers recover amplitude, bond phase, circulating
current, and winding.

The executed surrogate is a discrete time-dependent Ginzburg–Landau ring with
Peierls phase. The optical hardware binding remains unrun.

## Joint admission rule

One fixture is admitted only when the same parameter packet passes:

1. nonzero pair amplitude;
2. positive phase stiffness;
3. circulating response opposing inserted flux;
4. persistent winding after removal of the preparation drive.

No single signature can substitute for the conjunction.

## Decisive hostile

The pseudogap hostile retains pair amplitude while weak coupling and phase
noise destroy the joint gate. This separates local order from globally stiff
transport.

## Temperature boundary

The simulator noise is dimensionless. A claim about 300 K requires an
independently derived energy scale and a calibrated bath spectrum. Measurement
of a favourable dimensionless region cannot supply that missing constructor.

## First computational sweep

The coherent fixture passed all four gates. The pseudogap hostile retained
pair amplitude (0.995) and winding (1.000), but its stiffness (0.038) and
screening response (0.036) failed. The normal fixture failed all four gates.

An initially hostile moderate-noise fixture unexpectedly survived: pair
amplitude 0.987, stiffness 0.330, screening response 0.318, and winding 0.987.
That result is preserved as a candidate rather than tuned away. Raising the
noise while weakening coupling produced the sharper hostile: pair amplitude
remained 0.912, while stiffness fell to 0.061, winding to 0.326, and the flux
response reversed sign. The experiment therefore resolves a coherence-loss
boundary rather than equating noise with failure.

## Run

python research/aspect/checkers/check_optical_pair_stiffness_flux_cell.py
