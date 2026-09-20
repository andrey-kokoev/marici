# Prior-research clue audit for the terminal relative-Haar energy gate

## Search result

Prior research does contain a substantial partial unlock. The state-placement
map formerly described as missing has already been constructed as the
fixed-forcing joint graph

\[
\Gamma_\Phi
=
\{(C_\Phi u,\Phi\otimes u):u\in H_{\rm hist}\},
\qquad
(C_\Phi u)(t)=\int\Phi(x)u(x+t)\,dx.
\]

Its Haar projection is injective, it intertwines prime translation, and at an
Xi zero the two stable histories have the same nonzero graph image. Thus the
separation-history-to-Haar **state placement** is no longer missing.

## Why this does not yet close confinement

The Xi seam relation gives

\[
u_+=u_-=u_z.
\]

The relative-Haar cycle requires the different statement

\[
\mathcal E_z(J_\Phi u_+)
=
\mathcal E_z(T_pJ_\Phi u_-).
\]

After seam matching this becomes

\[
(1-p^{-2\operatorname{Re}z})
\mathcal E_z(J_\Phi u_z)=0.
\]

The joint graph identifies the state used by both theories, but does not imply
equality of the two route energies. Hence it removes the localization/type
objection while leaving the RH-strength metric identity intact.

## Strongest candidate unlock

The stable-history sign ledger identifies the uncancelled positive Green term
exactly:

\[
F_+(w,z)-F_-(w,z)
=
R(z)-R(-z)+\overline{R(w)-R(-w)}.
\]

With the causal history operator,

\[
R(z)-R(-z)
=
\langle\Phi,(H_z-H_z^*)\Phi\rangle.
\]

Therefore the missing arithmetic balance is not an unknown scalar. It is the
quadratic form of the source-native causal odd compression

\[
T_{\rm hist}(z)=\frac{H_z-H_z^*}{2}.
\]

The required local theorem is the parameter-free Green-form identity

\[
G_{{\rm win},p}
=
K_p^{\rm odd}G_{\theta,p}(K_p^{\rm odd})^*.
\]

Its finite residual is

\[
\mathcal E_{p,X}
=G_{{\rm win},p,X}
-K_{p,X}^{\rm odd}G_{\theta,p,X}(K_{p,X}^{\rm odd})^*.
\]

This is testable before Xi specialization and is the best noncircular unlock
candidate found.

## Equivalent C34 formulation

Prior work independently constructs the relative Tate--Hardy feature

\[
C=\frac12(F_T+F_0),
\qquad
D=\frac12(F_T-F_0),
\]

with

\[
C^*C+D^*D=I,
\qquad
C^*J_2D+D^*J_2C=Q^T-Q^0.
\]

Its signed current `q_(F34)` is reciprocal self-dual and source-derived. The
same missing theorem can be written

\[
q_{\mathfrak F_{34}}(\Phi\otimes u_z,
\Phi\otimes u_z)=P(z),
\]

with the orientation needed to cancel the theta forcing pairing. This is not a
new gate; it is the global C34 presentation of the local odd-compression Green
identity.

## Existing negative clues

The search also rules out several shortcuts:

- global reciprocal-jet neutrality does not localize primewise;
- Xi-square sewing controls the wrong forcing sum and leaves the positive
  forcing difference;
- reciprocal doubling gives two dependent Green equations;
- inverse-Hellinger scalar normalization is unbounded;
- state equality under prime translation is impossible for a nonzero `L2`
  state;
- the canonical Stokes cancellation vanishes for every parameter and is not an
  independent detector.

## Recommended finite attack

Do not search for another carrier. On one finite shell and one prime:

1. retain the four bordered coordinates `rho0,E,W,R`;
2. compute `K_p^odd` from the already fixed jump column;
3. evaluate all four matrix units of `G_win,p` and
   `K_p^odd G_theta,p (K_p^odd)^*`;
4. reject on the first unequal diagonal, real mixed, or oriented-imaginary
   entry;
5. only after exact finite equality, prove projective cutoff convergence.

This finite quadratic identity is the only concrete prior-research clue that
could unlock the terminal energy gate without assuming RH.