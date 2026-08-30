# A common completed Green lift makes Pauli covariance automatic

## The module law should not be proved twice

On the cyclic endpoint plane,

\[
O_X=J_pX,
\qquad
O_Y=J_pY,
\qquad
O_Y=O_X(XY).
\]

Suppose the complete theta-history carrier contains the cyclic Stieltjes cell
through one source-derived map

\[
I_p:
\mathcal H_p^{\mathrm{cyc}}
\longrightarrow
\mathcal H_p^{\mathrm{comp}}.
\]

Define both completed outputs through that same map:

\[
\widetilde O_X=I_pJ_pX,
\qquad
\widetilde O_Y=I_pJ_pY.
\]

Then

\[
\widetilde O_Y
=
\widetilde O_X(XY)
\]

holds algebraically. No independent phase theorem remains.

Thus Pauli module covariance is automatic if, and only if, the two ports are
transported by one common completed lift rather than by separately normalized
output maps.

## The actual remaining local identity

Let \(g_p^{\mathrm{cyc}}\) be the reduced cyclic Stieltjes Green form and
\(g_p^{\mathrm{comp}}\) the complete enlarged wall/history/tail form. The
required theorem is the restriction identity

\[
g_p^{\mathrm{comp}}(I_pu,I_pv)
=
g_p^{\mathrm{cyc}}(u,v)
\]

for all \(u,v\) in the common rapid core.

Equivalently,

\[
I_p^*G_p^{\mathrm{comp}}I_p
=
G_p^{\mathrm{cyc}}
\]

as closed forms after radical descent.

Once this holds,

\[
\widetilde O_\alpha^*\widetilde O_\beta
=
O_\alpha^*O_\beta,
\qquad
\alpha,\beta\in\{X,Y\},
\]

follows by inserting the fixed endpoint matrices. The entire Pauli linking
Gram is transported automatically.

## Radical compatibility is decisive

An algebraic inclusion before quotient is insufficient. The complete form may
have a larger radical that kills a nonzero cyclic endpoint class.

The exact conditions are

\[
I_p(\ker g_p^{\mathrm{cyc}})
\subseteq
\ker g_p^{\mathrm{comp}}
\]

and

\[
I_p^{-1}(\ker g_p^{\mathrm{comp}})
=
\ker g_p^{\mathrm{cyc}}.
\]

The first permits descent. The second proves that completion creates no new
dark cyclic state.

After quotienting, the induced map must be an isometry onto its range. It need
not be onto the enlarged carrier.

## Block criterion

Write the complete reduced form relative to cyclic and auxiliary sectors as

\[
G_p^{\mathrm{comp}}
=
\begin{pmatrix}
A_p&C_p\\
C_p^*&D_p
\end{pmatrix}.
\]

If \(I_pu=(u,0)\), the literal restriction is \(A_p\). Therefore the
cyclic identity requires

\[
A_p=G_p^{\mathrm{cyc}}.
\]

If instead the source lift has an auxiliary graph component

\[
I_pu=(u,R_pu),
\]

then the pullback is

\[
A_p+C_pR_p+R_p^*C_p^*+R_p^*D_pR_p.
\]

This full expression, not the upper-left block alone, must equal the cyclic
form. A fitted choice of \(R_p\) is not source authority.

## Uniformity

The raw cyclic Gram may retain a soft disagreement eigenvalue. Uniform
invertibility of \(I_p) relative to that raw metric is neither needed nor
possible.

Completion requires instead:

- the restriction identity primewise;
- one common closed lift for both Pauli ports;
- a uniform upper bound for \(I_p\) on the cyclic graph norm;
- preservation of the Pauli analysis lower bound after dilation;
- Euler-weighted control of auxiliary returns;
- prime-diagonal twisted Mellin covariance.

The uniform lower bound belongs to the doubled analysis map, not to the raw
cyclic Gram.

## Minimal hostiles

1. Construct separate lifts \(I_{p,X}\) and \(I_{p,Y}\) with a hidden
   relative phase.
2. Preserve the upper-left block while a graph component changes the
   pullback form.
3. Obtain descent but let the enlarged radical kill the cyclic disagreement.
4. Match scalar boundary energies without matching the polarized pullback.
5. Use a source-free graph correction \(R_p\) to force equality.
6. Prove the identity primewise with graph norms diverging after Euler
   assembly.

## Verdict

The Pauli module intertwiner is not an additional analytic gate once the
source supplies one common completed Green lift. The true earliest missing
constructor is the extension theorem from the reduced cyclic Stieltjes cell
into the complete enlarged Adams Green carrier.

That theorem must prove exact polarized pullback and radical reflection.
Afterward, every Pauli linking block and the uniform doubled-frame estimate
follow functorially.
