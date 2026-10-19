# Independent degree-five crossed-Born/Bose-cut compatibility

## Question and disposition

Does the archived c0*c1 degree-five photon cut actually follow from the full crossed Ward/Bose Born tensor, rather than an extrapolation of the degree-four normalization result?

[Contract](contracts/photon-degree5-cut-v1.json) · [checker](checkers/check_photon_degree5_cut_v1.py) · [tests](checkers/test_photon_degree5_cut_v1.py) · [receipt](results/photon-degree5-cut-v1.json).

**Yes for the declared two-term R family.** A separate tensor-to-partial-wave calculation agrees with the archived cut after the unchanged normalization dictionary. More importantly, deleting a forward-invisible Born term preserves all forward Born data but changes the forward loop cut. This is a constructive compatibility result and a counterexample to a restricted forward-only reconstruction, not a physical coupling determination or general degree-five EFT classification.

## 1. Born tensor before projection

Use the [local covariants](photon-local-ward-basis-v1.md), with the common strength lambda_gamma stripped:

    M_Born/lambda_gamma = r0*(G2-F2)/4+r1*(G3-3*F3)/4.

Equivalently, R(x)=r0*x^2+r1*x^3 gives Phi1=lambda_gamma*R(s)/4 and Phi2=-lambda_gamma*[R(s)+R(t)+R(u)]/4; Phi3/Phi4 are crossed and Phi5=0 for this family. The identity s^3+t^3+u^3=3stu fixes the F3 coefficient. It is not chosen by forward data. These are photon EFT symbols, not the earlier independent Dirac-current g3. No r0/r1 value is selected.

At s=1 let alpha=(1-z)/2, t=-alpha,u=-(1-alpha). The checker evaluates the covariant tensors, recovers the bounded-degree polynomials by exact unisolvent interpolation, and checks an unused fifth angle. Projection does not call the archived monomial-wave helpers. The degree bounds follow from the explicit source local jet; interpolation is not a claim about an unbounded unknown function.

## 2. Independent physical Bose partial waves

With pi times the physical Born waves and lambda_gamma*r_k stripped, the equal-helicity waves are

    p_(k,J)^+/- = integral_0^1 P_J(1-2alpha)*(Phi1_k+/-Phi2_k) d alpha /16.

The mixed wave is

    m_(k,J) = integral_0^1 d^J_22(alpha)*Phi3_k d alpha /8.

The factor differs because the physical mixed Bose amplitude is 2*Phi3. We use d^2_22=(1-alpha)^2 and d^3_22=(1-alpha)^2*(1-6alpha). Exact polynomial reconstruction proves that no further waves are present in this finite Born family. J=1 equal waves vanish; even J only survives in its scalar parity blocks.

    k=2: p0+=( -1/96), p0-=1/24, p2+=-1/960, p2-=1/960,
         m2=1/160, m3=0.
    k=3: p0+=1/128, p0-=3/128, p2+=1/640, p2-=-1/640,
         m2=-1/192, m3=-1/1344.

From 2*Im F_loop=F_Born^dagger F_Born, both interference orderings are retained. The coefficient pi*Im(M)/(lambda_gamma^2*r0*r1*s^5) reconstructs as

    D=8*sum_J (2J+1)*(p2+*p3+ + p2-*p3-)*P_J,
    O=8*sum_J (2J+1)*(p2+*p3+ - p2-*p3-)*P_J,
    M=8*sum_(J=2,3) (2J+1)*m2_J*m3_J*d^J_22.

Thus

    D(z)=(37-z^2)/5120,   O=-13/1536,
    M(x)=-x^2/768,        x=(1+z)/2.

In (++ , -- , +- , -+) order, the nonzero blocks are [[D,O],[O,D]] and [[M(x),M(1-x)],[M(1-x),M(x)]]. Only after this reconstruction does the checker read the [archived mixed-cut endpoint](../scattering/low-energy/MIXED-PHOTON-IR-LOGS.md). The comparison is exactly its angular polynomials divided by 16, as required by the already verified common-Born normalization. Neither a new scale factor nor a fit is used. The k=3 J=3 Born wave is nonzero, but its degree-five interference is zero because k=2 has no J=3 wave; it remains available in the degree-six square.

## 3. A forward-invisible term changes a forward loop cut

Drop only the -3*F3 Born term at degree three. The resulting tensor is still Ward/Bose compatible, and **every forward Born component remains identical**, since F3 vanishes at t=0. The independently projected loop cut nevertheless changes:

    pi*Delta Im(M)_D /(lambda_gamma^2*r0*r1*s^5) at z=1 = -1/320,
    pi*Delta Im(M)_O /(lambda_gamma^2*r0*r1*s^5)          = +1/512.

The defect is not a normalization ambiguity: the degree-four input and mixed channel are unchanged. Intermediate photons sample off-forward amplitudes. Forward-invisible local terms therefore cannot be erased when constructing higher-order forward unitarity cuts.

A second hostile omits one interference ordering and halves the entire degree-five cut. The comparison rejects it. Signed interference itself need not be positive: the J=0 plus product is negative, while the complete wave square is nonnegative. The exact r0=3,r1=4 cancellation reproduces the expected coherent zero without selecting physical coefficients.

## Boundaries and next constructor

The independent compatibility question is resolved for this R family. It does not cover arbitrary leading photon g3/f3/h3 values, all degree-six cuts, native dynamics, UV completion or physical incident preparation. Loop-order finite matching freedom is retained. The completed degree-four/window result is not retroactively broadened.

Next construct and test the on-shell local tensor inventory through degree five, including the independent single-minus channel and new forward-invisible terms, before a regular degree-five logarithmic/window lift. The archived odd-degree crossing signs must be kept; agreement of this right cut alone does not provide that new tensor or its two-variable matching remainder. No C13, planner forecasts, C12 renewal or high-energy execution is introduced.

```text
python -S research/nima/checkers/check_photon_degree5_cut_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_degree5_cut_v1.py
```
