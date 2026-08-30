# Five empty bins are the first reset candidate that meets the frozen tolerance

The existing finite dead-time detector model supplies a concrete candidate reset. After `k` empty recovery bins, residual dead-state mass is `(16/25)^k`. The difference between the next photon-click responses from initially ready and initially dead predecessors is therefore

\[
\Delta_k=\frac9{25}\left(\frac{16}{25}\right)^k.
\]

At the preregistered absolute tolerance `1/20`, four empty bins fail because the residual spread is `589824/9765625`, approximately `0.0604`. Five empty bins pass because the spread is `9437184/244140625`, approximately `0.0387`. Five is the minimum passing integer in this model.

The apparatus candidate is therefore: insert five consecutive empty recovery bins before every target photon probe, then run the full sixteen-cell predecessor-reset-target qualification.

This calculation nominates the reset; it does not self-certify the laboratory apparatus. Afterpulsing, thermal memory, modulator hysteresis, or additional detector states can invalidate the two-state geometric law. The no-reset control and full predecessor-invariance test remain decisive.

Executable witness: `checkers/check_five_empty_bin_reset_candidate.py`.
