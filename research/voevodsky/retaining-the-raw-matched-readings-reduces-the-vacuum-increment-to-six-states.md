# Retaining the raw matched readings reduces the vacuum increment to six states

## Result

The receiver/data distinction changes the structural answer:

| Retained matched-test data | Background-two vacuum increment | Inherited filtration |
|---|---:|---|
| One signed combined reading | 7 states | (7,5,1,0) |
| All 449 joint-filter readings separately | 6 states | (6,5,1,0) |

In BOTH cases the background-two vacuum acquisition is a nonsplit source-bimodule enlargement. Retaining the raw inputs makes one additional lower-filtration direction visible BEFORE the vacuum acquisition; it does not remove the acquisition's coupling obstruction.

The exact receiver manifest supplies the distinguishing raw coordinate: zero-based row index 76.

## 1. What the implementation actually promises

The interface in `../grothendieck/checkers/evaluate_finite_cubic_observer.py` requires 449 joint-filter readings in manifest order. `Observer.evaluate` sums them with the declared signs and gains and returns the combined scalar, error bounds, precision and measurement enclosure.

It does not return the 449 readings, archive them in observer state, or declare that callers discard them. Thus:

- all 449 values must be available at evaluation time;
- the returned product is a scalar certificate;
- persistent retention of the raw values is a caller/protocol decision, not an invariant established by this API.

The structural object depends on that decision. Treating the scalar-only and raw-retaining protocols as the same observer would be incorrect.

This audit does not assert that measurements have actually been performed or that a particular caller has archived its inputs.

## 2. Match the actual implementation rows, not an invented support

The checker loads `../grothendieck/results/finite-cubic-observer.json` and verifies:

- exactly 449 distinct shapes;
- the 448 crossed signs equal the owning matched correction signs;
- the remaining shape is the reserved positive block;
- both recorded final gains are nonzero.

The manifest is hashed into the result. The common finite filter has the owning response formula

    theta_fin(O Psi(F))
      =sqrt(2) X_F [C_effective+h_effective(mu_F-L)],

with C_effective>0 and h_effective>0. The owning positive-window bound gives nonzero values on [2,4] and [4,12]. No new quadrature is needed for the source-coefficient audit; that analytical positivity remains an explicit input.

The conclusions about the vacuum increment use equal-window cancellation and these nonzero factors. They hold for the ideal common test and its specified finite-filter counterpart. This does NOT identify the complete ideal and finite-filter observers on arbitrary source inputs.

When comparing raw and combined observer modules by restriction, use the SAME common filter on both sides: the combined test is then exactly the declared linear combination of the retained raw rows. An ideal scalar is not silently substituted for the implemented finite-filter sum.

## 3. The extra information is an actual manifest row

Row 76 has the mask-labelled shape

    retained seam 0->1,
    forgotten seam 7->15,
    forgotten seam 15->31,
    buffer feature counts (0,1,0,0).

At background two its arithmetic seams are

    2->4 retained, 60->420 forgotten, 420->4620 forgotten.

Prepend the retained path (2,3) to a forgotten input at corner 12->60060. The two retained windows are [2,4] and [4,12]. On every one of the 24 forgotten input path orders, this individual block reads exactly

    coefficient(5,7,11,13)

times the fixed positive joint-filter window response. Thus the canonical vacuum interval functional (2,6) is already in the saturated raw observer.

The signed matched sum, in contrast, reads a nonzero multiple of

    2[coefficient(5,7,11,13)-coefficient(5,7,13,11)].

The actual source

    h=(5,7,11,13)+(5,7,13,11)-2(5,11,7,13)

was invisible to that sum. It is detected by row 76 with normalized coefficient one. This is a direct same-source distinction between retained data products, not an argument from their different numbers of coordinates.

The same raw row, after the appropriate forgotten suffix, also supplies the already identified shared interval (2,5).

## 4. The exact raw-retaining increment

Let E_s retain the combined matched test, E_r retain all its raw rows, and add the background-two vacuum row to obtain E_s^+ and E_r^+. The other detector families are kept fixed.

Let D_s and D_r be the respective restriction kernels. The full fifteen-state vacuum module has interval basis z_(i,j) along

    2,4,12,60,420,4620,60060.

The scalar protocol shared eight of its interval functionals. The raw protocol shares those eight plus (2,6).

The remaining six old-invisible source lifts from the preceding audit vanish BLOCK BY BLOCK in every contributing context. Therefore they remain invisible even when all 449 inputs are retained independently. This gives both the lower and upper dimension bounds and proves

    D_r=span{z_(0,3),z_(0,4),z_(0,5),z_(0,6),z_(1,5),z_(1,6)}.

Its second filtration level is the same five-dimensional space as before, omitting only z_(0,3). The third level is span(z_(0,6)). Hence the inherited dimensions are (6,5,1,0).

The actual source actions are inherited from the interval module. In particular

    I D_r=0,
    D_r I=span(z_(0,5),z_(0,6)).

The inherited filtration is again not the intrinsic ideal-power filtration of this kernel.

## 5. Compare the two acquisition kernels

Restriction of raw-retaining observers to combined-reading observers induces an injection

    D_r -> D_s.

Under their faithful vacuum-coordinate representations it is the displayed inclusion of interval states. The quotient is one-dimensional at the actual corner 12->60060, represented by z_(2,6). It occurs only at filtration level one; both deeper inherited levels agree.

Even the sequence

    0 -> D_r -> D_s -> D_s/D_r -> 0

does not split equivariantly. The quotient's corner forces a lift to z_(2,6), but left multiplication by the forgotten edge 4->12 sends that lift to z_(1,6)!=0 in D_r. The quotient action is zero. Thus an equivariant section is impossible.

More retained old data therefore reduces the remaining acquisition increment, but not by deleting an independent trivial summand.

## 6. The acquisition remains nonsplit

Retaining raw matched readings still does not detect the all-forgotten cubic k_2: every such raw block has retained degree two. The old first two stages still exhaust the two-dimensional initial ideal corner 2->12.

The previous forced-lift proof therefore applies unchanged. A section E_r->E_r^+ would have to preserve the initial forgotten diamond; multiplying it by the last two forgotten diamonds is zero in E_r but nonzero in E_r^+.

Thus the raw-retaining acquisition extension is nonzero even unfiltered. The adjacent source-pushout distinction also remains: private-row detection gives filtered nonvanishing, while the retained-feature lower lift remains invisible to all the new vacuum contexts and gives unfiltered vanishing.

These are different extension statements, not contradictory status labels for one class.

## 7. Operational conclusion

The seven-state theorem matches a protocol retaining the signed scalar output. A protocol preserving the 449 input readings must use the six-state result instead. The API alone does not select an archival policy.

Future structural manifests should explicitly state whether their retained generators are final scalar tests or individual implementation readings. Error propagation through the same summation formula does not make these two source observers equivalent.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_raw_matched_readings_vacuum_increment.py

The checker freshly runs the full source/context audit, matches the actual receiver manifest, verifies the distinguishing row on every relevant forgotten input order, checks the old-invisible witnesses, records the six-state actions and inherited flag, and checks both nonsplitting witnesses.

Artifact: `results/raw-matched-readings-vacuum-increment.json`.

Input retention and actual acquisition remain explicit protocol assumptions; the program does not infer them from a function signature.
