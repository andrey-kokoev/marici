# Boundary Pairing and Surface Lift Handoff

## Record

Date: 2026-08-12

Status: corrected genus-zero boundary square; surface comparison and contact primitive remain
open.

## Division of labor

Entry 11 identifies the generic twisted-cohomology class \(\mathsf J\). Boundary naturality is a
separate problem with two interfaces:

- **YM** owns the Laurent/nearby-cycle behavior of the scalar/BAS pairing and physical internal
  state coevaluation.
- **Frost** owns the lift from scalar Rees grades to surface functions, including the cut kernel
  and contact primitives.

Neither interface should be hidden inside the notation \(I^{-1}\).

## Exact genus-zero square

For a separating divisor or cut \(C\), use dual half-spaces and retain the plumbing normal line.
The intended square is

\[
\begin{array}{ccc}
H_\Sigma^+ & \xrightarrow{\ I_\Sigma^\flat\ } & (H_\Sigma^-)^\vee\\
\downarrow\rho_C^+ && \downarrow B_C\\
H_L^+\otimes H_R^+ &
\xrightarrow{\ I_L^\flat\otimes I_R^\flat\ } &
(H_L^-\otimes H_R^-)^\vee,
\end{array}
\]

where the transpose boundary map is defined by

\[
(B_Ca)(u_L\otimes u_R)
=
\operatorname*{Res}_{C}
a\!\left(\gamma_C^-(u_L\otimes u_R)\right).
\]

Here \(\gamma_C^-\) glues test half-objects and \(\rho_C^+\) takes the residue of the raised
half-object. Pairing compatibility is

\[
B_CI_\Sigma^\flat
=
(I_L^\flat\otimes I_R^\flat)\rho_C^+.
\]

Whenever the relevant maps are invertible on the induced channel quotient, this becomes

\[
\rho_C^+(I_\Sigma^\flat)^{-1}
=
\bigl((I_L^\flat)^{-1}\otimes(I_R^\flat)^{-1}\bigr)B_C.
\]

Orientations, Koszul signs, the plumbing weight, and the normal line remain explicit. A scalar
formula appears only after trivializing those lines.

## Resonance qualification

The generic \((n-3)!\)-dimensional pairing cannot simply be specialized and inverted at
\(s_C=0\). The twist is resonant there and the residue matrix has lower rank in the full
\(n\)-point space.

In a channel-adapted basis,

\[
m_n
\sim
\begin{pmatrix}
s_C^{-1}\epsilon_C(m_L\otimes m_R)+O(1)& *\\
*&*
\end{pmatrix},
\]

and hence

\[
m_n^{-1}
\sim
\begin{pmatrix}
s_C\epsilon_C^{-1}(m_L^{-1}\otimes m_R^{-1})+O(s_C^2)&O(s_C)\\
O(s_C)&*
\end{pmatrix}.
\]

The \(s_C\) factor cancels the amplitude covector's pole. Index raising is monoidal on this
associated channel block, not by inversion of \(\operatorname{Res}_C m_n\).

## Three-column scalar-to-surface target

The full target is

\[
\operatorname{gr}_{Z}\mathcal A_\Sigma^{\rm scalar}
\xrightarrow{\ \chi_\Sigma\ }
(H_\Sigma^-)^\vee
\xrightarrow{\ (I_\Sigma^\flat)^{-1}\ }
H_\Sigma^+,
\]

with vertical maps

\[
\Delta_C^{\rm Rees},
\qquad
B_C,
\qquad
\rho_C^+.
\]

The second square is cyclicity or boundary compatibility of the perfect pairing. The first square
is the missing scalar comparison theorem:

\[
B_C\chi_\Sigma
\stackrel{?}{=}
(\chi_L\otimes\chi_R)\Delta_C^{\rm Rees}.
\]

For a normal grade \(r\), the Rees cut uses graded convolution rather than a same-grade tensor
product:

\[
\Delta_C\operatorname{gr}^{r}
=
\sum_{a+b+c=r-w_C}
\operatorname{gr}^{a}\otimes
\operatorname{gr}^{c}\eta_C\otimes
\operatorname{gr}^{b}.
\]

Derived normal data may be required when scalar degenerations are not transverse.

## Cut-kernel obstruction

Even if every cut in the three-column diagram commutes, cuts do not determine a unique surface
function. The solution set

\[
\left\{
\widehat{\mathsf J}_\Sigma:
\mathbf\Delta_\Sigma\widehat{\mathsf J}_\Sigma
=
\text{prescribed cuts}
\right\}
\]

is a torsor for

\[
\mathcal K_\Sigma
=
\bigcap_C\ker\Delta_C.
\]

Thus a mapping-class- and sewing-compatible primitive

\[
\omega_\Sigma\in\mathcal K_\Sigma
\]

or a natural splitting of the total-cut sequence is additional required data. The known
punctured-disk constant term already rejects the zero-primitive choice.

This is not a defect of the on-shell class \([({\rm Pf}'A)^2]\). It is the expected loss of local
contact information under cuts.

## Internal state sewing

The BAS/KLT kernel contracts ordering indices. Channel state coevaluation is separate data of the
half-object:

- \(\mathsf J\): scalar coevaluation;
- \(\mathsf G\): physical coevaluation on \(q_I^\perp/\langle q_I\rangle\);
- biadjoint colour: internal Killing metrics.

These are not new primitive half-integrands, but omitting them makes the gluing formula ill typed.

## Concrete ownership tests

### YM: six-point \(s_{123}\) channel

1. Form the \(6\times6\) BAS matrix in complementary KLT bases.
2. Construct channel residue maps \(R_{123}^\pm\).
3. Verify

   \[
   \operatorname*{Res}_{s_{123}=0}m_6
   =
   (R_{123}^-)^{\mathsf T}
   (m_4\otimes m_4)
   R_{123}^+
   \]

   with the selected orientation convention.
4. Verify the leading
   \(s_{123}(m_4^{-1}\otimes m_4^{-1})\) inverse block.
5. Apply it to the NLSM grade covector and recover \(\mathsf J_4\otimes\mathsf J_4\).
6. In the \(\mathsf G\)-\(\mathsf J\) pairing, show that the only additional contraction is the
   physical transverse-polarization coevaluation.

### Frost: six-point disk comparison

1. Compute \(R_6=\operatorname{in}_Z G^{\rm scalar}_{D_6}\).
2. Verify the first comparison square on each allowed \(3|3\) channel and zero residue on
   forbidden channels.
3. Raise the compatible channel covector and check
   \(\rho_C\mathsf J_6=\mathsf J_4\otimes\mathsf J_4\).
4. Subtract the Cut-Equation completion from \(R_6\); the remainder must define a cyclic,
   ordering-compatible primitive \(\omega_{0,6}\).

Plumbing dependence, failure of iterated-cut coassociativity, a singular induced channel pairing,
or a non-covariant primitive falsifies intrinsic surface naturality.

## Decision

Treat genus-zero CHY factorization of \((\operatorname{Pf}'A)^2\) as established. Treat pairing
monoidality as established only on the correctly oriented nearby-cycle channel quotient. Keep the
scalar comparison \(\chi_\Sigma\) and the cut-kernel primitive \(\omega_\Sigma\) as separate open
Frost problems.
