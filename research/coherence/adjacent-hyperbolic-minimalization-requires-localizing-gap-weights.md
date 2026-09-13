# Adjacent hyperbolic minimalization requires localizing gap weights

## Distinguish two theorems

The chain Pfaffian and cofactor identities are polynomial. They hold over any commutative ring.

The stronger congruence

\[
M\cong H(x_0)\oplus H(x_2)\oplus\cdots
\]

uses elimination coefficients containing inverses of selected gap weights. It therefore requires those weights to be units, or passage to a localization where they become units.

## Integral hostile

Over \(\mathbb Z\), take the three-point chain with gaps \(2,3\):

\[
M=
\begin{pmatrix}
0&2&6\\
-2&0&3\\
-6&-3&0
\end{pmatrix}.
\]

The first invariant of an integral alternating form is the gcd of its upper-triangular entries:

\[
\gcd(2,6,3)=1.
\]

Consequently its unimodular alternating normal form begins with \(H(1)\), not \(H(2)\). A unimodular congruence to

\[
H(2)\oplus0
\]

is impossible.

The standard adjacent elimination already exposes the problem: it requires the coefficient

\[
\frac{3}{2}.
\]

After localizing at \(2\), the adjacent reduction becomes available.

## Correct scope split

### Ring-generic

- Pfaffian polynomial cancellation;
- odd cofactor kernel equations;
- alternating incoming/outgoing charge fold;
- arbitrary odd--odd torsion sewing as a polynomial identity.

### Unit-dependent

- decomposition into the specifically weighted adjacent hyperbolic blocks;
- contractibility of every selected pair;
- inverses appearing in paired refinement inside an existing pair;
- determinant-one triangular minimalization with those prescribed pivots.

## Formalization consequence

The current Agda modules correctly prove polynomial identities over an arbitrary commutative ring. A future arbitrary-size matrix minimalization theorem must introduce an explicit unit witness for every selected even-indexed gap, or formulate its conclusion after localization.

It must not state the adjacent hyperbolic normal form over a bare commutative ring.

## Torsion interpretation

Before localization, a nonunit pair weight is not contractible. Its cokernel retains arithmetic torsion. Thus “contractible pair plus scalar torsion certificate” is valid only in a target where the pair differential has been inverted or where determinant data is separated from integral homology.

This adds a fourth required distinction:

```text
polynomial Pfaffian identity
integral alternating normal form
localized contractible decomposition
retained torsion certificate
```

## Verification

```text
python research/coherence/check_integral_chain_congruence_localization_obstruction.py
```

Artifacts:

- `check_integral_chain_congruence_localization_obstruction.py`
- `integral-chain-congruence-localization-obstruction.v1.json`
