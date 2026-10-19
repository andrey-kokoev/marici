# Local photon tensor jet through Mandelstam degree five

## Question and result

Can the eight-generator local jet be extended regularly through degree five, retaining single-minus and forward-invisible coefficients rather than inferring their absence from a restricted loop family?

[Contract](contracts/photon-local-degree5-v1.json) · [checker](checkers/check_photon_local_degree5_v1.py) · [tests](checkers/test_photon_local_degree5_v1.py) · [receipt](results/photon-local-degree5-v1.json).

**Result:** twelve explicit covariant multilinear forms have coefficient-polynomial rank twelve and forward-jet rank six. The six-dimensional forward kernel remains nonzero off forward. In particular the independent h5 single-minus term cannot be removed merely because a chosen R-family loop has zero single-minus cut.

This is a new algebraic extension of the [degree-four construction](photon-local-ward-basis-v1.md), not a primary-source claim that the paper printed a degree-five inventory. Completeness is within the declared regular parity-even on-shell invariant-polynomial helicity ansatz. It is not an off-shell operator classification or an interacting-QFT construction.

## 1. Explicit regular covariants

Retain the old chiral field-strength contractions, mixed pair products P_I, symmetric same-pair invariant x_I and crossed product w_I. Let S2=(1/2)*sum_(i<j) sij^2, equal to s^2+t^2+u^2 on conserved null kinematics. Append

    G5      = sum_(six subsets I) P_I*x_I^3,
    G5prime = sum_(six subsets I) P_I*x_I*w_I,
    F5      = S2*F3,
    H5      = S2*H3.

All expressions are polynomial, linear in every external polarization, with no kinematic denominators. Every term still contains one field strength per leg, proving each Ward identity. Complete pair sums and permutation-invariant weights preserve Bose/parity covariance; spinor contractions and scalar invariants preserve Lorentz covariance. These are algebraic arguments, supplemented by exact controls, not proof-assistant formalization.

The new independent-helicity projections are

    Delta Phi1 = g5*s^5+g5prime*s^3*t*u,
    Delta Phi2 = f5*S2*s*t*u,
    Delta Phi5 = h5*S2*s*t*u,

with Phi3/Phi4 obtained by crossing. These are amplitude-normalized photon matching coefficients, not the independent Dirac-current g3 or selected numerical physical constants.

Within the regular invariant-polynomial helicity ansatz, the mixed sector factors a fixed degree-two spinor structure; its degree-three invariant coefficient is symmetric in t,u. Modulo s+t+u=0 it is spanned by s^3 and s*t*u. The all-same-helicity phase multiplies a symmetric degree-five polynomial, uniquely proportional to S2*stu. The minimal degree-three single-minus structure multiplies a symmetric degree-two polynomial, uniquely S2. There is no symmetric degree-one term, explaining the missing degree-four single-minus coefficient. Thus four new parameters extend the eight old ones in this ansatz. Rational helicity-coordinate poles are not used to invent additional local directions; no assertion is made about an exhaustive off-shell operator basis.

## 2. Rank certificates and the surviving kernel

Use coefficient order

    (g2,f2,g3,f3,h3,g4,g4prime,f4,g5,g5prime,f5,h5).

The physical forward jet has independent rows Phi1_s2, Phi1_s3, Phi1_s4, Phi2_s2, Phi2_s4 and Phi1_s5. The old five rows are unchanged; the last row extracts g5. Its rank is six and kernel is exactly

    span(f3,h3,g4prime,g5prime,f5,h5).

This is a coefficient jet across energies, not a claim about twelve independent helicity responses at a single momentum. The full twelve-row witness uses four forward Phi1 energies, two forward Phi2 energies, and two energies each for off-forward Phi1/Phi2/Phi5. Exact rational row reduction gives rank twelve; restriction of its six off-forward rows to the six kernel columns also has rank six. These finite evaluation maps prove independence of the twelve explicit momentum-polynomial forms, not a universal classification inferred from sampled positivity.

At s=1,t=-16/25,u=-9/25, H5 has Phi5=138528/390625, nonzero. Removing it leaves every forward row unchanged but lowers the full witness rank to eleven. Two energies distinguish h3 from h5 despite their proportional helicity values at a fixed momentum. The same distinction is required for f3/f5 and g4prime/g5prime.

## 3. Controls, scope and next constructor

Exact controls evaluate all 16 helicities at four forward/backward/interior CM configurations, gauge-reference patches, 72 Bose permutations, Lorentz/parity transformations and homogeneous scaling. The new generators' 256 tensor components each supply 1024 scalar Ward constraints in total, in addition to the inherited degree-four controls. All ranks and nullspaces are computed, not supplied as dimensions alone.

The [independent degree-five cut audit](photon-degree5-cut-v1.md) already showed that deleting invisible Born F3 can change even forward loop data. The new basis does not determine arbitrary leading dimension-ten g3/f3/h3 couplings or their general cut inventory. Its twelve local coefficients remain free matching directions.

Next lift the checked R2/R3 degree-five cut into a regular logarithmic tensor and whole-window representative using this enlarged jet. Preserve odd-degree crossing signs and derive the two-variable analytic difference; do not transfer the even-degree subtraction formula by assertion. The degree-five log/window construction, physical matching, native preparation, UV completion and full all-orders IR inventory are not claimed. Historical packets and the exhausted C12 budget remain unchanged.

```text
python -S research/nima/checkers/check_photon_local_degree5_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_local_degree5_v1.py
```
