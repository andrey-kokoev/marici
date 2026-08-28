# The RH Object Is the Additive-Multiplicative Comparison Cone

## Why neither presentation can carry the divisor alone

The additive theta presentation supplies heat flow, Fourier sewing, moving
seams, and the completed scalar cross-transfer.  Positive Epstein theta
sources show that this architecture can have off-seam zeros.

The multiplicative valuation presentation supplies prime shifts, Euler
cumulants, reciprocal chains, and local interval operators.  Every finite
Euler product is nonzero away from its declared local poles.  Its individual
factors therefore do not contain the nontrivial zeta divisor.

The completed divisor first appears when the two presentations are compared.
It should therefore be assigned to their relative object rather than to
either carrier separately.

## Finite comparison complex

At cutoff $X$, let

\[
(C_{\theta,X},d_{\theta,X})
\]

be the complete additive boundary complex and let

\[
(C_{E,X},d_{E,X})
\]

be the complete bordered valuation complex.  Both must retain their input,
state, response, endpoint, and cutoff-terminal ports.

A source-derived chart comparison is a chain map

\[
F_X:C_{\theta,X}\longrightarrow C_{E,X}
\]

satisfying

\[
d_{E,X}F_X=F_Xd_{\theta,X}.
\]

Its mapping cone has differential

\[
d_{\operatorname{Cone},X}=
\begin{pmatrix}
d_{E,X}&F_X\\
0&-d_{\theta,X}
\end{pmatrix}.
\]

The chain-map identity is exactly the condition

\[
d_{\operatorname{Cone},X}^2=0.
\]

Thus the first finite falsifier is not a scalar mismatch.  It is the typed
chain-map residual

\[
R_X=d_{E,X}F_X-F_Xd_{\theta,X}.
\]

## Meaning of a zero

If the completed comparison cone is acyclic, the additive and multiplicative
presentations remain equivalent after completion.  Nonzero cone cohomology
is a state retained by one presentation but not paired by the other.

The desired forward bridge is

\[
\Xi(s)=u(s)\tau\bigl(\operatorname{Cone}F(s)\bigr),
\qquad
u(s)\ne0,
\]

where the torsion or determinant section is derived from the complete
boundary-bearing complexes.  Under that bridge, a zero is a failure of the
comparison to remain a quasi-isomorphism.

This is stronger than representing the theta scalar as a bordered
determinant.  Universal Schur bordering exteriorizes any transfer function;
the comparison cone additionally remembers which source distinctions the
additive and multiplicative charts preserve.

## Location of the previously found residuals

The known structures acquire precise cone roles:

- the scale-valuation Beck-Chevalley cell is a chain homotopy witnessing lax
  commutation of the two chart operations;
- the moving-seam ternary window is a homotopy for the relative response
  port;
- the common-path endpoint residual is the remaining cone boundary class;
- primitive and square currents are low-regularity determinant grades in the
  multiplicative chart, not extra theta states;
- the archimedean channel is required for the comparison map to reach the
  completed boundary object;
- hostile symmetric multipliers alter the comparison cone even when they
  preserve the scalar functional equation.

## Dirac form of the cone

After Hilbert or rigged completion, form the self-adjoint cone operator

\[
\mathscr D_X=d_{\operatorname{Cone},X}
+d_{\operatorname{Cone},X}^*.
\]

Its kernel represents cone cohomology when the required closed-range theorem
holds.  The centered normal parameter may then act as a mass only on this
relative carrier.  This avoids assigning the zeta divisor to the invertible
causal bulk or to a local valuation factor.

The RH-strength target becomes a controlled contraction

\[
d_sh_s+h_sd_s=I
\]

for the completed comparison cone in each open half-plane.  Such a
contraction must be source-derived and equicontinuous on compact off-seam
sets.  A formal contraction built from division by the determinant section
is inadmissible.

## Completion gate

Finite acyclicity is insufficient.  If $h_{X,s}$ are cutoff contractions,
the required condition is

\[
\sup_X\sup_{s\in K}\lVert h_{X,s}\rVert<\infty
\]

for every compact $K$ in either open half-plane.  Divergence of these norms
is the exact witness that a comparison partner escapes at infinity and the
completed cone acquires cohomology.

## DPC

The route is admitted only if all of the following are constructed in source
order:

1. the two complete cutoff complexes;
2. the chart comparison $F_X$;
3. exact vanishing of $R_X$;
4. a cutoff-compatible determinant-line isomorphism identifying cone torsion
   with the completed theta section up to a proved nonzero unit;
5. controlled off-seam contractions;
6. a completion theorem retaining primitive, square, seam, and archimedean
   boundary grades.

Failure of any one item closes the comparison-cone proof.  Passing all six
would turn an off-seam zero into impossible completed comparison cohomology.

## Current boundary

The existing scale-valuation and moving-seam cells provide pieces of the
chain homotopy, but no complete comparison map $F_X$ has yet been written.
The immediate construction problem is therefore finite and typed: assemble
the smallest cutoff complexes containing the bordered prime valuation chain,
the two-sector tail colligation, and their common endpoint and response
ports; then compute $R_X$ before taking any scalar determinant.

## Exact finite bulk comparison

The coefficient-level part of $F_X$ is already canonical.  Let

\[
\mathcal C_X=\operatorname{span}\{e_n:1\le n\le X\}
\]

and let $\mathcal V_X$ have the labelled basis vectors

\[
e_{\nu(n)}=\bigotimes_{p\le X}e_{v_p(n)}
\]

for the same integers.  Unique factorization defines

\[
F_X^{\mathrm{UF}}e_n=e_{\nu(n)}.
\]

With the labelled bases orthonormal, this is unitary.  On the partial domain
where $pn\le X$, integer multiplication $T_{p,X}$ and valuation shift
$S_{p,X}$ satisfy

\[
F_X^{\mathrm{UF}}T_{p,X}=S_{p,X}F_X^{\mathrm{UF}}.
\]

The additive and valuation syntheses also agree exactly:

\[
W_{\theta,X}e_n=U_{\log n}\Phi,
\]

and

\[
W_{E,X}e_{\nu(n)}
=U_{\sum_pv_p(n)\log p}\Phi
=U_{\log n}\Phi.
\]

Therefore

\[
W_{E,X}F_X^{\mathrm{UF}}=W_{\theta,X}.
\]

The finite bulk comparison residual vanishes.  Its two-term mapping cone is
contractible using $(F_X^{\mathrm{UF}})^{-1}$, with no cutoff-dependent norm
growth on the coefficient modules.

## Where a nontrivial cone can first appear

The finite isomorphism does not extend automatically through the analytic
theta Gram completion.  Adjacent logarithmic labels become arbitrarily close
under theta synthesis, while valuation predicates continue to distinguish
them.  Hence the inverse comparison can lose continuity even though every
finite cone is contractible.

The constructor-generated pro-Gram topology repairs the bulk comparison by
retaining all admitted valuation operations.  But once that topology is used,
the bulk cone again becomes contractible by construction.  Any nontrivial
relative class must therefore occur in one of the structures not contained
in the coefficient relabelling:

- input and response ports;
- moving-seam incidence;
- primitive and square determinant boundaries;
- cutoff-terminal defects;
- the archimedean completion port;
- the determinant-line readout.

This narrows the finite construction.  The comparison map should not be
searched for in the arithmetic bulk again.  It must be extended from
$F_X^{\mathrm{UF}}$ to the complete bordered complexes, and the first
failure of extension is the actual candidate comparison class.
