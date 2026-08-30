# Binary selector rank and the correlation matroid

## Affine selector model

Suppose \(k\) binary constructor choices are driven by \(r\) admitted
selector bits:

\[
y=As+b
\qquad\text{over }\mathbb F_2,
\]

where \(s\in\mathbb F_2^r\) and \(y\in\mathbb F_2^k\). The reachable joint
selector orbit is

\[
b+\operatorname{im}A.
\]

Therefore

\[
\boxed{
|\mathcal O_{\rm reachable}|=2^{\operatorname{rank}_{\mathbb F_2}A}.
}
\]

All \(2^k\) joint combinations are available exactly when
\(\operatorname{rank}A=k\).

## Correlation witnesses

If \(\operatorname{rank}A<k\), there is a nonzero vector
\(h\in\ker A^T\). It gives an invariant parity relation

\[
h\cdot y=h\cdot b
\]

for every reachable output. This is the smallest machine-readable witness
that some nominal choices are correlated.

For two outputs driven by one shared bit,

\[
A=\begin{pmatrix}1\\1\end{pmatrix},\qquad b=0.
\]

The rank is one, the reachable orbit has size two, and \(h=(1,1)\)
certifies \(y_1+y_2=0\). The missing combinations are exactly those with
odd parity.

## Matroid structure

The rows of \(A\) define a representable matroid on the constructor choices.

- Independent row sets are jointly selectable.
- Circuits are minimal correlated selector sets.
- Rank gives the number of independent choice dimensions.
- Deleting a selector column models loss of one source distinction.
- Adding a source-authorized selector column may increase rank by at most
  one.

This gives a bounded compiler audit without enumerating all \(2^k\)
combinations.

## Authority boundary

Matrix rank only measures distinguishability. It does not authorize:

- the selector bits;
- the affine interpretation \(A,b\);
- the candidate gadgets or capabilities;
- independence of selector fault roots;
- temporal reuse or replay behavior.

Every column needs a source authority root and fault-domain declaration.
Two syntactically separate columns governed by one common cause may be
linearly independent as values while still failing the fault audit.

## Cross-sector consequences

- **Strominger.** A DPC compiler can attach an affine selector matrix to a
  family of binary capability choices. Left-nullspace circuits become exact
  joint-selector-correlation witnesses.
- **Kitaev.** Shared predicate pointers across C/F/G/H create row
  dependencies. Selector rank distinguishes independently controllable
  gadget choices from nominal choices tied by one pointer.
- **Arithmetic/RH.** Binary probe or minor choices generated from shared
  gauges may have full marginal support but deficient joint rank. A
  two-copy kernel requires joint probe rank, not repeated one-copy checks.
- **Benincasa.** External binary controls may generate fewer independent
  period directions than their marginal responses suggest; left-nullspace
  relations expose the correlated control combinations.

## Finite gate

The compiler returns selector rank, required joint rank, reachable orbit
size, left-nullspace circuits, and the source-root partition. It accepts
joint distinguishability only when the required rank is met. Authority and
fault checks remain separate mandatory gates.

## Durable statement

> For affine binary selectors, joint constructor freedom is a matroid rank,
> not a count of locally varying outputs. Left-nullspace circuits are finite
> correlation falsifiers.

