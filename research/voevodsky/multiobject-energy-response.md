# Multi-object orbital continuation — iteration 5 of 5

## Real-axis dispersive follow-up

`offcenter-endpoint-dispersion.md` now certifies real-axis pair/vector endpoint
real parts at E=2,4 and restricted-fixture flux with 37 checks. It does not assign
those endpoint values to the distinct Slater-record triple channel.

## Result

Extended the genuine orbital-channel responses away from the common band-center
fixture. **98 checks pass** with current source hashes:

- Certified real-axis spectral densities/widths for all three output vertex types
  at E=2 and E=4, with reflected triple values at E=10 and E=8.
- Fifteen certified complex-energy resolvents, including both real and imaginary
  parts, at z=E+8i for E=2,4,6,8,10.
- Threshold, positivity, causality, spectral reflection and resolvent-norm controls.

The complex responses are **not** substituted for on-shell responses. Triple
principal-value real parts away from E=6 remain an executable open gate.

## 1. Fresh retained model

Freshly read `combined-orbital-scattering.md` and reload checked orbital,
distinct-record and combined-scattering receipts. Retain independent half-line
positions, the product endpoint and Slater |0 wedge 1 wedge 2> vertices, and the
scalar/vector projectors. No dispersion, statistics or coupling is recalibrated.

The pair band is [0,8]. Both triple bands are [0,12], but their vertex measures
are different: ordinary endpoint convolution versus Vandermonde-weighted Slater
measure. All densities are infinite-volume measures, not finite-box poles.

## 2. Off-center real-axis widths

The endpoint pair/vector densities use the preceding exact square-root box
construction. Generalize the scalar-record density to arbitrary grid-compatible E:

    rho_A(E)=(1/6) integral rho_1(x)rho_1(y)rho_1(E-x-y)
                      (x-y)^2 (x-(E-x-y))^2 (y-(E-x-y))^2 dxdy.

Every radicand and squared-difference factor is enclosed over each rectangle.
Integer square roots and rational pi bounds retain a genuine integral certificate.
The checker uses meshes 128,256,512 and verifies decreasing widths and exact
reflected box bounds for both triple measures.

Outward-rounded containing intervals at the finest mesh are

| Energy | Pair rho_2 | Vector triple rho_3 | Scalar-record triple rho_A |
|---:|---|---|---|
| 2 | [0.1169074,0.1184042] | [0.0160000,0.0168134] | [0.00009898,0.00014300] |
| 4 | [0.2693972,0.2709804] | [0.1220800,0.1246844] | [0.0484011,0.0579132] |

The matrix widths follow directly:

    Gamma_2(E)=2pi lambda_2^2 rho_2(E) P_s,
    Gamma_vector3(E)=2pi lambda_vector3^2 rho_3(E) P_v,
    Gamma_A(E)=2pi lambda_A^2 rho_A(E) P_s.

The input pair width uses rho_2 times I_4. All three measures have positive weight
at E=2,4. The small scalar triple weight at E=2 is a certified manifestation of
its distinct orbital spectral law, not an inferred photon suppression factor.

## 3. Threshold opening does not authorize nonexistent incidence

| Energy | Pair density | Triple densities | Chosen pair incidence |
|---:|---|---|---|
| 0 | zero | zero | threshold, no finite-flux assignment |
| 2,4,6 | positive | positive | open |
| 8 | zero | positive | upper pair threshold |
| 10 | zero | positive | pair channel closed |
| 12 | zero | zero | channels at/beyond upper thresholds |
| 14 | zero | zero | channels closed |

At E=8 the triple densities equal their E=4 values by reflection; at E=10 they
equal E=2 values. The pair density vanishes at and beyond its upper edge.
Thus open triple output fibers above eight do not imply an incoming pair with
that energy exists in this particular dispersion model. A probability for such
an incident pair would be a type/kinetic error.

Real-axis widths alone do not determine scattering: dispersive real parts also
enter the core denominators. No off-center flux probabilities are assigned here.

## 4. Certified complex-energy self-energies

For a normalized vertex measure on [0,4k], expand around its spectral midpoint:

    g(z)=sum_(n>=0) <(H-2k)^n>/(z-2k)^(n+1).

Compute centered moments exactly from the already specified endpoint Catalan
convolutions or exterior-power determinant moments. Since ||H-2k||<=2k, for
Im z=eta>2k the tail after N+1 terms satisfies

    |tail| <= (2k/eta)^(N+1)/(eta-2k).

The checker uses eta=8 and N=128. Exact arithmetic in Q(i) gives both response
components; the common norm-error bound is applied outward to each component.
All fifteen certificates have error below 10^-15.

For illustration, at z=4+8i the responses are approximately

| Vertex measure | Re g | Im g |
|---|---:|---:|
| Pair endpoint | 0 | -0.121369370895588 |
| Vector triple endpoint | -0.026324537902294 | -0.113897084315978 |
| Scalar triple Slater records | -0.028284692352757 | -0.116351252902151 |

Exact enclosing endpoints are retained in the receipt. Multiplication by the
appropriate lambda squared and typed projector gives the full self-energy
matrix. The scalar and vector triple responses remain measurably different away
from center energy; orbital records have not disappeared into a channel label.

Controls check

    Im g(z)<0, |g(z)|<=1/eta,
    g(4k-E+i eta)=-conjugate(g(E+i eta)).

A further negative-imaginary bound follows from the positive normalized measure:
Im g(E+i eta)<=-eta/[max(E^2,(E-4k)^2)+eta^2]. It is independently checked against
the certified component intervals.

## 5. Important distinction: eta=8 is not the boundary limit

These complex values are bona fide self-energies at specified complex spectral
parameters. They are not a computed eta->0 limit, a physical damping model, or
retarded real-axis principal-value certificates. The Neumann bound used here
requires eta>2k and cannot be extrapolated through the propagating band.

At E=6 the earlier real-axis triple real parts vanish exactly by symmetry and
full flux normalization is checked. Away from that center the real-axis triple
real parts remain uncomputed. Reporting the broadened values as those real parts
would silently change the model; this turn does not do that.

## 6. Status after the five-turn orbital construction

Constructed and source-bound:

1. Independent-position pair and bosonic triple orbital Hamiltonians.
2. Product-endpoint and distinct-record exchange-symmetric attachment vertices.
3. Their exact infinite spectral measures and matrix-valued self-energy formulas.
4. Certified below-band, selected real-axis width and complex-energy responses.
5. A normalized combined on-shell bright-channel scattering fixture at E=6,
   including covariance and coupling sensitivity.

Not established:

- Off-center real-axis triple principal-value responses and corresponding flux.
- A source-derived coupling to the native full-spinor/mismatch core.
- Physical positron/photon channels, calibration or the working ratio 372.

The narrower conditional orbital construction is now explicit and reproducible;
it must not be inflated into those further results.

## 7. Nonredundant next action

Integrate the last one-body spectral variable analytically in the off-center
triple resolvent. For the Slater vertex its polynomial factors can be divided by
z-x-y-t, expressing the inner integral through the exact one-body g_1 and moments.
Enclose the remaining branch-point integrals with adaptive interval partitions.
Then propagate those real-axis self-energy bounds through the combined core
optical identities. This avoids substituting finite eta for a real-axis limit.

## Reproduction

```sh
python research/voevodsky/checkers/check_multiobject_energy_response.py
```

Receipt: `results/multiobject_energy_response.json`, retaining exact off-center
density bounds, threshold table, certified complex responses and source hashes.
