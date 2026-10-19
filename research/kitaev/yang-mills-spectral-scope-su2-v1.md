# Iteration 1 — SU(2) scope and a source-derived plaquette gap

## Question and disposition

Can the proposed witness/detector mechanism produce a genuine positive spectral inequality on an independently specified gauge source, rather than a count of histories?

Yes for a single SU(2) plaquette with electric dynamics. Its gauge-invariant physical Hilbert space has electric gap 3 kappa. A bounded magnetic term gives the sufficient gap bound 3 kappa minus lambda after subtracting the actual ground energy. That certificate fails in the weak-coupling scaling direction; the true continuum gap is not thereby refuted.

This resolves `spectral-scope` as a selected target definition and first source test. It does not resolve `finite-gauge-source`, whose coupled lattice, reflection-positive family and transfer construction remain open. No atomic particle source or four-dimensional theory is supplied.

## Frozen target

The [scope contract](contracts/yang-mills-spectral-scope-su2.v1.json) selects SU(2), a nontrivial four-dimensional gauge-invariant Wightman target, unique invariant vacuum, nonnegative self-adjoint reconstructed time-translation generator and its physical form domain. An OS construction must prove its hypotheses and justify correspondence to that target. The official problem quantifies over compact simple groups; one selected SU(2) case would not exhaust it.

Use hbar=c=1 and an independently specified reference scale mu when comparing cutoff energies. No numerical physical calibration follows from the mathematical pilot. Its kappa is a declared energy parameter, not a clock or energy inferred from a workflow index.

The official Jaffe–Witten/Clay source is identified in the contract from the existing microprogram. A fresh local PDF search returned unrelated indexed sources; direct official PDF retrieval was refused by structured-command policy. No bypass was attempted. Thus this turn freezes a target definition, not a newly source-verified axiomatic-equivalence theorem. Official-target equivalence remains an explicit reconstruction/assembly obligation.

## Source, physical quotient and operator

Take a four-edge oriented cycle with links U0,U1,U2,U3 in SU(2), normalized product Haar measure and vertex gauge action

\[
U_e\longmapsto g_{s(e)}U_e g_{t(e)}^{-1}.
\]

The ordered holonomy W=U0 U1 U2 U3 transforms by conjugation at vertex zero. Tree gauge fixes the first three links to identity and leaves W on the fourth; the remaining action is conjugation. Product Haar pushes forward to normalized Haar in W. Hence gauge-invariant functions depend precisely on the conjugacy class of W, and the quotient map is isometric:

\[
L^2(SU(2)^4)^{SU(2)^4}\simeq L^2(SU(2))^{\mathrm{Ad}}.
\]

This is a physical Gauss-law quotient for this specified lattice model, not a quotient of arbitrary path words. All link variables and ordered multiplication are source data. Reversing multiplication of two noncommuting links is an exact hostile.

Let minus Delta on a link have spin-j Casimir j(j+1). Supply the electric Hamiltonian

\[
H_0=\kappa\sum_{e=0}^3(-\Delta_e),\qquad \kappa>0.
\]

This is the declared electric gauge operator, not an operator fitted to the desired gap. We use standard SU(2) Haar/Peter–Weyl and Casimir theory as imported mathematical results, not as a new formalization.

## All-spin gap and detector

The conjugation-invariant characters chi_n, n=0,1,..., with spin n/2, form an orthonormal basis. Each link derivative sees that same representation in the loop. Therefore

\[
H_0\chi_n=\kappa n(n+2)\chi_n.
\]

For psi=sum a_n chi_n, the closed form domain consists of sequences with sum n(n+2)|a_n| squared finite. The operator domain uses the squared eigenvalue weight. Finite character sums are a form core. The vacuum is chi_0 and every n at least one has n(n+2) at least three. It follows for every form-domain vector that

\[
q_0(\psi)=\kappa\sum_{n\ge1}n(n+2)|a_n|^2
\ge3\kappa\sum_{n\ge1}|a_n|^2.
\]

Equality occurs on chi_1. Thus the exact gap is 3 kappa, not merely a positive sampled spectrum.

The four-link invariant derivative packet D supplies a source-defined detector with squared norm equal to the sum without kappa. Its Poincare constant is three and its energy-cost constant is kappa. The detector is defined by the link derivatives; it is not chosen from a presumed unknown continuum spectral projector.

A reader restricted to center-even characters misses chi_1, which has unit norm and energy 3 kappa. Retaining only adjoint/center-even observations cannot establish a faithful detector bound on this full physical space. The group, source action and required observation domain matter more than the number of records retained.

## Add the magnetic term and test the vacuum

Write

\[
H_\lambda=H_0+\lambda V,\qquad V(W)=1-\tfrac12\operatorname{Tr}W,
\qquad \lambda\ge0.
\]

SU(2) gives 0 at most V at most 2. Bounded multiplication preserves the self-adjoint/form domains. H0 has compact resolvent; the bounded perturbation does too. If E0 and E1 are the first two eigenvalues counted with multiplicity, the min–max principle gives

\[
E_1\ge3\kappa,
\qquad E_0\le\langle\chi_0,H_\lambda\chi_0\rangle=\lambda,
\qquad E_1-E_0\ge3\kappa-\lambda.
\]

Here Haar mean of the fundamental character is zero. When lambda is less than 3 kappa this proves uniqueness of the ground state and a positive gap. The lower bound is sufficient, not asserted sharp.

The electric vacuum cannot simply be retained as the magnetic vacuum:

\[
H_\lambda\chi_0=\lambda\chi_0-\tfrac\lambda2\chi_1.
\]

Its residual orthogonal to chi_0 has squared norm lambda squared over four. Any gap statement using the unchanged constant vacuum at positive lambda is therefore rejected. The spectral theorem supplies an actual ground projection; no explicit ground wavefunction is claimed.

## Strong-coupling certificate versus continuum scaling

For the explicit pilot convention

\[
\kappa=\frac{g^2}{2a},\qquad
\lambda=\frac{2}{ag^2},
\]

the sufficient positivity condition is g to the fourth power greater than 4/3. The ratio lambda/kappa equals 4/g to the fourth power, which diverges as g tends to zero, independent of a. Consequently this perturbative estimate cannot certify a gap along that weak-coupling direction.

This is an explained failure of this bound, not proof that the true spectrum becomes gapless. Nor is an arbitrary parameter sequence automatically a renormalized Yang–Mills trajectory: the latter remains to be supplied by the continuum-construction node.

## DPC disposition

- Problem: witness-sensitive identity by itself contains no quantitative energy scale.
- Conjectured mechanism: source-derived faithful excitation detection plus a positive energy cost can certify separation.
- Rivals: blind even-sector reader; unchanged electric vacuum; a strong-coupling estimate promoted into a continuum theorem.
- Risky tests: detect chi_1, compute the actual magnetic vacuum residual, and inspect the sufficient bound under g tending to zero.
- Strongest residual: the magnetic vacuum residual is nonzero for every positive lambda; the sufficient bound loses positivity at weak coupling.
- Survivor: an all-spin single-plaquette electric gap and a rigorously scoped magnetic gap bound. Continuum and full-lattice gates remain open.

## Reproduction and next source operation

```text
python research/kitaev/checkers/check_yang_mills_spectral_scope.py
```

Receipt: `research/kitaev/results/yang-mills-spectral-scope-su2-v1.json`. It checks 36 rational quaternion gauge transformations, exact tree gauges, noncommutative order failure, Casimir normalization through n=32, 125 coefficient tests, the blind-reader/vacuum hostiles and rational scale controls. The all-spin and perturbation conclusions use the written harmonic-analysis, closed-form and min–max arguments; no finite character truncation is substituted for them. No proof-assistant closure is claimed.

Next nonredundant operation: extend the source to coupled plaquettes and derive the gauge-invariant transfer/form interface, retaining shared-link correlations. Repeating the one-plaquette gap at larger spin cutoff will not test volume-uniform or continuum separation. An independent atomic source can be investigated on its separate branch without importing this model as a particle.
