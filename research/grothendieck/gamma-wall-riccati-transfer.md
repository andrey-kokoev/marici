# The Gamma-Wall Cubic Gate Is a Backward Riccati-Flag Problem

## Bounded question

Can the full Pearson ladder be written as a closed source-derived transfer
whose boundary value is the primitive adjacent ratio?

This packet constructs that transfer exactly. It identifies the required
large-degree flag and the remaining cone-preservation theorem. It does not
prove that theorem.

## Ratio coordinates

For the Gamma-wall moments $I_{j,q}$, define

\[
R_{j,q}=\frac{I_{j+1,q}}{I_{j,q}},
\qquad
S_{j,q}=\frac{I_{j,q-1}}{I_{j,q}}.
\]

The physical adjacent ratio is the boundary readout

\[
r(q)=qS_{0,q}.
\]

Dividing the width-two Pearson ladder by $I_{j+1,q}$ gives

\[
R_{j+1,q}
=j+\frac{19}{4}
-\frac{(3/2)(j+5/4)}{R_{j,q}}
+\frac{qS_{j,q}(R_{j,q-1}-3/2)}{R_{j,q}}.
\]

The definition of $S$ gives the companion transport

\[
S_{j+1,q}
=S_{j,q}\frac{R_{j,q-1}}{R_{j,q}}.
\]

These two equations form an exact nonlinear Riccati system in the degree
$j$. No fitted coefficients or zero data enter.

## Explicit triangular backward map

The companion equation removes $S_{j,q}$ from the Riccati numerator. If the
level $q-1$ has already been propagated to degree $j$, define

\[
D_{j,q}
=j+\frac{19}{4}
+qS_{j+1,q}\left(1-\frac{3}{2R_{j,q-1}}\right)
-R_{j+1,q}.
\]

Then the inverse transfer is explicit:

\[
R_{j,q}
=\frac{(3/2)(j+5/4)}{D_{j,q}},
\qquad
S_{j,q}
=S_{j+1,q}\frac{R_{j,q}}{R_{j,q-1}}.
\]

This is triangular in exponent depth. At each backward degree step, propagate
the lower exponent level first and then evaluate the current level.

The first local cone gate is now exact:

\[
D_{j,q}>0.
\]

If it fails, the positive ratio coordinate either changes orientation or
hits a pole. At large $j$, the source flag predicts that $D_{j,q}$ tends to
$3/2$ with smaller logarithmic corrections. The missing theorem must keep it
positive uniformly during backward propagation and control the order-three
$q$-jet of the same rational map.

## Triangular closure in exponent depth

The transfer at exponent $q$ calls only the adjacent level $q-1$. Therefore
a bounded exponent interval closes as a finite triangular stack above one
base strip of width one. Differentiating in $q$ preserves this structure:
the order-three jet needed for $r'''$ calls order-three jets at the adjacent
level.

For the interval $4\le q\le10$, at most ten downward shifts reach the base
strip. The infinite Pearson array has therefore compressed to a finite
exponent-depth jet system evolving on the half-line $j\ge0$, but only after
the base strip is retained as independent boundary data.

## Endpoint correction: the base strip is an independent port

The homogeneous Pearson formula holds for $q>0$, because
$\log(x/c)^q$ vanishes at $x=c$. At $q=0$ that vanishing fails. Direct
integration by parts gives

\[
I_{j+2,0}
=\left(j+\frac{19}{4}\right)I_{j+1,0}
-\frac32\left(j+\frac54\right)I_{j,0}
+W_j,
\]

where

\[
W_j=c^{j+5/4}(c-3/2)^2e^{-c}.
\]

Define

\[
E_j=\frac{W_j}{I_{j,0}}.
\]

The base transfer is

\[
R_{j+1,0}
=j+\frac{19}{4}
-\frac{(3/2)(j+5/4)}{R_{j,0}}
+\frac{E_j}{R_{j,0}},
\]

\[
E_{j+1}=c\frac{E_j}{R_{j,0}}.
\]

The wall channel is source-fixed and positive. It is not reconstructible
from the ratio tail alone. For nonintegral exponent depth, repeated shifts
terminate in $-1<q\le0$. Those wall moments likewise form an independent
base strip; applying the homogeneous recurrence below $q=0$ would discard a
nonintegrable endpoint contribution.

## Exact linear and geometric-algebra lift

The nonlinear base Riccati system is the projectivization of a linear
three-channel transfer. Define

\[
X_j=
\begin{pmatrix}
I_{j+1,0}\\
I_{j,0}\\
W_j
\end{pmatrix}.
\]

Then

\[
X_{j+1}=M_jX_j,
\]

with

\[
M_j=
\begin{pmatrix}
j+19/4 & -(3/2)(j+5/4) & 1\\
1 & 0 & 0\\
0 & 0 & c
\end{pmatrix}.
\]

Its determinant is

\[
\det M_j=\frac32\left(j+\frac54\right)c>0.
\]

Thus every finite-degree source transfer is invertible and
orientation-preserving. Let $e_1,e_2$ span the tail plane and let $e_3$ be
the wall direction. The tail plane is invariant, while

\[
M_je_3=e_1+ce_3.
\]

The wall therefore enters the tail through a one-way shear. It is not a
separate spectator coordinate.

On the exterior algebra, the tail area and full volume transform as

\[
(M_je_1)\wedge(M_je_2)
=\frac32\left(j+\frac54\right)e_1\wedge e_2,
\]

\[
(M_je_1)\wedge(M_je_2)\wedge(M_je_3)
=\frac32\left(j+\frac54\right)c
e_1\wedge e_2\wedge e_3.
\]

No finite local step can erase either the tail orientation or the complete
three-channel orientation. The Riccati coordinates arise only after dividing
by one tail component. Their poles are chart failures of the projective
description, not singularities of the full linear transfer.

This is precisely an exterior-algebra correction. A scalar zero or projective
pole cannot be interpreted as disappearance of the complete state. The full
oriented blade survives every finite source step; only projection or a
nonuniform completion can hide it.

It is not yet a full geometric-algebra theorem. No source-derived metric,
Clifford product, rotor, spin action, or positive multivector cone has been
defined. The present result controls incidence, rank, and orientation only.
Any claim about angles, orthogonality, elliptic versus hyperbolic transport,
or scalar parts of Clifford products requires that additional metric data.

## Source-selected large-degree flag

For fixed $q$ and large $j$, the source integral is concentrated near
$x=j+9/4$. Standard Gamma-saddle expansion predicts

\[
R_{j,q}
=j+\frac94
+\frac{q}{\log(j/c)}
+O(j^{-1}),
\]

and

\[
S_{j,q}
=\frac{1}{\log(j/c)}
+O\left(\frac{1}{j\log(j/c)^2}\right).
\]

At $q=0$, the untruncated Gamma calculation fixes only the rational part:

\[
R_{j,0}
=j+\frac94
+\frac{3/2}{j-1/4}
\]

before the lower-wall correction. The normalized wall channel satisfies
$E_{j+1}=cE_j/R_{j,0}$ and decays faster than every algebraic order in
$1/j$. The logarithmic term at positive $q$ is the response of the saddle to
the factor $\log(x/c)^q$.

The asymptotic statement above is currently a derived target, not an
interval-certified theorem. Its role is to specify the candidate flag rather
than to assume a boundary value chosen for the desired sign.

## What remains

The physical problem is now a two-boundary problem. The source selects an
algebraic flag at large $j$ and an independent wall channel in the base
exponent strip. The transfer must combine both before reaching $j=0$. The
required theorem is that the order-three $q$-jet remains in a source-derived
cone whose boundary readout satisfies

\[
\frac{d^3}{dq^3}(qS_{0,q})>0.
\]

Forward positivity of the moments does not automatically make the inverse
transfer cone-preserving. Denominators, subtraction, the adjacent-level
channel, and the wall channel are the exact possible failure points.

The former proposal to initialize only at a large cutoff $J$ is invalid. The
wall amplitude is invisible to every algebraic order of the large-$j$ flag
but changes the finite-degree solution. Any finite falsifier must retain the
source wall channel or full base strip explicitly. A tail-only backward
calculation tests a quotient of the source system, not the Gamma wall.

## Verification

The checker
`research/grothendieck/checkers/gamma_wall_riccati_transfer.py` verifies both
transfer equations as exact consequences of the Pearson recurrence and
verifies the explicit backward inverse. It includes a deliberate coefficient
perturbation that leaves a nonzero residual. It also verifies the endpoint
current and its normalized transfer.
The checker also verifies the linear lift, its positive determinant, and the
induced tail-bivector and full-trivector scale factors.
