# Owning charge models supply conditional opposite sectors, not seed-derived charge conjugation

**Third batch, iteration 5 of 10.**

**Strength:** read-only source comparison, exact endpoint sign/flux tests and signed quotient-state controls. Not a physical charge assignment, implemented sector switch or annihilation.

[Previous antiunitary gate](ANTIUNITARY-CHARGE-GATE.md) · [Checker](check_source_charge_sector_bridge.py) · [Receipt](results/source-charge-sector-bridge.v1.json)

## 1. Fresh owning sources

The earlier within-doublet obstruction concerns Q_q=qN: no antiunitary confined to a nonzero real scalar charge sector reverses its charge. It does not show that all opposite-charge source constructions are absent.

Freshly read owning mechanisms already construct larger conditional domains:

- `research/nima/mass-primitive-quotient-charge.md`: signed integer rotor states with joint charge Q=k-n_e and explicitly chosen primitive quotient symmetry.
- `research/strominger/common-endpoint-charging.md`: a source-graph endpoint/lead parent accepting signed charge q, lead flux and common charging coefficients.

Their charge assignments, gauge laws and physical identification remain inputs. In particular the quotient law is a different external symmetry from the old degree-1836 diagonal action; it is not a coordinate renaming.

The current endpoint-parent receipt's fifteen referenced hashes match. This checker reconstructs its electron selected-sector kinetic operator and graph resistance and exercises the unchanged core without calling owner producer entrypoints. The earlier native-spinor historical producer-hash caveat remains separately recorded upstream.

## 2. Endpoint sectors have a conditional charge-sign involution

The physical basis at matter position i satisfies

    n=q e_i-S ell, sum ell=q, sum n=0.

The joint sign map

    (q,n,ell) -> (-q,-n,-ell)

preserves these constraints. Its quadratic charging energy is unchanged, including internal graph resistance, lead cost and q-squared offset.

The checker enumerates 160 integer flux cases with q=+1 or -1 and four lead values in [-2,2]. It checks every matter-position Gauss solution, identical charging diagonals under sign reversal and rejection of incompatible total flux. These finite cases exercise the structural quadratic-evenness argument; they are not a physical flux cutoff.

A doubled selected endpoint space admits a linear swap between two identical-K blocks that flips an explicitly assigned signed charge operator and preserves their energy. The core's charge parameter permits these sectors; it does not derive the sector swap from inverse affine arrows or microscopic control.

## 3. Charge sign and kinetic complex conjugation are different inputs

The endpoint electron model uses four face-line coordinates. Its K is Hermitian but not real, and its four triangular Wilson phases are +/-i. Reversing q and lead flux leaves the charging diagonal unchanged and can leave K unchanged.

For the **bare conjugating sector swap**, two identical K blocks are not invariant: coefficient conjugation changes K. Pairing K with conjugate(K) makes that particular antiunitary swap covariant; every stored triangular Wilson phase then changes sign on the partner.

This is not a no-go for other antiunitaries using additional frame/port maps. It establishes that charge sign reversal alone does not specify the kinetic-conjugation choice, and that the simple antiunitary partner construction requires explicit coefficient data.

The selected parent has four face-line coordinates, while the native tetrahedral spinor has eight raw coordinates and a rank-two coherent return. The exact adapter between those carriers is the next obligation; their equal particle naming is not a map.

## 4. Quotient rotors also have signed sectors—but not a supplied spinor adapter

On signed integer states |k,n_e>, the owning quotient law gives

    Q=k-n_e,
    E=(k^2 sum_s(1/C_s)+n_e^2/C_e)/2.

The involution (k,n_e)->(-k,-n_e) flips Q and preserves E. Elementary states (0,1) and (0,-1) have charges -1 and +1 with equal energy. Exact small-window tests verify this for three distinct inertia choices, including the owning 1836 and 1944 collective controls. Charge consistency does not select the charging coefficients or a mass.

These are rotor momentum sectors, not automatically two physical species on the checked native spinor. A rotor/spinor embedding and interaction must still be supplied. The owning source also exhibits charge-preserving mixing (1,0)->(0,-1): both have Q=+1, despite changing carrier sector. Charge alone therefore does not protect particle identity.

## 5. Refined correspondence result

The conditional doubled construction from the preceding turn is compatible with existing signed-sector mechanisms. Opposite-charge representations are not wholly absent. But neither source makes the assignment a consequence of inverse seed data, supplies physical electron/positron preparation or constructs an annihilation vertex.

The residual questions are now explicit:

1. Relate native eight-coordinate spinor data to the endpoint parent's four face-line coordinates and signed field basis.
2. State whether the partner retains K or conjugates K, including actual loop phases and any frame map.
3. Supply the sector-changing operation, charge law and physical interpretation together.
4. Retain complement, flux and reservoir records rather than treating a charge label as a physical species proof.

## 6. Next executable test

Construct the exact native-to-face-line adapter, retaining the four directions excluded by local negative-polarization projectors. Check its kinetic, metric and loop-phase transport. Then determine whether coefficient conjugation stays within that selected source or requires an explicit partner.

The scientific root stays null; physical conjugation, energy calibration and photon outputs remain open. Shared sources, atlas and formal contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_source_charge_sector_bridge.py
python research/scattering/seed-composition/check_source_charge_sector_bridge.py --check
python research/scattering/seed-composition/check_antiunitary_charge_gate.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact rational and multiquadratic calculations replay the scoped identities above, not the owner's entire mass/field verification suite. Only the local receipt is written; `--check` is read-only.
