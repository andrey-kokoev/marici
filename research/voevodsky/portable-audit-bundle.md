# Portable local audit bundle

Created `results/audit-bundle-v131/`: nine Python reference/recognition/semantic modules plus the signature table and declared70-step trace, with an explicit11-file SHA-256 manifest. No production reducer or compiler is included. The directory preserves a minimal checkers/results layout internally, so replay no longer depends on the original repository's generated results.

`audit_bundle.build` requires fresh successful closure evidence before copying. `verify_bundle` checks the exact manifest path set and each required file's content, rejecting missing files or file symlinks. Execution is off by default; explicit execute=True or --execute-trusted runs semantic replay in a separate Python -I interpreter using the copied modules. The caller must trust the code. This is not a safe executor for unauthenticated third-party bundles, and no path/race adversary or process sandbox is claimed.

Fresh validation:29 closure suites pass; source/dependency freshness checks pass; a temporary copy replays70 steps with source-semantic agreement outside the repository, and six missing/altered module/signature/trace cases reject. The durable bundle was then created from that fresh source state. This bundle is locally prepared, not published to an external recipient or independently reviewed.

Review command (consistency only):

```
python research/voevodsky/checkers/audit_bundle.py research/voevodsky/results/audit-bundle-v131
```

Add `--execute-trusted` only for locally trusted code. The verifier itself remains a repository tool; the copied kernel can also be reviewed and run directly through its semantic_replay.py CLI. Bundle hashes do not sign the verifier or establish authorship.

## Programme checkpoint and next obligation

The programme now supports compile-once finite mixed operations with local strict completion, conditional insertion and runtime fuel-bounded scanning; written correctness/confluence/resource arguments; independent snapshot replacement and source interpretation; declaration-bound offline replay; and portable review evidence. Formal certification, external review, unrestricted loops/branch bodies, authenticated provenance and hostile-input sandboxing remain absent.

Next selected work is an independent-review handoff specification: list the smallest proof obligations a reviewer could accept or falsify, anchored to this frozen manifest, and define what evidence would change the current assurance status. Do not fabricate review, send messages without an appropriate recipient/authority, or keep expanding test counts as a substitute. The parked source-reversion task remains unchanged.
