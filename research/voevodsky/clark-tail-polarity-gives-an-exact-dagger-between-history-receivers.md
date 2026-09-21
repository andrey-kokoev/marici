# Clark tail polarity gives an exact dagger between history receivers

## Constructed comparison

The actual four-tail construction has an antilinear polarity comparison. It extends to the weighted analytical history receiver, preserves its positive carrier norms, and intertwines the oriented signed Clark forms. Its action changes left creation into right creation. It does not identify creation with annihilation or invert arithmetic events.

This is a specific tail-polarity dagger, with spectral conjugation and ordered-slot reversal. Identifying it with the earlier full convolution/source involution still requires the spatial reciprocal source comparison.

## 1. Actual tail identity

For a complex forcing f on the half-line, define

    G_(sigma,j)(f;z;x)=integral_x^infinity exp(sigma i z(t-x)) t^j f(t) dt,
    h_(sigma,j)(f;z)=G_(sigma,j)(f;z;0).

The common source estimates from `clark-source-interface-domain-and-positivity-audit.md` apply uniformly over reflected compact spectral regions. Direct complex conjugation gives

    G_(sigma,j)(conjugate(f);conjugate(z);x)
      = conjugate(G_(-sigma,j)(f;z;x)).

This holds both for the entire tail and its endpoint trace. On the four-vector ordered as (+,0),(-,0),(+,1),(-,1), let

    P(h_+,0,h_-,0,h_+,1,h_-,1)=(h_-,0,h_+,0,h_-,1,h_+,1).

Then h_(conjugate(f))(conjugate(z))=P conjugate(h_f(z)). For the real completed forcing and real shell indicators, conjugation acts on chamber coefficients alone, so the source diagram commutes explicitly.

No derivative-delta incidence or fitted return row enters this identity.

## 2. Clark and Wronskian orientation

Let C be the fixed four-port coefficient matrix, B=S D_phase the endpoint sewing matrix, and S_2 the two-sheet swap. Exact matrix multiplication gives

    P* C P=-C,
    B P=S_2 B,
    S_2* diag(1,-1) S_2=-diag(1,-1).

The two-sheet alternating Wronskian matrix W_2=[[0,1],[-1,0]] also satisfies

    S_2^T W_2 S_2=-W_2.

Thus this actual tail comparison reproduces the orientation reversal of the earlier Clark-sheet and Wronskian calculations. It does not identify the full Clark coefficient form with the distinct two-endpoint swap pairing; their source crosswalk still involves the complete kernel.

## 3. Correct upper and lower feature spaces

Let Omega_+ be the upper-half-plane disk from the weighted receiver, and Omega_-=conjugate(Omega_+). Set

    k_z^+(t)=exp(izt),       z in Omega_+,
    k_z^-(t)=exp(-izt),      z in Omega_-.

Both belong to L2(R_+). Their pairings are

    <k_w^+,k_z^+>=1/[-i(z-conjugate(w))],
    <k_w^-,k_z^->=1/[+i(z-conjugate(w))].

Therefore the feature realization of the same analytically normalized Clark kernel uses C_+=C and C_-=-C. The lower sign is forced by the Cauchy denominator, rather than selected to fix an isometry residual.

Let E_+ and E_- be the L2 spaces of these four-vector features on their spectral disks times the half-line. Define

    (A F)(zeta,t)=P conjugate(F(conjugate(zeta),t)),       zeta in Omega_-.

Spectral reflection preserves area measure, so A:E_+ -> E_- is antiunitary. Its inverse has the same reflected formula. For the source feature maps L_+,L_-,

    A L_+(v)=L_-(conjugate(v)).

Moreover,

    <A F,C_- A G> = conjugate(<F,C_+ G>).

The full divided-difference kernels consequently obey

    K_-(conjugate(w),conjugate(z);conjugate(f),conjugate(g))
      = conjugate(K_+(w,z;f,g)).

Using C rather than -C on the lower feature space gives the wrong sign. The checker explicitly tests this hostile.

## 4. Extension to ordered histories

The weighted source norm is real in the chamber basis. Define on tensor histories

    (v_1...v_r)^dagger=conjugate(v_r)...conjugate(v_1).

It is an isometric antilinear involution on A_rho(V), reverses multiplication, and preserves the analytic domain. Unlike the separately proposed inverse-event involution, it is degree preserving.

On weighted feature histories define

    A_r(x_1 tensor ... tensor x_r)=A x_r tensor ... tensor A x_1,
    A_0(c)=conjugate(c).

The direct sum A_F is antiunitary between the two weighted Fock carriers. The vacuum feature map Z(h)=Pi(h)Omega_vac satisfies the exact source square

    A_F Z_+(h)=Z_-(h^dagger).

For the explicitly chosen graded signed forms J_+=direct_sum C_+^(tensor r) and J_-=direct_sum C_-^(tensor r),

    <A_F x,J_- A_F y>=conjugate(<x,J_+ y>).

This constructs a polarity mate for that graded extension. It does not prove that the graded extension is the unique full arithmetic Green form.

## 5. Creation, transpose, and inverse stay separately typed

For left creation c_L and right creation c_R,

    A_F c_L(L_+v) A_F^(-1)=c_R(L_-conjugate(v)).

Both operators increase tensor degree. The ordinary Hilbert adjoint of c_L decreases tensor degree, so it is a different map.

For a history comparison acting on memory by right multiplication with

    r=S_w^(-1)S_w',

dagger gives

    r^dagger=(S_w')^dagger ((S_w)^dagger)^(-1),
    (h r)^dagger=r^dagger h^dagger.

Thus the comparison becomes left multiplication on the opposite record algebra. It carries S_w^dagger to (S_w')^dagger and preserves the existing comparison identities with their proper variance. It does not require r^dagger=r^(-1).

Reversing recorded tensor slots also does not by itself turn a forward prime route into a different forward prime ordering. Typed arrow reversal belongs to the opposite path category; identifying it with reciprocal arithmetic operations requires the independent endpoint and source transport.

## 6. What the previous obstruction still says

The all-order graded-form obstruction concerned right multiplication preserving one fixed form on one carrier. The present result compares two polarity carriers through an antilinear, order-reversing map with their correctly oriented forms.

It supplies no positive functional on the entire formal history and no star representation identifying the record involution with operator adjoint. The analytic source is still A_rho, and the actual history comparison is not asserted unitary for its terminal graded metric.

## 7. Exact remaining source comparison

The new diagram is explicit for half-line tail polarity. The earlier full source involution g->g* includes convolution reversal and spatial/reciprocal identification. To equate the two, one must supply a map from the labelled arithmetic record into that source and check that its involution induces

    (f,z,sigma)->(conjugate(f),conjugate(z),-sigma)

with the required shell and endpoint transport. That equation must be checked before calling the present A_F the full physical source dagger.

The moving-seam metric bundle and Wronskian translation pairing remain the appropriate independently specified targets for that comparison. The four-tail polarity and oriented spectral normalization are now settled.

## Verification

Fresh command:

    uv run --with sympy --with mpmath python research/voevodsky/checkers/check_clark_history_polarity_dagger.py

Passed exact matrix tests for the Clark coefficient, sheet sewing, Wronskian sign, and full-kernel orientation, plus a wrong-sign hostile and finite word-reversal tests. A 35-digit compact-source regression tests the tail identity for complex shell coefficients at four spatial points; its reported discrepancy was zero at that precision.

The analytical antiunitarity, bounded extension, and all-order tensor statements follow from the displayed formulas and the preceding weighted receiver estimates. No physical inverse/adjoint identification is inferred from the finite fixture.
