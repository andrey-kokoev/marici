# The Gamma-Wall Port Is a Mellin Residue

## Bounded question

Is the independent wall channel an added correction, or does it arise
canonically from the same continuous Mellin source as the tail?

This packet proves that the wall current is the first endpoint residue of the
meromorphically continued moment transform. It identifies the finite Laurent
data required by an integer third-response jet and the remaining continuous
base-strip problem.

## Mellin source

Set $x=ce^y$ and define

\[
f_j(y)
=(ce^y)^{j+5/4}(ce^y-3/2)e^{-ce^y}.
\]

Then

\[
I_{j,q}=\int_0^\infty y^q f_j(y)\,dy.
\]

The function $f_j$ is analytic at the wall $y=0$. Standard Mellin
continuation gives simple poles at

\[
q=-1,-2,-3,\ldots
\]

with residues

\[
\operatorname*{Res}_{q=-n-1}I_{j,q}
=\frac{f_j^{(n)}(0)}{n!}.
\]

Thus the complete wall Taylor jet is the polar data of the same transform
whose regular values give the tail moments.

## The first residue is the wall current

Let

\[
K_j(q)=I_{j+1,q}-\frac32 I_{j,q}.
\]

Its first shifted residue is

\[
\operatorname*{Res}_{q=0}K_j(q-1)
=f_{j+1}(0)-\frac32 f_j(0).
\]

Since

\[
f_j(0)=c^{j+5/4}(c-3/2)e^{-c},
\]

the residue is exactly

\[
W_j=c^{j+5/4}(c-3/2)^2e^{-c}.
\]

The wall current is therefore not an auxiliary correction. It is the polar
part forced by the Mellin shift in the Pearson equation.

## Meromorphic Pearson identity

For positive real part of $q$, integration by parts gives

\[
I_{j+2,q}
-\left(j+\frac{19}{4}\right)I_{j+1,q}
+\frac32\left(j+\frac54\right)I_{j,q}
=qK_j(q-1).
\]

Both sides admit meromorphic continuation. Near $q=0$, write

\[
K_j(q-1)
=\frac{k_{-1}}q+k_0+k_1q+k_2q^2+O(q^3).
\]

Then

\[
qK_j(q-1)
=k_{-1}+k_0q+k_1q^2+k_2q^3+O(q^4).
\]

The value-level wall port is $k_{-1}=W_j$. The first three exponent
derivatives additionally require $k_0$, $k_1$, and $k_2$. Hence an integer
order-three jet needs a four-coordinate Laurent port, not merely the residue.

## Continuous exponent depth

For a noninteger exponent, repeated Pearson shifts terminate in a fractional
strip between $-1$ and $0$. Values and derivatives on that strip cannot be
reconstructed from the single residue at $q=-1$. They constitute a
function-valued base port.

Therefore two statements must remain separate:

1. At a fixed integer grade, third response requires a finite Laurent jet.
2. Uniform control on a continuous exponent interval requires the complete
   base-strip family and its first three derivatives.

The integer rank-21 carrier is a value-level slice. It is not the complete
carrier for continuous cubic response.

## Geometric interpretation

The regular and polar parts are two presentations of one meromorphic source
object. Passing to tail asymptotics discards the polar fiber. Retaining the
Mellin completion restores it canonically.

In exterior-algebra terms, the wall direction is the residue direction of
the completed carrier. The one-way wall-to-tail shear is the finite part of
crossing the endpoint pole under the Pearson shift.

## Remaining theorem

The next construction is the continuous base-strip module over
$-1<q\le0$, together with its order-three jet and its induced transfer into
positive exponent levels. The decisive question is whether the resulting
completed exterior orientation controls the scalar boundary compression.

## Verification

The checker
`research/grothendieck/checkers/gamma_wall_mellin_residue.py` verifies the
wall value, the shifted residue, and the four-term Laurent transport exactly.
It includes a hostile wrong-wall coefficient that leaves a nonzero residue.

