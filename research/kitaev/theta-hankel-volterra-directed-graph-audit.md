# Theta Hankel--Volterra graph does not yet enter the anomaly-line system

Owner: `marici.Kitaev`

## Bounded question

Do Grothendieck's finite boundary lines and Tate bonding maps already define a
directed system of closed theta tail--seam graphs?

## Source-supplied objects

For every prime cutoff (X\), the primitive anomaly packet supplies a Hilbert
line (L_X\simeq\mathbb C\) and invertible bonding map

\[
 U_{X,Y}(s)=\prod_{X<p\le Y}\gamma_p(s).
\]

On \(\Re s=1/2\), these maps are unitary and their direct-limit line exists.
Independently, the tail--seam packet supplies the densely defined relation

\[
 \Gamma_X(G_Xc)=H_Xc,
\]

with

\[
 \operatorname{Dom}\Gamma_X^*
 =\{y:H_X^*y\in\operatorname{Ran}G_X\}.
\]

The sources do not yet supply maps from the tail and seam Hilbert spaces to
(L_X\), or coefficient bonding maps intertwining (G_X,H_X\). Consequently
these are presently two typed systems, not one directed graph system.

## Exact directed-graph criterion

Let (V_{X,Y}:C_X\to C_Y\) bond coefficient packets and let
(U^G_{X,Y},U^H_{X,Y}\) bond the tail and seam targets. The graph relations
are compatible precisely when

\[
 U^G_{X,Y}G_X=G_YV_{X,Y},\qquad
 U^H_{X,Y}H_X=H_YV_{X,Y}.
\]

Equivalently,

\[
 (U^G_{X,Y}\oplus U^H_{X,Y})\operatorname{Graph}\Gamma_X
 \subseteq\operatorname{Graph}\Gamma_Y.
\]

For everywhere-defined scalar operators (\Gamma_X=a_X\) on the anomaly
lines, with the same nonzero scalar bonding on domain and codomain, this
reduces to (a_X=a_Y\). Thus finite-cutoff closability is automatic in the
line, but it says nothing about directed compatibility.

Compatibility of closures requires the stronger equality

\[
 (U^G_{X,Y}\oplus U^H_{X,Y})
 \overline{\operatorname{Graph}\Gamma_X}
 =\overline{\operatorname{Graph}\Gamma_Y}
\]

onto the transported closed subspace. It cannot be inferred from equality of
scalar Tate pairings.

## Seam and off-seam behavior

On the critical seam, unitarity preserves graph norms once the intertwining
laws hold. It does not make a distinguished pairing nonzero: the zero
functional is invariant under every unitary transition.

Off the seam the raw line transport is already nonuniform. At (t=0\), put
(x=p^{-1/4}\). For (s=3/4\),

\[
 \gamma_p(3/4)=\frac{1-x^3}{1-x}=1+x+x^2>1.
\]

The finite products therefore grow without a cutoff-independent operator
bound. At (s=1/4\), the factor is its reciprocal and products collapse.
This is a theta-specific escape sequence in the raw seam metric. It does not
decide the completed two-metric correspondence.

## Hostile fixtures

1. **Finite closability, directed failure.** Take (L_N=\mathbb C\), identity
   bonding, and (\Gamma_N=N\). Every graph is closed, but no two successive
   graphs intertwine.
2. **Unitary transport, vanishing pairing.** Identity transport preserves a
   unit vector and also preserves the zero functional; unitarity supplies no
   nonvanishing theorem.
3. **Scalar-equivalent traces, different seams.** The traces
   (J_\pm(x,y)=(x,\pm y)\) have the same scalar projection but opposite seam
   character.
4. **Primitive omission.** Replacing (U_{X,Y}\) by identity forgets the
   nontrivial (C_1\) transition cocycle. It is not a change of scalar frame
   authorized by the source.
5. **Density lost at completion.** On finite sequences in \(\ell^2\), the
   maps (Te_n=e_1\) are bounded at every cutoff. In the limit,
   (x_N=N^{-1}\sum_{n\le N}e_n\to0\) while (Tx_N=e_1\), and
   \(\operatorname{Dom}T^*=e_1^\perp\) is not dense.
6. **Cutoff-fitted graph norm.** Rescaling the seam norm separately at each
   cutoff can make every (\Gamma_N\) contractive, but the rescalings fail the
   isometric bonding law and therefore define no common completion.

## Disposition

The finite anomaly lines are closable and form a unitary direct system on the
seam. The theta Hankel--Volterra graph is separately typed and has an exact
adjoint-domain criterion. The requested combined operator is blocked by the
missing incidence and intertwining maps

\[
 C_X\xrightarrow{(G_X,H_X)}T_X\oplus S_X
 \longrightarrow L_X.
\]

Therefore no source-authorized theta vector can yet witness density or
nondensity in the line-valued completed graph. The smallest currently
available theta-specific sequence is instead the off-seam anomaly-line escape
above. A decisive next packet must provide (V_{X,Y}\), the tail/seam-to-line
incidence, and verify both intertwining equations. Only then is density of the
completed adjoint domain a well-typed question.

## Claim strength

This is a source-typing obstruction plus exact finite and directed-system
falsifiers. It is not a theorem that the ultimate rigged theta correspondence
is nonclosable.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_hankel_volterra_directed_graph.py`.
The result is written to
`research/kitaev/results/theta-hankel-volterra-directed-graph.json`.
