# Exact finite Ramsey certificate interface

## Result and scope

The selected `finite-certificate-interface` attempt is implemented on the **candidate** even-sum lattice. `ramsey_certificate.verify(instance, certificate)` accepts exactly the declared well-formed finite homogeneous-copy records, under the ordinary mathematical interpretation of Python's built-in exact integers and finite JSON-shaped lists/dictionaries. Invalid records raise `CertificateError`.

Verification level: a written soundness/completeness/termination argument, code inspection and exact executable regression controls. This is not a proof-assistant verification of Python, a proof that every coloring contains a witness, or native Marici source admission. Execution resource exhaustion is not an invalid-certificate verdict.

## Frozen data interface

An instance has exactly these keys:

```text
N: nonnegative integer
r: positive integer
pattern: nonempty list of {label: nonempty string, point: [integer,integer,integer]}
coloring: list of {point: [integer,integer,integer], color: integer in [0,r)}
```

Pattern labels and points are separately distinct. Every pattern point has even coordinate sum; it need not belong to the finite region. Coloring entries are distinct even-sum points in `[-N,N]^3` and cover **all** such points exactly once. Booleans, numeric strings and floating-point values are not accepted as integers. Record order is not significant. Unknown keys are rejected rather than silently interpreted as native witnesses.

A certificate has exactly these keys:

```text
a: even-sum integer triple
m: positive integer
color: integer in [0,r)
image: nonempty list of {label: nonempty string, point: integer triple}
```

Image labels agree exactly with pattern labels. For each label s, its image is exactly `a + m*pattern[s]`, belongs to the colored region and has the claimed color. Image points are distinct. Translation a is not required to be inside the region; only the resulting image is. A singleton pattern and radius zero are valid. Positive dilation is allowed; collapsing scale zero is not.

Native construction histories are deliberately outside this interface. A supplied history field is not treated as verified history. A later typed native adapter must supply its own source-operation verifier.

## Complete-domain cardinality

Write E and O for the counts of even and odd integers in `[-N,N]`. Their sum is `2N+1` and their difference is `(-1)^N`. Hence

$$
|L_N|=E^3+3EO^2=\frac{(2N+1)^3+(-1)^N}{2}.
$$

After checking that all supplied coloring points are distinct members of L_N, equality of the supplied count with this number is equivalent to complete coverage. This avoids enumerating a huge requested region merely to reject an obviously incomplete record. The argument depends on membership and uniqueness checks: a count alone would be insufficient.

## Soundness, completeness and termination

**Soundness.** Successful type checks give exactly the declared finite domains. The cardinality argument gives a complete coloring, not a partially observed one. Label equality identifies each supplied image with its pattern point; exact coordinate equality enforces the same translation and positive scale for every label. Region membership and color lookup then establish containment and homogeneity. Positive scale and distinct pattern points imply injectivity; the implementation also explicitly checks distinct image points. Therefore every accepted pair is a valid certificate for the frozen predicate.

**Completeness.** Conversely, serialize any instance and witness satisfying the frozen predicate in the declared interface. All membership, type, distinctness and range checks hold. Completeness supplies the required coloring count. The labelled homothety, containment and common color satisfy the remaining comparisons. The verifier accepts, independently of record order. This is completeness of checking an already supplied witness, not a guarantee that a witness exists.

**Termination.** Checks traverse finite supplied records and fixed-length triples. Integer comparisons, sums, products and exponentiation have finite operands; the only variable exponent is the finite nonnegative integer N in `(-1)^N`. There is no search over witnesses or unbounded tower construction. In the idealized exact-integer model this terminates for every finite input. No practical memory/time guarantee for arbitrarily large encodings is claimed.

## Executable evidence

- Implementation: `research/voevodsky/ramsey_certificate.py`.
- Independent regression/oracle checker: `research/voevodsky/checkers/check_ramsey_certificate_interface.py`.
- Result with replayable accepted fixtures, rejected controls and source hashes: `research/voevodsky/results/ramsey-certificate-interface-v1.json`.
- Scope: `D3-labelled-homothety-verifier-v1`.

The checker uses separately declared tetrahedral/octahedral templates and compares them with the net's templates. It independently enumerates small lattice boxes to check the region-size formula, exercises reordered and translated/scaled positive fixtures and malformed controls, and compares verifier decisions with a separate direct color oracle over every binary coloring of L_1 for the tested unit-scale tetrahedral placements. These bounded checks do not replace the written all-input argument or establish any Ramsey forcing bound.

Run:

```text
python research/voevodsky/checkers/check_ramsey_certificate_interface.py
```

The parent Ramsey objective, source admission, uniform forcing, native construction and naturality claims remain open. The frozen selected interface attempt stops here; no further scientific attempt is implicitly selected.
