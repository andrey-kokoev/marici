# Prior fixed-cutoff continuity for the source-retaining comparison graph

## New source material inspected

- `research/strominger/archimedean-cutoff-entry-v1.md`, physical carrier, cosine kernel and trace-class justification;
- `research/voevodsky/two-sided-schwartz-localization-makes-the-regular-relative-hardy-kernel-trace-class.md`;
- `research/voevodsky/trace-class-localization-makes-transported-regulator-removal-automatic.md`;
- `research/nima/many-many-trace-class-response-continuity.md`.

Retain the previously located correction `correction-the-relative-projection-trace-formula-does-not-directly-evaluate-the-left-hardy-compressed-product.md` when interpreting trace-value claims in these sources.

This search extracts an explicit fixed-cutoff estimate from the prior kernel argument. It is not a fresh certification or a complete native/semilocal F736 instantiation. No tests were run.

## 1. Actual physical one-sector carrier, not a toy regulator

The existing archimedean construction uses

    H=L2(R_plus,dx),
    C f(x)=2 integral_0^infinity cos(2 pi x xi) f(xi) dxi,
    P_Lambda=1_(0,Lambda],
    Q_Lambda=C P_Lambda C*,
    Z_R=P_R.

The source-normalized dilation U_t f(x)=t^(-1/2) f(x/t) is unitary. For a log-coordinate observer a in C_c^infinity(R),

    A_a=integral_R a(u) U_(exp u) du,
    ||A_a|| <= ||a||_L1.

The physical half-density is retained when translating this log observer into the multiplicative source notation. Bare dilation and unitary dilation must not be interchanged without that factor.

## 2. Explicit trace-norm bound extracted from the prior Taylor argument

The prior note justifies trace class by an absolutely summable rank-one Taylor expansion on bounded spatial/frequency intervals. Its quantitative form is as follows.

On (0,Lambda)^2 the kernel of P_Lambda C P_Lambda is

    2 cos(2 pi x xi)
      =2 sum_(n>=0) (-1)^n (2 pi)^(2n) x^(2n) xi^(2n)/(2n)!.

The nth rank-one term has trace norm

    2 (2 pi)^(2n) Lambda^(4n+1)/((2n)!(4n+1)).

Therefore

    ||P_Lambda C P_Lambda||_1
      <= B_Lambda
      :=2 Lambda sum_(n>=0)
         (2 pi Lambda^2)^(2n)/((2n)!(4n+1))
      <=2 Lambda cosh(2 pi Lambda^2).

Since P_Lambda Q_Lambda=(P_Lambda C P_Lambda) C* and C is unitary,

    ||P_Lambda Q_Lambda||_1 <= B_Lambda.

This is a direct quantitative extraction from the existing physical kernel, not an alternative finite matrix or quadrature approximation.

## 3. Continuity of the fixed-cutoff ordered trace coordinate

The operator coordinate is continuous from log L1 to trace class:

    ||P_Lambda Q_Lambda A_a||_1
      <= B_Lambda ||a||_1.

For the actual bounded outer projection, the fully retained ordered expression obeys

    ||Z_R P_Lambda Q_Lambda A_a Z_R||_1
      <= B_Lambda ||a||_1.

Thus its trace is a continuous linear observer functional for every fixed finite cutoff. No observer/cutoff commutation or replacement by a symmetric Mellin window is used.

For polarized amplitudes a,b, the actual operator pair gives

    ||Z_R P_Lambda Q_Lambda A_a A_b* Z_R||_1
      <= B_Lambda ||a||_1 ||b||_1.

This proves a continuous sesquilinear trace coordinate on the declared compact physical log-test domain. It does not give a finite-dimensional convolution closure.

Use D=C_c^infinity(R) in this one character sector with its LF topology. Fixed-support stages D_K make all these estimates continuous in the defining seminorms. Convolution is continuous on the appropriate pair of stages and sends supports K1,K2 to their sum/difference stage. A fixed K is not itself a convolution algebra.

## 4. Other source coordinates on the compact physical core

For support in [-M,M], the Mellin/Fourier entire evaluations satisfy

    |m_a(+/-i/2)| <= exp(M/2) ||a||_1.

These bounds establish endpoint continuity on a fixed compact-support stage, not on unrestricted Plancherel completion. Point evaluation a(0), used by the source volume density, is continuous in the smooth compact-test topology. The source's response map is continuous in its declared test/history/strong-dual topology; the normalized spectral local pairing is a continuous source distribution on its admitted test class.

Accordingly, once the exact physical/multiplicative conventions and the chosen source distribution are matched, the fixed-cutoff coordinates needed in the v11 comparison graph have concrete source continuity evidence: response, represented observer, ordered trace, volume, spectral pairing, remainder and endpoints. The remainder is their actual difference, not zeroed by the finite-part limit.

This gives a substantive one-sector starting point for the open carrier-instantiation task. It does not by itself match every native analytical presentation or all semilocal places/characters.

## 5. What this estimate does NOT prove about regulator families

The bound 2 Lambda cosh(2 pi Lambda^2) is deliberately crude. It proves fixed-cutoff trace-norm continuity, but not polynomial-log growth, uniform trace-norm tails, rapid decay or any simultaneous limit.

For stronger family topology one must use the source-specific centered estimate, with its exact observer normalization and bounded-packet hypotheses, not infer it from this nuclear bound. The v7 remainder note supplies a conditional family estimate under the admitted Connes source theorem; identifying that theorem's domain and normalization with the present physical sector remains explicit.

Coordinatewise product-family continuity is a weaker claim and must be labelled as such if used for a retained graph carrier. Its graph closedness is not a proof of stronger family continuity.

## 6. Prior relative-kernel continuity and regulator-removal tools

The two-sided Schwartz-localization note gives, for fixed cutoff and character after index separation,

    T_K=D_osc^(-1) (D_osc T_K D_osc) D_osc^(-1),
    ||T_K||_1 <= ||D_osc^(-1)||_2^2 ||D_osc T_K D_osc||,

with the middle norm controlled by finitely many Schwartz-kernel seminorms. This provides source/trace-ideal continuity for the regular symmetric relative projection placement under the declared smooth polynomially controlled phase assumptions.

The note's additional ORDERED Hardy placement requires its separate Sobolev/commutator hypotheses. Its trace cannot be read off from the uncompressed DeltaQ diagonal: the later placement correction explicitly withdraws that inference. Trace-class membership and trace evaluation are different results.

The transported-regulator lemma states: if T is trace class and Z_r,Z_r* converge strongly to identity with uniform operator bound, then

    ||Z_r T Z_r* - T||_1 -> 0.

It applies only after proving trace class for the ACTUAL inherited placement. It gives fixed-cutoff outer removal, not all-path simultaneous limits. Angular assembly additionally requires finite support or a summable trace-norm majorant. Endpoint/index channels remain separately included.

## 7. Polarized source linearization is available conditionally

The many-many continuity note says a bounded bilinear bordered response extends via the projective tensor universal property to a bounded linear map on the trace-class source, where rank-one inputs recover the original pair response.

Its required graph bound is a hypothesis; finite-shell Gaussian estimates do not automatically establish the global bound. This is useful for typing the candidate comparison graph when a linear source is wanted, rather than pretending a pair-dependent form is a linear map on a single observer variable.

## Refined next step

The open carrier task can start with the fixed-cutoff one-sector estimates above and actual source-preserving round trips. It should report exactly that strength, then separately match the source normalized spectral and cutoff distributions and audit the chosen regulator-family topology.

Only after that carrier/domain audit comes the modification-boundary identification, inverse mate and coupled bottom/filler calculation. A new generic graph theorem is unnecessary; a fixed-cutoff estimate cannot be silently promoted to the full native analytical witness.

## Disposition

Prior physical-kernel research supplies a quantitative route to the first coordinate-continuity gate on a genuine infinite-dimensional observer test space. The remaining issues are source-normalization matching, regulator-family strength, semilocal/native binding and modification-level comparison—not existence of a fixed-cutoff trace functional in this physical sector.
