# Raw retention loses fifteen visible states, but the vacuum square is a pullback

## Status and result

The minimal retention policy does NOT reproduce the full raw observer. A new exact audit finds a 15-dimensional source submodule of

    K=ker(E_raw -> E_minimal).

This is a lower bound for the complete loss module, not its final dimension. The full inherited filtration of K remains open.

The coupling question, however, is resolved without computing every state of K: the vacuum-acquisition square is a strict filtered pullback. In particular the vacuum extension restricts canonically split over K. This does not split the acquisition over the whole old observer.

## 1. The acquisition square

Use the SAME common filter and unchanged background detector families throughout. Let E_m retain the combined scalar plus raw row 76, and E_r retain all 449 inputs. Superscript + means adjoining the background-two vacuum row.

There is a commutative square

    E_r^+  -----> E_m^+
      |             |
      v             v
    E_r    -----> E_m.

The preceding minimal-retention certificate proved that the vertical kernels D_r and D_m map isomorphically, as source bimodules with inherited filtrations. Both are the same six-state submodule of the full vacuum module, with filtration dimensions (6,5,1,0).

Therefore the natural map

    E_r^+ -> E_r x_(E_m) E_m^+

is an isomorphism.

Proof: an element of its kernel belongs to D_r and maps to zero in D_m, so it is zero. For a compatible pair (x,y), lift x to E_r^+. The discrepancy with y lies in D_m and can be uniquely corrected using D_r. For a pair at filtration level k, strictness of the observer quotient maps supplies a level-k lift, and the filtered isomorphism D_r->D_m supplies a level-k correction. Thus the isomorphism is strict filtered, not only unfiltered.

Consequently, writing K^+=ker(E_r^+->E_m^+), restriction induces

    K^+ ~= K

as filtered source bimodules. The map x |-> (x,0) gives a canonical equivariant lift of K into E_r^+. In particular the inverse image of K under E_r^+->E_r is canonically K direct-sum D_r.

This is the precise absence of additional vacuum-acquisition coupling on the discarded information. It does NOT identify E_r with E_m direct-sum K, and it does not split the known nonsplit vacuum acquisition over E_r.

## 2. A first exact slice of the discarded information

The new checker evaluates every four-event, entirely forgotten source corner in the six-prime packet. There are 60 such corners. Only four have nonzero loss in this slice:

| Actual source corner | Raw rank | Minimal rank | Loss |
|---|---:|---:|---:|
| 70 -> 60060 | 2 | 1 | 1 |
| 30 -> 60060 | 2 | 1 | 1 |
| 28 -> 60060 | 2 | 1 | 1 |
| 20 -> 60060 | 4 | 2 | 2 |

Thus this slice of K has dimension five. Its intersection with the inherited second level is zero; there is no third-level contribution at a four-event corner.

These ranks are computed on the actual forgotten ideal: the 24 path orders are restricted to the 23-dimensional coefficient-sum-zero subspace. The second-level computation uses the complete minimal two-diamond product basis, not a path-length proxy.

All retained marks for the contextual cubic readings lie OUTSIDE these four-event inputs. For a fixed context every row therefore has the same pair of retained windows. Dividing out its common nonzero response factor makes the rank computation exact over the rationals. No fictitious independent window variables or numerical midpoint ranks are introduced.

The original private and sector detectors vanish blockwise on these contexts; the reserved positive row is absent. Lower stages cannot contribute a retained feature outside a four-event input within their shorter support. These facts are checked or follow immediately from the support lengths.

The physical interpretation assumes the owning common filter is nonzero on the displayed external windows. Exact source cancellation is independent of the magnitudes of those responses.

## 3. An explicit lost source

At corner 70->60060, one lost source is

    h= -1/2 (2,3,11,13)
       -1/2 (2,3,13,11)
       +    (2,11,3,13),

with every displayed event forgotten. The coefficients sum to zero, so h is an actual ideal source. Every minimal-retention contextual detector kills it, whereas at least one raw contextual row sees it.

The artifact supplies source bases for all four loss corners, including both independent directions at 20->60060. These are not assignments of scores to abstract observer states.

## 4. Close these five generators under source actions

Retained left edges propagate the lost information to longer source intervals. The generated submodule G has the following corner dimensions:

| Retained degree | Actual corner(s) | Dimensions |
|---|---|---|
| 0 | 70,30,28,20 -> 60060 | 1,1,1,2 |
| 1 | 4,10 -> 60060 | 2,3 |
| 2 | 2 -> 60060 | 5 |

Therefore dim G=15 and G is a source submodule of K.

Forgotten left edges give zero: after such an extension there are too few external events left to supply the required two retained marks. Positive-length right extensions leave the supported endpoint and also give zero. The two possible retained left extensions exhaust all nonzero further actions of these generators.

The artifact records every retained-prefix action column by actual manifest row, together with its common window pair. Multiplying the column by that window response recovers the actual evaluation. Nonzero column rescalings do not affect the reported ranks.

There are dependencies between images of different generators. In particular the two-dimensional corner at 20->60060 maps with rank two along EACH retained-prefix branch. The module is not inferred to be five independent three-state chains.

The inherited filtration of these degree-one and degree-two images has NOT yet been computed. It cannot be read off from retained degree, source length, or the filtration level of the initial generators.

All these source lifts are already killed by the new vacuum row: the degree-zero generators are at unsupported vacuum corners, and their retained-edge images have positive retained degree. They explicitly exhibit the canonical lift of this submodule through the acquisition square.

## 5. What remains open

This settles two important boundaries of the minimal data product:

- preserving the six-state vacuum increment still discards at least fifteen source states;
- that discarded-information kernel acquires no new extension obstruction from the vacuum row, because the whole acquisition square is a filtered pullback.

It does not yet classify the complete K. The next finite calculation must include the remaining source lengths and retained degrees and determine their inherited ideal levels. In those sectors retained windows can vary WITH the source term; the common-factor rank simplification used here cannot simply be assumed.

Nor has the independent compression extension 0->K->E_r->E_m->0 been classified as split or nonsplit.

## Verification and maintenance

    uv run --with sympy python research/voevodsky/checkers/check_four_event_raw_retention_loss.py

Artifact: `results/four-event-raw-retention-loss.json`.

The audit passes, as do fresh raw-retention and minimal-retention regression checks. During review, a shadowed variable in the earlier vacuum-increment checker was fixed: the name holding the separate detector set had been reused for a swapped path. The corrected full detector checks still reproduce the seven-/six-state results. The standalone minimal-retention verifier was already independent of that variable.

The pullback statement is proved above from the verified filtered kernel isomorphism; it is not presented as an empirical matrix test.
