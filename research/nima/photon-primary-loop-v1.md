# Primary-source photon loop regression

## Question

Does the published loop amplitude independently reproduce the normalized-carrier audit, including angular information invisible at forward scattering?

[Checker](checkers/check_photon_primary_loop_v1.py) · [tests](checkers/test_photon_primary_loop_v1.py) · [contract](contracts/photon-primary-loop-v1.json) · [receipt](results/photon-primary-loop-v1.json) · [source provenance](sources/photon-scattering-2024-provenance.json).

This discharges the primary-text residual in the frozen [normalization packet](photon-normalization-v1.md). Its earlier nonverification flags remain historical provenance, not the current source-check result. The SCC obligation is readout compatibility on the declared imported scattering conventions.

### Issue boundary

- Problem: review-derived numbers alone could conceal a source-convention error or an incorrect angular coefficient.
- Conjecture: the four published one-loop coefficients follow from the physical Bose partial waves and agree with the existing reduced cut after its independently derived normalization dictionary.
- Rivals: the review copied or fitted a factor; one mixed ordered helicity entry is a physical Bose eigenvalue; forward agreement conceals an angular error.
- Risky consequence: all four coefficients must match as quadratic polynomials in independent photon EFT couplings, including the forward-invisible coefficient.
- Strongest test: parse the primary TeX, corroborate it against the published PDF text, independently derive the coefficients, then double the forward-invisible term while keeping every forward target unchanged.
- Disposition: the primary coefficients match; the angular hostile fails. This verifies the normalization comparison, not a completed off-forward tensor or physical source selection.

## Primary source and retrieval

Kelian Häring, Aditya Hebbar, Denis Karateev, Marco Meineri and João Penedones, *Bounds on photon scattering*, JHEP 10 (2024) 103, DOI [10.1007/JHEP10(2024)103](https://doi.org/10.1007/JHEP10(2024)103), arXiv:2211.05795. The published article is CC-BY-4.0.

The operator authorized retrieval following the earlier curl command-policy refusal. The authorized fallback downloaded the publisher PDF and the matching author TeX archive; no execution-policy change was made. `pdftotext -enc UTF-8 -layout` preserved the Greek symbols and powers. The inputs are pinned by SHA-256; attributed, unmodified TeX quotations and selected published PDF text pages are stored under `sources/`. The capture script is an offline exporter of those inspected inputs, not TeX execution. Ordinary regressions use only the stored excerpts and do not contact the network.

Inspected locators: equations (1.6)-(1.8), (1.21)-(1.22), (A.3)-(A.7), (A.32), and Appendix C, especially (C.4). The paper uses mostly-plus metric; its positive numerical Mandelstam s and negative t,u agree with the project's mostly-minus convention after their declared definitions. Its interacting invariant amplitude is denoted by mathcal T, not by the normalized angular operator T_red.

## Source equations and independent calculation

The paper's leading Born amplitudes are Phi1=g*s^2, Phi2=f*(s^2+t^2+u^2), and Phi3=g*u^2. Here g,f denote its photon EFT g2,f2, NOT the earlier dimension-minus-three Dirac-current g2. It defines ordered partial-wave coefficients by

    Phi_i^J=(1/(32*pi))*integral_0^pi sin(theta)*d_J(theta)*Phi_i dtheta.

Its normalized physical partial waves are F=Phi1+/-Phi2 in the equal-helicity channels and F=2*Phi3 in the mixed channel. The latter factor follows also from the normalized mixed state sqrt(2)*|+-> in (A.32). Appendix C imposes 2*Im(F4)=F2^2 and log(-s-i0)=log(s)-i*pi for s>0.

Equation (1.8) prints

\[
\beta_{1,1}=-\frac{14f^2+5g^2}{160\pi^2},\qquad
\beta_{1,2}=\frac{f^2}{240\pi^2},\qquad
\beta_{1,3}=-\frac{g^2}{80\pi^2},\qquad
\beta_2=-\frac{5fg}{48\pi^2}.
\]

The checker extracts these rational coordinates from the quoted author TeX; they are not copied into the derivation. It uses the polynomial basis (g^2,g*f,f^2), keeping the inverse-pi-squared grade explicit. Twelve rational coordinate equalities establish the four polynomial identities within this degree-four EFT loop ansatz.

Independently put t=-s*alpha, u=-s*(1-alpha). The scalar Born angular polynomial is p=1+alpha^2+(1-alpha)^2. Its only Legendre moments are E0=5/3 and E2=1/15. The mixed Born wave has d22=(1-alpha)^2 and squared norm integral 1/5. Squaring the normalized physical waves, using the unitarity equation, and reconstructing with 16*pi*(2J+1) yields the four coefficients above. In particular P2=1-6*t*u/s^2 produces beta12 from the J=2 scalar cut rather than from a forward fit.

For the common-Born control R=s^2, set g=lambda_gamma/4, f=-lambda_gamma/4 and strip lambda_gamma^2, with lambda_gamma=16*pi*b. The published right-log coefficients become

    pi^2*(beta11,beta12,beta13,beta2)
      =(-19/2560,1/3840,-1/1280,5/768).

The upper-rim logarithm therefore gives

    pi*(D_std,O_std,M_std)=(19/2560,-5/768,1/1280),
    (D_red,O_red,M_red)=16*pi*(D_std,O_std,M_std)
                     =(19/160,-5/48,1/80).

Thus the existing reduced coefficients stay unchanged. This uses the common-Born expansion parameter; at fixed b the invariant coefficients instead multiply by 16*pi, as derived in the predecessor packet.

## Hostile and claim boundary

Doubling beta12 changes none of the three forward targets: its s-channel structure is s^2*t*u*log(-s), which vanishes at t=0. Nevertheless the partial-wave comparison rejects it with exact residual f^2/(240*pi^2). Additional controls reject a wrong printed coefficient, wrong power of pi, omitted mixed-Bose factor, reversed logarithm rim and changed source bytes.

Verified here: the primary amplitude/state conventions, four published loop-coefficient polynomial identities, and their normalization pullback to the existing reduced cut. The source-check result is independently primary-verified, rather than review-only. Source inspection and exact arithmetic do not certify every conclusion of the paper.

Not constructed: a covariant Ward/Bose off-forward tensor, regular matching, a UV completion, global fixed-order positivity, native preparation, or physical rates. The full finite matching coefficients remain free. The review's criticism of other papers is not adopted by this check.

## Disposition

The retrieval/source-coefficient gate is closed at this stated scope. Next construct the degree-four Ward/Bose off-forward lift with all independent helicities and forward-invisible local terms retained. Agreement of these cuts is a constraint on that construction, not a proof of joint analyticity.

```text
python -S research/nima/checkers/check_photon_primary_loop_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_primary_loop_v1.py
```
