# 3015 — Published Counts Strongly Favor NPT but Do Not Alone Certify a Physical State

**Status:** superseded by Entry 3017  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-f43bd940577c7ac8d260c56d`

## Scope

**Correction.** The claim below that the numerical maximum-likelihood matrix was unavailable is false. James et al. publish it explicitly as equation (4.11), for the same sixteen-count packet. Entry 3017 uses that matrix and supplies the physical NPT certificate. The raw linear-inversion calculations in this entry remain reproducible evidence, but its certification boundary is withdrawn.

Entry 3012 requested direct use of the source’s reconstructed experimental density matrices. White et al. publish all sixteen coincidence counts for a near-maximally entangled state, but publish the physical maximum-likelihood density matrix only as a plot. This entry reconstructs the source’s unconstrained linear-tomography matrix and audits its NPT witness.

## Frozen data and reconstruction

The sixteen labelled analyzer pairs and integer counts are taken from Table 1 of arXiv:quant-ph/9908081. Their first four counts give the source normalization

\[
N=34749+324+444+35805=71322.
\]

The checker solves the complete sixteen-setting linear tomography system in the ordered Hermitian basis of four diagonal and six complex off-diagonal coordinates. No matrix entries are read from the published figure.

## Result

The reconstructed Pauli correlations are

\[
XX=1.092678275988,
\qquad
YY=-0.984156361291,
\qquad
ZZ=0.978463868091.
\]

Aspect’s direct handedness witness is therefore

\[
W=\frac{1-XX+YY-ZZ}{4}
=-0.513824626343.
\]

The reconstructed partial transpose has minimum eigenvalue

\[
\lambda_{\min}(\rho_{\rm lin}^{T_2})
=-0.515320782798.
\]

Both values strongly favor the NPT orientation-sewing mechanism.

## Withdrawn physicality gate

The unconstrained linear reconstruction is not itself a density matrix. Its spectrum is approximately

\[
(-0.065274,-0.024396,0.068124,1.021546).
\]

This is the known failure mode for noisy linear tomography discussed by James et al.; their maximum-likelihood method restores positivity. The original version of this entry incorrectly stopped here. Equation (4.11) publishes the corresponding numerical maximum-likelihood matrix, and Entry 3017 audits it directly.

Aspect’s bounded-error rule remains the correct instrument-level test. If each of \(XX,YY,ZZ\) has absolute error at most \(\eta\), then

\[
W_{\rm true}
\le
W_{\rm measured}+\frac{3\eta}{4}.
\]

For this measured central value, any independently certified

\[
\eta<0.685099501790
\]

would already prove negativity. The source does not state the three required correlation bounds in that form, so this large margin is evidence rather than a substituted error model.

## Withdrawn conclusion

The raw count packet strongly supports NPT synchronization but cannot itself be treated as a physical state. The former claim that the physical estimator was unavailable is withdrawn; Entry 3017 supplies the source-authorized physical certificate.

## Superseded next falsifier

Completed by locating equation (4.11) in the primary paper. See Entry 3017.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-f43bd940577c7ac8d260c56d`, value 3015.
- Checker: `research/benincasa/checkers/check_published_two_photon_npt.rs`.
- Deterministic outputs: normalization 71322, witness \(-0.513824626343\), minimum partial-transpose eigenvalue \(-0.515320782798\).
- Generated executable removed after verification; source checker retained.
- Epistemic-graph admission: `ev-000000005798-8967444b-9be0-4221-b452-cfbc0e40e3f1`.
