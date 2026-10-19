# A scale-independent native cycle discriminator, with a preparation rival

## Result

The retained native cycle supplies a conditional discriminator that does not use the unknown relative native/orbital energy scale. For the same declared encounter preparation rho=I4/4, a coherent comparison of cycle versus no cycle gives

    p_minus(option0)=(5-sqrt(5))/16 =0.1727457514...,
    p_minus(option1)=(5+sqrt(5))/16 =0.4522542486... .

Both chiralities give these same two probabilities. All local cell populations are identical between the doublets. Unknown preparation can nevertheless reproduce this contrast exactly, even with a strictly positive density. Neither a physical preparation nor a controlled-cycle detector is supplied by the calculation.

## Prior research used

[pentachoron-cycle-spin-energy-transport](../voevodsky/pentachoron-cycle-spin-energy-transport.md) already constructs the two native doublets, their isometric local extensions and distinct cycle traces. Its five-step amplitude observer is an information-retention identity, not five nondestructive physical copies.

[native-spinor-pair-adapter](../voevodsky/native-spinor-pair-adapter.md) transports each doublet to its pair cycle U=D tensor conjugate(D). We use that actual action, not an oscillator invented from the desired probability.

A newly read [selected source K](../voevodsky/selected-source-k.v1.md) records operator selection of the cycle-defect constructor for its101-state reaggregation branch. That is a genuine convention selection for that branch, not physical calibration or authorization of controlled-U in this scattering experiment. Both doublets remain retained. Calling the cycle-defect law universally unselected would now be too broad.

## Exact test

[Contract](contracts/native-cycle-discriminator.v1.json), [checker](checkers/check_native_cycle_discriminator.py), [result](results/native-cycle-discriminator.json). SCC obligation: forward realization of the source readout, followed by preparation/instrument boundary checks.

The cycle/no-cycle comparison effect is

    F_minus=(I-U)^dagger(I-U)/4=(2I-U-U^dagger)/4.

Its complement is I-F_minus. This effect can be realized mathematically by coherent path/ancilla control with the specified relative phase; simply having a native unitary U does not supply that control or apparatus.

For each of four chirality/doublet cases, the exact checker reconstructs U from the pinned native adapter and verifies its unitarity and the defect-square identity. The effect has spectrum

    0,0,c_i,c_i,
    c_0=(5-sqrt(5))/8, c_1=(5+sqrt(5))/8.

The projector Q_i=F_i/c_i is exactly Hermitian, idempotent and rank2. Since0<c_i<1, both complementary effects are positive. Tr(F_i rho)=c_i/2 for rho=I4/4.

Every two-row cell block of either native W obeys W_cell^dagger W_cell=I2/5. Thus each single-cell occupation is1/5 and each pair-cell occupation is1/25, irrespective of the encounter density. Local occupation counts cannot replace the cycle comparison.

Applying U alone also leaves rho=I4/4 unchanged. The signal above belongs to a coherent comparison with the no-cycle path, not a claim that cycling the unpolarized state makes its ordinary density change.

Known visibility v gives F_v=I/2+v(F_minus-I/2). The checker verifies v=4/5 and complete dephasing v=0, where both readings become1/2. Unknown phase/visibility therefore cannot be silently ignored.

## Strictly positive preparation rival

Let Q_1=F_1/c_1 and set

    w=c_0/(2c_1),
    rho_1=(w/2)Q_1+((1-w)/2)(I-Q_1).

Because0<w<1/2, this is positive definite and trace one. Exactly,

    Tr(F_1 rho_1)=c_0/2=Tr(F_0 I4/4).

The checker retains the complete rival matrices for both chiralities. This is not a dark-state or zero-signal exception. General preparation ranges[0,c0] and[0,c1] overlap. The new contrast therefore removes energy-scale dependence but does not alone remove preparation ambiguity.

This rival is an explicit mathematical allowed-density test, not a claim that an existing physical preparation protocol produces it. Conversely, the source's unpolarized fixture is not independently validated merely because the formula uses I4/4.

## Decision

There is now a concrete additional source observable to pursue instead of collecting more of the scale-degenerate flux curves. The next operational task is to supply a source-supported cycle/no-cycle comparison (or an equivalent instrument) together with independently constrained preparation and visibility. The prior full retained amplitude observer is another candidate only if its measurement capabilities are supplied.

Do not claim the doublet physically identified until those controls are available. The native complementary states remain retained, Strominger's coefficient-law bridge remains blocked in its tested operation class, and no physical scattering explanation follows yet.

## Verification

```text
python research/nima/checkers/check_native_cycle_discriminator.py
python research/aspect/scc/scc.py check native-cycle-discriminator-v1
```

Run via structured-command. The checker uses exact number-field arithmetic and verifies direct native source pins. It does not run source-owner main functions or modify their receipts. No scattering integral, physical experiment, new formal-kernel proof or Git commit/push is claimed.
