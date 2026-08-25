# Theta radial-score quartic polarization

## 1. Objective

The first two-sheet interference gate has been reduced to radial
log-concavity of

\[
W(u)=\frac{V'(u)}u,
\qquad V(u)=-\log\Phi(u).
\]

This packet clears every logarithmic denominator and identifies the exact
source-copy order of that theorem.  The result is important for proof design:
the obstruction is quartic in the completed theta source.  It cannot in
general be oriented by a two-label argument.

## 2. Denominator-free curvature

Write

\[
f=\Phi,qquad
a=f',\qquad b=f'',\qquad c=f''',
\qquad P=V'=-\frac af.
\]

The radial curvature numerator is

\[
\mathcal R_W
=u^2(P'^2-PP'')+uPP'-2P^2.
\]

Direct substitution gives the exact identity

\[
\boxed{
\begin{aligned}
f^4\mathcal R_W={}&
u^2\left[-a^4+fa^2b+f^2(b^2-ac)\right]\\
&+u\left[-fa^3+f^2ab\right]
-2f^2a^2.
\end{aligned}
}
\]

Since `f>0`, radial log-concavity is equivalent to nonnegativity of the
right-hand side.  No quotient estimate is required.

## 3. Why four copies are intrinsic

Every monomial in the cleared numerator has total source degree four:

\[
a^4,quad fa^2b,quad f^2b^2,quad f^2ac,quad
fa^3,quad f^2ab,quad f^2a^2.
\]

If

\[
f(u)=\sum_{n\ge1}\phi_n(u),
\qquad
\phi_n(u)=n^{-1/2}\phi_1(u+\log n),
\]

then `f^4 R_W` is a convergent sum over ordered quadruples
`(n_1,n_2,n_3,n_4)`.  Symmetrizing derivative placement produces a canonical
four-copy kernel

\[
f(u)^4\mathcal R_W(u)
=\sum_{n_1,n_2,n_3,n_4\ge1}
\mathscr K_u(n_1,n_2,n_3,n_4).
\]

The kernel is symmetric only after averaging over the derivative placements.
This is the faithful combinatorial object.  A proof based only on pairwise
stiffening would silently discard the `a^4` and `fa^3` interference channels.

## 4. Pair-pair organization

The quartic order does not force an uncontrolled four-dimensional argument.
It admits a pair-pair presentation.  Introduce the logarithmic-curvature
minor

\[
D_2=f'^2-ff''=f^2P'.
\]

Then the first part of the obstruction is

\[
P'^2-PP'',
\]

which compares the curvature channel `P'` with its transport by the radial
score `P`.  After clearing denominators, this is a polarization between two
two-copy packets.  The remaining terms

\[
uPP'-2P^2
\]

are the dilation counterterm.  Thus the correct architecture is

\[
\boxed{
\text{two-copy curvature packet}
\times
\text{two-copy radial packet}
+
\text{dilation counterterm}.
}
\]

This is structurally compatible with reciprocal modular sewing: reflection
may orient the two pair packets separately and then control their mixed
product.  It is not compatible with claiming positivity of each raw ordered
quadruple.

## 5. Exact falsifier

The sufficient route fails at the first `u>0` for which

\[
\boxed{
\begin{aligned}
0>{}&u^2\left[-f'^4+ff'^2f''
+f^2(f''^2-f'f''')\right]\\
&+u\left[-ff'^3+f^2f'f''\right]-2f^2f'^2.
\end{aligned}
}
\]

This is a local, source-exact falsifier.  It requires neither zero data nor a
finite spectral scan.

## 6. Next symbolic attack

For each label define its local score

\[
p_n(u)=-\frac{\phi_n'(u)}{\phi_n(u)}.
\]

Substitution of `phi_n'=-p_n phi_n` and its differentiated forms converts
the symmetrized four-copy kernel into a positive product
`phi_(n_1) ... phi_(n_4)` times a polynomial in the four scores and their
first two derivatives.  The next question is then finite and algebraic:

\[
\boxed{
\text{Does reciprocal-scale pairing turn that score polynomial into
squares plus one modular-seam current?}
}
\]

The hostile outcome is equally informative: if even a reflected quadruple
has an irreducible negative remainder, radial-score log-concavity is not the
source explanation of the interference gate.

## 7. Scope

The denominator clearing and source-copy classification are exact.  No sign
of the four-copy kernel has yet been proved.  This packet sharpens a
sufficient route to the first interference gate; it does not prove the full
Laguerre hierarchy or RH.
