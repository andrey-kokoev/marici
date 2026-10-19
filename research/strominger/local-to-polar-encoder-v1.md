# The collective polar encoder is not a finite word in the current rational local gates

## Scope and source

Test the existing collective residual-memory encoder against finite compositions of the newly constructed local record swaps. The source, target memory chart, post-storage Hamiltonian and contact task are kept fixed. No arbitrary continuous-angle gates, fitted memory reader or conjugated target Hamiltonian are introduced.

Prospective protocol: `inputs/local-to-polar-encoder-protocol-v1.json`.
Checker: `checkers/check_local_to_polar_encoder.py`.
Receipt: `results/local-to-polar-encoder/verification.json`.

The exact24-coordinate native/bank metric M,21-row residual B, memory metric Gamma and actual5-column scattering basis E are read from the existing source packets. Reconstruct

    S=M^-1 B^T Gamma B,
    H_memory=B M^-1 B^T Gamma,
    K=A0+S.

The checker verifies that the five-dimensional bright space is invariant under S, that E has rank5, and that A0 E=0. Thus this is the already energy-compatible sector, not an arbitrary excited input chosen to recreate the earlier obstruction.

## Exact finite-word obstruction

Let g=E^T M E and S_b=g^-1 E^T M S E. Its nonzero invariant image has rational dimension4. The checker constructs a rational basis for that image and computes its restricted determinant:

    det(S_positive)=28845111555/35676273088.

This positive rational is not a rational square. In particular its reduced numerator has exactly one factor5 and its denominator has none.

In the original unwhitened metric charts, polar decomposition has

    B=W sqrt(S).

If the polar memory output W E were rational, then

    g^-1 (W E)^T Gamma B E

would be a rational matrix representing sqrt(S_b). Its restriction to the rational invariant image of S_b would have rational determinant. Squaring that determinant would give det(S_positive), contradicting the nonsquare value.

Therefore the actual polar ready-memory embedding has an irrational component already on this energy-compatible sector. Every finite product of the current exact rational local gates, applied to rational ready-memory inputs, remains rational. It cannot equal this encoder there.

This rules out ALL finite words in that declared gate class, not just the schedules tested below. It does not rule out approximation, infinite limits, continuous controls with irrational parameters, a different energy-compatible encoder, or a changed memory chart with a separately checked reader. It is not an impossibility theorem for physical implementation.

## Concrete schedules and energy diagnostics

Four schedules were frozen before execution. Each is tested on all five bright-basis columns, with initially empty occurrence memory. The correct post-storage Hamiltonian is diag(A0,H_memory), rather than the previous diagnostic that kept the live seam energy as well.

| Schedule | Gate count | Native-output discrepancy rank versus polar encoder | Hamiltonian-intertwining discrepancy rank |
|---|---:|---:|---:|
| Forward sweep of21 seams |21|3|4|
| Reverse sweep |21|3|4|
| Two forward sweeps |42|4|4|
| Forward sweep then exact backtrack |42|4|4|

Every schedule preserves the inherited metric exactly and reverses to its complete initial state. Nevertheless every quadratic energy discrepancy also has rank4. Backtracking gives the identity operation, not the required storage operation; its energy discrepancy compares that identity output with the specified post-storage Hamiltonian.

The first two columns of E are the actual two rim contact columns, with Gram matrix3I. Transporting those contacts with each candidate embedding preserves their readout exactly. Leaving the contacts untransported produces rank2 errors for the first three schedules. The identity/backtrack schedule preserves the old readout but still does not encode the residual or intertwine the post-storage dynamics.

Thus a transported contact and exact recovery alone do not establish equality of scattering dynamics. No new numerical scattering calculation or numerical polar SVD was needed for these exact failures.

## Disposition

The existing collective encoder cannot be synthesized exactly using only finite words of the current rational endpoint gates in unchanged charts. Searching longer words in that same class cannot close the gap.

The remaining constructive choices must change the declared task or operation class explicitly: permit a controlled approximation with a bound on dynamics and readouts; admit source-supported continuous operations; or construct a different encoder and prove its energy compatibility. The determinant obstruction does not select among those options.

## Verification

Seven exact groups, targeted SCC check and frozen challenge pass at `ccf4fab27d819121`. They accept the negative factorization result and retained diagnostics, not a successful implementation of the collective gate.

    python research/strominger/checkers/check_local_to_polar_encoder.py
    python research/aspect/scc/scc.py check local-to-polar-encoder
    python research/aspect/scc/scc.py challenge local-to-polar-encoder research/strominger/checkers/check_local_to_polar_encoder.py survives

Full rational schedule outputs are saved in `results/local-to-polar-encoder/schedule-outputs.json`. Source files remain unchanged and hash-bound. No other-owner checker was run, no Agda theorem compiled, and no commit or push performed.
