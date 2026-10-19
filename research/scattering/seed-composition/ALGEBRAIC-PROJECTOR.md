# An exact algebraic spectral split retains the complementary sector

**Iteration 9 of the requested ten-turn work-net run.**

**Strength:** exact algebraic projector identities, explicit branch conditions and local agreement with the moving-plane construction. Not native preparation, a physical measurement or a two-output particle construction.

[Previous rational-operation gate](RATIONAL-NORMALIZATION-GATE.md) · [Checker](check_algebraic_projector.py) · [Receipt](results/algebraic-projector.v1.json)

## 1. Fresh branch data

Finite rational operations cannot select the moving plane or its gain as exact parameterized functions. This turn explicitly permits the additional algebraic determinant branch instead of hiding that operation inside a coordinate change.

Let delta(z) be the selected determinant branch already specified by its degree-six equation and delta(1)=1. Define

    epsilon=-z^5/delta,
    tau=-(z^4+z^5)/(delta-epsilon).

Then the characteristic polynomial factors as

    f(lambda)=lambda^2-tau lambda+delta,
    g(lambda)=lambda^2+tau lambda+epsilon,
    chi=f g.

The checker verifies the factorization after clearing denominators using the determinant branch equation; this is not only a Taylor comparison. At z=1,

    f=lambda^2+lambda+1,
    g=lambda^2-lambda-1.

Along positive z, delta>0 and epsilon<0. The selected branch is continued from the reference sector, not chosen anew among roots at each parameter. Thus delta-epsilon never vanishes on that axis.

## 2. Explicit projector without individual eigenvectors

Write

    R=(epsilon-delta)^2+2 tau^2(delta+epsilon),
    h(lambda)=2 tau^2+epsilon-delta-2 tau lambda.

The polynomial h is an inverse numerator for g modulo f:

    g h = R mod f.

For the actual four-dimensional operator M(z), define

    Pi = g(M) h(M) / R.

The checker verifies universal polynomial remainder identities modulo f g. By Cayley–Hamilton they give

    Pi^2=Pi,
    Pi M=M Pi,
    f(M)Pi=0,
    g(M)(I-Pi)=0,
    Pi(I-Pi)=0.

The ranks are two and two while f and g are coprime. R is their inter-sector resultant; at z=1, R=4.

No individual eigenvector, eigenvalue ordering inside the selected pair, or diagonalization at the defective point is used.

## 3. The internal collision does not make this projector singular

The prior positive-axis audit proves that the selected and complementary root clusters remain disjoint for all z>0. Hence R never vanishes there, including at the selected pair's internal collision z_c.

The projector selects the full generalized eigenspace when f has its double root. Its denominator does not divide by the selected pair's own discriminant. This is why the plane and projector remain regular even though a basis of individual eigenvectors and a positive invariant metric fail at that collision.

This conclusion is specific to the continued selected/complementary splitting on the positive axis. Complex-parameter branch changes and possible inter-sector collisions are not erased by this formula.

## 4. Check against the independently constructed moving graph

The checker evaluates the algebraic formula as a local series around z=1 using the independently checked trace and determinant jets. Through order four it verifies:

- projector idempotence and commutation with the actual M(z);
- trace equal to two;
- annihilation of the complementary record;
- Pi applied to the Riccati graph frame equals that same frame.

Thus the projector follows the intended local branch rather than merely being some idempotent with the same dimension. The receipt includes the base projector, its complement and the full checked jet.

The universal identities establish the exact algebraic formula. The finite series check establishes agreement with the prior local construction; it is not presented as an exact polynomial expression for the projector in z.

## 5. Retain both records

The map

    x -> (Pi x,(I-Pi)x)

is reversible by adding the two outputs. The complementary two-dimensional information is not discarded. The original full history, predictor residuals and preparation-reject records likewise remain outside this selected-sector observer and are not silently erased.

At z=1 the computed projector is not symmetric in the four-carrier's ordinary coordinate-counting metric. Correspondingly,

    Pi^t Pi + (I-Pi)^t(I-Pi) != I

in that metric. A reversible algebraic decomposition is therefore not automatically a counting-norm isometry, an orthogonal measurement or a Born-probability split. A physical preparation/measurement interpretation would need its own source and metric justification.

The algebraic branch selection itself is still an added mathematical operation. Its exact specification and successful verification do not establish that the underlying seed dynamics implements it, or the determinant-normalizing gain from the preceding turn.

## 6. Next source-level gate

This projector acts on the **four-dimensional correlated boundary carrier** constructed earlier. It must not be confused with a projector on all twelve displayed occurrences, or with two independent photon outputs merely because its rank is two.

The next executable test is to lift the selected/complementary split to that original twelve-occurrence boundary space, compute spectral multiplicity there, and identify any additional correlation selection needed to recover this carrier. That checks whether the current construction preserves the actual source degrees of freedom before stronger output claims are contemplated.

Existing work-net contracts and formal outcomes remain unchanged. No physical annihilation, independently prepared photons or ratio 372 is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_algebraic_projector.py
python research/scattering/seed-composition/check_algebraic_projector.py --check
python research/scattering/seed-composition/check_rational_normalization_gate.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All polynomial remainders and series identities use exact rational arithmetic. The checker recomputes the preceding algebraic data and writes only its own receipt; `--check` is read-only. No source-owner physical replay or formal admission is claimed.
