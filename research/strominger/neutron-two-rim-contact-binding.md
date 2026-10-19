# Full neutron rim response bound to the existing internal-channel interaction

## Result

The full two-port neutron response now has an exact attachment to the prior charge-compatible internal-channel law. The response is matched as a rational matrix function, not by choosing a gap at one pole or fitting a static stiffness.

The retained space has **26 complex coordinates**: the existing 24 neutron/bank coordinates plus two same-particle internal channels. Both channels, all native modes and all active source-bank coordinates remain present.

## Existing law and explicit extension

Reuse `research/voevodsky/charge-compatible-internal-contact.md`, extending its one internal contact to the two actual collective rim ports:

    H=mu I + [[Delta I2, g T],
              [g W,       K]].

W inserts equal amplitudes around each of the three lower or upper rim triangles. Their squared norms are three in the existing coefficient chart. Use auxiliary metric 3 I2 and T=W* M/3, so T W=I2. This is the normalized two-port attachment expressed without introducing square roots into the coefficients.

The inherited carrier operator is exactly the recovered convention

    K=H_native/4+sum_e P_e.

It is not silently replaced by the unscaled native lift or by a sum of the canonical pulses. The bank part of this static operator is zero; its explicit source-pulse interactions remain separate operations.

Using two channels, equal Delta and g, and this attachment is an explicit extension of the prior interaction rule. Geometry supplies the actual contacts and response; it does not uniquely select the interaction rule or its parameters.

## Full response matching

Let R_even(x) and R_odd(x) denote the previously recovered resolvents evaluated at spectral argument -x. The physical lower/upper-port response is

    R(x)=1/2 [[R_even+R_odd, R_even-R_odd],
              [R_even-R_odd, R_even+R_odd]].

It has nonzero off-diagonal response: the rims cannot be treated as independent terminal bits. The interaction's exact Schur complement is

    (Delta+x) I2-g² R(x).

The checker verifies parity decomposition and equality of the complete rational functions by characteristic/minor polynomial identities. Full-matrix Schur complements are additionally checked at three rational points. No sampled identity is substituted for the polynomial proof.

The equal-rim channel retains its two visible poles and the opposite-rim channel all three. A source dark mode remains in the full carrier, although it cancels from the port resolvent.

## Conditional stationary energies

Use the prior illustrative comparison parameters, without fitting:

    Delta=g=1/2.

In each parity channel the negative shift -x obeys

    Delta+x=g² R_channel(x).

The even channel always has a positive solution because of its zero-mode pole. The odd channel has a negative-energy state only when

    g² > Delta/R_odd(0).

At this fixture the threshold is 6431463/47288498, below g²=1/4, so both solutions exist.

Exact rational brackets give

    x_even = 0.19269806301279097...,
    x_odd  = 0.10112726721962662....

Therefore

    E_ground=mu-x_even,
    E_odd=mu-x_odd.

The even response is strictly larger for all x>0, certified by nonnegative coefficients of its cross-multiplied response difference. It has the larger downward shift. A weighted positive-definiteness check on the full 26-dimensional matrix certifies the lower ground bracket with all unobserved directions retained.

At the prior illustrative mu=1/4, these energies are approximately

    0.05730193698720905,
    0.14887273278037338.

The separate common empty sector has energy zero. All occupied internal channels carry the same declared particle label, and the chosen illustrative baseline keeps the full sector above that vacuum. The unshifted mu=0 model would have a negative dressed energy, as expected from the already known zero-mode contact mechanism.

## What this accomplishes

The proposed comparison now actually works: source-derived rim response, metric, all poles, interport mixing and internal-channel interaction are retained in one executable model. No arbitrary two-level spectrum replaces the neutron response.

These are conditional dressed energies, not a source-selected physical neutron mass. Delta, g, mu and physical time/action normalization remain explicit inputs. The construction does not turn the odd rim parity into a vacuum sector, identify the auxiliaries with the earlier 21 neutral seam bits, or identify this static Hamiltonian with chronological canonical-pulse execution.

## Verification

```sh
python research/strominger/checkers/check_neutron_two_rim_contact_binding.py
```

Seven checks passed. Full 26-dimensional metric/operator, exact aligned embedding, response matrices, rational energy brackets and source hashes:

`research/strominger/results/neutron-two-rim-contact-binding.json`.

No shared neutron or source backend was modified.
