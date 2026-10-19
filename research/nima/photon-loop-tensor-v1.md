# Regular covariant degree-four photon logarithmic tensor

## Question, rivals and disposition

Can the independently checked photon logarithms be attached to the local Ward/Bose tensor without losing helicities or adding rational kinematic poles?

[Contract](contracts/photon-loop-tensor-v1.json) · [checker](checkers/check_photon_loop_tensor_v1.py) · [tests](checkers/test_photon_loop_tensor_v1.py) · [receipt](results/photon-loop-tensor-v1.json).

**Result:** a local-plus-log representative of the sourced parity-even on-shell EFT jet is constructed. Rival forward-only normalization passes miss beta12; a regular scalar multiplier of the all-same-helicity F2 generator alone fails on the complex S2=0 divisor. The construction below retains the forward-invisible F3 generator and avoids that failure. This is not yet the whole-window lift or a physical matching result.

## Inputs and perturbative scope

Use the [eight local covariants](photon-local-ward-basis-v1.md), their chiral field strengths F_i^+,F_i^-, contractions C, six mixed-chirality pair products P_I, symmetric pair invariants x_I and crossed products w_I. The three complementary partitions label s,t,u logarithms. On shell their invariants obey s+t+u=0. All external momenta are null, all-in and conserved; comparisons do not claim an off-shell operator classification.

Write ell_x=Log(-rho*x), rho>0. Its positive-channel upper rim is log(rho*x)-i*pi. The primary paper uses rho=sqrt(g2_gamma); at a fixed positive g2 this is one common scale choice. A change of rho is an analytic local shift, not a fitted amplitude normalization. Set B_a=pi^2*beta_a, in quadratic coordinate order (g^2,g*f,f^2). The [primary regression](photon-primary-loop-v1.md) independently derives these four B vectors by normalized physical Bose partial waves; the new constructor reads the frozen source and checks against that derivation.

The benchmark leading Born control is g=lambda_gamma/4, f=-lambda_gamma/4, lambda_gamma=16*pi*b. Its higher-Mandelstam-degree leading Born coefficients vanish. All eight finite local coefficients remain at their declared matching orders, including allowed loop-order shifts. B(g,f) is already quadratic in the leading couplings; it must not receive an additional lambda_gamma^2 factor or double insertion of those shifts. The photon g,f are not the earlier Dirac-current coefficients. Earlier packets' incomplete-stage flags remain historical provenance.

## Explicit tensor

For each of the six size-two subsets I={i,j} with complement {k,l}, the mixed-chirality contribution to pi^2*M_log is

    P_I * [(B11*x_I^2+B12*w_I)*ell_I
           +(B13/2)*sum_(a in I,b in complement I) sab^2*ell_(ab|complement ab)].

The four cross terms duplicate the two crossed partitions, so their half sum is precisely B13*(t^2*ell_t+u^2*ell_u) in the s-pair sector. Complete subset sums and symmetric weights make Bose and parity covariance explicit.

The all-same-chirality contribution is

    B2 * [(F2/2)*sum_x x^2*ell_x + F3*sum_x x*ell_x].

Here F2 and F3 are the previously constructed local tensor generators, not scalar EFT coefficients. There is no division by S2=s^2+t^2+u^2 or stu. On a four-point spinor patch F2=chi*S2 and F3=chi*stu. Each x satisfies

    x^3-(S2/2)*x-stu=0,
    x^4=(S2/2)*x^2+stu*x.

Consequently the all-same-helicity projection is chi*B2*sum_x x^4*ell_x, exactly the primary expression. The mixed projection is s^2*[(B11*s^2+B12*t*u)*ell_s+B13*(t^2*ell_t+u^2*ell_u)]. Crossed helicities follow by relabelling; the three-plus/one-minus logarithmic component is zero. Its independent analytic h3*H3 term is **not** deleted.

Adding this tensor divided by pi^2 to the arbitrary eight-coefficient local jet constructs the retained representative. Every logarithmic coefficient is a momentum/polarization polynomial with constant rational denominators only. Thus the only nonanalyticities introduced are the declared channel logarithms, not rational kinematic poles.

Ward identities follow because every term contains one field strength from each external leg. Lorentz covariance follows from invariant spinor contractions and scalar pair invariants. Bose permutations relabel complete sums and their channel logarithms together. These are algebraic construction arguments, not universal identities inferred from samples; no proof-assistant formalization is claimed.

## Cuts and the discriminating counterexamples

The checker retains three independent formal log channels and all three quadratic coupling coordinates. Equality of their tensor/helicity coefficients gives each channel monodromy. With the declared physical rims,

    Disc_x M_log = -(2*i/pi)*C_x,
    pi*Im(M_log) = -C_s  (s>0,t,u<0),

where pi^2*M_log=sum_x C_x*ell_x. The independently verified Bose-unitarity coefficients and tensor crossing therefore supply every retained channel cut. This does not establish exact all-orders unitarity. At the common Born control, forward pi*Im(D,O,M)=(19/2560,-5/768,1/1280), without rescaling any earlier reduced coefficient.

Doubling beta12 preserves every forward target and still permits Ward/Bose covariance, but changes the off-forward s-log Phi1 coefficient by (3/3125)*f^2 at s=1,t=-16/25,u=-9/25. The independent partial-wave/source comparison rejects it.

A stronger regularity control uses omega^2+omega+1=0 and s=1,t=omega,u=omega^2. Exact momentum-conserving null spinors are

    lambda = ((1,0),(0,1),(1,1),(1,-omega)),
    tilde  = ((1,0),(0,1),(omega^2,omega),(omega,-omega)).

Here S2=0 and the all-plus projection of F2 vanishes, but the required s-log g*f coefficient is -5*omega/48, nonzero. Thus a regular F2-only scalar form factor cannot work there. The F3 term above supplies it with no pole. The exact control uses the existing algebraic field toolkit, not floating-point complex arithmetic. This proves a failure of that restricted representation, not uniqueness of the chosen tensor representative.

## Common logarithmic-scale transport

For ell_x -> ell_x+delta in every channel, holding the leading couplings fixed, the full tensor changes by

    pi^2*Delta M = delta*[(B11+B13)*G4
                         +(B12-2*B13)*G4prime+(B2/2)*F4].

The proof uses s+t+u=0 and S2=2*(x_I^2-w_I); the F3 term has zero common-scale shift. The checker verifies this identity on all 256 matrix-unit polarization tuples, not only transverse helicities. The g4prime shift is forward invisible but not discarded. To keep the total amplitude fixed, the matched local coefficients must compensate with the negative of this vector divided by pi^2. This is transport between representatives, not a determination of finite local matching coefficients or the window endpoint dependence.

## Verification and remaining frontier

Exact controls cover all 16 helicities at four CM configurations, 72 labelled Bose permutations, gauge-reference changes, Lorentz/parity controls, and 2304 scalar component Ward constraints. Separate tests and fresh receipt equality accompany the scoped SCC check. The receipt contains the coupling-polynomial flow, complex-divisor control and nonzero hostile residual.

Remaining EF-WB4 construction: lift the prescribed whole-window forward subtraction in two variables and derive cancellation of channel logarithms plus the analytic local difference through degree four. Forward equality alone does not prove that remainder exists. The **unsubtracted** massless amplitude is not analytic at the origin; local polynomial regularity and analyticity away threshold divisors do not change that fact.

Native preparation, numerical physical matching, UV completion and same-scope global dispersive assumptions remain unearned. No C1–C12 disposition, C12 budget or planner forecast is changed.

```text
python -S research/nima/checkers/check_photon_loop_tensor_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_loop_tensor_v1.py
```
