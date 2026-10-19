# Endpoint charging mixes the original coherent doublet with retained line mismatch

**Third batch, iteration 7 of 10.**

**Strength:** exact all-integer-flux closure criterion, leakage identity and dressed unit-flux ground decomposition. Not physical spin loss or a no-go for dressed carriers.

[Previous face-line adapter](NATIVE-ENDPOINT-FACE-LINES.md) · [Checker](check_charged_spinor_closure.py) · [Receipt](results/charged-spinor-closure.v1.json)

## 1. Fresh interacting test

The free adapter transports native H=(I-L)+2(I-N) to endpoint K=I-Q. Its coherent projector in line coordinates is P=(I+Q)/2. This turn adds the owning endpoint charging diagonal rather than assuming that free intertwining preserves the interacting doublet.

For the four-vertex graph and total integer flux sum ell=q, exact reconstruction gives

    d_i=c-(beta*q/4)ell_i,
    c=(beta/8+eta/2)q^2+(5beta/8)||ell||^2.

The tested parent contract has beta>0 and signed unit charge. All charge, flux and coupling assignments remain conditional inputs.

## 2. Closure fails for every signed-unit integer flux

Every off-diagonal entry of P is nonzero. For any real diagonal potential,

    [diag(d),P]_ij=(d_i-d_j)P_ij.

Because the interaction is Hermitian, invariance of im P is equivalent to commutation. Therefore a diagonal potential preserves the coherent doublet **iff all four d_i are equal**.

For q=+/-1 and beta>0 this requires equal integer ell_i. But sum ell=q would imply 4ell_i=q, impossible. This proves failure for the full integer flux lattice, not just the tested finite window.

Exceptions outside that unit-charge case are explicit: q=0, uniform flux for charge divisible by four, or removing beta outside the owning positive-coupling contract. These exceptions are not physical electron identifications.

## 3. Exact leakage and retained sectors

Let A_leak=(I-P)diag(d)P. Exact matrix algebra gives

    ||A_leak||_HS^2 = sum_i(d_i-mean(d))^2/3
                    = beta^2*q^2/48 * sum_i(ell_i-q/4)^2.

The checker exercises 160 signed-unit flux cases and records their ranks and exact squared leakage. Each unit-lead flux has rank-one leakage with squared Hilbert–Schmidt norm beta^2/64. Thus not all coherent input directions leak equally; a rank-one branch has a kernel direction.

For short abstract Hamiltonian time and normalized coherent y, mismatch norm begins as t^2||A_leak y||^2+O(t^3). This is an operator expansion in model units, not a derived physical lifetime or emission rate.

The native eight-coordinate accounting retains:

- coherent return: rank two;
- noncoherent selected-line mismatch L-N: rank two;
- excluded polarization I-L: rank four.

The declared minimal potential extension is H_native+V diag(d)D. It exactly intertwines the charged line operator and leaves the free polarization block 3(I-L) unchanged. Leakage enters L-N, not I-L. This extension supplies no independently sourced field law on the polarization complement.

## 4. Dressed unit-flux ground is not the old doublet

For a unit-lead flux, remove the constant c and put v=beta/4. The line Hamiltonian is K-v|i><i|. Its existing exact ground is

    r=(v+sqrt(v^2+4))/2,
    psi=r e_i+Qe_i,
    eigenvalue=1-r,
    r^2-vr-1=0.

The checker verifies the source Q identities and eigenvector coefficients modulo that quadratic relation. Its decomposition is

    ||psi||^2=r^2+1,
    ||P psi||^2=(r+1)^2/2,
    ||(I-P)psi||^2=(r-1)^2/2.

The normalized mismatch fraction is

    1/2-1/sqrt(v^2+4)>0 for v>0.

Strict rational bounds are retained for the fixture v=3/20. Thus the interacting ground is genuinely dressed outside the original coherent doublet, while remaining within the four selected lines.

The owning model's fourfold ground multiplicity comes from four orthogonal lead-flux labels. It is not proof of a preserved two-dimensional logical-spin ground in each fixed flux sector. Neither this distinction nor leakage justifies declaring physical spin lost.

## 5. Next executable gate

Construct the dressed low spectral projectors in each unit-flux block. Test whether one common rank-two carrier or a source-compatible transport exists across all four flux labels. Keep the field labels, line mismatch and polarization records rather than projecting the interacting state back to the old spinor without accounting.

The root remains null. Physical preparation, charge conjugation, energy calibration and annihilation stay open; shared sources, atlas and formal contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_charged_spinor_closure.py
python research/scattering/seed-composition/check_charged_spinor_closure.py --check
python research/scattering/seed-composition/check_native_endpoint_face_lines.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact rational/multiquadratic identities and quadratic remainders certify these statements. Prerequisites are recomputed; only the local receipt is written and `--check` is read-only.
