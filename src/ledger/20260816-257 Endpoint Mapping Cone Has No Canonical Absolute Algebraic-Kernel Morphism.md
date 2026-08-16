---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Endpoint Mapping Cone Has No Canonical Absolute Algebraic-Kernel Morphism

## Record

The next comparison proposed in entry 255 is finitely falsified before
coordinates are chosen. In the frozen coefficient calculus, the canonical
sewn endpoint mapping cone has no morphism into

\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle\subset H^2(S).
\]

The endpoint extension remains marked relative coefficient data. This
requires no new carrier incidence.

## Deutsch--Popperian conjecture

The hard-to-vary claim was

\[
\boxed{
\text{the source endpoint mapping cone canonically and horizontally maps
to }\mathcal A_{--}.
}
\]

Before computing a matrix, freeze the source objects and every available
nonzero canonical arrow. Let \(W\subset S\) be the finite marked wall and
\(U=S\setminus W\). The relevant localization sequence is

\[
H^2(S)\longrightarrow H^2(U)
\longrightarrow H^1(W)(-1)
\longrightarrow H^3(S).
\]

The endpoint cone realizes in \(H^1(W)(-1)\). The algebraic Gysin kernel
is a subobject of \(H^2(S)\), so its canonical arrow has the opposite
variance:

\[
\mathcal A_{--}\hookrightarrow H^2(S).
\]

Consequently the frozen arrow closure contains

\[
\text{EndpointCone}\longrightarrow H^1(W)(-1)
\longrightarrow H^3(S),
\]

and

\[
\mathcal A_{--}\longrightarrow H^2(S)
\longrightarrow H^2(U)
\longrightarrow H^1(W)(-1),
\]

but contains neither

\[
\text{EndpointCone}\longrightarrow H^2(S)
\]

nor

\[
\boxed{\text{EndpointCone}\longrightarrow\mathcal A_{--}.}
\]

This is the finite falsifier.

## Why the apparent shortcuts fail

The parent label \(e_6\) records integrand ancestry. Residue changes
support and cohomological degree, so ancestry is not a morphism back to the
absolute master.

Disjointness from the infinity divisor gives zero direct elliptic boundary
image. A zero image does not select a lift into the kernel of the infinity
map.

Finally, the generic algebraic kernel already splits without
\(\mathcal Q\) support (entry 211). Even a post hoc localization splitting
would therefore not provide a source-derived home for \(\mathcal Q\).

Any nonzero endpoint-to-\(\mathcal A_{--}\) map would require one of:

- a localization splitting or contracting homotopy;
- a separately derived physical relative-realization correspondence.

Neither datum is present in the frozen construction. Adding one after
seeing \(e_6\), \(v_{\rm alg}\), or \(\mathcal Q\) is prohibited.

## Classification

- endpoint mapping cone: marked relative coefficient data;
- finite wall: existing marked carrier;
- \(\mathcal A_{--}\): absolute algebraic coefficient subobject;
- \(e_6\) relation: ancestry only;
- direct Legendre image: zero;
- canonical endpoint-to-algebraic-kernel morphism: absent;
- genuinely new carrier datum: none.

Thus the source frame failure of entry 255 cannot be repaired by replacing
the frame with an absolute algebraic-kernel target. The two objects are
compatible outputs of the same carrier calculus, not canonically identified
coefficient objects.

## Update to the home of \(\mathcal Q\)

The following homes are now excluded:

1. the pure elliptic infinity-Gysin quotient;
2. the generic rank-seven algebraic connection and its internal extension;
3. the intrinsic endpoint-jet connection;
4. a canonical endpoint-to-\(\mathcal A_{--}\) comparison.

The surviving source-compatible alternatives are narrower:

\[
\boxed{
\text{physical moving relative-chain/discriminant extension}
\quad|\quad
\text{apparent cyclic/alphabet singularity}.
}
\]

This updates the shared-carrier conjecture positively but only narrowly:
all tested endpoint complexity remains coefficient or chain data over the
unchanged marked energy carrier.

## Exact evidence

- research/benincasa/marici-gm/src/bin/endpoint_to_algebraic_kernel_type_gate.rs;
- research/benincasa/endpoint-to-algebraic-kernel-type-gate.json;
- entries 211, 237, 245, 254, and 255;
- warning-denied Rust compilation and execution.

## Next hostile falsifier

Freeze the physical source chamber and its continuation prescription. At a
generic smooth point of \(\mathcal Q=0\), compute whether the physical
relative chain acquires a nonzero boundary variation while the absolute
Gauss--Manin connection remains regular.

The claim to test is

\[
\boxed{
\mathcal Q=0\text{ is a genuine collision divisor of the source physical
relative chain.}
\]

A surviving claim must exhibit the colliding source-defined boundary
components and a nonzero relative-homology monodromy class. If no such
collision exists, \(\sqrt{\mathcal Q}\) is apparent alphabet/cyclic data,
not coefficient support and not a carrier stratum.

## Outcome contract

~~~json
{
  "claim": "The canonical endpoint mapping cone admits a source-defined horizontal morphism into A_--.",
  "status": "falsified_by_type_and_variance",
  "endpoint_object": "marked wall relative coefficient object",
  "target_object": "A_-- subset H2(S)",
  "canonical_endpoint_to_H2_arrow": false,
  "canonical_endpoint_to_A_--_arrow": false,
  "e6_ancestry_is_coordinate": false,
  "zero_infinity_image_selects_kernel_lift": false,
  "new_carrier_incidence": false,
  "Q_remaining_homes": [
    "physical moving relative-chain/discriminant extension",
    "apparent cyclic or alphabet singularity"
  ],
  "next_experiment": "Compute source physical relative-chain monodromy around a generic smooth Q=0 point."
}
~~~
