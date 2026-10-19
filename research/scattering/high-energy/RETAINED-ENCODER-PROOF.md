# H3: retained encoder and declared continuation

## Fixed model and both endpoint poses

This proves H3 for the supplied unitary cycle-comparison model, not that this law follows from underlying physical dynamics. At each endpoint the source selects the two cycle links adjacent to the prospective small cell in each body: indices 1->2 and 2->3 at the positive endpoint; 2->3 and 3->4 at the negative endpoint. The two bodies' cell coordinates are disjoint. All coordinates are retained.

Each link is a unitary spin comparison. This is preserved by the source's endpoint spin-frame transport: a link V becomes F_j V F_i*, with unitary frame blocks. Therefore the following argument applies to each actual endpoint separately; it does not assign the positive endpoint's matrix to the negative endpoint.

For arbitrary unitary two-spinor links A,B, the two-row path comparison is

    D_path = [ -A   I   0 ]
             [  0  -B   I ].

Consequently

    M_path = D_path D_path* = [ 2I  -B* ]
                                          [ -B   2I ].

The off-diagonal Hermitian block K=M_path-2I satisfies K²=I and tr(K)=0. Thus M_path has eigenvalues 1 and 3, each twice, independently of A,B. With two disjoint bodies, M=DD* has each eigenvalue four times. In particular it is positive and invertible at **both** endpoints, without any numerical threshold or generic-rank assumption.

## Exact retained encoder identities

Let P1=(3I-M)/2 and P3=(M-I)/2. From (M-I)(M-3I)=0 these are orthogonal Hermitian projectors summing to I. The positive inverse square root is

    R=M^(-1/2)=P1+P3/sqrt(3).

Set W=RD, Q=W*W and N=I-Q. Then

    WW*=R M R=I8,
    Q*=Q=Q², N*=N=N², WN=0,
    W* M W=D* R M R D=D*D.

For U=[[N,W*],[W,0]], direct multiplication gives U*=U and U²=I28. In particular U preserves the full norm for **every** cell-and-memory input, not only initially empty memory. N and the eight memory coordinates are essential parts of the construction.

## Continuation is explicitly transported, not independently identified

H_pre=H_111 direct-sum M is the fixed finite Hermitian endpoint operator. Define H_post=U H_pre U*. Induction yields H_post^n U=U H_pre^n for all n. The finite-dimensional exponential series converges in operator norm, so

    exp(-it H_post) U = U exp(-it H_pre)

for all real t and all inputs, hence also for H3's t>=0. This establishes the declared continuation without computing a finite selection of times.

It does **not** prove H_post=H_F. The native outgoing H_F has a trace sixteen units lower at epsilon=1 (H9); motion remains part of the complete scattering energy ledger. No kinetic scattering solver was run for H3.

## Fresh verification and its boundary

`check_retained_encoder.py` checks the exact source archive's ten unitary cycle blocks, reconstructs the positive-frame crossing D independently from T, reconstructs M,W,N,U, and compares them with the archived exact matrices. It checks both cell choices' path support and their exact positive spectra in that frame. The negative endpoint's transported matrix is covered by the arbitrary-unitary-link proof above, **not** claimed as a fresh reconstruction of its geometry or spin transport.

The checker also verifies the generic projector/inverse-square-root polynomial identities modulo (x-1)(x-3), the full archived encoder's norm and energy identities, and the native Hamiltonian trace obstruction. Thus the archive replay supplies a source-specific audit in addition to the universal proof. Nested/source hash checks and these algebraic identities do not authorize physical outcomes.

```sh
uv run --with sympy python research/scattering/high-energy/check_retained_encoder.py --check
```
