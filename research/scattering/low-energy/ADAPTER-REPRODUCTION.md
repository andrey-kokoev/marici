# Current-source reproduction of the native rim adapter

[Branch audit](BRANCH-EVIDENCE.md) · [replay checker](check_adapter_reproduction.py) · [receipt](results/adapter-reproduction.v1.json)

## Disposition

The stale `assemble_relative_geometry.py` binding has been narrowed to a **provenance-only difference in this adapter replay**. The existing native rim adapter, run against the current copied helper and current copied dependencies, passes all 24 exact checks and reproduces **every non-provenance field** of the stored owner receipt: full adapter matrix, metric, source-packet root, mode norm budget, all sixteen schedule snapshots, return period and scope qualifications.

Only the helper entry in `source_hashes` differs:

- Historical: `f155f96079238a2f21c5147c5eae8c41212db1dbdab4d5e40cfb26f1a45bec7a`.
- Current: `5e088a6d19f61f9cc449328c072ac34c3a4c62a3fb1deac88859ec10d8482d2c`.

The historical helper bytes have not been recovered or compared, so this does not establish that the helper's change was comment-only, globally semantics-preserving, or harmless for every caller. It establishes agreement of this finite adapter's complete recorded result under the current implementation.

## Isolation and checks

The unmodified checker, its conservatively discovered local Python import closure and the source files named by its receipt are copied into a temporary source-relative tree. Python isolated mode runs the checker there. Runtime local module origins must lie in that tree, correspond to tracked source copies, and never resolve into the original repository. No constructor functions, hash checks or output paths are monkey-patched.

The replay checks that the owner receipt and copied-source originals remain byte-identical before/after execution. It requires exact equality of all mathematical output, not just the pass flags. It admits exactly one reviewed provenance difference, with no source-key additions or removals.

Negative controls reject a changed adapter matrix, changed schedule, failed verification, extra source binding and unreviewed helper hash. Both the historical and current helper versions are explicitly pinned; another helper edit requires a separate review, even if the adapter's output happens to match. The receipt records the current source hashes, imported modules and full fresh adapter result. Verification of the predecessor packet root and geometry hash occurs in the original adapter checker; this is not a replay of every producer of those packets.

## What is and is not resolved

- **Resolved for this local adapter:** current-source reproduction of the mathematical payload. There is no observed adapter regression in this exact test.
- **Still historically stale:** the old receipt's helper hash. It is deliberately not overwritten or silently re-pinned.
- **Not established:** a fresh complete ancestor chain, a general equivalence of helper versions, physical spinor coupling, native operation selection or independent output particles.
- **Unchanged:** C1–C11, their proof outcomes, frozen contracts, source-owner results and the paused high-energy execution budget.

The branch audit can now cite a separate current-source reproduction alongside its historical mismatch. Its strict historical-lineage mode must still refuse a claim that all old bindings are current. Do not block unrelated low-energy threshold/packet or comparison work merely because the historical receipt is preserved.

## Replay

```sh
python research/scattering/low-energy/check_adapter_reproduction.py --check
```

A changed helper, import, input or mathematical output invalidates the receipt and requires review. No new conjecture is added by this reproduction certificate.
