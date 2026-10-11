# Fixed-reversal closure conjecture: a failed finite candidate

## Frozen test

Use the same coefficient reversal, allowed attachments, and observable in both putative isotope branches:

- Reverse all proton coefficient arrows, retaining their weights. This is K-linear dualization, not conjugate reversal.
- Allow only the 24 rigid vertex identifications of the tetrahedron. Apply each identification to the triangle labels and its induced orthogonal map to the spatial coefficient axes.
- Require the aligned reversed return E to preserve the retained source states: E N = N.
- Seek both a direct closure and a distinct closure requiring an additional retained complex.

The last condition necessarily requires at least one direct closure. No complex phase alignment is admitted as a repair in this test.

These rules define an explicit finite candidate. They are not yet derived from the outward geometric construction. This test sharpens the previous alignment audit into a counterexample to its proposed two-closure interpretation; it is not a previously unseen prediction of that audit.

## Outcome: no direct closure

All 24 permitted identifications fail, even on one particular retained state w: the first column of N. Exactly Nw=w, but E_S w differs from w for every permitted alignment S.

The result file records an output port and its exact nonzero discrepancy for each alignment. Since the source N has rank one and every column is proportional to w, testing E_S w=w is equivalent here to E_S N=N. This is not an unnecessarily strong demand that the two operators agree on all raw inputs.

Therefore this frozen candidate fails its necessary prediction: it lacks the direct, hydrogen-like branch. No search for a second closure can repair the absence of the first under these same rules.

This refutes the specified finite candidate, not every possible outward-electron attachment law or the neutron-as-glue conjecture in general.

## Why the geometry has not selected the coefficient rule

The oriented tetrahedral boundary has only real signed incidence coefficients. Transpose reversal and Hermitian-adjoint reversal agree on those incidence matrices. Both obey the geometric reversal and boundary identities.

But they differ on the actual complex proton coefficients. Thus the geometric incidence data supplied so far do not discriminate between these two extensions. Selecting unchanged weights is an additional rule, not a deduction from outward branching.

The checker verifies both statements exactly. This locates the missing specification rather than hiding it in an isotope-dependent choice.

## Controls are not rescues

The adjoint rule closes on the retained image. The previously constructed complex phase identification also repairs the transpose mismatch. Both remain outside this test's frozen rule set.

A phase identification does not by itself force an intermediate object. For the first column w of N, put

```text
A = diag(1 / conjugate(w_i)),
B = diag(w_i),
D = B A.
```

The intermediate coordinate copy in A followed by B can be contracted to the interface map D without changing its coefficient action. This checks a particular factorization, not removal of every possible retained complex. It shows why distinguishing a necessary nonidentity map from a necessary extra object matters.

If a retained-history observable forbids that contraction, its specification must be fixed independently of which branch is to be called deuterium. Such an observable has not been supplied by this calculation.

## Next substantive obligation

Supply an outward construction that determines its complex coefficient action and its attachment identifications, rather than specifying only real incidence arrows. With those rules fixed, test direct closure again. Only after that succeeds is there a hydrogen-like branch to compare against a proposed nonremovable second closure.

No isotope assignment or new Three.js particle geometry is added by this failed test.

## Reproduce

```text
python research/voevodsky/checkers/check_fixed_reversal_closure_conjecture.py
```

Thirteen verification checks pass, while the conjecture status is explicitly `refuted_under_frozen_contract`. Artifact: `results/fixed_reversal_closure_conjecture.json`. It includes the fixed contract and hash, freshly verified source root and hash, checker hash, retained input state, and 24 exact counterexamples. The source is unchanged.
