# The SCC all-interfaces-checked flag tests descriptor membership, not radial G4 conformance

## Question

Does the current SCC result `all_interfaces_checked: true` expose enough of `conservative_green_complex` to compare it with the source-derived radial boundary feature?

## Claim boundary

No. The compiler checks that every constructor names the shared `g4_common` descriptor and has no override. That descriptor contains five coarse metadata fields but no carrier maps, traces, metrics, return variance, arithmetic loading, or codiagonal. The pass is valid for the contract it implements, but it is not a pullback or conformance check against the radial interface.

## Contract readback

The current `g4_common` descriptor declares only:

1. `coefficient_object`;
2. `completion`;
3. `topology`;
4. `quotient`;
5. `authority`.

The compiler freezes exactly these fields in

```text
G4_INTERFACE_FIELDS=(
  coefficient_object,
  completion,
  topology,
  quotient,
  authority
)
```

and accepts an edge when its constructor has

```text
interface_ref == g4_common
```

and no `interface_overrides`. The hostile called `interface_mismatch_rejected` changes only the reference to an undeclared descriptor. It does not perturb any mathematical map because none is represented.

## Meaning of the pass

The result

```text
all_interfaces_checked: true
```

therefore certifies:

- descriptor existence;
- nonempty coarse metadata;
- uniform descriptor reference;
- absence of undeclared overrides.

It does not certify equality or compatibility of source and target columns, trace maps, Green forms, or feature codiagonals. Calling the compiler output an `interface_pullback` does not construct a categorical pullback when the compared arrows are absent.

## Missing radial fields

The source-derived radial comparison now requires at least:

1. carrier for \(\partial_t\oplus(-\partial_t)\) or an explicit comparison map from it;
2. complete directed wall trace \((\gamma_+,\gamma_-)\);
3. endpoint feature maps \((E_+,E_-)\);
4. function-valued Wronskian maps \((W_+,W_-)\);
5. Green or Krein feature metric;
6. source injection \(U_X^{\rm rad}\);
7. return map with declared Hermitian-adjoint or analytic-transpose variance;
8. arithmetic coefficient by prime and grade;
9. prime-diagonal or cross-prime return structure;
10. codiagonal preserving wall signs and the Wronskian coefficient \(-1/2\);
11. rigged seam domain and compact-local jet topology;
12. witness locators and digests for each map.

Without these fields, both the valid radial model and hostile models with reversed wall signs, missing Wronskian incidence, or the wrong return variance inhabit the same `g4_common` metadata class.

## Cheapest contract strengthening

A backward-compatible SCC revision need not assert radial conformance. It can add an optional typed subdescriptor for `conservative_green_complex` and classify each required map as:

- `constructed` with witness;
- `open` with exact dependency;
- `not_applicable` with source authority.

The checker should then include hostiles that independently reverse one wall sign, replace \(-1/2\) by another coefficient, erase one Wronskian channel, exchange adjoint and transpose, alter the arithmetic loading, and introduce a cross-prime return. Passing those hostiles would make the interface claim informative.

## Direction rescore

- SCC interface exposure: 10/10, but Aspect-owned and unavailable for mutation without crossing authority.
- Further inference from `all_interfaces_checked`: 0/10.
- Finite radial--G4 comparison under the current descriptor: 0/10 because the target arrows are absent.
- Preparing exact conformance requirements and hostiles: completed in this packet.
- Adjoint/transpose analysis independent of G4: 9/10 and the next available depth-first lane.

## Disposition

The top-ranked direction is mechanically blocked at interface representation, not at another radial calculation. The current SCC pass remains a topology and coarse-metadata certificate. It cannot decide whether `conservative_green_complex` realizes the six-coordinate radial feature. No RH conclusion is authorized.
