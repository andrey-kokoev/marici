# Coherent inverse-filter dilation and the disturbance left by a measured flag

**Fourth batch, iteration 9 of 20.**

**Strength:** exact full unitary dilation, coherent undoing and measured-flag channel. Not a physical readout apparatus or reversal of earlier history measurements.

[Previous inverse filters](HERALDED-HISTORY-INVERSE.md) · [Checker](check_inverse_flag_dilation.py) · [Receipt](results/inverse-flag-dilation.v1.json)

## 1. Fresh flag construction

For either witnessed known code, write its history map K=U sqrt(G), with U its logical polar unitary. On the inverse-filter input let H=Pi_output,high and L=I-H. Define

    r=sqrt(lambda_min/lambda_max),
    s=sqrt(1-r²),
    D=L+rH, F=sH.

A neutral supplied flag initialized in |0> undergoes

    R_flag=exp(-i phi sigma_y,flag tensor H),
    phi=acos(r), 0<phi<pi/2.

Its flag-first blocks are [[D,-F],[F,D]]. Then apply U* on the success flag only. The full unitary is

    W=[[U*D,-U*F],[F,D]].

Its first column is exactly the prior optimal success operator N and retained failure operator F. The checker verifies both W*W=I and WW*=I, not just Kraus completeness.

Positive roots r,s and the history scale root u are represented by masks with exact squares in Q(sqrt(19)). This verifies the polar unitary and complete flag matrices without numerical square roots or fitted rotations.

## 2. Coherent uncomputation

If the flag and system remain coherent, W*W restores their input, with the flag returned to |0>. This identity extends to every reference-entangled input.

The restored input here is the state entering the inverse filter, after the preceding witnessed history. It does not undo the earlier state-dependent history measurement or make that history probability independent of the logical state.

## 3. Measuring the flag is different

Measure/dephase the flag after W and retain the outcome, then apply W*. The controlled polar factors cancel, but the lost flag coherence does not. Four retained Kraus maps, indexed by measured and terminal flags, are

    D², F², -FD, DF.

Their effects sum to identity. Exact operator-basis tests give the reduced system channel

    LXL+HXH+r²(LXH+HXL).

Thus the input-eigenstate coherence is multiplied by r²=lambda_min/lambda_max, not restored. The terminal flag-one effect is

    2r²(1-r²)H.

Both the original measured flag and terminal flag remain accounted for. For a Bell input/reference probe of this flag interaction, undo fidelity is (1+r²)/2<1 and terminal flag-one probability is r²(1-r²). These are tests of the flag interaction itself, not claims that the prehistory Bell state is recovered unconditionally.

Access to the full coherent measurement apparatus could permit a different undoing. Classical records alone do not recreate the missing coherences for an unknown state.

## 4. Gauge extension and control obligations

Embed H into the physical dressed ground and set it zero outside. With a neutral flag, its controlled rotation preserves the Gauss sector and is compatible with the physical endpoint Hamiltonian. The projector, flag, pulse area/phase and success-controlled polar unitary are added controls, not terms supplied by the native fixed Hamiltonian.

For a plus code the polar undoing can act on plus and fix minus. For a minus target it must map the output plus frame into the original minus frame, with a complementary ground-frame map completing a unitary. It cannot be extended by identity on an overlapping target subspace. Other physical/gauge sectors may be fixed. This is an existence construction; no local device, control work cost or pulse implementation is derived.

## 5. Next apparatus-record gate

Model explicit copying of the flag into an apparatus and partial decoherence. Quantify how apparatus-state overlap changes undo fidelity. Test whether an accessible outcome record can remain while an arbitrary unknown reference-entangled input is recovered exactly, distinguishing coherent record uncomputation from classical record retention.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_inverse_flag_dilation.py
python research/scattering/seed-composition/check_inverse_flag_dilation.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor filters are freshly recomputed. Exact radical-mask arithmetic verifies the complete unitary and measured-flag channel. Gauge extensions and reference-fidelity statements are explicitly scoped mathematical arguments, not new machine-formal or physical admission.
