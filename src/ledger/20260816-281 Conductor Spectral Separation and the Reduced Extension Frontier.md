---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Conductor Spectral Separation and the Reduced Extension Frontier

## Result

Entries 279--280 reduce the marked \(q_{\mathcal G_{12}}\)-residue
system to

\[
0\to H^2(S_E)\to H^2(S_E\setminus W)
\to H^1(W)(-1)\to0
\]

and identify the two mixed quotient lines as Kummer characters on

\[
\Delta_{W_1}=-4xD_1,
\qquad
\Delta_{W_2}=-4yD_2.
\]

At a generic point of either conductor discriminant, away from every
ambient surface discriminant and all other frozen supports, the mixed line
cannot carry a nontrivial rational extension by the absolute rank-nine
system:

\[
\boxed{
\operatorname{Ext}_{\rm loc,dR}^1
(\mathcal K_{\Delta_{W_i}},H^2(S_E))=0.
}
\]

The reason is spectral separation. The absolute system has local monodromy
\(+1\), while the conductor line has monodromy \(-1\). The forced
projector uses the same half-sum mechanism exposed integrally in entry 280.

Thus generic conductor support is completely classified as
Tate/Kummer coefficient support. The unresolved ambient extension is
confined to loci where quotient and absolute eigenvalues can collide.

## Frozen generic locus

Fix a smooth point of \(\Delta_{W_i}=0\) satisfying:

- the del Pezzo surface \(\overline S_E\) and its affine complement
  \(S_E\) remain smooth;
- the elliptic boundary remains smooth;
- the other conductor discriminant is nonzero;
- soft, signed-energy, \(\Lambda\), and \(\mathcal Q\) factors are
  nonzero.

The equation \(\Delta_{W_i}=0\) expresses tangency of the already frozen
wall with the Cayley--Menger branch divisor. It does not make the ambient
surface singular at such a generic point. Therefore the absolute
Gauss--Manin system extends across this divisor and has monodromy

\[
T_{\rm abs}=I_9.
\]

Entry 280 gives the mixed conductor monodromy

\[
T_{\rm mix}=-1.
\]

## Exact block calculation

Any local monodromy of an extension of the mixed line by the absolute
system has, after choosing an arbitrary vector-space lift, the form

\[
T=
\begin{pmatrix}
I_9&c\\
0&-1
\end{pmatrix}
\]

for some column \(c\). Write a vector as \((a,q)\), so

\[
T(a,q)=(a+cq,-q).
\]

Define

\[
a'=a+\frac12cq.
\]

Then

\[
T(a',q)=(a',-q),
\]

and hence

\[
\boxed{
T\sim_{\mathbb Q}
\begin{pmatrix}
I_9&0\\
0&-1
\end{pmatrix}.
}
\]

This is not an optional fitted gauge. It is the unique spectral projector
because \(1-(-1)=2\) is invertible in the de Rham field.

Over an integral lattice the shift exists precisely when \(c\) is even.
Thus an integral class \(c\bmod2\) may remain, but it is occurrence
\(2\)-torsion and not a de Rham off-diagonal singularity.

## Consequence for the rank-twelve connection

In the rational quotient frame of entry 280,

\[
H^1(W)_{\mathbb Q}
\simeq
\mathcal K_{\Delta_{W_1}}
\oplus
\mathcal K_{\Delta_{W_2}}
\oplus
\mathbb Q_{\rm top},
\]

the first two columns of the ambient extension class are locally zero in
their gauge classes at generic \(\Delta_{W_i}=0\).

Therefore any nonzero rational class

\[
[\Theta]\in
H^1_{\rm dR}\!
\left(
\operatorname{Hom}(H^1(W)(-1),H^2(S_E))
\right)
\]

must be detected at an eigenvalue-collision locus:

1. \(\Lambda=0\), where the two same-sheet points defining the
   trivial-character top quotient collide;
2. an intersection with the elliptic/ambient discriminant;
3. soft or signed-energy support;
4. simultaneous conductor support;
5. \(\mathcal Q=0\), if the physical moving-chain extension—not the
   absolute surface—carries that singularity.

The list is derived from frozen geometry. It is not a fitted pole ansatz.

## Relation to the exceptional-wall calculations

Entries 235--239 found a nonzero weight-minus-one local coefficient on an
exceptional wall, then proved it exact on the punctured wall and zero in
the tangential endpoint cone. That representative therefore cannot define
one of the rank-three conductor extension columns.

This prevents an invalid shortcut: the ambient extension cannot be read
off from the ancestry of that exact coefficient.

## Deutsch--Popperian verdict

The hard-to-vary conjecture was

\[
\boxed{
\text{a generic conductor discriminant can support a new rational
off-diagonal extension between the mixed line and }H^2(S_E).
}
\]

It is falsified by the \((+1,-1)\) spectral decomposition.

The surviving frontier is

\[
\boxed{
\text{only eigenvalue-collision loci can carry the unresolved rational
ambient extension.}
}
\]

## Classification

\[
\boxed{
\begin{array}{c|c}
\text{structure}&\text{home}\\
\hline
\Delta_{W_i}=0\text{ generically}
&\text{Kummer coefficient support}\\
\text{mixed rational ambient extension}
&0\text{ locally by spectral separation}\\
\text{mixed integral residual}
&\text{possible occurrence class }c_i\bmod2\\
\Lambda=0
&\text{top-quotient eigenvalue-collision frontier}\\
\text{new carrier datum}
&\text{none}
\end{array}
}
\]

## Limits

This result is local at generic points of one conductor discriminant. It
does not:

- compute the integral vectors \(c_i\bmod2\) coupling to the absolute
  lattice;
- compute the top-column extension at \(\Lambda=0\);
- treat intersections of support divisors;
- construct the physical relative chain;
- decide whether \(\mathcal Q\) belongs to the moving-chain extension.

## Exact evidence

- entries 265 and 280 for the conductor discriminants and characters;
- entry 279 for the ambient rank-twelve extension;
- entries 238--239 for exactness of the exceptional-wall candidate;
- research/benincasa/conductor-spectral-separation.json.

## Next hostile falsifier

Restrict to a generic transverse slice through

\[
\Lambda=E(-x+y+z)(x-y+z)=0
\]

with all conductor, elliptic, soft, and \(\mathcal Q\) factors nonzero
except the selected factor of \(\Lambda\). Compute the local monodromy
on the invariant top lift

\[
g_{111}^{\rm inv}
=\widetilde g_{111}-\frac12(g_{101}+g_{110})
\]

and its extension into \(H^2(S_E)\).

The finite falsifier is a nonzero unipotent class not generated by the
frozen collision of \(P_+\) and \(P_-\). Only a class requiring an
additional incidence datum can challenge the shared-carrier hypothesis.

## Outcome contract

~~~json
{
  "claim": "A generic conductor discriminant can support a new rational off-diagonal extension between a mixed Kummer line and H2(S_E).",
  "status": "falsified_by_spectral_separation",
  "absolute_local_monodromy": 1,
  "mixed_local_monodromy": -1,
  "forced_rational_shift": "c/2",
  "generic_rational_extension_class": 0,
  "possible_integral_residual": "c mod 2",
  "remaining_frontier": "top trivial-character column and support intersections",
  "new_carrier_datum": false
}
~~~
