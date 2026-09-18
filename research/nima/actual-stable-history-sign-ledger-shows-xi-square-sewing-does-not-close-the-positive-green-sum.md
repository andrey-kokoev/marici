# Actual stable-history sign ledger shows Xi-square sewing does not close the positive Green sum

The source histories satisfy

$$
(\partial_q-z)u_\pm=\Phi,
$$

with `u_-` left-stable and `u_+` right-stable. Put both sectors on the positive half-line by defining

$$
G_z^+(t)=-u_+(t;z),
\qquad
G_z^-(t)=u_-(-t;z),
\qquad t\ge0.
$$

Using evenness of `Phi`, their equations are

$$
(\partial_t-z)G_z^+=-\Phi,
\qquad
(\partial_t+z)G_z^-=-\Phi.
$$

Thus the forward Green parameter is `-z` in the `+` sector and `z` in the `-` sector. The polarized identities are

$$
-(z+\overline w)K_+(w,z)=E_+(w,z)-F_+(w,z),
$$

$$
(z+\overline w)K_-(w,z)=E_-(w,z)-F_-(w,z),
$$

where

$$
E_\pm(w,z)=\overline{G_w^\pm(0)}G_z^\pm(0).
$$

The forcing transforms are

$$
F_+(w,z)=R(z)+\overline{R(w)},
$$

$$
F_-(w,z)=R(-z)+\overline{R(-w)}.
$$

To obtain the positive bulk sum, subtract the `+` identity from the `-` identity:

$$
(z+\overline w)(K_-+K_+)
=E_- -E_+ +F_+-F_-.
$$

At a pair of Xi zeros, seam matching gives

$$
G_z^-(0)=-G_z^+(0),
$$

so `E_-=E_+`. But Wiener–Hopf sewing gives

$$
R(-z)=-R(z)
$$

at an Xi zero. Consequently

$$
F_+(w,z)-F_-(w,z)
=2R(z)+2\overline{R(w)},
$$

which does not vanish in general.

By contrast, the Xi-square factorization controls the sum

$$
F_++F_-
=\Xi(z)^2+\overline{\Xi(w)^2},
$$

but that sum is paired with the indefinite bulk difference `K_- - K_+`, not the positive bulk sum.

Therefore scalar Xi-square Wiener–Hopf sewing does not close the desired positive Green cycle. An additional source channel must convert the forcing **difference** into an Xi-divisible boundary, or the relative-Haar/linking system must supply exactly its negative.

Status: reciprocal sign ledger completed; naive Xi-square positive-cycle closure rejected.
