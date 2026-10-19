# Retained word composition works; its multiplicative shortcut still fails mode transport

**Strength:** source-backed finite retained-word construction plus an exact polynomial obstruction for one specified coefficient readout. No physical preparation, state-space factorization, metric/face transport or formal outcome admission.

[Previous incidence audit](INCIDENCE-AUDIT.md) · [Checker](check_retained_word_transport.py) · [Receipt](results/retained-word-transport.v1.json)

## 1. Use an existing operation, not a fitted photon operator

The existing [retained weighted-path construction](../../nima/retained-path-family-composition-synthesis.md) provides an explicit operation:

- match endpoints;
- concatenate complete primitive words;
- multiply the operand coefficients;
- retain registered operand identities, assembly trees and parent-slot bindings.

The new checker instantiates the actual `RetainedSuccessorLedger` from `research/nima/checkers/retained_path_successor.py` on the ten owner-labelled primitive arrows of the supplied three-vertex candidate. It uses the existing methods, rather than replacing them with a desired output matrix.

This is authorization at the **finite combinatorial API** level only. Its supplied rational coefficients are not automatically physical amplitudes, and using the same coefficient vector as both operands of a bilinear composition is not a linear quantum-state evolution.

Each displayed edge is constructed as a retained singleton family of primitive length one or two. Every composite has its actual source parents and slots. Zero product coefficients retain both the word and its parents. Consequently deconstruction can recover the stored operands even when multiplication itself is noninvertible.

The displayed coordinate values alone are not reversible: replacing (c,d)=(5,7) by (1,35) leaves c*d unchanged. The retained records distinguish the two preparations. This is provenance recovery, not an inverse of multiplication.

## 2. Word expansion commutes with composition, but not with a common step count

For a displayed macro-edge e, let w(e) be its retained primitive word. For every endpoint-compatible pair of macro-paths p,q,

    w(p q) = w(p) w(q).

This follows directly from concatenation, without adding coefficients or identifying opposite arrows. The checker verifies all cuts of both proposed output graphs' macro-paths through length four: 12, 20, 32 and 52 records at the four successive grades.

**Flat words alone do not recover macro-paths.** In the first output,

    w(AC) = (AB,BC) = w(AB then BC).

One macro-edge and two macro-edges have the same flattened word. Also the CA macro-edge in each of the two outputs expands to the same (CB,BA), so flattening erases the output-pair identity.

Retain the pair label and the sequence of segment lengths along with the primitive word. These data recover the macro-path uniquely: within each pair, distinct displayed edges have distinct primitive words, and the stored segmentation identifies each block. The checker verifies injectivity on the enumerated grades. This retains an existing presentation; it does not prove physically independent sectors.

A second distinction is the continuation clock. Starting with the first output's CA word (CB,BA), two allowed macro-extensions are:

    CA then AB -> (CB,BA,AB),       primitive length 3;
    CA then AC -> (CB,BA,AB,BC),    primitive length 4.

Both are one macro-extension, but one adds one primitive step and the other adds two. Therefore literal expansion cannot identify macro continuation with one fixed-length primitive extension. A boundary-aware, variable-length operation would have to be specified. This is a grading issue, not an established physical-time obstruction.

The existing weighted-family API correctly rejects a single supplied family mixing primitive lengths one and two. We keep the heterogeneous collection as separate registered families; we do not silently bypass the source type restriction.

## 3. Test the actual multiplicative alternative to additive path sums

Retain the previous coordinate order

    (a,b,c,d,e,f,g,h,i,j)
      =(AB,BC,CD,DE,EA,AEp,EpDp,DpC,CB,BA).

The existing coefficient multiplication gives the displayed readout

    q1 = (a,b,i*j,c*d,e,a*b),
    q2 = (f*g,h,i*j,i,j,a*b).

Unlike the previous additive B, this is a polynomial map. The same supplied primitive coordinate is reused each time its primitive occurrence is encountered. Independently supplied path-family coefficients would be different input data, not this construction.

We now ask a necessary question that does not require guessing input dynamics:

> Can a nonzero output in the two reference photon planes and its next reference continuation step both belong to this multiplicative image?

Use the same endpoint-checked shared-edge relabellings and the same source reference plane and continuation as in the previous audit. Give the two planes parameters (s,t) and (u,v). Their occurrences, in the displayed order, are

    q1 = (-s,(s+t)/2,s,s,-(s+t)/2,-s),
    q2 = (-u,(u+v)/2,u,u,-(u+v)/2,-u).

Membership in the multiplicative image is equivalent to

    u = s,
    rminus = s*(s+t-2) = 0,
    rplus  = s*(s+v+2) = 0.

Necessity comes from the two shared products a*b and i*j. Sufficiency is constructive: choose

    a=-s, b=(s+t)/2, c=1, d=s, e=-b,
    f=1, g=-s, h=(s+v)/2, i=s, j=-h.

The exact polynomial checker verifies that this representative's only output discrepancies are -rminus/2 and -rplus/2 on the shared product coordinates. Thus the claim is not based only on sampled values.

## 4. Exact one-step obstruction

The reference step on each plane is

    T(s,t) = ((-s+t)/2,(-3s-t)/2).

At the next step, equality of the two shared CA coordinates requires

    delta = v-t = 0.

The next first-plane product constraint requires

    rstep = (s-t)*(s+1) = 0.

The following polynomial identities are checked coefficient-by-coefficient over the rationals:

    rplus - rminus - s*delta = 4*s,
    s*(s+1-t) - rstep = t,
    t + delta = v.

If both the output and its next step lie in the multiplicative image, all four residuals vanish. These identities force s=t=v=0, and u=s=0. The proof holds over the rationals, reals or complexes; it is not a numerical scan.

**Result:** the only reference-plane output whose next reference step is also in this multiplicative image is zero.

For a small explicit falsifier, the parameters (1,1,1,-3) are realizable, but their next step is (0,-2,-2,0). The two shared CA coordinates would then be 0 and -2, although both are required to equal the same primitive product i*j.

Zero output does not force zero input: for example c=f=1 with all other primitive coordinates zero gives zero output. The retained parents/residuals may remain nonzero.

This excludes a nonzero reference-plane intertwiner whose output always factors through **this repeated-primitive multiplicative readout**, regardless of how its input dynamics might be chosen. It does not exclude independently prepared path coefficients, context-sensitive couplings, other output readouts or more elaborate retained-state operations.

## 5. What has advanced, and the new gate

We now have a positive construction and two precise failure boundaries:

- **Constructed:** source-API retained concatenation, parent recovery and a composition-respecting word expansion with pair and segmentation records.
- **Not interchangeable:** a macro-step and a fixed primitive step; flat words erase the necessary parsing information.
- **Rejected:** both the additive shortcut from the previous audit and the repeated-primitive multiplicative shortcut as nonzero reference photon-mode transport.

Appending stored parents does not by itself fix the output readout's continuation failure. A replacement cannot merely assign desired photon-mode coefficients to newly supplied records and call that an emission construction.

The next gate is an actual **segmentation-aware continuation/coupling** on the retained source, or a source-derived preparation of correlated path payloads. It must specify how macro-boundaries are selected, how shared histories are retained, and why the resulting output readout obeys the reference continuation. Metric and two-face transport still need separate checks. Physical e-minus/e-plus preparation, photon sectors, conservation and normalized scattering remain downstream.

No existing work-net contracts, pinned source records or formal outcomes are changed. No physical annihilation or ratio 372 is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_retained_word_transport.py
python research/scattering/seed-composition/check_retained_word_transport.py --check
python research/scattering/seed-composition/check_incidence_audit.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The new checker reruns the previous finite audit, uses the existing retained-path implementation, verifies exact polynomial certificates, and writes only its own receipt. `--check` compares the receipt read-only. It does not replay all historical source-owner scientific suites or publish a proof outcome.
