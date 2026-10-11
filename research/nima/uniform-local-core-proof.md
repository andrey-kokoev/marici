# A uniform local core exists (standard complex semantics)

## Precisely what is tested

We adopt the agreed existential meaning of source-derived: a uniform construction from the native factor maps within declared analytic mathematics. We do not demand that the source uniquely selects a construction.

Contract: `contracts/uniform-local-core-test.v1.json`.

The inputs are the finite factor sets and their involutive maps. The background is standard finite-dimensional complex Hilbert space and ordinary real/complex analysis. No per-source generator, phase profile or path is an input. The following spectral rule is part of the construction itself. Choosing this uniform rule is legitimate for an existence theorem; it would not settle a uniqueness theorem.

## Construction and proof

For a finite set S, let C[S] be its free complex vector space with orthonormal delta basis. A bijection f extends uniquely to the linear operator P_f defined by P_f e_s = e_(f(s)). An involution gives P_f squared equal to I and P_f*=P_f. Thus

`Q_f=(I-P_f)/2`

is a self-adjoint projection. Define, uniformly from P_f,

`H_f=pi Q_f`, `U_f(t)=(I-Q_f)+exp(-i*pi*t) Q_f`.

The input does not contain an independently chosen H or U.

Orthogonal complementary projections give

`U_f(t)* U_f(t) = (I-Q_f)+|exp(-i*pi*t)|² Q_f = I`

for every real t. The standard exponential is continuous and differentiable, so U_f is continuous, `i U_f'(t)=H_f U_f(t)`, `U_f(0)=I`, and `U_f(1)=I-2Q_f=P_f`. These are all-time analytic arguments, not deductions from sampled parameter checks.

For the native square, the canonical basis identification C[Bool x Bool] = C[Bool] tensor C[Bool] gives

`P_L=X tensor I`, `P_R=I tensor X`.

Writing `q=(I-X)/2` and `u(t)=(I-q)+exp(-i*pi*t)q`, the construction gives

`H_L=pi q tensor I`, `H_R=I tensor pi q`,

`U_L(t)=u(t) tensor I`, `U_R(t)=I tensor u(t)`.

This proves more than slice locality. For every factor operator A,

`U_L(t)(A tensor I)U_L(t)* = (u(t) A u(t)*) tensor I`,

while `U_L(t)(I tensor B)U_L(t)* = I tensor B` for every B. The right factor has the symmetric laws. Generators likewise act within their own factor algebras. The two legs commute, so `U(a,b)=U_R(b)U_L(a)` is a continuous unitary square with the four native corners. No return interpretation is needed for this claim.

For a relabeling h, free linearization gives `P_(hfh^-1)=T_h P_f T_h^-1`. The projector and generator are polynomials in P_f, so they obey the same covariance. The explicit exponential projector formula does too. Factor exchange swaps L and R and their parameters. Thus the construction is not tied to arbitrary names of the four states.

These formulas supply a witness of the standalone local-core claim under the declared meaning. The proof outcome is **++ in standard complex-matrix semantics**.

## What the executable check does

`checkers/check_uniform_local_core.py` constructs permutation operators from maps on labels rather than importing preselected generators. It checks the native basis action, involution and projector identities, tensor decomposition, exact endpoint and unit-circle phase cases, factor-algebra action on a matrix-unit basis, and covariance under relabelings and factor exchange. These exact rational-complex checks support the algebraic construction. They are not a kernel verification of the universal analytic proof above.

## Boundaries

- We have not shown that this interpolation is forced by the source. Other uniformly specified interpolations may exist.
- This local-core theorem alone does not supply a whole-Tick return interpretation. The separate follow-up `spectral-whole-return-proof.md` now proves that interpretation for this particular witness in the same declared semantics.
- The operational Cauchy-completion phase remains unimplemented in the required strength. This theorem does not close ScheduledNormBound or any of its kernel verification gates.
- The earlier stopped planning portfolio assumed a stronger/unspecified source contract. Its failure is preserved historically; it is not used to refute this now-clarified local-core proposition.
- This clarification must apply to L in both the standalone claim and the parent. Otherwise the projection/rejection edges would compare different predicates. The parent still additionally requires its whole-Tick return structure.
