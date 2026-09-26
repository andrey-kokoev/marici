# Consolidation: one density, one normalization, one shared singular coefficient

## Frozen comparison

Use exactly the restored representative from `restored-period-threshold-continuation.md`:

    D_delta=1/[a b w ell1 ell3 (delta+a+b-P)],
    I_0(delta)=integral_R3 D_delta d3l.

Fix noncollinear focal geometry, positive X1,X3 and the same external factors. No omitted graph summands are added and no old printed measure is substituted.

Declare the regulator extension explicitly: rotational Lebesgue integration in d=3+2epsilon, multiplied by mu^(-2epsilon), with mu>0. There is no (2pi)^(-d), MS factor or subtraction in this convention. This is a calibrated mathematical continuation of this density, not a claim that an unresolved physical source prescription has selected it. Any comparison with another convention must retain its prefactor through the required regulator order.

## Exact geometric factor behind the match

In the same prolate variables v=a+b-P and z=a-b,

    rho^2=v c(v,z),
    c(v,z)=(2P+v)(P^2-z^2)/(4P^2),
    d^(3+2epsilon)l/(ab)
      =rho^(2epsilon) dv dz dOmega_(1+2epsilon)/(2P).

The angular continuation for a function of the cosine t to the transverse third-center direction is

    integral dOmega_(1+2epsilon) f(t)
      =[2 pi^(epsilon+1/2)/Gamma(epsilon+1/2)]
        integral_-1^1 (1-t^2)^(epsilon-1/2) f(t) dt.

Its total area is2 pi^(1+epsilon)/Gamma(1+epsilon). At epsilon0 this is exactly the dphi integration used in the threshold proof.

Choose a reference energy M>0 solely to make logarithms dimensionless. Then

    I_epsilon(delta)=integral_0^infinity (v/M)^epsilon
                       beta_epsilon(v)/(delta+v) dv,

where beta_epsilon contains (M c(v,z)/mu^2)^epsilon and the angular integral of1/(w ell1 ell3), with the same1/(2P) factor. In particular beta_0(v)=B(v), the previous Stieltjes density.

Near v0,

    beta_epsilon(0)=B0+epsilon B1+O(epsilon^2),
    B0=(2pi/P) integral_0^P f0(u) du,
    f0(u)=1/[w(u)(X1+u+w(u))(X3+P-u+w(u))],
    B1=(2pi/P) integral_0^P f0(u)
       [gamma_E+log(pi)+log(2M u(P-u)/(P mu^2))] du.

Endpoint logarithms in B1 are integrable. The noncollinear third center makes f0 bounded on the full segment. The angular derivative is log(pi)+gamma_E; it must not be dropped when comparing finite parts.

## Match and finite-part discrepancy

The positive-sheet continuation already proved

    I_0(delta)=-B0 log(delta/M)+C_M+o(1), delta->0+.

At delta0, the same prolate integral yields

    I_epsilon(0)=B0/epsilon+FP_dim+O(epsilon),
    FP_dim=C_M+B1.

Proof: split at any small V>0, subtract beta_epsilon(0) on[0,V], and integrate its constant term exactly:

    beta_epsilon(0)*(V/M)^epsilon/epsilon.

The remainder has a finite limit; it is the same subtracted integral contributing to C_M. Near the focal endpoints the additional factor(P^2-z^2)^epsilon is integrable uniformly for epsilon in a small neighborhood. Away from v0, the UV and isolated-center bounds from the restored-density proof remain integrable for sufficiently small epsilon. These facts justify the local meromorphic expansion. This is a written analytic proof, not a formalized integration theorem.

Therefore the sharp consolidation statement is

    Res_(epsilon=0) I_epsilon(0)
      = coefficient of[-log(delta/M)] I_0(delta)
      = B0 >0.

It is NOT an equality of finite parts. For mu->exp(sigma)mu, FP_dim shifts by-2sigma B0 while the threshold finite constant C_M is unchanged. Changing M shifts C_M and B1 oppositely, leaving FP_dim unchanged. No scale is selected merely to force agreement.

For the signed response -8L_ext I with fixed L_ext, both singular coefficients acquire the same factor-8L_ext. This preserves the match without identifying this representative with a full physical graph sum.

## Order of limits remains observable

For delta>0 the epsilon0 integral is regular, whereas at delta0 it has the pole above. Consequently

    lim_(epsilon->0+) lim_(delta->0+) epsilon I_epsilon(delta)=B0,
    lim_(delta->0+) lim_(epsilon->0+) epsilon I_epsilon(delta)=0.

The common coefficient does not make the two operations interchangeable.

## Consolidated evidence boundary

| Layer | What is now supplied | What is not inferred |
|---|---|---|
| Physical source | Normalized boundary-field correlator; deletion rules; external-leg comparison; specified Gaussian susceptibility model | Universal preparation/measurement access or a unique subtraction scheme |
| Existing observer | Source direct-score port recovers the Gram-dark direction | Acyclicity of an unaugmented3->6 cone; the explicit compatibility differential is needed |
| Restored representative | Full dash/component factors, distinct deletion masks, positive-energy integrability | Inversion of the integrated relative-normal grade or full graph assembly |
| Analytic comparison | Positive-sheet Taylor/integration commutation; endpoint-inclusive threshold logarithm; regulator residue match for identical density | Selection of physical i0 boundary value or canonical finite-part equality |
| Completion | Exact retained-grade recovery and scoped norm estimates | Uniform bounded observability in every physical topology |

The older six-term localized triangle period and this restored deletion representative are related research objects, not silently identical densities. The present equality is internal to the explicitly frozen D_delta; it does not assert that B0 equals an earlier triangle coefficient without a term-by-term source comparison.

## Programme disposition

Freeze this analytic benchmark. Further auxiliary asymptotics are not the priority. The next obligation is source admission: select the actual graph combination, continued chain/i0 and readout prescription, and identify the normalized operator-level extraction. Existing evidence-bearing owner handoffs remain open; no acknowledgment or adoption is inferred. Local primary-source comparison can continue without fabricating those inputs.

## Verification

`check_threshold_regulator_match.py` verifies angular normalization, the threshold/pole/finite-part identities on an exact Mellin model, scale bookkeeping and an endpoint beta-integral control. `check_comparison_consolidation.py` freshly reruns eight relevant headless checks and records their receipts. These finite checks support the scoped written proofs, not physical source admission or machine-formalized analysis.
