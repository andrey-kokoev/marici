# Heat-sandwiched seam is trace class, but its determinant is regulator data

## 1. Source completion

Let \(A_\Phi\ge0\) be the completed theta source's Friedrichs generator on
\(\mathcal H_\Phi\), as typed by the generic completion packet. Assume its
heat operator is trace class for every \(t>0\):

\[
  e^{-tA_\Phi}\in\mathcal S_1.
\]

Let \(C_a=P-T_aPT_a^{-1}\) be the bounded moving-seam projection cocycle.
Define its heat-sandwiched compression

\[
  C_{a,t}
  =
  e^{-tA_\Phi/2}C_a e^{-tA_\Phi/2}.
\]

## 2. Exact trace-class gate

Because \(e^{-tA_\Phi/2}\) is Hilbert--Schmidt and \(C_a\) is bounded,
\(C_{a,t}\) is trace class. The ideal estimate gives

\[
  \|C_{a,t}\|_1
  \le
  \|C_a\|\,
  \|e^{-tA_\Phi/2}\|_2^2
  =
  \|C_a\|\operatorname{Tr}(e^{-tA_\Phi}).
\]

Therefore the Fredholm determinant

\[
  D_{a,t}(\lambda)
  =
  \det\bigl(I+\lambda C_{a,t}\bigr)
\]

exists for every \(t>0\).

This resolves compactness at a fixed positive heat scale without choosing a
finite spectral cutoff.

## 3. What the theorem does not select

The family \(D_{a,t}\) depends on \(t\). As \(t\downarrow0\),
\(C_{a,t}\) approaches the noncompact seam operator only strongly, not in
trace norm. Its trace norm is controlled by a heat trace that generally
diverges in the ultraviolet.

Consequently there is no automatic unregularized determinant:

\[
\boxed{
\text{source heat flow gives Fredholm typing at }t>0,
\quad
\text{not a canonical }t=0\text{ determinant}.}
\]

Selecting one convenient \(t\), subtracting heat coefficients, or taking a
finite part requires additional authority.

## 4. The self-dual heat scale

The theta vacuum has a distinguished Fourier self-dual Gaussian scale. This
can nominate a dimensionless heat point, conventionally \(t=1\), after Haar
and Fourier normalizations are fixed.

But self-duality alone is insufficient. Hostile self-Fourier carriers also
possess a fixed heat scale and can produce heat-sandwiched determinants.
Hence \(t=1\) removes one regulator ambiguity without proving that

\[
  D_{a,1}(\lambda)
\]

is \(X(z)\), or that its divisor has RH orientation.

## 5. Determinant mismatch gate

The determinant must be derived in the direction

\[
  (A_\Phi,C_a,\text{modular transport})
  \longrightarrow
  D(z)
  \longrightarrow
  X(z).
\]

At minimum one must compute its infinitesimal logarithm:

\[
  \partial_a\log D
  =
  \operatorname{Tr}
  \left[
  (I+\lambda C_{a,t})^{-1}
  \lambda\,\partial_aC_{a,t}
  \right],
\]

and show that the trace produces the labelled moving-seam current with all
endpoint and modular terms. Matching only after choosing \(\lambda(z)\) from
\(X\) is the universal rank-one/determinant tautology in a larger disguise.

## 6. Reopen criterion

Heat compression becomes RH-relevant only if the completed source proves:

1. a unique heat scale or a regulator-independent relative determinant;
2. covariance under rational scale and Fourier quarter-turn;
3. the exact theta seam logarithmic derivative before scalar integration;
4. a hostile self-Fourier source fails one of these laws; and
5. the resulting determinant is a transition section of a maximal
   self-adjoint boundary pair.

Absent those items, heat sandwiching is a useful operator-class theorem and
nothing more.

## 7. Scope

The trace-class estimate and existence of \(D_{a,t}\) are exact under the
stated heat-trace hypothesis. The theta completion packet supplies the
candidate generator but does not itself prove the determinant comparison.
No regulator-independent determinant, identity with \(X\), boundary
maximality, or RH result is claimed.
