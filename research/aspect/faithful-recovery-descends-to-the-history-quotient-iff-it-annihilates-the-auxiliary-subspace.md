# Faithful recovery descends to the history quotient exactly when it annihilates the auxiliary subspace

## Question

Can the existing faithful labelled incidence and recovery certify the two-endpoint quotient map without evaluating the full shortened Gram?

## Descent criterion

Let

\[
I:E\longrightarrow H,
\qquad
R:H\longrightarrow E,
\qquad
RI=I_E,
\]

be the source incidence and its continuous recovery. Let \(N\subset H\) be the closed auxiliary history subspace and \(q:H\to H/N\) the quotient.

A map

\[
\overline R:H/N\longrightarrow E,
\qquad
\overline R(qh)=Rh,
\]

is well-defined exactly when

\[
R(N)=0.
\]

When this condition holds,

\[
\overline R\,qI=RI=I_E.
\]

Therefore \(qI\) is injective. Restricted to the two-endpoint plane, this proves the no-dark-endpoint condition and hence strict positivity of the shortened determinant.

## Quantitative consequence

With quotient norm

\[
\lVert qh\rVert=\operatorname{dist}(h,N),
\]

boundedness of \(\overline R\) gives

\[
\lVert qIx\rVert
\ge
\frac{1}{\lVert\overline R\rVert}\lVert x\rVert.
\]

Thus a prime-uniform bound on the descended recovery norm supplies the required uniform quotient angle and determinant margin.

## Necessity for this recovery route

If some \(n\in N\) has \(Rn\ne0\), then \(h\) and \(h+n\) represent the same quotient class but recover different source vectors. The proposed \(\overline R\) is not defined. Faithfulness of \(I\) before quotienting does not repair this failure.

This does not prove that \(qI\) is noninjective; it proves that the existing recovery cannot certify injectivity until its action on \(N\) is typed.

## Current source readback

The repository proves \(RI=I_E\) for the labelled theta incidence. It does not identify the actual completed auxiliary/Green subspace \(N\), and therefore does not establish either \(R(N)=0\) or a prime-uniform bound for the descended recovery. Existing radical-descent work explicitly distinguishes the faithful incidence kernel from the undeclared G4 Green radical.

## Hostile finite model

Take \(H=\mathbb C^2\), \(E=\mathbb C\), \(I(x)=(x,0)\), and \(R(a,b)=a+b\). Then \(RI=I_E\). For \(N=\operatorname{span}\{(0,1)\}\), one has \(R(N)\ne0\), so recovery does not descend even though \(qI\) remains injective. This separates pre-quotient faithfulness from recovery-based quotient certification.

## Disposition

The no-dark-endpoint quotient map has a sharp source acceptance test: identify the completed auxiliary subspace \(N\), prove \(R(N)=0\), and bound the descended recovery uniformly. Without that typed subspace, the existing left inverse cannot be transported through the quotient.
