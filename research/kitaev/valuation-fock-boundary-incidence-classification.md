# Valuation/Fock-to-boundary incidence is incompatible on the literal four-label Adams module

> **Superseded before verification.** Strominger subsequently supplied the
> finite prime-power incidence
> \(I_k(p,k)=k^{-1}p^{-k/2}\delta_{k\log p}\). The live obstruction is no
> longer absence of finite \(P,Q\) coordinates; it is lifting this incidence
> through the rigged adelic trace correspondence. This draft was not ledgered
> and its checker was not used as evidence.

## Minimal source module

Let

\[
V_0=\operatorname{span}\{e_p,e_{p^2},e_q,e_{pq}\},
\qquad p\ne q.
\]

The required scalar current is

\[
\Lambda=(\log p,\log p,\log q,0).
\]

A minimal channel separation writes it as

\[
P=(\log p,0,\log q,0),
\qquad
Q=(0,\log p,0,0),
\qquad
\Lambda=P+Q.
\]

Thus primitive primes enter \(P\), the square \(p^2\) enters \(Q\), and
\(pq\) carries neither primitive nor square flux. These rows are independent.

## Finite Adams incompatibility

The literal demand for compatibility with every Adams operation cannot be
typed on \(V_0\). Although

\[
\psi^2(e_p)=e_{p^2}
\]

is present, the same operation requires

\[
\psi^2(e_q)=e_{q^2},
\qquad
\psi^2(e_{p^2})=e_{p^4},
\qquad
\psi^2(e_{pq})=e_{p^2q^2},
\]

and none of these targets lies in \(V_0\). Therefore the four-label module is
not an Adams module.

The first decisive result is

\[
\boxed{\text{finite incompatibility theorem for total Adams compatibility}.}
\]

The repair is not to invent missing columns. Grothendieck must either enlarge
the valuation domain to an Adams-stable source object or declare a partial
category whose admitted arrow is only \(e_p\mapsto e_{p^2}\).

## Classification after partialization

If only the displayed partial Adams arrow is retained, incidence exists but
is not unique. Let the boundary have endpoint functional \(\epsilon\) and a
nonzero kernel direction \(k\). If \(b_P\) is one primitive attachment, then

\[
b_P(t)=b_P+t k
\]

has the same endpoint value for every scalar \(t\). Channel separation and
the scalar \(\Lambda\)-readout do not remove this shear.

The checker realizes the exact family

\[
b_P(t)=(1,0,t),
\qquad b_Q=(1,1,0),
\qquad \epsilon=(1,0,0).
\]

Unless an authorized boundary equivalence identifies all such shears, or a
source reference fixes \(t\), the admissible attachments form an infinite
family—not a unique signature or finite torsor.

## Extended Gramian does not follow from incidence laws

For any candidate maps,

\[
\ker Q_{\rm extended}
=\ker Q_{\rm partial}\cap\ker\iota_P\cap\ker\iota_Q.
\]

Consequently incidence typing alone cannot prove injectivity. In the smallest
rank-one analytic fixture, adding the two independent \(P,Q\) rows yields
rank three on the four-dimensional module and leaves one exact kernel vector.
An actual full-rank \(K_X\), or another authorized constructor row, must close
that direction.

Finite injectivity would still not prove cutoff-independent continuity. The
compiler must additionally bound all generalized eigenvalues uniformly using
one fixed finite authorized family.

## Mandatory hostile cases

1. \(\iota_P=\iota_Q\) fails primitive/square channel separation.
2. Incidence depending only on \(\log n\) assigns \(2\log p\) to \(p^2\),
   violating \(\Lambda(p^2)=\log p\), and generally assigns flux to \(pq\).
3. Any nonzero primitive \(pq\) column violates the connected-composite
   exclusion.
4. Scaling the final attachment by \(1/X\) can make every cutoff injective
   while its least Gram eigenvalue tends to zero.
5. A new coordinate constructor at every cutoff supplies no fixed finite
   pro-Gram controller.
6. A bounded incidence can still violate
   \(\iota_P\psi^2=\psi^2_{\partial}\iota_P\).
7. A boundary-kernel reflection can preserve the scalar \(\Lambda\)-readout
   while reversing the required sheet character.

## Laws the future source map must prove

Before \(P_X,Q_X\) enter the common feature matrix, the source construction
must provide:

- an Adams-stable domain, or a precisely declared partial Adams category;
- primitive/square channel separation and zero primitive \(pq\) incidence;
- boundary actions intertwining every admitted Adams arrow;
- frozen sheet characters and equivariance of both maps;
- naturality under cutoff inclusions;
- compatibility with the already typed endpoint and seam carriers;
- kernel closure using one fixed finite authorized constructor family;
- cutoff-uniform domination constants;
- an authorized boundary equivalence or reference that classifies/removes
  endpoint-invisible shears.

## Boundary

This packet neither constructs the theta incidence formula nor selects a
boundary shear parameter. It proves that the literal minimal module cannot
support the requested total Adams law, and that the partial law alone leaves
continuous underdetermination.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_valuation_boundary_incidence_laws.py
```

The checker uses exact rational surrogate logarithmic weights, verifies the
current split, Adams closure failure, infinite shear family, extended-Gram
kernel, and all seven hostile cases.
