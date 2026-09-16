# The oriented Hankel quarter turn is a metaplectic square root of the declared G4 radial swap

## Question

How does the newly constructed radial Fourier quarter turn relate to the declared G4 radial amendment, which correctly identifies only Fourier square with the reciprocal radial swap?

## Claim boundary

It refines rather than contradicts the amendment. The oriented oscillatory Hankel operator is an explicit order-four lift whose square is exactly the declared order-two radial swap. For every wall phase \(|u|=1\), gauge conjugation supplies the corresponding lift. This does not identify the quarter turn with the swap.

## Declared half-turn interface

At phase \(u=1\), oriented radial half-density coordinates are

$$
(C_1f)_\epsilon(r)=f(\epsilon r),
\qquad r>0.
$$

Reflection acts as channel exchange

$$
W_1=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

and the declared contract law is

$$
C_1\mathcal F^2=W_1C_1.
$$

## Constructed quarter-turn lift

Define on the radial image

$$
\widetilde W_1=C_1\mathcal FC_1^{-1}.
$$

In logarithmic half-density coordinates it has the explicit kernel

$$
K_{\epsilon',\epsilon}(v,u)
=e^{(u+v)/2}
 e^{-2\pi i\epsilon\epsilon'e^{u+v}}.
$$

Therefore

$$
\widetilde W_1^2
=C_1\mathcal F^2C_1^{-1}
=W_1,
$$

and

$$
\widetilde W_1^4=I.
$$

Thus \(\widetilde W_1\ne W_1\): it is a metaplectic square root of the radial swap.

## Spectral form

Logarithmic Mellin transform gives

$$
\mathcal M_{\log}\widetilde W_1\mathcal M_{\log}^{-1}
=G(t)\mathcal R_t,
$$

where \(\mathcal R_t h(t)=h(-t)\) and

$$
G(t)=
\begin{pmatrix}
m_+(t)&m_-(t)\\
m_-(t)&m_+(t)
\end{pmatrix}.
$$

The identity \(\widetilde W_1^2=W_1\) is equivalently

$$
G(t)G(-t)=W_1
$$

in orientation coordinates. In parity coordinates this says that the even Tate branch squares to \(+1\) under spectral reflection while the odd branch squares to \(-1\).

## Phase-wall family

Let

$$
D_u=\operatorname{diag}(1,u),
\qquad |u|=1.
$$

The declared radial swap is

$$
W_u=D_uW_1D_u^{-1}
=
\begin{pmatrix}0&u^{-1}\\u&0\end{pmatrix}.
$$

Define

$$
\widetilde W_u
=D_u\widetilde W_1D_u^{-1}.
$$

Then

$$
\widetilde W_u^2=W_u,
\qquad
\widetilde W_u^4=I.
$$

Because \(D_u\) is unitary, this preserves the radial Hilbert metric and the regulated comb Gram identities.

## Contract comparison

The radial amendment declares:

- \(\mathcal F^4=I\);
- \(W_u^2=I\);
- \(C_u\mathcal F^2=W_uC_u\);
- quarter turn must not be identified with radial swap;
- a metaplectic lift is optional presentation bookkeeping.

The constructed \(\widetilde W_u\) satisfies every prohibition and fills the optional lift with an analytic operator. It leaves the existing half-turn declaration unchanged.

## Disposition

The external radial contract and the oriented Fourier construction now have an exact common operator relation:

$$
\boxed{\widetilde W_u^2=W_u,\qquad \widetilde W_u^4=I.}
$$

The quarter turn is not the declared radial swap; it is its source-derived oscillatory Hankel square root. Remaining external work is owner acceptance of this optional lift and its response-carrier typing.