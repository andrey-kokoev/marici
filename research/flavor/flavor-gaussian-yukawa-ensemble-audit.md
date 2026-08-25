# Isotropic Gaussian Yukawa ensemble audit (WP120)

Owner: `marici.Figueiredo`.

## Candidate freeze

The candidate `C_GAUSS` consists of two dimensionless complex `3 x 3` Yukawa
matrices at one declared UV slice with density

\[
d\mu_\beta(Y_u,Y_d)=
\left(\frac{\beta}{\pi}\right)^{18}
e^{-\beta(\operatorname{Tr}Y_uY_u^\dagger+
                 \operatorname{Tr}Y_dY_d^\dagger)},d^{36}Y,
\qquad \beta>0.
\]

For the bounded audit, `beta=1`; no observed quark mass, mixing angle, or CP
quantity fixes it. The candidate is a mathematical isotropy/maximum-entropy
ansatz, not an asserted physical production mechanism.

The finite-dimensional normalization follows from eighteen copies of
`integral_C exp(-beta |z|^2) d^2z = pi/beta`. Standard complex Ginibre/Wishart
SVD results give squared singular-value density proportional to

\[
e^{-\beta\sum_i\lambda_i}\prod_{i<j}(\lambda_i-\lambda_j)^2,
\]

with Haar singular frames. Background references are Ginibre's Gaussian
matrix ensemble and the SVD/Laguerre–Wishart construction summarized in
Menon's random-matrix notes.

References: J. Ginibre, *Statistical Ensembles of Complex, Quaternion, and
Real Matrices* (1965), DOI `10.1063/1.1704292`; G. Menon, *Lectures on Random
Matrix Theory*, Section 6.2,
`https://www.dam.brown.edu/people/menon/publications/notes/intro-rmt.pdf`.

## Full weak-basis descent

Under

\[
(Y_u,Y_d)\mapsto
(U_QY_uU_u^\dagger,U_QY_dU_d^\dagger),
\]

the Frobenius action is invariant by trace cyclicity, and unitary left/right
multiplication has real Jacobian one. Therefore the probability measure—not
only its scalar density—descends through the full weak-basis group.

After quotienting, the two spectra have independent square complex Wishart
laws and the relative left frame

\[
V=U_{uL}^\dagger U_{dL}
\]

is Haar on `U(3)` modulo the usual phase redundancy. This produces a genuine
normalized probability law on `physical16`. Degenerate spectra and `J=0` have
measure zero; the CP-sign distribution is symmetric.

The checker verifies exact invariance under a nontrivial monomial-unitary
subgroup and exhibits a chart-weight deformation that fails even a row-swap
arrow. The analytic trace/Jacobian argument supplies the full-group step.

## Bounded-audit disposition

`C_GAUSS` passes more mathematical gates than any earlier candidate:

- concrete finite-dimensional source domain;
- normalized positive measure;
- full weak-basis measure descent;
- nontrivial quotient ensemble;
- no measured-ten injectivity claim;
- no downstream selector.

It nevertheless fails the WP118 audit at **independently validated physical
source**. The Gaussian density is an analyst-chosen prior. No admitted UV
action, stochastic production process, equilibrium theorem, or external
experiment derives this law or fixes `beta`, the UV scale, and the RG/matching
contract.

Calling the measure “maximum entropy” does not repair authority: maximum
entropy depends on a chosen base measure and constraint set. Those choices are
the missing physical source data.

## Exact hostile controls

1. Multiplying the density by a chart weight such as
   `1 + eta (Y_u Y_u^dagger)_11` breaks weak-basis descent.
2. Choosing `beta` after inspecting quark masses is scale fitting.
3. Conditioning on the measured ensemble produces a posterior, not the source
   law.
4. Haar mixing is a quotient prediction, but agreement or disagreement with
   historical CKM data is not a protected test for this retrospective audit.
5. RG may transport the Gaussian measure into a non-Gaussian law; it cannot
   silently re-Gaussianize it or select a preferred `beta`.

Current classification:

`normalized quotient ensemble; no source-relative physical explanation`.

The next gate is a physical mechanism that derives the measure class and its
scale/transport contract independently of flavor readouts.
