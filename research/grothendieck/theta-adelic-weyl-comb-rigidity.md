# Adelic Weyl rigidity selects the rational comb, not yet the Dirac boundary

## 1. Question

After ordinary tangent linearization collapses the rational adelic lattice,
does the exponentiated Weyl formulation remain noncanonical?

Two standard rigidity mechanisms answer a substantial part of this question:

1. Stone--von Neumann uniqueness for the Heisenberg representation with fixed
   central character; and
2. uniqueness of the rational-comb distribution under the two rational Weyl
   polarizations.

## 2. Canonical ambient representation

Fix the standard global additive character

\[
  \psi_{\mathbb A}:\mathbb A/\mathbb Q\longrightarrow\mathbb T.
\]

On \(L^2(\mathbb A)\), translations and modulations act by

\[
  (T_qf)(x)=f(x+q),
  \qquad
  (M_pf)(x)=\psi_{\mathbb A}(px)f(x).
\]

They generate the adelic Schrödinger representation of the Heisenberg group.
The locally compact abelian form of the Stone--von Neumann theorem makes the
irreducible regular representation with this nontrivial central character
unique up to unitary equivalence. Thus the exponentiated carrier is not an
arbitrary choice once \(\psi_{\mathbb A}\) and the Haar normalization are
fixed.

For \(p,q\in\mathbb Q\), the product formula gives

\[
  \psi_{\mathbb A}(pq)=1,
\]

so rational translations and rational modulations commute.

## 3. Joint fixed distribution

Let \(\mathcal S(\mathbb A)\) be the Bruhat--Schwartz space and
\(\mathcal S'(\mathbb A)\) its distributional dual. Suppose
\(\Theta\in\mathcal S'(\mathbb A)\) satisfies

\[
  T_q\Theta=\Theta,
  \qquad
  M_p\Theta=\Theta
  \qquad(p,q\in\mathbb Q).
\]

Translation invariance makes \(\Theta\) a distribution on the compact
quotient \(\mathbb A/\mathbb Q\). Its Fourier modes are indexed by the dual
group

\[
  \widehat{\mathbb A/\mathbb Q}\cong\mathbb Q.
\]

Write the corresponding distributional Fourier coefficients as \(c_r\),
\(r\in\mathbb Q\). Modulation by \(p\) translates the Fourier index:

\[
  c_r\longmapsto c_{r-p}.
\]

Invariance under every \(p\in\mathbb Q\) therefore forces

\[
  c_r=c_0
  \qquad(r\in\mathbb Q).
\]

The distribution with every Fourier coefficient equal to one is the delta
mass at the identity of \(\mathbb A/\mathbb Q\). Lifted to \(\mathbb A\), it
is the rational comb

\[
  \Delta_{\mathbb Q}=\sum_{q\in\mathbb Q}\delta_q.
\]

Consequently,

\[
\boxed{
  \{\Theta:T_q\Theta=M_p\Theta=\Theta\ \forall p,q\in\mathbb Q\}
  =\mathbb C\,\Delta_{\mathbb Q}.}
\]

This is a faithful sense in which the two complementary localizations select
one relative object: neither polarization alone selects the comb, while
their joint fixed condition does.

## 4. The ninety-degree rotation

Adelic Fourier transform implements the metaplectic quarter-turn

\[
  T_q\longleftrightarrow M_{-q}.
\]

It preserves the one-dimensional joint fixed line, hence

\[
  \mathcal F_{\mathbb A}\Delta_{\mathbb Q}
  =c\,\Delta_{\mathbb Q}.
\]

Self-dual Haar normalization fixes \(c=1\). Poisson summation is therefore
the scalar shadow of invariance of the unique joint fixed distribution under
the quarter-turn.

This realizes the operator's proposed conceptual rotation exactly:

\[
\boxed{
\text{two polarization actions}
\to
\text{one joint fixed distribution}
\to
\text{theta/Poisson scalar readout}.}
\]

## 5. What has been gained

The hostile ambiguity has narrowed:

- the ambient regular irreducible Weyl representation is fixed up to unitary
  equivalence;
- the arithmetic boundary distribution is fixed up to normalization by the
  two rational polarization actions; and
- Fourier sewing fixes that normalization under self-dual measure.

A hostile scalar multiplier cannot alter this joint fixed line while
remaining merely a change of Weyl presentation.

## 6. What remains missing

The rational comb is a distribution, not an \(L^2\) boundary vector. Joint
fixedness does not automatically produce:

1. a boundary trace for the logarithmic Dirac operator;
2. a closed linear relation in a Hilbert boundary space;
3. maximal self-adjointness of that relation; or
4. a relative determinant equal to \(X(z)\).

Most importantly, Stone--von Neumann uniqueness controls the Heisenberg
carrier, not the choice of a Dirac generator or its self-adjoint extension.
The RH-bearing ambiguity has moved from the representation to the
representation-to-generator passage.

## 7. Next falsifier

Hold the Schrödinger representation and \(\Delta_{\mathbb Q}\) fixed. Construct
two inequivalent self-adjoint generators or Cayley boundary relations that
both implement the same rational Weyl actions and Poisson quarter-turn. If
they yield different relative determinants, Weyl rigidity alone cannot
select the RH operator.

Conversely, a source-derived covariance law that uniquely selects the
logarithmic dilation generator and its graph boundary would close the next
gate without reference to zeros.

## 8. Scope

The joint-fixed-line calculation is exact Fourier analysis on
\(\mathbb A/\mathbb Q\). Stone--von Neumann uniqueness is invoked for the
regular irreducible Heisenberg representation with fixed central character.
No Dirac boundary trace, self-adjoint extension, determinant identity, or RH
claim follows here.
