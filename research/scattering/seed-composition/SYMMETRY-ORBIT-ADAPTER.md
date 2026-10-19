# Retained symmetry-orbit observation and the parity of path products

**New batch, iteration 2 of 10.**

**Strength:** executable lossless local observer and exact parity identities for retained concatenation. Not an implemented coherent preparation or a source-owner extension.

[Previous gate](PARITY-PREPARATION-GATE.md) · [Checker and adapter](check_symmetry_orbit_adapter.py) · [Receipt](results/symmetry-orbit-adapter.v1.json)

## 1. Fresh state and construction

The current source can register signed coefficients, but positive forward operations cannot prepare nonzero odd coefficients from nonnegative inputs. Its successor detail readout is not a global reflection-parity selector. This turn constructs the missing mathematical observer without attributing it to the owning source API.

The adapter uses the actual glued-graph reflection on primitive endpoints and labelled path words. It accepts a registered homogeneous payload only if its entire word domain is reflection-closed. It retains:

- the original source-owned payload, hence its complete assembly history;
- the reflected slot permutation and orbit partition;
- even coefficients (x+Jx)/2 and odd coefficients (x-Jx)/2.

Adding the two records recovers every coefficient. Their squared counting norms sum to the original norm. Nonclosed word domains are rejected without padding; substituted observer objects are rejected. Existing source files and operation tags are unchanged.

For primitive words there are ten slots in five reflection orbits. For length-two successor words there are sixteen slots in eight orbits. Neither tested domain has a singleton orbit. The generic adapter also handles singleton orbits by giving them zero odd coefficient.

When an observer component is registered back through `retain_path_payload`, its source operation is explicitly **supplied**. The adapter does not install a new preparation operation or promote its own subtraction to source dynamics.

## 2. Reflection intertwines retained concatenation

Write x*y for the existing fixed-cut, endpoint-sewn bilinear path product. Graph reflection preserves endpoint compatibility and word cuts. Thus

    J(x*y) = (Jx)*(Jy).

This is simultaneous reflection of both factors, not reflection of only one operand. Keeping that distinction avoids assigning an incorrect parity to the product.

Writing x=x_even+x_odd and y=y_even+y_odd gives

    (x*y)_even = x_even*y_even + x_odd*y_odd,
    (x*y)_odd  = x_even*y_odd  + x_odd*y_even.

In particular, even*even and odd*odd are even; even*odd and odd*even are odd. This is a Z2 grading of the retained path algebra, not independent closure of both parity subspaces as algebras.

The checker exercises all basis pairs on the complete domains with operand lengths (1,1), (1,2), (2,1), (2,2): respectively 100, 160, 160 and 256 pairs, totaling **676**. It verifies reflection equivariance, the four homogeneous products, reconstruction and original source parents on every pair. Exact bilinearity extends these tests to arbitrary rational inputs on those domains. The structural argument extends the sign rule to other reflection-closed homogeneous word domains.

The source does not implement the displayed sums as a new preparation: the checker compares exact coefficient records and retains the original composed payload. The receipt includes a nonzero odd*odd witness, so the even-product conclusion is not merely a zero-product artifact.

## 3. Odd preparation followed by odd composition does not preserve the mode assumption

Two arbitrary supplied odd factors yield an even product. Therefore an odd-only restriction is not compatible with using unrestricted bilinear composition as an odd-sector continuation. Selecting odd inputs twice and then calling their product an odd prepared state is incorrect unless the product vanishes or another operation changes parity.

This is not a contradiction of the earlier odd moving-plane continuation. Equal-copy successor transport is linear in the inherited coefficient: it appends a neutral all-ones primitive payload, which is even. Odd*neutral-even remains odd. The checker constructs a nonzero example through the actual ledger.

Thus the continuation and preparation questions have different operand requirements. A controller or interaction must specify the parity of all factors, rather than import the linear successor result into a two-input composition claim.

## 4. Boundary and next executable test

The observer is a reversible accounting operation, not a physical measurement. Its coefficient norm is a counting metric, not a derived physical energy or probability. Neither independently prepared odd inputs nor native cross-word phase control is supplied by these tests.

The next executable test is to audit the existing controller masks and contexts under graph reflection. A single primitive selector may break parity, while a reflected pair of contexts may restore covariance on a larger retained carrier. Compute that distinction and retain rejected control records rather than assuming symmetry of the bare graph makes its chosen controller symmetric.

The scientific root remains null. Existing formal work-net and low-energy contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_symmetry_orbit_adapter.py
python research/scattering/seed-composition/check_symmetry_orbit_adapter.py --check
python research/scattering/seed-composition/check_parity_preparation_gate.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker uses exact rational coefficients, recomputes prior checks, and writes only its own receipt. `--check` is read-only.
