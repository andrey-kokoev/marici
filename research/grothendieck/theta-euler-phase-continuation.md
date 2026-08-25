# Theta--Euler phase continuation to the fixed seam

Author: `marici.Grothendieck`

## 0. Origin of the move

The operator's sequence was:

\[
\text{half-plane distinction}
\longrightarrow
\text{loss of projected meaning}
\longrightarrow
\text{integral phase defect}.
\]

The naive implementation by deforming theta-label coefficients is impossible:
finite packets are not modularly closed, and preservation of every prime
recursion forces all weights to be equal.  The correct transport therefore
keeps the source fixed and moves the spectral point.  Arithmetic supplies a
canonical phase in the Euler chamber; modular completion must carry that
phase to the reciprocal fixed seam.

## 1. The arithmetic phase anchor

Use

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

In the simply connected half-plane `Re(s)>1`, every factor is nonzero after
the pole at `s=1` is kept outside the domain, and the absolutely convergent
Euler product gives

\[
\log\zeta(s)
=\sum_p\sum_{k\ge1}\frac{p^{-ks}}k.
\]

Hence `xi` has a canonical holomorphic logarithm there, after fixing one base
value:

\[
\begin{aligned}
L_{\rm E}(s)={}&-log2+log s+log(s-1)
-\frac{s}{2}\log\pi+log\Gamma(s/2)\\
&+\sum_p\sum_{k\ge1}\frac{p^{-ks}}k.
\end{aligned}
\]

This is the initial integral trivialization.  Prime powers determine its
phase before analytic continuation is required.

## 2. RH as continuation of meaning

Let

\[
\Omega_+=\{s:\operatorname{Re}s>1/2\}.
\]

Because `Omega_+` is simply connected,

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
L_{\rm E}\text{ extends holomorphically from }\operatorname{Re}s>1
\text{ to all of }\Omega_+
}
\]

with `exp(L_E)=xi`.  The functional equation then supplies the reflected
trivialization on `Re(s)<1/2`.  Critical-line zeros are boundary failures of
gluing; an off-line zero would obstruct the arithmetic logarithm before it
reaches the fixed seam.

This is the operator's “loss of meaning after distinction” in exact form:
the right chamber first receives its arithmetic orientation from the Euler
product, and the question is how far that phase remains single-valued under
completed continuation.

## 3. Why ordinary Euler continuation is insufficient

The double prime sum converges absolutely only for `Re(s)>1`.  It cannot be
continued termwise through that boundary.  Moreover, `log(s-1)` and
`log(zeta(s))` are individually singular at `s=1`, while their contribution
to the completed entire function has a removable combined singularity.

Therefore the required object is not a continued raw prime logarithm.  It is
a source-derived renormalized logarithmic packet in which

\[
\text{completion pole}
+
\text{prime divergence}
+
\text{theta modular seam}
\]

are sewn before branches are chosen.  Separating these terms first creates
false singularities and loses the physical phase coordinate.

This matches the earlier prime-scale recursion result: a prime multiplier
creates apparent arithmetic singularities, while the finite modular sewing
current cancels them exactly.  Those cancellations are finite local models
of the continuation required here.

## 4. Static index formulation

The fixed logarithmic connection is

\[
\omega_\xi=\frac{\xi'(s)}{\xi(s)}\,ds.
\]

It is exact in the Euler chamber.  For a loop `gamma` in `Omega_+` avoiding
the divisor,

\[
\frac1{2\pi i}\oint_\gamma\omega_\xi
\]

is an integer.  RH says that continuation from the Euler chamber gives zero
for every such chamber loop.  Crucially, the source is unchanged; only the
domain of its canonical logarithm is enlarged.

The desired modular identity should therefore have the form

\[
\boxed{
\omega_\xi=dL_{\rm ren}
\qquad(\operatorname{Re}s>1/2),
}
\]

where `L_ren` is constructed without presupposing a zero-free branch.  Merely
writing `L_ren=log(xi)` is circular.  Its construction must come from a
convergent theta/prime sewing formula whose exponent is visibly nonzero.

## 5. Relation to the two-sheet Carrier

In the spectral coordinate `s=1/2+iz`, the right chamber corresponds to one
open `z` half-plane.  The decomposition

\[
X(z)=F(z)+F(-z)
\]

then asks whether the Euler-anchored phase of this scalar sum survives until
the projective Carrier reaches its destructive divisor `[1:-1]` on the real
`z` boundary.

The prime and theta descriptions have complementary roles:

\[
\boxed{
\text{Euler product anchors the integral phase far from the seam;}
\quad
\text{theta modularity must transport it across the critical strip.}
}
\]

Neither description alone covers the entire chamber in its natural
convergent coordinates.

## 6. Minimal theorem and falsifier

The minimal theorem is a convergent, branch-independent formula for a
renormalized primitive `L_ren` on `Re(s)>1/2` satisfying

\[
L_{\rm ren}'(s)=\frac{\xi'(s)}{\xi(s)}
\]

wherever the quotient is initially defined, and agreeing with `L_E` in
`Re(s)>1`.  If `L_ren` is holomorphic on the whole chamber, exponentiation
proves nonvanishing there.

The sharp falsifier is monodromy of any proposed sewn primitive around a
compact chamber loop, or a residual uncancelled prime/seam singularity.  A
formula that defines its branch by reference to the zeros is inadmissible.

## 7. Scope

The Euler-chamber logarithm and its equivalence with zero-free continuation
are exact.  Constructing the required renormalized primitive on the larger
half-plane is equivalent in strength to the missing zero-free theorem unless
the theta--prime sewing supplies an independently convergent nonvanishing
representation.  No such representation has yet been derived, and RH is not
proved.
