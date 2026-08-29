# The correct Birman–Schwinger object lives on the finite boundary space

## Exterior observer obstruction

The scalar Euler/Riemann observer is not bounded on the source-normalized Green Hilbert space. Therefore the rank-one bulk loading

\[
U^{*}U
\]

is not the correct spectral object.

The source already supplies the ingredients of a boundary-triplet formulation:

- a closed first-order history operator;
- continuous endpoint traces;
- a Green/Stokes identity;
- a finite typed boundary carrier;
- reciprocal sewing.

These move the Birman–Schwinger reduction from the infinite label space to the finite boundary space.

## Boundary triple

Let \(A_{\min}\) be the closed minimal history operator and \(A_{\max}=A_{\min}^{*}\). Let

\[
\Gamma_0,\Gamma_1:
\operatorname{dom}A_{\max}
\longrightarrow
\mathcal B
\]

be the typed boundary traces, where \(\mathcal B\) is the reduced five-wall or four-character boundary space.

The required Green identity is

\[
\langle A_{\max}f,g\rangle
-
\langle f,A_{\max}g\rangle
=
\langle\Gamma_1f,\Gamma_0g\rangle_{\mathcal B}
-
\langle\Gamma_0f,\Gamma_1g\rangle_{\mathcal B}.
\]

The rapid twisted core and endpoint-trace theorem already provide the local analytic form of this identity. The remaining task is to assemble all typed wall coordinates and prove boundary surjectivity or the appropriate quasi-boundary version.

## Poisson operator and Weyl function

For spectral parameter \(s\) away from a reference extension, define the Poisson operator

\[
\gamma(s):
\mathcal B
\longrightarrow
\ker(A_{\max}-s)
\]

by

\[
\Gamma_0\gamma(s)=I_{\mathcal B}.
\]

Then define the Weyl function

\[
M(s)
=
\Gamma_1\gamma(s).
\]

The exterior observer is now boundary data in \(\mathcal B'\), while \(\gamma(s)\) provides the source-authorized lift into the defect space. No infinite prime summation row is treated as a Green-Hilbert vector.

## Boundary spectral pencil

Let \(\Theta(s)\) encode the arithmetic boundary condition. The completed state exists precisely when

\[
(\Theta(s)-M(s))b=0
\]

for some nonzero boundary packet \(b\).

Thus the spectral identification target becomes

\[
\det_{\mathcal B}(\Theta(s)-M(s))=0
\]

at finite boundary rank, or the corresponding determinant-line section when the boundary object is typed rather than scalar.

A Birman–Schwinger form may be written on \(\mathcal B\), for example

\[
K_{\partial}(s)
=
\Theta(s)^{-1/2}
M(s)
\Theta(s)^{-1/2},
\]

only when positivity and invertibility are source-authorized. Otherwise retain the generalized pencil.

## Advantages

This formulation:

- keeps prime aggregation in the exterior boundary condition;
- uses the closed history operator to regularize boundary data;
- makes completion failure a boundary-extension defect;
- preserves all Fourier character ports;
- avoids the false identity-metric eigenvalue crossing;
- reduces determinant formation to the finite typed boundary space.

## Exact remaining gates

1. freeze \(A_{\min}\), \(A_{\max}\), \(\Gamma_0\), and \(\Gamma_1\);
2. prove the complete typed Green identity;
3. prove boundary surjectivity or characterize the boundary relation;
4. construct \(\gamma(s)\) and \(M(s)\) on compact off-seam regions;
5. derive \(\Theta(s)\) from arithmetic source assembly;
6. prove the determinant section equals the completed zeta or xi section;
7. prove off-seam invertibility of \(\Theta(s)-M(s)\).

The last two are the actual RH-bearing obligations.

## Hostiles

A bounded Poisson operator chosen without the source Green identity is merely fitted smoothing.

A scalar Weyl function formed after collapsing the four boundary characters can miss an oriented kernel.

A boundary determinant may reproduce zeta numerically while its arithmetic condition \(\Theta\) was inferred backward from zeta; that is circular.

## Frontier

The next constructor is not another bulk norm. It is the complete typed boundary triple and its Weyl function.

This restores a legitimate operator collision mechanism while respecting the exterior nature of prime aggregation.
