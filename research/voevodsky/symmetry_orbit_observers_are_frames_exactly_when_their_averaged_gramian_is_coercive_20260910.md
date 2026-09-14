# Symmetry-orbit observers are frames exactly when their averaged Gramian is coercive

## Question

When source-rotated copies of one observer detect genuinely new directions, what distinguishes a true complementary observer family from presentation aliases?

## Claim boundary

For a finite unitary symmetry group, the orbit family is stably reconstructing exactly when its averaged Gramian is bounded below. Source rotations can reduce the joint kernel, unlike scalar-phase aliases, but finitely many orbit copies of a compact observer remain compact and cannot be bounded below on an infinite-dimensional source.

## Problem

Let \(G\) be a finite group with a unitary representation

\[
\rho:G\to U(X)
\]

on a Hilbert space \(X\), and let

\[
A:X\to Y
\]

be bounded. Define the orbit observer

\[
\mathcal O_Ax
=
\bigl(A\rho(g)x\bigr)_{g\in G}
\in
\bigoplus_{g\in G}Y.
\]

Unlike scalar-phase target aliases, the source rotations may present different directions to \(A\).

## Bold conjecture

A finite symmetry orbit of any injective or coordinatewise nonzero observer restores stable reconstruction.

## Named rivals

1. Stability is controlled by the averaged Gramian, not coordinatewise nonvanishing.
2. Finite source rotations may remove a kernel in finite dimension.
3. Finite orbiting cannot repair compactness on an infinite-dimensional source.
4. Group irreducibility alone forces every nonzero observer orbit to be stable.

## Orbit-frame theorem

The orbit Gramian is

\[
S_A
=
\mathcal O_A^*\mathcal O_A
=
\sum_{g\in G}
\rho(g)^*A^*A\rho(g).
\]

The following are equivalent:

1. \(\mathcal O_A\) is bounded below by \(\delta>0\);
2. the orbit family satisfies

   \[
   \sum_{g\in G}\|A\rho(g)x\|^2
   \ge
   \delta^2\|x\|^2;
   \]

3. the averaged Gramian satisfies

   \[
   S_A\ge\delta^2I;
   \]

4. \(\mathcal O_A\) is injective with closed range.

### Proof

Direct computation gives

\[
\|\mathcal O_Ax\|^2
=
\langle S_Ax,x\rangle.
\]

The equivalences are the row-operator lower-frame theorem applied to the finite family \((A\rho(g))_{g\in G}\).

## Equivariance of the Gramian

For every \(h\in G\), reindexing the finite sum gives

\[
\rho(h)^*S_A\rho(h)=S_A.
\]

Thus \(S_A\) lies in the commutant of the source representation. The stability test decomposes across isotypic components rather than across arbitrary presentation coordinates.

## Finite-dimensional irreducible corollary

Suppose \(X\) is finite-dimensional and irreducible over \(\mathbb C\). By Schur's lemma,

\[
S_A=\lambda I.
\]

Taking traces,

\[
\lambda
=
\frac{|G|}{\dim X}\operatorname{tr}(A^*A).
\]

Hence every nonzero \(A\) gives a stable orbit frame, with exact lower bound

\[
\delta^2
=
\frac{|G|}{\dim X}\|A\|_{\rm HS}^2.
\]

Rival 4 is therefore true only in this finite-dimensional irreducible setting.

## Reducible criterion

If

\[
X=\bigoplus_\alpha X_\alpha
\]

is an orthogonal isotypic decomposition, then \(S_A\) is block diagonal across \(X_\alpha\). Stability requires a positive lower bound for every block, uniform over all components when infinitely many occur.

Merely detecting one vector in each component does not provide a uniform bound.

## Compact-orbit no-go

Assume \(X\) is infinite-dimensional and \(A\) is compact. Every

\[
A\rho(g)
\]

is compact. Since \(G\) is finite, the row operator \(\mathcal O_A\) is compact. A compact operator on an infinite-dimensional Hilbert space cannot be bounded below.

Equivalently, \(S_A\) is compact and cannot satisfy

\[
S_A\ge\delta^2I
\]

for \(\delta>0\).

Thus finite symmetry orbiting does not repair the completed-source margin of a compact analytic channel, even when it removes a finite-dimensional kernel.

## Hostile infinite example

Let

\[
X=\ell^2(\mathbb N)\otimes\mathbb C^2,
\qquad
G=C_2,
\]

with the generator swapping the two coordinates in each \(\mathbb C^2\) fiber. Define

\[
A(e_n\otimes(a,b))
=
\frac1n a\,e_n.
\]

The original observer kills the second coordinate. Its orbit copy detects that coordinate:

\[
A\rho(s)(e_n\otimes(a,b))
=
\frac1n b\,e_n.
\]

The joint orbit observer is injective, but

\[
S_A|_{e_n\otimes\mathbb C^2}
=
\frac1{n^2}I_2.
\]

Its lower margin still tends to zero. Symmetry removes the fiberwise kernel but not the completion collapse.

## Presentation aliases versus orbit observers

A target phase alias has the form

\[
A_g=V_gA
\]

and adds no source direction when \(V_g\) is unitary. A source orbit has the form

\[
A_g=A\rho(g)
\]

and may alter the kernel. Therefore:

- target-unitary aliases are `presentation_lift` data;
- source-rotated families are `symmetry_orbit_observer` data;
- the latter becomes a `complementary_observer` only when \(S_A\) is coercive.

## Green/Real worked-example consequence

The four Fourier presentations can be treated as an orbit observer only if each presentation acts on the source before readout and the averaged Gramian is computed. If they differ merely by metaplectic target phases, they are presentation aliases.

For the compact Euler-to-radial analytic map, any finite Fourier orbit remains compact on the completed infinite source. The orbit may distinguish presentation sectors or finite-cutoff fibers, but it cannot replace the discrete complementary observer required for a global lower margin.

The fold

\[
C_uF^2=W_uC_u
\]

transports the half-turn orbit component unitarily and therefore preserves the same Gramian bound.

## Strongest falsification attempt

The finite-dimensional irreducible result is the strongest case against the no-go: a single nonzero scalar probe and its symmetry orbit can reconstruct the entire representation stably. This does not extend to a compact observer on an infinite direct sum because the isotypic block bounds can approach zero.

The conjecture is therefore rejected at completion while surviving on each fixed finite-dimensional irreducible block.

## Disposition

A symmetry orbit is an operational observer precisely through its averaged Gramian. Source rotations can add detected directions, but finite orbiting cannot repair compactness on an infinite source. The constructor language now distinguishes presentation aliases from orbit observers by whether the group acts before or after the observation map, and promotes an orbit family to a stable complement only after a coercive Gramian test.
