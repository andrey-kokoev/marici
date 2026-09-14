# Minimal sphere map into the Aspect residue complex

## Question

What is the smallest chain-level object that maps to the closed Aspect vector \((1,1)^T\), and what does its mapping cone establish?

## Claim boundary

This constructs the minimal algebraic chain map using the published Aspect residue matrix. The source generator is formal and has no resolved/Rees or Cayley--Menger provenance. Therefore the construction does not satisfy the physical source-authority gate.

## Target complex

Use the two-term residue complex

\[
B_1=\mathbb Z^2
\xrightarrow{D_{\rm res}}
B_0=\mathbb Z^3,
\qquad
D_{\rm res}=
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix}.
\]

The vector

\[
v=(1,1)^T
\]

satisfies \(D_{\rm res}v=0\) and generates \(H_1(B)\cong\mathbb Z\).

## Minimal source and map

Let \(A=\mathbb Z[1]\) have one generator \(e\) in degree one and zero differential. Define

\[
F_1(e)=v,
\qquad F_0=0.
\]

The complete chain-map equation is the single equality

\[
D_{\rm res}F_1=0.
\]

No smaller nonzero chain complex can represent a degree-one class.

## Mapping cone

The cone is

\[
0\longrightarrow
A_1
\xrightarrow{F_1}
B_1
\xrightarrow{D_{\rm res}}
B_0
\longrightarrow0.
\]

Its consecutive differentials compose to zero. Since \(F_1\) maps the source generator onto the kernel generator of \(D_{\rm res}\),

\[
H_2(\operatorname{Cone}F)=0,
\qquad
H_1(\operatorname{Cone}F)=0,
\qquad
H_0(\operatorname{Cone}F)\cong\mathbb Z^2.
\]

Thus the minimal generator accounts exactly for the closed relative line. It does not eliminate the two-dimensional residue cokernel.

## Interpretation

The algebraic interface is now minimal and complete: one generator, one image column, one chain square, and one mapping cone. The only missing datum for the requested physical test is not more linear algebra. It is a source-derived identification of \(e\) with an exceptional geometric generator, followed by contour/readout authority.

## Computed result

The chain square vanishes exactly. The target kernel is rank one and is generated integrally by \((1,1)^T\); the formal source maps onto the full kernel. Both the kernel generator and the residue-image generator are primitive. The mapping cone has integral homology

\[
H_2=0,
\qquad H_1=0,
\qquad H_0\cong\mathbb Z^2.
\]

## Disposition

The smallest algebraic interface is complete and exact. It kills precisely the closed relative line and retains the two-dimensional residue cokernel. Its status remains `formal_source_only`: no resolved/Rees or Cayley--Menger object has been identified with the generator, and no contour/readout authority follows. The next admissible action is geometric source identification, not further enlargement of the formal complex.
