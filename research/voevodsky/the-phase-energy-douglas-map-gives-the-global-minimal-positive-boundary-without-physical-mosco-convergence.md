# The phase-energy Douglas map gives the global minimal positive boundary without physical Mosco convergence

## Prior clues

The prior research contains three ingredients that fit together directly.

First, the recentered Tate/reference difference row has exact positive Gram density

\[
\kappa_{loc,S}.
\]

Second, the signed Tate multiplier satisfies

\[
|w_S|
\le
C_Se_S,
\qquad
 e_S=1+\kappa_{loc,S}.
\]

Third, finite-character Mellin--Schwartz observers are dense in

\[
\mathscr E_S=L^2(e_Sdt).
\]

These data already supply a global source-derived positive minimalization map.

## Resolved phase-energy feature

On the observer core, define the graph feature

\[
\Gamma_Sm
=
\left(
m,
D_S^{loc}M_m
\right).
\]

After incorporating the fixed normalization of the Hilbert--Schmidt row, its Gram is equivalent to

\[
\|\Gamma_Sm\|^2
=
\int e_S|m|^2.
\]

Complete its generated source-labelled range. The result is canonically the phase-energy Hilbert space \(\mathscr E_S\), up to the declared normalization equivalence.

This feature retains placewise positive energy and does not rely on the signed Weil form for its norm.

## Bounded signed operator

Define

\[
a_S=rac{w_S}{e_S}.
\]

Multiplication by \(a_S\) is a bounded self-adjoint operator on \(\mathscr E_S\):

\[
\mathcal A_S=M_{a_S}.
\]

The signed Tate form is represented exactly by

\[
q_{Tate,S}(m,n)
=
\langle m,
\mathcal A_Sn
\rangle_{\mathscr E_S}.
\]

## Global Jordan feature

Functional calculus gives

\[
a_{S,+}=
\max(a_S,0),
\qquad
 a_{S,-}=
\max(-a_S,0).
\]

Define

\[
\Phi_S^{min}m
=
\left(
M_{\sqrt{a_{S,+}}}m,
M_{\sqrt{a_{S,-}}}m
\right).
\]

This is a bounded map

\[
\Phi_S^{min}:
\mathscr E_S
\longrightarrow
\mathscr E_S\oplus\mathscr E_S.
\]

Its signed readout is

\[
(\Phi_S^{min})^*J\Phi_S^{min}
=
\mathcal A_S.
\]

Its ordinary Gram is

\[
(\Phi_S^{min})^*
\Phi_S^{min}
=
|\mathcal A_S|.
\]

Thus it is the global minimal two-polarity positive boundary.

## Douglas factorization

The domination

\[
|w_S|
\le
C_Se_S
\]

is equivalent to

\[
|\mathcal A_S|
\preceq
C_SI_{\mathscr E_S}.
\]

Therefore Douglas factorization gives a bounded source-labelled map from the phase-energy graph feature to the minimal Jordan feature.

In the multiplication model, this map is explicit. It is the pair of multipliers

\[
M_{\sqrt{a_{S,+}}},
\qquad
M_{\sqrt{a_{S,-}}}.
\]

No packetwise Jordan decomposition is used. The construction occurs once on the global phase-energy carrier.

## Balanced energy

The graph feature generally has more positive norm than the minimal Jordan feature. Its excess is

\[
I-|\mathcal A_S|/C
\]

for any normalization constant \(C\) dominating \(|\mathcal A_S|\).

This excess need not decay with a physical cutoff. It lies in the kernel of the non-isometric minimalization semantics rather than in a common positive subfeature that must be subtracted inside the original physical carrier.

This explains why the noncommuting common-face obstruction does not prevent existence of the minimal boundary. It prevents realizing minimalization as orthogonal subtraction of one physical positive Gram. It does not prevent a bounded quotient/compression map into the phase-energy boundary.

## Relation to the lattice cell

The internal polarized lattice cell supplies the exact signed relative feature and its strict incidence coherence. The phase-energy graph completion is formed from its cutoff-independent difference rows.

The bounded Douglas map sends this completed relative cell to its minimal positive boundary. Since all ingredients are source-labelled multiplication or placewise direct-sum operators, conductor restriction and placewise feature inclusion commute with the construction.

Thus the minimal boundary is compatible with the analytic lattice without requiring raw physical positive legs to converge.

## What happens to the Mosco gate

If the objective is existence of a source-derived closed positive boundary and a comparison map from the relative feature, the gate is already closed by the phase-energy construction.

One does not need forms \(r_\alpha\) satisfying a physical Mosco limit. The completion is defined directly from the stationary relative graph norm and the bounded multiplier \(\mathcal A_S\).

A Mosco theorem remains meaningful only as the stronger assertion that a specifically chosen family of physical absolute residual Grams converges to the same minimal boundary. That assertion is not required to construct or type the completed lattice boundary.

## Endpoint channel

Finite-rank endpoint and index rows are adjoined orthogonally to the regular phase-energy carrier. Their signed coupling is already represented by the closed bounded augmented Green operator.

Their positive Schur--Douglas condition remains independent. The regular phase-energy minimalization does not prove endpoint positivity.

## Exact completion diagram

The regular channel now has the sequence

\[
\text{regulated relative cell}
\longrightarrow
\text{stationary difference-row graph feature}
\longrightarrow
\mathscr E_S
\longrightarrow
\Phi_S^{min}.
\]

The first map forgets divergent common volume while retaining the relative feature. The second is graph completion. The third is bounded global Jordan functional calculus.

Every map is source derived.

## Status split

The following result is closed:

\[
\text{global minimal positive regular boundary on }
\mathscr E_S.
\]

The following stronger result remains open:

\[
\text{physical absolute residual Grams converge to that boundary.}
\]

These should not be listed as the same gate.

## Disposition

Prior phase-energy research already contains the correct global minimalization mechanism. The key map is not positive common-face subtraction inside the physical prolate carrier. It is the bounded Douglas compression from the cutoff-independent local difference-energy completion to the Jordan feature of

\[
\mathcal A_S=M_{w_S/e_S}.
\]

Therefore the regular completed positive boundary exists globally and coherently. Physical Mosco convergence is an optional realization theorem rather than a prerequisite for completion of the analytic lattice.
