# Photon amplitude normalization: carrier kernel and invariant amplitude

## Question

Does the literature review's proposed 1/(16*pi) conversion expose an error in the existing reduced photon cut, or identify the missing dictionary to the relativistic invariant amplitude? The active SCC obligation is **readout compatibility** between two imported scattering conventions, not realization of native dynamics.

[Contract](contracts/photon-normalization-v1.json) · [checker](checkers/check_photon_normalization_v1.py) · [receipt](results/photon-normalization-v1.json) · [SCC manifest](scc-models/photon-normalization-v1.json)

### Issue-boundary test

- Problem: physical comparisons cannot identify a normalized angular kernel with an invariant amplitude without its phase-volume map.
- Conjecture: the photon-elastic dictionary is T_red=M/(16*pi); the existing reduced cut coefficients need no rescaling.
- Rivals: no conversion is needed; the factor is 32*pi from a second Bose division; a common factor works for every channel; replacing b leaves quadratic coefficients unchanged.
- Risky consequences: standard phase-space integration and physical mixed-Bose projection must reproduce the same forward cut; fixed-b and common-Born-kernel conversions must differ.
- Falsifier: derive the complete two-photon phase measure and compare three rational cut coefficients and all allowed partial waves in declared polynomial controls. Independently checking a primary printed coefficient remains a separate source gate.
- Disposition: the normalization dictionary survives exact controls. The primary-paper check is deferred at an explicit retrieval residual, not counted as verified literature evidence.

## 1. Source operation and carriers

Declare relativistic one-particle normalization

    <p,h|q,k>=2*E_p*(2*pi)^3*delta^3(p-q)*delta_hk,
    <out|S-I|in>=i*(2*pi)^4*delta^4(P_out-P_in)*M.

For a massless pair at timelike total momentum, the invariant phase measure is

    dPhi2=dOmega/(32*pi^2),
    dPhi2/2!=dOmega/(64*pi^2)=dmu/(16*pi),
    dmu=dOmega/(4*pi).

This follows by integrating the spatial momentum delta function, then the radial energy delta function; |p|/sqrt(s)=1/2. The 1/2! is the identical-intermediate-particle factor. Helicity sums remain explicit.

At fixed s>0, let H_B be the full-sphere L2 helicity sections obeying Bose exchange, using the same transported frames as the existing photon kernel. Its physical phase-weighted norm is c*integral dmu sum_h |psi_h|^2, with c=1/(16*pi). The unitary change of coefficient coordinates is f=sqrt(c)*psi. Transporting the invariant kernel through this map gives

    T_red=c*M=M/(16*pi),
    S_B=I_B+i*T_red_operator,
    2*Abs(T_red)=T_red^dagger*T_red.

The identity here is on the Bose-equivariant subspace, not on four independent ordered-helicity partial waves. A second 1/2 on the normalized angular convolution would double-count the Bose measure. The L2 statement follows from the constant measure identity for every section; positive samples are not used to infer this completion.

This is a photon-elastic dictionary. For general channel phase weights v_i, the normalized operator has kernel sqrt(v_i*v_j)*M_ij. A distinct charged pair has v_c=beta/(8*pi), whereas the photon pair has v_gamma=1/(16*pi). At beta=0 the charged-channel inverse coordinate map degenerates; this audit's comparison stratum excludes that threshold. No common scalar factor is asserted for all photon/charged/multiplicity blocks.

## 2. Two different perturbative coefficient conversions

The project defines

    T_red=(b/2)*A+b^2*B_red+... .

At the SAME b,

    M=(b/2)*(16*pi*A)+b^2*(16*pi*B_red)+... .

If instead the invariant amplitude uses the SAME stripped Born kernel A, define lambda=16*pi*b. Then

    M=(lambda/2)*A+lambda^2*B_std+...,
    B_std=B_red/(16*pi).

There is no contradiction between multiplying and dividing: the second equation also changes the expansion parameter. Changing amplitude normalization while silently holding both A and b fixed is not a valid dictionary. The leading r_k and all existing reduced receipts remain unchanged.

The earlier g2 relation is already fixed algebraically by `PACKET-WEAK-COUPLING-TAIL.md`. Write kappa for THAT document's linear bookkeeping lambda, distinct from this audit's quadratic common-Born parameter lambda. It defines

    epsilon2=|kappa*g2|*m^3/(sqrt(128)*pi),
    b=epsilon2^2=|kappa*g2|^2*m^6/(128*pi^2),
    lambda=16*pi*b=|kappa*g2|^2*m^6/(8*pi).

Indeed the earlier outgoing coefficient has squared phase factor Phi_in*Phi2/2!=beta/(128*pi^2), giving |kappa*r2|^2=b*beta*(M/m)^6 for the earlier kernel r2. This independently reconciles the original Fock Born norm with Im(T_gamma_gamma)=|kappa*r2|^2/2 and the scalar response convention. With A held fixed, the invariant leading term is |kappa*g2|^2*m^6*A/(16*pi). This is an algebraic relation between declared imported conventions, not a numerical physical calibration or an equality with g3.

For a normalized physical Bose partial wave, the phase-shift amplitude a_J=(S_J-1)/(2*i) equals T_J/2. Thus Im(a_J)=|a_J|^2 for an elastic channel corresponds to 2*Im(T_J)=|T_J|^2, not Im(T_J)=|T_J|^2.

## 3. Exact loop and Bose-projection regressions

For R=s^2 the existing reduced forward coefficients are

    (D_red,O_red,M_red)=(19/160,-5/48,1/80)*s^4.

In the common-A invariant convention above,

    pi*(D_std,O_std,M_std)=(19/2560,-5/768,1/1280)*s^4.

An independent phase-space Gram derivation uses general real PHOTON-EFT contact coefficients g,f: invariant Born equal-helicity diagonal g*s^2, off-diagonal f*(s^2+t^2+u^2), and mixed entries g*u^2,g*t^2. With t=-s*alpha and u=-s*(1-alpha),

    pi*D=(g^2+(14/5)*f^2)*s^4/32,
    pi*O=5*g*f*s^4/48,
    pi*M_mixed=g^2*s^4/80.

Putting g=lambda/4 and f=-lambda/4 and stripping lambda^2 gives the displayed standard targets. The angular integrals used independently are integral [1+alpha^2+(1-alpha)^2]^2=14/5 and integral [1+alpha^2+(1-alpha)^2]=5/3. These g,f are four-photon EFT contact coefficients. In particular, a paper's symbol g2 for a photon Wilson coefficient is NOT the project's dimension-minus-three Dirac-current contact g2; no physical coupling identification is derived.

The same coefficients follow from the physical partial-wave carrier. In a mixed-helicity wave, the ordered block has diagonal H/2 and off-diagonal (-1)^J*H/2. Its allowed Bose eigenvalue is H, with cut H^2/8. The ordered diagonal cut is H^2/16. Squaring one ordered entry alone and dividing by eight gives H^2/32: it misses a factor four for the physical eigenvalue, or two for the reconstructed ordered diagonal. These factors are projection effects, not extra phase-volume factors. The checker compares 25 ordered monomial pairs across all their allowed J values with the full forward formulas.

The standard right-cut logarithm is -Abs(B_std)*log(-s/nu)/pi. Consequently its s-channel log coefficient has another inverse pi beyond the standard absorptive coefficient. This is a convention conversion, not a change of the conditional spectral coefficients inside R.

## 4. Literature provenance and residual

The operator supplied Shoshin's review citing Haring et al., *Bounds on photon scattering*, JHEP 10 (2024) 103, equations (1.6)-(1.8) and Appendix C:

https://link.springer.com/content/pdf/10.1007/JHEP10%282024%29103.pdf

The three standard rational targets above were DERIVED in that review. They have not been independently transcribed from the primary paper here. The first-principles phase-space regression reproduces them, but that is not an independently source-verified paper regression.

Direct retrieval using curl through structured-command was refused because curl is not allowlisted. The declared local `pnpm pdf:search` route found no copy by title. No alternative network wrapper was used. The first missing object is an inspectable, provenance-bound primary PDF or exact source excerpt. Acceptance: verify the paper's state/amplitude convention, its definitions of photon g2/f2, and at least one printed loop-log formula; substitute the declared Born control and compare without fitting a factor. A supplied PDF or an explicitly authorized retrieval capability reopens that source check.

The proposed E_n domain correction is not a new defect: `research/scattering/low-energy/FORWARD-IR-SUBTRACTION.md` already restricts the formula to n>=2, and its checker rejects lower n. The twice-subtracted generated difference has E0=E1=0. No existing shared scattering files were changed by this audit.

## Claim boundary

Established: a normalization comparison on declared relativistic and normalized Bose carriers, the algebraic map to the earlier amplitude-normalized Dirac g2, exact polynomial Gram regressions, explicit coupling-parameter bookkeeping and a review-target reproduction. General identities are documented mathematics, not machine-formalized theorems.

Not established: independent primary-paper verification, source-selected numerical values or native calibration of g2/g3, native physical preparation, physical rates, global fixed-order UV positivity, an off-forward lift or a UV completion. The review's paper-specific criticism is not adopted as verified. The existing conditional photon-kernel mathematics is not promoted to a physical scattering explanation.

## Disposition and continuation

Keep the existing reduced coefficients. Use the explicit dictionary for any invariant-amplitude comparison. Defer primary-source admission at the single source object described above. The next executable mathematical step is a Ward/Bose off-forward lift through a specified EFT order, with forward-invisible contact terms retained; a missing PDF must not be treated as proof of a different normalization or as permission to alter old coefficients.

Verification:

```text
python research/nima/checkers/check_photon_normalization_v1.py --check
python -m unittest discover -s research/nima/checkers -p test_photon_normalization_v1.py
```
