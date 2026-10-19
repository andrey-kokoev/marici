# Regular local photon tensor jet through degree six

## Question and result

Can the complete degree-six cut be given its required local tensor inventory without deleting single-minus or forward-invisible matching terms?

[Contract](contracts/photon-local-degree6-v1.json) · [checker](checkers/check_photon_local_degree6_v1.py) · [tests](checkers/test_photon_local_degree6_v1.py) · [receipt](results/photon-local-degree6-v1.json).

**Result:** eighteen explicit regular covariants have full coefficient-polynomial rank eighteen, forward-jet rank eight and a ten-dimensional forward-invisible kernel. The six new terms include an independent single-minus H6. No finite matching coefficient is selected. This constructs the local inventory, not yet the generic logarithmic/window tensor.

This is an algebraic extension of the [twelve-generator jet](photon-local-degree5-v1.md), not a claim that the primary source printed this higher inventory. Completeness is within the declared real parity-even on-shell invariant-polynomial helicity ansatz, not an exhaustive off-shell operator classification, native dynamics or UV completion.

## 1. Six explicit regular additions

Retain the old chiral field strengths, mixed pair products P_I, symmetric same-pair invariant x_I and crossed product w_I. Put

    S2=(1/2)*sum_(i<j) sij^2 = s^2+t^2+u^2,
    S3=(1/6)*sum_(i<j) sij^3 = s*t*u

on conserved null momenta. Append

    G6            = sum_(six subsets I) P_I*x_I^4,
    G6prime       = sum_(six subsets I) P_I*x_I^2*w_I,
    G6doubleprime = sum_(six subsets I) P_I*w_I^2,
    F6            = S2^2*F2,
    F6prime       = S3*F3,
    H6            = S3*H3.

These forms have no kinematic denominators and are linear in each polarization. Each term retains one field strength per leg, proving the Ward identities algebraically. Complete pair sums and symmetric scalar factors preserve Bose/parity covariance; spinor index contractions and invariant weights preserve Lorentz covariance. Exact evaluations are supplementary controls, not machine formalizations of these general identity arguments.

In the unchanged physical helicity normalization the new projections are

    Delta Phi1 = g6*s^6+g6prime*s^4*t*u+g6doubleprime*s^2*t^2*u^2,
    Delta Phi2 = f6*S2^3+f6prime*(s*t*u)^2,
    Delta Phi5 = h6*(s*t*u)^2,

with Phi3/Phi4 from crossing. This defines the higher coefficient normalization; it is not fitted to a loop result. F6prime and H6 have the same scalar projection in different helicity sectors, not interchangeable tensors.

Within the scoped ansatz, the mixed degree-two spinor factor multiplies a t/u-symmetric degree-four polynomial. Modulo s+t+u=0 it is spanned by s^4, s^2*tu and (tu)^2. The symmetric degree-six all-same-helicity scalar ring is spanned by S2^3 and S3^2. The minimal degree-three single-minus structure multiplies the unique symmetric degree-three polynomial S3. Thus there are precisely six new directions in this ansatz. This invariant-ring argument supplies the scoped spanning statement; finite evaluations below prove independence, not universal completeness by sampling.

## 2. Rank and invisible-kernel certificates

The coefficient order is the old twelve followed by

    (g6,g6prime,g6doubleprime,f6,f6prime,h6).

The old six forward-jet rows remain unchanged; new rows Phi1_s6 and Phi2_s6 extract g6 and 8*f6. The full rank is eight and the exact kernel is

    span(f3,h3,g4prime,g5prime,f5,h5,
         g6prime,g6doubleprime,f6prime,h6).

These are energy-coefficient jet ranks, not eighteen independent helicity values at a single momentum. The exact eighteen-row full witness uses five forward Phi1 energies and three forward Phi2 energies, plus ten off-forward rows: three Phi1 energies at one interior angle and one Phi1 row at another, then three energies each for Phi2 and Phi5. The ten off-forward rows restricted to the ten kernel columns have rank ten, so the kernel is genuinely visible off forward rather than declared redundant.

In this selected Phi1/Phi2/Phi5 readout, deleting the second interior-angle row leaves rank seventeen: the degree-six mixed invisible columns are proportional at a fixed Phi1 scattering shape. This is not a statement about a one-angle experiment also observing crossed Phi3/Phi4. The witness is explicit and adequate, not a claimed minimal measurement prescription.

At s=1,t=-16/25,u=-9/25, H6 has Phi5=20736/390625. Removing H6 preserves every forward row but lowers the full coefficient witness rank to seventeen. Three energies separate H3,H5,H6 and F3,F5,F6prime; their proportionality at one energy is not an operator identity.

## 3. Controls, boundaries and next constructor

Controls compare all eighteen field-strength forms with an independent helicity-polynomial evaluation on all sixteen sectors at four forward/backward/interior CM configurations and two reference patches. They check 72 Bose permutations, Lorentz/parity transformations, Ward substitutions, homogeneous energy scaling, and all 256 tensor components of each new form. The latter give 1536 scalar component Ward constraints across the six new generators.

All eighteen coefficients remain free local matching directions. The [source-fibre results](photon-zero-leading-fibres-v1.md) for quadratic cuts through degree six concern an eight-leading-coupling Born jet, not a selection of these higher local coefficients. Neither a vanished single-minus response on a special source locus nor a forward null direction licenses setting H6 or any other local coefficient to zero.

Next lift the [complete degree-six cut](photon-general-degree6-cut-v1.md), retaining all twelve source monomials including 2-by-4 interference and the cubic square, into a regular crossed logarithmic tensor and whole-window representative. Derive common-log transport in the full six-dimensional new local block and the analytic window difference; do not infer them from a forward fit or the special R-family. Physical matching, source preparation, same-scope UV hypotheses and all-orders/native IR inventory remain open. C1–C12, C12's exhausted budget and the high-energy pause are unchanged.

```text
python -S research/nima/checkers/check_photon_local_degree6_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_local_degree6_v1.py
```
