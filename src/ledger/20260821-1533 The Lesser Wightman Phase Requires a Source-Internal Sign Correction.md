# 1533 — The Lesser Wightman Phase Requires a Source-Internal Sign Correction

## Source defect

The TeX source of arXiv:1408.4801 prints

\[
G_k^>(\eta,\eta')\propto
(1+ik\eta)(1-ik\eta')e^{-ik(\eta-\eta')},
\]

and

\[
G_k^<(\eta,\eta')\propto
(1-ik\eta)(1+ik\eta')e^{-ik(\eta-\eta')}.
\]

The second phase cannot be literal.

## Source-internal correction

The paper defines

\[
G^>(t,t')=\langle\zeta(t)\zeta(t')\rangle,
\qquad
G^<(t,t')=\langle\zeta(t')\zeta(t)\rangle.
\]

For the real field \(\zeta\), these definitions and the Bunch--Davies mode
functions force

\[
G_k^<(\eta,\eta')=G_k^>(\eta,\eta')^*
\]

and therefore

\[
\boxed{
G_k^<(\eta,\eta')\propto
(1-ik\eta)(1+ik\eta')e^{+ik(\eta-\eta')}.
}
\]

The later formulas involving \(\cos K(\eta_0-\eta)\) and
\(\sin K(\eta_0-\eta)\) are also incompatible with using the same exponential
in both Wightman functions.

## Epistemic status

This is not a fitted normalization or an external repair.  It is the unique
phase consistent with the source's own operator definitions, Hermiticity, and
downstream oscillatory formulas.

Accordingly, Entry 1520's reconstruction is source-complete only after this
explicit correction is frozen.  A checker using the literal printed lesser
phase is invalid.

## Finite falsifier

The contraction engine must support two modes:

1. `hermitian`, with the corrected positive lesser phase;
2. `literal_tex`, retaining the printed negative phase as a negative control.

Only the Hermitian mode may reproduce the source's finite-time sine/cosine
structure and Eq. (19).  If it does not, another convention defect remains.

## Verification artifacts

- `research/benincasa/checkers/wightman_phase_contract.rs`
- `research/benincasa/results/wightman-phase-contract.json`

The standalone Rust checker evaluates three unequal-time samples.  The
Hermitian mode agrees with \((G^>)^*\) to floating-point roundoff at every
sample.  The literal TeX mode fails every sample; its smallest squared defect
in the frozen sample set is approximately \(29.2831\).
