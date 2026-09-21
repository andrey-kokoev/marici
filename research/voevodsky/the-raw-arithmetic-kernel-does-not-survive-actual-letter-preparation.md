# The raw arithmetic kernel does not survive actual-letter preparation

## Result and disposition

The constructed reduced-response kernel does not supply an arithmetic-invisible forcing letter for the existing filtered attachment. The obstruction is a precise domain mismatch:

- a nonzero kernel vector is an AGGREGATED half-line function;
- an actual prepared even letter, at each retained spectral label, is one exponential profile;
- interpreting the kernel function as an analytic forcing and preparing it again produces a NONZERO endpoint response.

In fact the actual preparation map does not preserve the raw arithmetic kernel. It cannot descend through the quotient by that kernel on the enlarged analytic forcing domain. This is an obstruction to a proposed quotient, not a new two-seam witness in the existing source.

Inputs:
- `infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md`
- `../nima/holomorphic-endpoint-output-recovers-actual-residual-ports-but-not-arbitrary-graph-inputs.md`
- `../nima/the-residual-port-restores-the-labelled-two-seam-comparison.md`

## 1. Keep the two coordinates and operations distinct

Use x for the forcing variable and u for the receiver half-line variable. An actual forcing h is prepared by

    X_h(z)=integral_0^infinity cos(zx)h(x)dx,
    U_h(z)(u)=sqrt(2)X_h(z)exp(i z u),
    V_h(z)(u)=sqrt(2)[iX_h'(z)-L(s(z))X_h(z)]exp(i z u),
    s(z)=1/2-i z,  L=xi'/xi.

The reduced receiver map acts on u-functions:

    T_red k=(Atilde_rig E_+k,beta_end(k)).

The constructed nonzero k_M satisfy T_red k_M=0. This does not assert that T_red U_(k_M)(z)=0. Applying the receiver map directly to a function and first using that function as forcing are different operations.

## 2. A nonzero kernel vector cannot itself be a prepared even fibre

For any profile a exp(i z u) in the Euler sector,

    ell_+(a exp(i z u))=a/s(z).

Since s(z)!=0, a zero endpoint forces a=0. Thus a nonzero k_M with ell_+(k_M)=0 cannot equal U_h(z) for ANY forcing h and any admitted fixed spectral label z.

Nor can k_M be inserted as a constant family of prepared even states. Slotwise preparation retains independent spectral arguments; it does not aggregate an unbounded vertical spectral measure into one u-function before applying the endpoint response.

On the full compatible holomorphic family, vanishing endpoint output implies X_h identically zero, then X_h' identically zero, so BOTH U and V vanish. The supplied endpoint-derivative reconstruction is a continuous inverse with its compact-margin loss. There is consequently no nonzero compatible primal letter killed by this reduced family output.

At one isolated spectral point U can vanish while V does not. The previously supplied two-window hostile proves that separate pointwise phenomenon; it is not the aggregated kernel construction here.

## 3. Analytic forcing admissibility does not remove the obstruction

Fix forcing weight beta and receiver weight gamma with beta>gamma>1/2. Choose the kernel construction on a line sigma>beta+1/2. Its source k_M lies in D_beta and hence in the analytic forcing Hilbert space H_beta.

So it is legitimate to compute X_(k_M), U_(k_M) and V_(k_M) as analytic forcing maps. This membership does NOT by itself make k_M an actual edge forcing of the arithmetic path source. Such an edge carries its prescribed window and labels; we do not adjoin a new edge.

Write its source Cauchy transform as

    C_M(q)=integral exp((q-1/2)x)k_M(x)dx
          =q(q-1)B(q)/(sigma+2-q)^M,  Re q<sigma.

Then, on the forcing strip,

    X_(k_M)(z)=[C_M(s(z))+C_M(1-s(z))]/2,
    iX_(k_M)'(z)=[C_M'(s(z))-C_M'(1-s(z))]/2.

These identities explicitly compute the re-prepared letter and its moment. Its window-residual amplitude is therefore

    [C_M'(s)-C_M'(1-s)-L(s)(C_M(s)+C_M(1-s))]/2.

There is no reason for this to equal the zero raw Tate response; the two constructions act on different data.

## 4. The re-prepared endpoint is strictly visible

Choose the Blaschke product with conjugate-paired zeros and B(0)>0, as allowed in the kernel construction. It obeys real symmetry. There are no real xi zeros, so B is real, continuous and strictly positive on the real axis in its half-plane of analyticity.

For real 1<s<sigma, both s and 1-s lie in that half-plane. The factors q(q-1) are positive at BOTH arguments, and the denominators sigma+2-q are positive. Hence

    C_M(s)>0,   C_M(1-s)>0.

At any admitted imaginary spectral point z=i y with gamma<y<beta, s=1/2+y lies in (1,sigma). Consequently

    X_(k_M)(i y)>0,
    ell_+(U_(k_M)(i y))=sqrt(2)X_(k_M)(i y)/s>0.

Thus the prepared arithmetic output is explicitly nonzero, even though the same function k_M has zero raw reduced output.

The raw endpoint conditions C_M(0)=C_M(1)=0 have not been violated. They are different evaluations from the cosine combination C_M(s)+C_M(1-s) appearing in actual preparation.

## 5. Its re-prepared residual is not identically zero either

Set A(s)=[C_M(s)+C_M(1-s)]/2. This is analytic on 1-sigma<Re s<sigma. The residual amplitude is A'(s)-L(s)A(s).

If it vanished on an open Euler region, analytic uniqueness on Re s>1 would imply A(s)=c xi(s) there. Continuing to s=1 gives

    A(1)=[C_M(1)+C_M(0)]/2=0,
    xi(1)=1/2,

so c=0. That contradicts A(s)>0 on the real interval (1,sigma). Hence the residual is not identically zero. In every open admitted real-s interval it is nonzero at some point.

This computes a genuine analytic forcing residual. It does not turn k_M into a prescribed event window or authorize building a new diamond around it.

## 6. Why this is not a finite actual window replacement

Every nonzero actual positive event window has strictly positive ell_+ when regarded as a forcing function. The sign-changing k_M, whose ell_+ is zero, cannot be such a window.

More strongly, k_M is not compactly supported. If it were, C_M would extend to a nonzero entire function of exponential type, with zero count O(R) by Jensen's formula. But C_M contains every xi zero with its multiplicity. Classical xi zero counting gives order R log R zeros up to radius R, a contradiction.

Thus it cannot be a finite linear combination of bounded event windows either. Membership in a larger completed span of prescribed windows would require its own proof and norm estimates. Even such membership would not bypass sections 2--4: continuous letter preparation still yields the labelled exponential family rather than the raw aggregate.

## 7. The failed quotient diagram

On the common enlarged analytic domain consider two linear operations:

    k -> T_red k,
    k -> [z -> T_red U_k(z)].

The vector k_M is in the kernel of the first and not of the second. Therefore the second map cannot factor through the quotient by ker T_red of the raw forcing functions. Equivalently, re-preparation does not preserve this kernel.

This is a concrete obstruction to treating the raw arithmetic quotient as a source congruence for the existing attachment. It is NOT the original terminal-record ideal I, and must not be substituted for that ideal.

For the actual compatible holomorphic letter image the reduced family output instead has the supplied continuous reconstruction. Tensoring that inverse on the declared compact-open, feature-radius scales preserves the existing balanced attachment and its nonzero roof. The raw aggregate kernel therefore produces no new invisible class in that image.

## 8. Exact closure of this target

Established:
- the kernel vector cannot itself be an admitted prepared even fibre;
- it can be made analytically admissible as forcing, but re-preparation has strictly nonzero endpoint output;
- its re-prepared residual is explicitly computable and not identically zero;
- the raw reduced kernel is not preserved by preparation, so the proposed raw quotient does not support this source factorization.

No new actual two-seam witness has been constructed from k_M. Doing so by replacing an edge with it would change the source rather than prove descent in the existing one. The previously supplied residual-sensitive witness and endpoint-derivative reconstruction remain the valid attachment statements.

No positivity, ordinary L2 response limit, or recovery of the original forcing norm is inferred.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_kernel_preparation_domain_barrier.py`

Passes exact cosine/moment preparation, endpoint recovery, and a conjugate-paired Blaschke fixture showing zero raw endpoints but positive re-prepared endpoint. Actual kernel existence and the analytical domain and zero-count arguments are the proofs above, not inferred from the toy zeros.
