# C1: exact nonresonant two-rim threshold; C4: packet corollary

[Conjectures](CONJECTURE-NET.md) · [checker](check_rim_threshold.py) · [certificate](results/rim-threshold.v1.json)

## Fixed model and exact coordinates

Use precisely the source fixture kappa=ell=hbar=1, eta=2, theta=1/2. Extract the rational 24-coordinate core K, metric M and raw rim columns B from `neutron-two-rim-contact-binding.json`, exactly as the owning continuum checker does. Verify its recorded source hashes, M-positive definiteness by exact Schur pivots, MK=K^T M and B^T M B=3I.

If M=L L^T, set chi_whitened=L^T x/sqrt(3). Then W=L^T B/sqrt(3), and W*chi_whitened=Sx with S=B^T M/3. The two lead amplitudes are unchanged. This rational coordinate change avoids numerical whitening without changing the physical metric of the conditional model.

For E=theta+k², the complete boundary/core system is

    A(k) [u;x] = [2ik a;0],
    A(k) = [[(2ik-2)I2, 2S],
            [2B, (theta+k²)I24-K-2BS]].

Here a is the incident lead amplitude. Both open channels have the same velocity, so flux normalization leaves the resulting transmission matrix unchanged. Continuity gives R=T-I2.

## Exact threshold calculation

The checker constructs all 26 coordinates, retaining all dark/core directions, and obtains

    det A(0) =
      942774261680963407393311072136806726006955 /
      25920173316456057567479932702348287542296576 != 0.

It computes the rational inverse and checks multiplication on both sides. There is no threshold kernel. In particular there is no bounded threshold solution with a nonzero lead component. No singular eliminated core resolvent is used.

## Uniform small-momentum bound, not a scan

Let L0=||A(0)^(-1)||_infinity, computed exactly in the receipt, and choose

    k0=min(1,1/(6L0)), C=8L0.

For 0<k<=k0,

    ||A(k)-A(0)||_infinity=max(2k,k²)<=3k,
    ||A(0)^(-1)(A(k)-A(0))||_infinity<=1/2.

The Neumann series therefore gives ||A(k)^(-1)||_infinity<=2L0. Since T(k)=2ik times its upper-left 2x2 block, conversion to the spectral matrix norm gives

    ||T(k)||_2 <= C k,
    ||R(k)+I2||_2 <= C k.

This proves **C1** in the declared fixture. Analytic inversion also gives T(k)=2ik[A(0)^(-1)]_lead+O(k²); the exact leading real coefficient matrix is retained in the receipt. The constants are deliberately conservative, not optimal numerical fits.

## C4 follows

For any normalized asymptotic incoming packet f(E) supported in theta<E<theta+epsilon, with epsilon<k0²,

    integral ||T(E)f(E)||² dE
       <= C² epsilon integral ||f(E)||² dE
       = C² epsilon.

Thus **C4** is established, with explicit epsilon0=k0² and C_packet=C². This is opposite-side transmission for incoming scattering packets, not capture from infinity or escape of an initially central bound component.

C6's C1 premise is now discharged. Its separate three-port threshold/channel assumptions remain visible. C2 remains open; this calculation says nothing about three-chain asymptotic completeness.

## Reproduce

```sh
python research/scattering/low-energy/check_rim_threshold.py
python research/scattering/low-energy/check_rim_threshold.py --check
python research/scattering/low-energy/check_low_energy_net_v4.py
python research/scattering/low-energy/check_low_energy_net_v4.py --check
python research/scattering/low-energy/check_low_energy_net_v3.py
```

These are exact finite algebra plus the explicit analytic estimates above, not proof-assistant formalization or a physical calibration. Historical producers are not replayed or rewritten. The physical explanation remains open.

**Next:** C2, specifically singular-continuous exclusion and outgoing completeness for the fixed finite-rank three-chain contact, including its threshold resonance.
