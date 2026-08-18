# Explicit Incidence Formula for the Corrected D03 Dualizing Complex

## Result

Let

\[
f=\widetilde b:\widetilde G_{03}\longrightarrow X,
\qquad z=(\sigma,H),
\qquad f(z)=(b(\sigma_0),H)
\]

be the corrected 1,169-to-215 point ringed map of Entry 365. Write
(A_x=\mathcal O_{X,x}), and let (C_z(Q)) denote the costandard
(\mathcal O_{\widetilde G})-module right adjoint to the stalk functor at
(z), with coefficient (Q) over (A_{f(z)}).

For every strict source chain

\[
c=(z_0<\cdots<z_p),
\]

put (a_c=f(z_0)), (d_c=f(z_p)). The target restriction
(A_{a_c}\to A_{d_c}) is the explicit localization obtained by adjoining
the normal units in

\[
(S_{d_c}\setminus H_{d_c})
\setminus(S_{a_c}\setminus H_{a_c}).
\]

Unwinding the representing functor in Theorem 4.1 gives the actual
incidence formula

\[
\boxed{
\omega_f\simeq
\operatorname{Tot}_{-p+r}
\left(
\prod_{z_0<\cdots<z_p}
C_{z_p}\!left(
\operatorname{Hom}_{A_{a_c}}(A_{d_c},I_{a_c}^{,r})
\right)
\right),
}
\]

where (mathcal O_X\to I^\bullet) is a K-injective resolution. Equivalently,
the coefficient attached to (c) in the derived category is

\[
R\operatorname{Hom}_{A_{a_c}}(A_{d_c},A_{a_c}).
\]

This is no longer an abstract unnamed representing object: its indexing
chains, endpoint rings, localization sets, costandard supports, and
differential are all fixed by the corrected finite incidence map. The
horizontal differential is the alternating standard-chain differential;
the endpoint face uses the target restriction. The vertical differential
is that of (I^\bullet).

## Perfectness gate

Zero-jump chains have coefficient (A_{a_c}). A nonzero-jump chain has a
derived localization-dual. Already for one regular nonunit (u),

\[
R\operatorname{Hom}_{A}(A[u^{-1}],A)
\]

is represented by the dual of the countable telescope resolution of
(A[u^{-1}]); its degree-one term is an adic-completion quotient and is
not a finitely generated (A)-module. Therefore the individual standard
terms are not finite projectives. Perfectness can hold only if the full
incidence differential cancels every nonzero-jump localization-dual
sector and compresses the remaining costandards.

The checker enumerates the complete finite chain census by standard degree
and number of newly inverted normal parameters. This census is the input
for the next exact step: assemble the localization-dual differential and
test whether any completion quotient survives.

## Occurrence factor and Entry 176

For

\[
\widetilde q=f\circ\operatorname{pr}_{\widetilde G},
\]

the already proved interval calculation gives

\[
\omega_{\widetilde q}
\simeq\operatorname{pr}_{\widetilde G}^{!}\omega_f.
\]

No comparison with Entry 176 is performed yet: the bounded
finite-projective compression remains undecided until the nonzero-jump
sectors are resolved.

## Evidence boundary

The incidence formula follows directly by decomposing
(f_*\mathcal C^p) chain-by-chain and applying the right adjoint of the
stalk functor. The existence and totalization are Theorem 4.1 of Sancho de
Salas--Torres Sancho. The checker fixes the complete combinatorial census;
it does not by itself prove cancellation or noncancellation of the derived
localization-duals.
