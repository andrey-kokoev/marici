# Exact normalization requires an algebraic selection beyond finite rational transport

**Iteration 8 of the requested ten-turn work-net run.**

**Strength:** exact field-of-definition obstruction for a declared finite operation class, plus algebraic branch equations. Not a no-go for every source operation, approximation, spectral calculus or physical mechanism.

[Previous conditional metric](CONDITIONAL-BOUNDARY-METRIC.md) · [Checker](check_rational_normalization_gate.py) · [Receipt](results/rational-normalization-gate.v1.json)

## 1. Fresh state and tested operation class

The moving selected plane admits a conditional positive invariant metric below the collision after multiplying its step by g(z)=delta(z)^(-1/2). That scalar is not a coordinate change; it changes eigenvalue moduli.

Test the class of **uniform exact maps with coefficients in Q(z)** obtained from:

- finitely many rational incidence maps and sums/products;
- rational invertible coordinate changes;
- finite rational auxiliary blocks and their Schur complements;
- fixed finite fiber means and retained-coordinate reindexing.

This class is closed under those operations. Retaining additional records does not by itself introduce algebraic coefficient functions.

The scope excludes supplied algebraic branches, arbitrary function-valued coefficient payloads and infinite limiting/functional-calculus constructions. The source ledger can accept supplied coefficients; that API ability does not derive the coefficient functions under discussion. The claim concerns exact families on a nonempty open parameter set, not just z=1 or finite-order Taylor approximations.

## 2. The selected plane has no rational frame or projector

The actual four-family has characteristic polynomial

    chi(lambda,z)=lambda^4-z^4 lambda^2-(z^4+z^5)lambda-z^5.

Specialize z=2:

    chi(lambda,2)=lambda^4-16lambda^2-48lambda-32.

Modulo 13 this quartic has no root and no monic quadratic factor. The checker evaluates all thirteen field elements and divides by all 169 monic quadratics. A reducible quartic must have a factor of degree one or two, so this certifies irreducibility of the specialization over Q.

Because chi is monic with integer polynomial coefficients, a factorization over Q(z) would give monic polynomial factors by Gauss' lemma/integral closure; specialization would preserve their positive degrees. Thus chi is irreducible over Q(z).

A rank-two invariant subspace defined over Q(z) would factor the characteristic polynomial into the characteristic polynomials on that subspace and quotient. Therefore the selected analytic two-plane cannot have an exact rational frame or rational rank-two spectral projector on an open parameter set.

This does **not** say that rational M(z) cannot act on the selected plane: it already does. The obstruction is to defining/selecting that plane by rational coefficient data. Its local analytic and positive-real-axis continuations remain valid.

## 3. The determinant and normalization are nonrational too

Let delta be the product of the two selected eigenvalues. The complementary product is -z^5/delta. Their sum

    u=delta-z^5/delta

satisfies the pairing resolvent

    u^3+z^4 u^2+4z^5 u-z^8(z-1)^2=0.

At z=2 this becomes

    u^3+16u^2+128u-256.

Its values modulo 5 are (4,4,2,4,1), so it has no field root and is irreducible. The same monic-specialization argument makes the resolvent irreducible over Q(z).

If delta were rational in z, u would be rational, contradicting that irreducibility. Hence delta is not in Q(z). Nor can g=delta^(-1/2) be rational, since then delta=g^(-2) would be rational.

Thus finite rational incidence operations and Schur elimination cannot exactly supply the proposed gain as a parameterized scalar function. Arbitrarily adding rational auxiliary coordinates does not evade this conclusion. A larger operation class may do so; it must be named and justified.

## 4. Give the missing algebraic operation an exact specification

Clearing denominators in the resolvent gives an equation for the determinant:

    delta^6 + z^4 delta^5 + z^5 delta^4
    - z^8(1+z^2)delta^3 - z^10 delta^2
    + z^14 delta - z^15 = 0.

At (z,delta)=(1,1), the derivative with respect to delta is 8. Thus delta(1)=1 selects a unique local analytic root, whose derivative is 5/2. This agrees with the earlier independently computed moving-plane jet.

Substitute delta=g^(-2) and clear g^12:

    1 + z^4 g^2 + z^5 g^4
    - z^8(1+z^2)g^6 - z^10 g^8
    + z^14 g^10 - z^15 g^12 = 0.

At (z,g)=(1,1), the derivative with respect to g is -16. The base value g(1)=1 therefore determines a unique local analytic gain branch, with derivative -5/4, again matching the previous jet.

These equations are exact specifications of an algebraic branch-selection operation. They are not an authorization to call that selection native dynamics, nor a proof that the source implements the gain. The displayed polynomial degrees are not asserted to be minimal degrees for the selected branches.

## 5. What remains possible

The obstruction does not reject:

- the existing base-point construction at z=1;
- finite-order rational approximations to the analytic branches;
- an algebraic field extension with a declared branch;
- infinite spectral/functional-calculus limits with their own convergence and source conditions;
- an independently supplied physical control law that actually realizes the required operation.

The next executable step is to construct an exact algebraic spectral projector with explicit branch conditions and retain its complementary record. This will distinguish an available mathematical selection recipe from the still-missing source authority for using it as a preparation or normalization.

No conditional scalar is promoted to physical energy, a clock law or an emitted-particle count. Existing work-net contracts and formal outcomes remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_rational_normalization_gate.py
python research/scattering/seed-composition/check_rational_normalization_gate.py --check
python research/scattering/seed-composition/check_conditional_boundary_metric.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker performs exhaustive finite-field certificates and exact polynomial eliminations with the standard library, checking the base derivatives against prior source jets. It writes only its own receipt; `--check` compares read-only. The field-of-definition conclusions use the explicitly stated algebraic arguments, not a new machine-formal admission.
