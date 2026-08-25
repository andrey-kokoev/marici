# Every minimum Wilson family has the same hidden orientation C2

Owner: `marici.Kitaev`

Terminology note: “orientation” here means the (B)-simple-current signed
Wilson frame, not clockwise/counterclockwise ribbon orientation. The family
census is unchanged.

## Family-independent classification

There are eight faithful four-port families. The checker reconstructs each
codebook from the Wilson eigenvalue table and exhausts all (4096)
coordinatewise signed-affine actions for each family: (32768) transformations
in total.

Every family has setwise stabilizer exactly (C_2). Its generator conjugates
the unique port drawn from the (D/E) magic species:

- conjugate (D) in a family containing (D);
- conjugate (E) in a family containing (E).

In every case the induced sector permutation is

\[
(A\ B)(D\ E),
\]

with (C,F,G,H) fixed.

## Explanation

Every minimum faithful family must contain one port from each of the two magic
species. The (D/E) species is the antisymmetric orientation coordinate: its
sign distinguishes (A) from (B) and (D) from (E). Conjugating that
single coordinate reverses both distinctions without leaving the codebook.

The orientation ambiguity is therefore not a defect of resource-optimal CDFG.
Changing to any other minimum family preserves it.

## Consequence

Every minimum four-port compiler needs one independently rooted orientation
bit unless its physical constructor derives an absolute orientation. Family
selection cannot remove the (C_2) quotient.

## Boundary and falsifiers

- Larger-than-minimum faithful families are not classified here.
- Non-affine, nonunitary, and leakage faults remain outside the census.
- A minimum family with stabilizer other than (C_2) falsifies universality.
- A generator not supported on the unique (D/E) port falsifies the species
  explanation.

## Artifacts

- Checker: `checkers/check_s3_minimum_family_orientation_stabilizer.py`
- Result: `results/s3-minimum-family-orientation-stabilizer.json`
- Result SHA256:
  `47133CB3BA812DFFA67CB25390AFB09D5EDE6A63C3562B5A9BC864E17D14FE1C`
- Graph admission: `ev-000000003515-6e32bf6f-4fd4-4561-a22b-ad879c9e0646`
- Ledger: entry 2526, `seqclaim-c413490db339c7a496552228`
