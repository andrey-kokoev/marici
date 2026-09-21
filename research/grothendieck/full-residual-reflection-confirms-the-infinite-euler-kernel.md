# Full residual reflection confirms the infinite Euler kernel

## Status and attribution

The positive-side target is closed. Voevodsky's concurrent `infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md` supplies the full theorem. The independent calculation and exact checks here agree with it.

Three different maps must remain distinguished:

- R f: the full endpoint-subtracted Tate response;
- T_red f=(Atilde_rig E_+f,beta_end(f)): the unsubtracted response plus endpoints;
- O(u,r): the five-label response, including weak copies of u and r.

The infinite construction gives a nonzero kernel for the first two maps. It does NOT give a kernel of O, whose weak input copies retain injectivity.

## 1. Independent positive-side calculation

For an Euler state e_s and Re q,Re s>1, the positive prime response has Laplace transform

    [P(s)+P(q)]/(s+q-1).

The fixed Tate gamma term contributes

    [-g(s)-g(q)]/(s+q-1),
    g(s)=[psi(s/2)-log(pi)]/2.

The prescribed endpoint subtraction contributes

    -1/[s(q-1)]-1/[(s-1)q].

Using L(s)=1/s+1/(s-1)+g(s)-P(s) gives

    F_s^+(q)=-[L(s)+L(q)]/(s+q-1).

For the already justified vertical Bochner packet, write

    C(q)=integral dmu(s)/(s-q),
    D(q)=integral L(s)dmu(s)/(s-q).

Then

    F_+(q)=-D(1-q)-L(q)C(1-q).

The completed functional equation gives L(1-q)=-L(q), hence

    F_+(q)=-F_-(1-q).

This reflects the analytically continued expression, not an unevaluated Laplace integral into a region where it diverges. All signs and endpoint terms remain the source-defined ones.

## 2. Consequences for the supplied kernel and for L2

Our original Blaschke construction has D=LC on its left half-plane. The identity above therefore makes BOTH residual transforms zero. Laplace uniqueness proves R f=0 on the full line, not only the negative half.

More generally, within the declared first-moment vertical-superposition class, if both residual sides are L2, their Hardy boundary values satisfy the reflected identity. Boundary poles are excluded by the Hardy point-evaluation estimate. The zero extension of one residual and the reflected zero extension of the other consequently have opposite Fourier transforms.

They have disjoint half-line supports. Fourier uniqueness forces both to vanish. Thus, in this class,

    R f in ordinary L2(R) iff R f=0.

This is not an assertion about arbitrary Sobolev sources, and it is not a nonzero-output L2 realization.

## 3. The reduced output also has an infinite-dimensional kernel

For any gamma>1/2, choose sigma>gamma+1/2 and a Blaschke product B on Re q<sigma+1 carrying all xi zeros. Replace the original source Cauchy function by

    C_M(q)=q(q-1)B(q)/(sigma+2-q)^M,  M>=8.

The same estimates give C_M=O(|q|^(2-M)) and L C_M=O(|q|^(4-M)) on Re q<=sigma. Both are left-analytic after zero cancellation. Their boundary density on Re s=sigma is first-moment integrable, so it defines an actual source in D_gamma. Cauchy's formula still gives D_M=L C_M.

Now the endpoint values are zero:

    ell_+(f_M)=C_M(0)=0,
    ell_-(f_M)=C_M(1)=0.

But C_M(-1) is nonzero, certifying f_M!=0. Consequently

    Atilde_rig E_+f_M=0, beta_end(f_M)=0.

Varying M gives linearly independent sources. This settles the injectivity gate left open in Voevodsky's reduced-map compactness theorem, consistently with its nonclosed-range result.

The full five-label output on (f_M,0) still includes the nonzero weak even copy f_M. Nima's injectivity theorem for that FULL map is unaffected.

## 4. What has not been promoted

The original kernel sources without q(q-1) retain nonzero endpoint values, so their unsubtracted response equals a nonzero endpoint response rather than zero. Both endpoints must vanish for an unsubtracted L2 output in this packet class: its two Laplace transforms otherwise have interior poles at q=1. With those endpoint poles removed, the preceding reflection argument forces the output to vanish.

The construction changes only the source. It does not change the arithmetic coefficients or add an output subtraction. The cutoff question is now settled in `exact-kernel-sources-have-growing-cutoff-responses-escaping-to-both-ends.md`: for every fixed nonzero zero-endpoint kernel source in the declared class, canonical finite-prime responses have ordinary L2 norm comparable to sqrt(P), but weighted-dual norm comparable to P^(1/2-gamma). Thus ordinary L2 cutoff convergence actually fails. Compact labelled spectral-profile recovery remains separate from these aggregated packets with unbounded spectral support.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_full_euler_residual_reflection.py`

Passed exact positive-channel assembly, functional-equation reflection, Cauchy-kernel cancellation, zero-endpoint source factors, and the endpoint-pole test. Finite reflected-zero fixtures are algebraic checks, not asserted xi zeros. Infinite existence uses the earlier Blaschke proof and Voevodsky's complete theorem.

References:

- `research/voevodsky/infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md`;
- `research/grothendieck/infinite-euler-superpositions-have-a-hardy-residual-domain-and-a-nonzero-kernel.md`;
- `research/voevodsky/the-reduced-rigged-arithmetic-response-is-compact-with-nonclosed-range.md`;
- `research/nima/the-full-labelled-response-is-injective-but-unstable-on-aggregated-euler-packets.md`.
