# A symbolic modular–Evans–Krein colligation for the theta/Tate programme

## Status

Research synthesis and falsifiable target. This packet rotates the strongest
physical parallels into one symbolic machine. It does not claim that the
required source maps already exist.

## 1. Spectral rotation and the two sectors

Set

\[
z=s-\frac12,
\qquad
\lambda=-iz.
\]

The critical line becomes the real \(\lambda\)-axis. The two open half-planes
become the upper and lower spectral half-planes. Introduce typed sector spaces

\[
\mathcal H_-,\qquad \mathcal H_+,
\]

and a source-derived sewing map

\[
\mathsf S(\lambda):\mathcal H_-\longrightarrow\mathcal H_+.
\]

The local Tate functional equation suggests boundary unitarity,

\[
\mathsf S(\lambda)^*\mathsf S(\lambda)=I,
\qquad \lambda\in\mathbb R.
\]

This determines a lossless seam, not scalar nonvanishing. For fixed source and
readout vectors, the amplitude

\[
\xi(\lambda)
=
\langle e_+,\mathsf S(\lambda)e_-\rangle
\]

may vanish even when \(\mathsf S(\lambda)\) is unitary.

## 2. Canonical bulk and boundary flux

The energy-bearing realization should have a first-order form such as

\[
J\partial_qY=\lambda H(q)Y,
\qquad
J^*=-J,
\qquad
H(q)\ge 0.
\]

For solutions at \(\lambda\) and \(\mu\), the Lagrange identity is

\[
\left[Y_\mu(q)^*JY_\lambda(q)\right]_{a}^{b}
=
(\lambda-\overline\mu)
\int_a^bY_\mu(q)^*H(q)Y_\lambda(q)\,dq.
\]

At \(\mu=\lambda\), this becomes

\[
\left[Y_\lambda^*JY_\lambda\right]_{a}^{b}
=
2i\operatorname{Im}(\lambda)
\int_a^bY_\lambda^*HY_\lambda\,dq.
\]

Because \(\operatorname{Im}\lambda=-\operatorname{Re}z\), a source-derived
vanishing of total boundary flux would imply

\[
2\operatorname{Re}z\,\mathcal E(Y)=0,
\qquad
\mathcal E(Y)=\int_a^bY^*HY\,dq.
\]

If the zero-state bridge produces a nonzero \(Y\), and \(\mathcal E(Y)>0\), then
\(\operatorname{Re}z=0\). This is the exact symbolic confinement mechanism.
The unresolved work is deriving \(H\), the state, and the closed boundary
packet from labelled theta/Tate data without using the zero set.

## 3. Evans determinant: the zero-to-state bridge

Let \(\mathcal E^u(\lambda)\) and \(\mathcal E^s(\lambda)\) be the source-derived
unstable and stable solution spaces of the two sectors. Choose analytic frames
\(Y^u\) and \(Y^s\) and define

\[
D(\lambda)
=
\det\!\left(Y^u(0,\lambda),Y^s(0,\lambda)\right).
\]

Then

\[
D(\lambda)=0
\quad\Longleftrightarrow\quad
\mathcal E^u(\lambda)\cap\mathcal E^s(\lambda)\ne\{0\}.
\]

The required arithmetic theorem is a forward construction satisfying

\[
\Xi\!\left(\frac12+i\lambda\right)=u(\lambda)D(\lambda),
\qquad
u(\lambda)\ne0,
\]

with the multiplicity relation preserved through restricted-product
completion. Defining \(D\) backward from \(\Xi\) would provide no explanation.

## 4. Krein signature: the missing orientation

For a self-adjoint analytic pencil \(L(\lambda)\), a simple real characteristic
value with state \(v\) carries the local form

\[
\kappa(v)=\langle v,L'(\lambda_0)v\rangle.
\]

The Evans determinant locates the mode; it does not determine this signature.
This matches the arithmetic separation already found: the completed scalar
readout is not the source-derived orientation form.

Buzzard's symmetric-square calculation gives the same warning in finite
algebra: orientation reversal preserves rank but reverses determinant sign.
Thus a nondegenerate state realization does not select its positive cone.

## 5. Modular involution: genesis of reciprocity and half-weight

The modular pattern is

\[
S_{\mathrm T}=J_{\mathrm m}\Delta^{1/2},
\qquad
J_{\mathrm m}\Delta J_{\mathrm m}=\Delta^{-1},
\]

The modular flow \(\Delta^{it}\) is unitary.

It supplies a symbolic origin for sector exchange, reciprocal dilation, and
the half-weight. A compatible source pencil would obey a relation of the form

\[
\Theta L(z)\Theta^{-1}=L(-\overline z)^*.
\]

This symmetry still does not orient a scalar overlap. A cyclic and separating
vacuum can prevent operator erasure while allowing

\[
\langle\Omega,U(z)\Omega\rangle=0.
\]

## 6. Reflection positivity and closed-time-path doubling

Reflection positivity offers a candidate construction of the energy form:

\[
(F,G)_{\mathrm{OS}}=\langle\Theta F,G\rangle_{\mathrm E},
\qquad
(F,F)_{\mathrm{OS}}\ge0.
\]

Its missing bridge is the implication from a scalar theta zero to a nonzero
null or eigenstate in the reflected completion.

Closed-time-path variables explain the two-sheet bookkeeping:

\[
\phi_c=\frac{\phi_++\phi_-}{\sqrt2},
\qquad
\phi_q=\frac{\phi_+-\phi_-}{\sqrt2}.
\]

The common component carries visible transport; the difference component
carries response and boundary supply. Endpoint cancellation therefore need
not erase path energy. This is an accounting analogy only: the theta variable
is scale unless a source construction derives a time evolution.

## 7. Prime-local frame renormalization

Grothendieck's phased-packet estimate gives a concrete arithmetic ingredient.
For \(L=\log p\), let

\[
W_p(\theta)
=
\frac1L
\sum_m
\left|
\widehat\Phi\!\left(\frac{\theta+2\pi m}{L}\right)
\right|^2.
\]

The baseband term yields

\[
W_p(\theta)\ge\frac{c_\Phi}{\log p}.
\]

Weighting by the primitive current \(\log p\) gives

\[
(\log p)W_p(\theta)\ge c_\Phi,
\]

uniformly in \(p\). Thus the same source quantity can act as transport
increment, primitive-current weight, and frame renormalizer. This is the
first credible local contribution to the Hamiltonian \(H\). It becomes an
orientation mechanism only if the doubled Green identity inserts the
weighted labelled seam Gram with the required sign.

## 8. The combined colligation

The physical parallels compress to the following data:

\[
\mathfrak C_X
=
(\mathcal H_-,\mathcal H_+,L_X,\Theta,H_X,\mathcal B_X,D_X).
\]

They must satisfy four independent laws:

\[
\Theta L_X(z)\Theta^{-1}=L_X(-\overline z)^*,
\]

\[
D_X(-i(s-\tfrac12))
=
u_X(s)\Xi_X(s),
\qquad u_X(s)\ne0,
\]

\[
2\operatorname{Re}z\,\mathcal E_X(\psi)
=
-\partial_q\mathcal J_X(\psi)+\mathcal B_X(\psi),
\]

\[
\mathcal E_X(\psi)>0.
\]

The last inequality is required for every nonzero admissible zero-state
\(\psi\).

The first law is architecture. The second is the spectral bridge. The third
is conservation. The fourth is orientation. None of these laws implies all
the others.

## 9. Finite falsifier

At a finite cutoff \(X\), construct the actual source matrices

\[
L_X(z),\qquad H_X,qquad \Theta_X,qquad B_X.
\]

For every computed characteristic state \(v\), test

\[
L_X(z)v=0
\]

and the residual

\[
\mathfrak R_X(z,v)
=
2\operatorname{Re}z\,v^*H_Xv
-
\operatorname{Flux}_X(v)
-
v^*B_Xv.
\]

Any one of the following closes the proposed realization:

1. \(\mathfrak R_X(z,v)\ne0\) for source-admissible data;
2. a nonzero zero-state lies in \(\ker H_X\);
3. the source boundary packet has an undeclared residual channel;
4. the determinant has a zero not represented by a state, or conversely;
5. the weighted prime seam term appears with the opposite sign;
6. the required maps fail uniform continuity under completion.

## Verdict

The deepest physical parallel is not one named theory. It is a division of
labour:

- Lax–Phillips and modular theory explain why there are two analytic sectors;
- Evans theory converts a scalar zero into a matched global state;
- canonical systems convert that state into a bulk–boundary identity;
- Krein or reflection-positive structure supplies the orientation needed to
  exclude off-seam states.

The present arithmetic programme has much of the architecture and a plausible
prime-local energy renormalizer. It does not yet have the complete
source-derived colligation or the proof that its boundary packet closes with
positive energy.
