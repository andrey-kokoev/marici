# No faithful subset of the available Wilson ports removes orientation C2

Owner: `marici.Kitaev`

Terminology note: the (C_2) below is the (B)-simple-current signed Wilson
frame. It is distinct from geometric ribbon reversal. The no-go is unchanged.

## Redundancy question

Can one eliminate the hidden orientation bit by measuring more than the
minimum four Wilson ports, especially by including both (D) and (E)?

## Complete subset census

Among subsets of (C,D,E,F,G,H), exactly fifteen are faithful on the eight
sectors:

- eight families of size four;
- six families of size five;
- the full size-six family.

The checker exhausts the coordinatewise signed-affine group for every one of
them. All fifteen have setwise stabilizer exactly (C_2), inducing

\[
(A\ B)(D\ E).
\]

For a family containing one of (D,E), the generator conjugates that port.
For a family containing both, it conjugates both simultaneously. In
particular, the full codebook (CDEFGH) retains the ambiguity.

## Explanation

The orientation automorphism is already present on the full six-coordinate
Wilson packet. Faithful subfamilies are projections of that packet. Exact
enumeration shows that none has a smaller stabilizer. Extra available Wilson
coordinates therefore add redundancy without supplying absolute orientation.

## No-go

No choice among the available Wilson spectral ports can replace the external
orientation root. The only remedies within the present typing are:

1. an independently rooted orientation datum;
2. a physical constructor that derives absolute (D/E) orientation;
3. a new observable outside the (CDEFGH) packet that breaks the (C_2).

## Boundary and falsifiers

- Observables outside (CDEFGH) are not classified.
- Non-affine, nonunitary, and leakage faults remain outside the action census.
- A faithful subset with trivial signed-affine stabilizer falsifies the no-go.
- A new typed observable odd under the (C_2) may break the ambiguity.

## Artifacts

- Checker: `checkers/check_s3_all_faithful_family_orientation_no_go.py`
- Result: `results/s3-all-faithful-family-orientation-no-go.json`
- Result SHA256:
  `844D03B01E8454A5AAFCB0912EE6E07B4A768E623C848D6CE76044EF0E4F2D03`
- Graph admission: `ev-000000003517-2edc45c0-850b-4c12-99f0-c5f29c1daf67`
- Ledger: entry 2527, `seqclaim-dd896c00cff558a906ca500d`
