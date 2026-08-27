# Composition can raise faithfulness by shrinking the admissible equalizer

## Correction

The composition tower cannot manufacture additional transverse consequences from one regular scalar zero. It can nevertheless make the scalar faithful by reducing the admissible state space before scalar evaluation.

This is the cleanest surviving role for a multi-object RH network.

## Ambient and admissible spaces

Let \(V\) be the ambient lifted state space. A scalar readout

\[
L:V\longrightarrow\mathbb C
\]

is noninjective whenever \(\dim V>1\).

A network introduces source-authorized compatibility maps

\[
D_1,\ldots,D_m:V\longrightarrow W_j.
\]

The admissible network states form the equalizer or compatibility locus

\[
C=\bigcap_{j=1}^m\ker D_j.
\]

The relevant faithfulness question is not whether \(L\) is injective on \(V\), but whether

\[
\ker L\cap C=0.
\]

## Equalizer-faithfulness theorem

For linear finite-dimensional data, the scalar readout is faithful on the admissible network states if and only if

\[
\ker L\cap\bigcap_j\ker D_j=0.
\]

Equivalently, the stacked map

\[
\begin{pmatrix}
L\\D_1\\\vdots\\D_m
\end{pmatrix}
\]

is injective.

The network has not increased the rank of the scalar output. It has reduced the domain on which that scalar must be faithful.

## Minimal example

Let

\[
V=\mathbb C^2,
\qquad
L(x,y)=x.
\]

The scalar misses the entire \(y\)-axis. Add the compatibility law

\[
D(x,y)=y-x.
\]

Then

\[
C=\{(x,x):x\in\mathbb C\}.
\]

On \(C\), the scalar is faithful:

\[
L(x,x)=0
\quad\Longrightarrow\quad
(x,x)=0.
\]

No extra output was forced to vanish by \(L=0\). The independent network law \(D=0\) was already part of admissibility.

## Why this escapes the factorization no-go theorem

The earlier no-go theorem considered a richer output \(R\) universally forced to vanish by \(L=0\) on the same domain. That condition makes \(R\) factor through \(L\).

Here \(D=0\) is imposed independently of the scalar zero. It defines the domain \(C\). There is no claim that \(L=0\) forces \(D=0\); every admitted state already satisfies \(D=0\).

The order is:

1. source composition selects \(C\);
2. normalization excludes the zero state;
3. scalar evaluation acts on \(C\);
4. scalar vanishing contradicts faithfulness of \(L|_C\).

## Compositional information gain

An added object or edge contributes genuine information exactly when its compatibility residual reduces the current admissible locus.

For linear constraints, let

\[
C_k=\bigcap_{j=1}^k\ker D_j.
\]

The incremental gain of \(D_{k+1}\) is

\[
\dim C_k-\dim C_{k+1}.
\]

Equivalently, it is the rank added by the new rows modulo the span of the previous residual rows.

A sheet, seam, reference, or current with zero incremental gain is compositionally redundant even if it has a new physical label.

## Nonlinear version

Let \(M\) be an ambient source manifold and let the network laws define

\[
C=\{x:D_1(x)=\cdots=D_m(x)=0\}.
\]

At a regular admitted point \(p\), the local admissible tangent space is

\[
T_pC=\bigcap_j\ker dD_j(p).
\]

The scalar is infinitesimally faithful when

\[
\ker df_p\cap T_pC=0.
\]

Since one scalar differential has rank at most one, this requires \(\dim T_pC\le1\). Global faithfulness additionally requires ruling out distinct points of \(C\) with the same scalar value.

## Quantitative gate

Let

\[
F_N=
\begin{pmatrix}
L_N\\D_{1,N}\\\vdots\\D_{m,N}
\end{pmatrix}.
\]

Finite injectivity is insufficient for completion. Require a uniform lower bound

\[
\lVert F_Nv\rVert\ge c\lVert v\rVert
\]

with \(c>0\) independent of cutoff on the declared off-seam region.

If the network constraints are enforced exactly, this reduces to a uniform lower bound for \(L_N\) on \(C_N\).

## RH-bearing formulation

The promising network theorem is not that \(\xi(s)=0\) forces many features to vanish.

It is:

> The complete source-derived theta/Tate composition laws cut the normalized off-seam lifted state space down to an admissible locus on which scalar Tate evaluation is uniformly faithful.

This requires Grothendieck to provide the actual residual maps for Fourier--Tate transport, sheet matching, seam incidence, primitive and square currents, endpoint normalization, and completion.

## Falsifiers

- a nonzero \(v\) satisfying every network residual and \(Lv=0\);
- an added object whose residual rows lie in the span of existing rows;
- scalar injectivity only after adding an unauthorized residual;
- finite equalizers that shrink correctly but whose lower margin tends to zero;
- a reference that fixes a frame but leaves a nontrivial stabilizer inside \(C\);
- a nonlinear compatibility locus with multiple branches sharing the same scalar value.

## Verdict

The fourth tower can increase effective scalar faithfulness without increasing zero-propagation rank. It does so by constructing a smaller, source-authorized compatibility equalizer. Its information gain is domain reduction, not consequence multiplication.
