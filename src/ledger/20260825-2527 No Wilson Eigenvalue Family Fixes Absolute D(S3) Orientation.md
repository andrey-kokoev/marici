---
author: marici.Kitaev
sequence_claim: seqclaim-dd896c00cff558a906ca500d
---

# 2527 — No Wilson Eigenvalue Family Fixes Absolute D(S3) Orientation

## Redundant CDEFGH ports do not help

Exactly fifteen subsets of (C,D,E,F,G,H) are faithful: eight of size four,
six of size five, and the full size-six family. Exhausting their signed-affine
actions shows that all retain the orientation (C_2). When both (D,E) are
present, its generator conjugates them simultaneously.

## Full eight-Wilson theorem

For the full modular Wilson eigenvalue matrix

\[
W_{xa}=S_{xa}/S_{0a},
\]

the sector permutation (sigma=(A\ B)(D\ E)) satisfies

\[
W_{x,\sigma(a)}=\varepsilon_xW_{x,a},
\qquad
\varepsilon_D=\varepsilon_E=-1,
\]

with every other (arepsilon_x=1). The (A) coordinate is constant and the
(B) coordinate is invariant, so neither breaks orientation.

All 255 nonempty Wilson subsets were checked. Exactly sixty are faithful—of
sizes (4,5,6,7,8) with counts (8,22,21,8,1)—and every faithful subset
inherits the automorphism.

## Consequence and scope

No readout formed solely from ordinary Wilson eigenvalue coordinates fixes
absolute orientation. A breaker must be independently rooted, derived by an
oriented physical constructor, or come from a non-spectral/interferometric
observable outside this packet. Non-affine and arbitrary CPTP faults remain
unclassified.

## Durable verification

- Packets: `research/kitaev/s3-all-faithful-family-orientation-no-go.md` and
  `research/kitaev/s3-full-wilson-orientation-no-go.md`.
- Checkers:
  `uv run python research/kitaev/checkers/check_s3_all_faithful_family_orientation_no_go.py`
  and
  `uv run python research/kitaev/checkers/check_s3_full_wilson_orientation_no_go.py`.
- Result hashes:
  `844D03B01E8454A5AAFCB0912EE6E07B4A768E623C848D6CE76044EF0E4F2D03`
  and `E506F18691D3E73F1733E933FC1E5F9B6D6293A3E2861097E58460AD74476656`.
- Graph admission: `ev-000000003517-2edc45c0-850b-4c12-99f0-c5f29c1daf67`.
- Ledger allocation: `seqclaim-dd896c00cff558a906ca500d`.
