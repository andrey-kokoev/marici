# Theta bordered divisor has a canonical Krein realization

## Bounded question

After the Hilbert self-adjoint border fails, is there a canonical enlarged
geometry that preserves the theta bordered divisor without importing its
zeros?

## Real bordered polynomial

At a finite real theta compression, cancel the carrier poles from the
source-to-endpoint transfer and write the remaining bordered numerator as a
real monic polynomial

\[
p(z)=z^d+a_{d-1}z^{d-1}+\cdots+a_0.
\]

Its coefficients are derived from the finite carrier and the two labelled
ports. Let \(C_p\) be its companion matrix, so

\[
\det(zI-C_p)=p(z).
\]

This realization is coefficient-derived, but \(C_p\) is not generally
self-adjoint in the Euclidean metric.

## Canonical Hermite form

Let \(s_k\) be the Newton power sums determined recursively by the coefficients
of \(p\). Define the Hermite matrix

\[
\mathcal H_p=(s_{i+j})_{0\le i,j<d}.
\]

The companion action is symmetric for this form:

\[
\mathcal H_p C_p=C_p^T\mathcal H_p.
\]

Thus \(C_p\) is canonically self-adjoint in the possibly indefinite or
degenerate geometry carried by \(\mathcal H_p\). No root locations are needed
to construct the matrix or the form; Newton identities suffice.

## Signature theorem

The classical Hermite theorem gives:

- the rank of \(\mathcal H_p\) equals the number of distinct complex roots of
  \(p\);
- the signature of \(\mathcal H_p\) equals the number of distinct real roots
  of \(p\).

Every nonreal conjugate pair contributes one positive and one negative
direction. Repeated roots contribute degeneracy.

Consequently:

- \(\mathcal H_p>0\) exactly when all roots are real and simple;
- \(\mathcal H_p\ge0\) exactly when all roots are real, allowing
  multiplicities;
- an indefinite direction is a finite certificate for a nonreal conjugate
  pair.

## Meaning for the theta lane

The bordered cross-transfer divisor always has a canonical self-adjoint
realization, but generally in a Krein geometry rather than a Hilbert geometry.
Promoting it to Hilbert space is precisely the positivity theorem for
\(\mathcal H_p\).

This is not an RH proof. It identifies the exact metric whose positivity must
be explained without manufacturing an operator from known zeros.

The source-level target is now:

> Factor every finite theta Hermite form as a Gram matrix of labelled
> theta/Tate constructors, compatibly with cutoff completion.

Such a factorization would derive positivity from source relationships rather
than assert real-rootedness. A factorization obtained by diagonalizing
\(\mathcal H_p\) after its coefficients are aggregated would be tautological;
the Gram vectors must arise before scalar compression.

## Relation to the complete positivity tower

The Hermite forms provide a coefficient-space version of the earlier
generalized Laguerre and moment hierarchies. Both test whether a real entire
function belongs to a real-zero class, but they retain different coordinates:

- Laguerre forms compare derivatives at a spectral point;
- Hermite forms compare Newton sums of a finite bordered divisor;
- a source Gram factorization would explain both as shadows of one labelled
  positive correspondence.

Agreement between these tests is not independent evidence. Their value is
that the Hermite form exposes the minimal indefinite directions directly.

## Spin-two scope

For a declared real symmetric positive \(2\times2\) block, a labelled
anisotropy quadrature can recover cross-minor magnitude beyond spectral data,
as in Kitaev's spin-two compiler. The current bordered companion is not yet
such a block. That compiler becomes applicable only after a source-derived
symmetric-positive presentation is established.

## Completion gate

At increasing cutoffs \(X\), let \(\mathcal H_{p_X}\) be the finite Hermite
forms. Finite positivity alone is insufficient. A completed theorem requires:

1. compatible embeddings or a declared change-of-basis correspondence;
2. convergence in a source-authorized topology;
3. no negative direction escaping to increasing degree;
4. retention of multiplicity and sheet data;
5. a bridge from the completed form to the entire theta divisor.

## Result

The faithful bordered theta divisor has a canonical coefficient-derived Krein
realization. The missing Hilbert--Polya theorem is exactly the conversion of
its Hermite form from indefinite to positive by a source-labelled Gram
factorization. This is the first enlargement that preserves the correct
divisor, holomorphicity, and a genuine self-adjoint law simultaneously; what
remains unresolved is positivity of its metric.

## Sharp falsifier

For the first finite theta polynomial \(p_X\), compute
\(\mathcal H_{p_X}\) from coefficients alone. Any negative principal minor or
negative eigenvalue disproves the proposed finite source Gram factorization.
If every finite form is positive, incompatible cutoff maps or a collapsing
normalized reserve falsify completion stability.
