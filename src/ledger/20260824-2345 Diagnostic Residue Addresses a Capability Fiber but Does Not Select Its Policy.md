# Entry 2345: Diagnostic residue addresses a capability fiber but does not select its policy

The complementary record of Entry 2337 has a precise downstream role.
In the minimal error-bit model, syndrome-conditioned XOR repairs both error
branches reversibly, while neither fixed reversible bit operation repairs
both without the syndrome.  The record therefore supplies an operational
address.

It does not, however, uniquely determine the response.  In the toric code,
distinct recovery chains can share one syndrome and differ by a stabilizer.
They agree on the code space but remain distinct ambient instruments.  A
noise model, metric, cost/latency functional, boundary condition, or history
is needed to select among them.

The resulting architecture is

\[
\text{diagnostic residue}
\longrightarrow
\text{conditional capability fiber},
\]

\[
\text{source policy/dynamics}
\longrightarrow
\text{section of that fiber}
\longrightarrow
\text{next operation}.
\]

Thus diagnostic output is neither passive commentary nor an executable
command.  It preserves the distinction needed for conditional action;
policy remains separately source-derived.

Evidence:

- `research/nima/diagnostic-residue-is-capability-not-policy.md`
- `research/nima/checkers/check_diagnostic_residue_control.py`
- `research/nima/results/diagnostic_residue_control.json`
- sequence claim `seqclaim-f9bdf92df96bf0b49abdf1d1`
