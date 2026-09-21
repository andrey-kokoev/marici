# The theta packet is a tensorized localized common-history observation

## Source match

The earlier note `research/nima/every-completed-theta-pair-shell-is-a-product-weighted-ratio-translate-of-one-base-correlation-kernel.md` defines, for arbitrary shell endpoints,

    K_[A,B](s) = integral_A^B Phi_1(v) Phi_1(v+s) dv.

The cutoffwise construction in `common_radial_history_has_a_cutoffwise_half_line_L2_bound_20260911.md` uses precisely this integral with interval-source coefficients and a ratio shift D. Our atoms H_i are its D=0 columns, with [A,B]=[log a_i,log b_i]. The completed-atom normalization is the one recorded in `theta-parity-channel-transport-and-absolute-noise-obstruction.md`.

This identifies the integral and its finite interval source directly. The later completed projective-source theorem is restricted to a particular consecutive-prime catalogue; inclusion of our interval catalogue into that completed source requires an additional catalogue map. The finite construction below uses the earlier arbitrary-shell formula.

## Explicit source map

Let the consecutive endpoints be

    2,4,6,10,12,14,20,28,30,42,60,70,84,140,210,420.

Write I_i=[log a_i,log b_i] for the fifteen adjacent intervals, I=[log 2,log 420], and L=L2(I,dv). Define

    J:C^15 -> L,       J e_i = 1_(I_i),
    C:L -> L2(R_+,ds),
    (Cf)(s) = integral_I f(v) Phi_1(v) Phi_1(v+s) dv.

Endpoints of adjacent intervals have measure zero. Consequently

    J*J = D,       D_ii = log(b_i/a_i) > 0,
    C J = H.

Let X=C^24 be the route source and K_r its event-segmented interval signature maps. Define the multipoint interval source and observation by

    E = L2(I^2) direct-sum L2(I^4),
    A c = (J^(tensor 2) K_2 c, J^(tensor 4) K_4 c),
    O = C^(tensor 2) direct-sum C^(tensor 4).

Under the standard Hilbert tensor identifications,

    O A = (H^(tensor 2) K_2, H^(tensor 4) K_4) = F.

This constructs the observation square with the tensorized finite localized common-history source. Extension of the full earlier signed analytical system to these tensor degrees remains a separate comparison.

## Boundedness with the actual kernel

The kernel of C is k(s,v)=Phi_1(v)Phi_1(v+s). Tonelli gives

    ||C||_HS^2
      = integral_I |Phi_1(v)|^2 integral_0^infinity |Phi_1(v+s)|^2 ds dv
      <= ||Phi_1||_2^2 ||1_I Phi_1||_2^2 < infinity.

Thus C is Hilbert--Schmidt. O is bounded, with

    ||O|| <= max(||C||^2, ||C||^4).

For a simple tensor the formula OA=F follows by Fubini; boundedness extends it to the tensor Hilbert spaces. No inverse theta Gram computation enters this argument.

## Pulled-back pairing

The ordinary interval-source L2 pairing pulls back to the explicit positive matrix

    Lambda = A*A
      = K_2* D^(tensor 2) K_2 + K_4* D^(tensor 4) K_4.

The matrix formed by the selected eighteen two-point and six four-point rows is the previously verified invertible M. Therefore the combined map (K_2,K_4) is injective. Since D is positive definite, Lambda is positive definite and A is an isomorphism onto its finite-dimensional image.

The observation pairing is

    Gamma = F*F = A* O* O A
      = K_2* G_H^(tensor 2) K_2 + K_4* G_H^(tensor 4) K_4,
    G_H = H*H.

These formulas identify both positive pairings without changing any atom amplitude. Lambda is the inherited interval-source pairing. Identification with an earlier signed Green form still requires that form's explicit restriction to this source.

The adjoint of A for these ordinary Hilbert structures is

    A*(f_2,f_4) = K_2* (J*)^(tensor 2) f_2 + K_4* (J*)^(tensor 4) f_4,
    (J*f)_i = integral_(I_i) f(v) dv.

Its image inverse is Lambda^(-1) A*. Thus the finite source comparison includes a concrete inverse and its precise pairing.

## Packet growth and its remaining independent comparison

At each finite packet use its own endpoint segmentation and construct A_k in the same way. On the admitted source image E_k^packet=ran(A_k), whenever A_k is injective, a packet map U:X_k -> X_l induces

    U_interval = A_l U Lambda_k^(-1) A_k* : E_k^packet -> E_l^packet.

It obeys U_interval A_k=A_l U. Compositions agree exactly on the packet images. Injectivity must be checked for each packet and signature order; the four-prime degree-(2,4) instance above has that certificate. At other orders, descent instead requires ker(A_k) subset ker(A_l U).

The earlier common-dilation law translates shell endpoints by log p, changes the label half-density by p^(-1), and retains the ratio. Identifying a fixed-slot route insertion with this earlier operation requires a source calculation: insertion changes only the appropriate suffix and its incident signature contributions. A single global shell translation does not encode that slot dependence.

Accordingly, the remaining growth task is to express the independently specified earlier source operations on these multipoint interval functions and compare them with U_interval. The displayed transported map establishes packet coherence on its image, while leaving that independent comparison explicit.

## Result

The finite observation comparison is now constructed: A is the interval-signature step-function map, O is the tensorized prior common-history integral, and OA=F exactly. Its ordinary source pairing is Lambda and its output pairing is Gamma. The remaining identifications concern the completed catalogue, the earlier signed Green form, and independently defined arithmetic successors.
