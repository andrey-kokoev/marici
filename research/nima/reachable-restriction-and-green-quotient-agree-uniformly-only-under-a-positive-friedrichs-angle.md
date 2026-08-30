# Reachable restriction and Green quotient agree uniformly only under a positive Friedrichs angle

## Two reduced carriers

Let \(H_X\) be the typed boundary Hilbert carrier. Let

\[
R_X\subset H_X
\]

be the source-generated reachable carrier and

\[
N_X=\ker B_X
\]

the Green radical.

There are two natural reductions:

\[
R_X/(R_X\cap N_X)
\]

and the reachable image inside the Green quotient,

\[
(R_X+N_X)/N_X
\subset
H_X/N_X.
\]

The canonical map is

\[
C_X:
R_X/(R_X\cap N_X)
\longrightarrow
(R_X+N_X)/N_X,
\]

\[
C_X\bigl(r+(R_X\cap N_X)\bigr)
=
r+N_X.
\]

It is algebraically bijective.

## Topological criterion

The quotient norm on the target is

\[
\lVert r+N_X\rVert
=
\operatorname{dist}(r,N_X).
\]

The inverse of \(C_X\) is bounded exactly when \(R_X+N_X\) is closed.

Therefore restriction followed by quotient and quotient followed by reachable
image define the same topological carrier if and only if the sum
\(R_X+N_X\) is closed.

Finite-dimensional cutoffs always satisfy closedness. Completion requires a
uniform version.

## Friedrichs angle

Let

\[
M_X=R_X\cap N_X.
\]

The Friedrichs cosine is

\[
c_X
=
\sup
\left\{
|\langle r,n\rangle|:
r\in R_X\ominus M_X,\ 
n\in N_X\ominus M_X,\ 
\lVert r\rVert=\lVert n\rVert=1
\right\}.
\]

Define

\[
s_X=\sqrt{1-c_X^2}.
\]

Then

\[
s_X
=
\inf
\left\{
\operatorname{dist}(r,N_X):
r\in R_X\ominus M_X,\ \lVert r\rVert=1
\right\}.
\]

A positive angle

\[
s_X>0
\]

is equivalent to closedness of \(R_X+N_X\). Moreover,

\[
\lVert C_X^{-1}\rVert
=
s_X^{-1}
\]

with the natural quotient norms.

Thus the missing metric cell is exactly the angle between reachable states and
the Green radical.

## Uniform bridge condition

On a compact spectral set \(C\), the two reduction mechanisms agree uniformly
through cutoff completion when there is \(\alpha_C>0\) such that

\[
s_X(s)\ge\alpha_C
\]

for every cutoff \(X\) and \(s\in C\).

Then \(C_X(s)\) and \(C_X(s)^{-1}\) are uniformly bounded, so:

- reduced norms are uniformly equivalent;
- closed-form estimates transfer between reductions;
- reciprocal congruences remain controlled;
- determinant-line transition maps do not acquire unbounded frame factors;
- spectral gaps can be compared on the two presentations.

Pointwise trivial intersection

\[
R_X\cap N_X=0
\]

does not imply this condition.

## Two-dimensional hostile

Let

\[
H_n=\mathbb C^2,
\qquad
N_n=\operatorname{span}\{e_1\},
\]

and

\[
R_n=\operatorname{span}\{e_1+\varepsilon_ne_2\},
\qquad
\varepsilon_n\downarrow0.
\]

For every \(n\),

\[
R_n\cap N_n=0
\]

and

\[
R_n+N_n=\mathbb C^2.
\]

Yet the angle satisfies

\[
s_n
=
\frac{\varepsilon_n}{\sqrt{1+\varepsilon_n^2}}
\longrightarrow0.
\]

The quotient image of the normalized reachable vector has norm \(s_n\).
Hence

\[
\lVert C_n^{-1}\rVert\longrightarrow\infty.
\]

Every finite reduction is algebraically valid, but restriction and quotient
are not uniformly equivalent at completion.

## Effect on Green normalization

Suppose \(B_X\) descends to the Green quotient. On the reachable restriction,
a unit vector nearly parallel to \(N_X\) can have arbitrarily small Green norm.

Therefore even if the quotient Green form is uniformly coercive in its own
norm, its pullback to \(R_X\) can lose coercivity as \(s_X\to0\).

The apparent collapse is not necessarily a new quotient radical. It can be
failure of transversality between the reachable presentation and the radical.

This distinguishes collapsing support from collapsing angle.

## Effect on pencils

Let

\[
(\overline F_X,\overline B_X)
\]

be the quotient pencil and

\[
(F_X^R,B_X^R)
\]

the reachable-restriction pencil. When the constructors descend correctly,

\[
F_X^R=C_X^*\overline F_XC_X,
\qquad
B_X^R=C_X^*\overline B_XC_X.
\]

Generalized eigenvalues agree algebraically at each finite cutoff.

Uniform spectral estimates do not transfer unless \(C_X\) is uniformly
well-conditioned. A vanishing angle can turn a stable quotient eigenvector
into an unbounded reachable coordinate, invalidate compactness, or destroy
norm-resolvent convergence.

Therefore algebraic equality of finite generalized spectra is weaker than
completion equivalence of the pencil families.

## Reciprocal transversality

Let \(J_X\) carry positive-sector pairs \((R_{+,X},N_{+,X})\) to the negative
sector. Reciprocal congruence must preserve not only intersections but the
angle geometry.

If \(J_X\) is uniformly bounded with uniformly bounded inverse and maps both
subspaces exactly, positive transversality in one sector transfers to the
other with controlled constants.

An unbounded reciprocal frame can preserve algebraic pencils while collapse
the Friedrichs angle. Thus reciprocal carrier comparison and transversality
belong to one typed cell.

## Cutoff compatibility

For \(X\le Y\), cutoff maps must carry both subspaces:

\[
j_{XY}R_X\subseteq R_Y,
\qquad
j_{XY}N_X\subseteq N_Y.
\]

Exact radical compatibility controls intersections with the old ambient
carrier. Uniform angle control adds the missing norm geometry.

Together they ensure that the canonical maps \(C_X\) form a bounded natural
comparison between the reachable-restriction system and the radical-quotient
system.

Without naturality, even a positive angle at each cutoff may not define one
completed comparison.

## Determinant-line consequence

At finite cutoff, changing between the two reduced presentations conjugates
the pencil by \(C_X\). Determinants differ by the induced determinant-line
frame.

If \(\lVert C_X^{-1}\rVert\) diverges, that frame can fail to descend even
though finite zero sets agree. The multiplier relating the two determinant
sections need not converge to an invertible completed unit.

Hence the \(\Xi\) bridge must be established after uniform transversality, not
merely after finite algebraic identification.

## Ordered audit

The carrier audit now has five cells:

1. classify and authorize the radical reduction;
2. construct the source-generated reachable carrier;
3. verify exact cutoff and reciprocal transport of both subspaces;
4. prove compact-local positive Friedrichs angle;
5. only then compare reduced pencils spectrally.

Norm-resolvent or collectively compact convergence begins after cell four.

## Hostile tests

1. Trivial intersection without angle control permits unbounded inverse
   comparison.
2. Finite-dimensional closed sums do not imply a uniform completed sum.
3. Stable quotient coercivity may collapse on the reachable presentation.
4. Equal finite generalized spectra do not imply equivalent spectral limits.
5. Reciprocal algebraic transport can preserve intersections while distort
   angles.
6. A divergent determinant-frame comparison invalidates the completed
   nonvanishing multiplier.

## Consequence for categorical RH

Kitaev's proposed bridge is exact. Reachable restriction and Green quotient
are algebraically the same on the reachable image, but they define one stable
completed carrier only when the reachable space remains uniformly transverse
to the Green radical.

The next spectral theorem must therefore be stated on a chosen reduced
presentation together with the positive-angle comparison cell. Otherwise
support convergence and spectral-gap claims can refer to inequivalent
completion geometries.

## Verdict

The Friedrichs angle is the missing metric coherencer between the two
authorized Green reductions. A compact-local positive lower bound makes
restriction and quotient uniformly equivalent. Vanishing angle is an
independent completion failure that finite intersections and finite spectra
cannot detect.
