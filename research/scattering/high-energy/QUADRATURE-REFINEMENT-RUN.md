# H6: live 33-node fixed-response calculation

The calculation is complete and has undergone an [independent numerical review](QUADRATURE-REFINEMENT-REVIEW.md). All measured inequalities pass, but H6 remains open pending certified error/peak margins. Read `results/quadrature33-job.v1.json` for process history; do not relaunch the completed solve.

## Scope

`run_quadrature_refinement.py` verifies the pinned full-response and higher-cutoff archives and their manifests, extracts them into `.ai/tmp/scattering-h6-response33/`, and invokes the unchanged source `reproduce_feedback.py` with `--directions 128 --points 33`. All 33 energies are solved afresh. This is more expensive than solving only the 16 missing nodes, but avoids mixing independently rebuilt phase frames across the packet.

After source analysis and verification complete, the runner uses the pinned source's moment-matched packet evaluator on the new 33-node kernels and their nested 17-node subset. It compares peak signed transport, whole-packet transport and product probability against the declared 1% criterion, and separately compares the new subset with the historical 17-node result. The difference between matched subsets, not a 9-node extrapolation or interpolated missing field, is the H6 test.

Even if the computed inequalities pass or fail, the result remains pending review of source verification and solver-error margins. The runner never promotes H6 by itself.

## Operation and ownership

```sh
python research/scattering/high-energy/run_quadrature_refinement.py --status
```

The worker owns one source-driver process tree, logs its PID, and has a 3600-second runtime budget. On timeout it terminates only that owned tree. Never launch a duplicate while the state is `preparing` or `running`. Recorded failures/exhaustion can be retried only with explicit `--retry-failed`; prior attempt metadata are preserved.

On this Windows host, background Python must use a **persistent** environment. The initial ephemeral `uv run` environment was removed after launch, causing `pyvenv.cfg` failure before computation. The retry uses `.ai/tmp/scattering-h6-response33/venv/Scripts/python.exe` with NumPy, SciPy, SymPy and threadpoolctl installed. A second launch exposed MAX_PATH in deeply nested source archives; the runner now supplies an extended-length calculation path without modifying any solver source. Both failures are preserved in the job history. A subsequent build completed the source spectrum and model cache, then exposed the source's undeclared `threadpoolctl` dependency. That dependency was installed and the guarded retry reuses the completed cache; no solver equations or parameters were changed.

The current invocation is:

```sh
.ai/tmp/scattering-h6-response33/venv/Scripts/python.exe research/scattering/high-energy/run_quadrature_refinement.py --retry-failed
```

Do not run that command while a current attempt is active. The live job record contains the actual command, source hashes, log paths and process IDs. Preflight found approximately 74.6 GiB available RAM and 1345.8 GiB free disk; these are launch-time observations, not reservations or ongoing resource guarantees.

Frozen archives, source-owner records, original receipts and earlier results are not modified. Scientific output, if the whole calculation finishes, is written to `results/quadrature17-vs33.v1.json`; large mutable caches remain in the scratch directory.
