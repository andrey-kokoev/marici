# Even amplitudes act on odd Pfaffian state lines

## Module identity

Let an ordered chain be split contiguously into an even block \(E\) and an odd block \(O\). Let

\[
\operatorname{cof}(M)_i=(-1)^i\operatorname{Pf}(M_{\widehat i})
\]

be the canonical odd cofactor state of the union.

Restriction to the odd block satisfies

\[
\boxed{
\operatorname{res}_O\operatorname{cof}(E\cup O)
=
\operatorname{Pf}(E)\operatorname{cof}(O).
}
\]

The same identity holds when the odd block precedes the even block.

## Proof

Delete a position \(i\) belonging to \(O\). The remaining configuration consists of two contiguous even blocks:

- the original block \(E\);
- the block \(O\setminus\{i\}\).

Even-cut factorization gives

\[
\operatorname{Pf}((E\cup O)_{\widehat i})
=
\operatorname{Pf}(E)
\operatorname{Pf}(O_{\widehat i}).
\]

Because \(|E|\) is even, shifting the local odd-block index by \(|E|\) introduces no additional cofactor sign. This proves the formula.

## Meaning

Even configurations act as scalars on odd boundary states:

\[
Z(E)\cdot\psi_O
=
\psi_{E\cup O}\big|_O.
\]

The full cofactor vector may also have components supported in \(E\); those record extensions of the odd state across the sewing interface. But the retained odd boundary line transforms by the scalar even amplitude exactly.

Together with the previous laws:

\[
\text{even}\otimes\text{even}\to\text{even},
\]

\[
\text{even}\otimes\text{odd}\to\text{odd},
\]

\[
\text{odd}\otimes\text{odd}\to\text{even},
\]

we obtain a \(\mathbb Z_2\)-graded sewing algebra.

## Emerging kind

On contiguous ordered configurations, the structure now has:

- a unit from the empty configuration;
- associative even multiplication;
- an odd state module;
- a pairing of two odd states into an even amplitude;
- Koszul orientation under permutation.

This is precisely the finite algebraic profile of a one-dimensional fermionic factorization algebra. Calling it a full field theory still requires compatibility with arbitrary refinements and the analytic Green fibers, but the parity sewing operations are no longer conjectural.

## Verification

The checker verifies 256 exact-rational left and right module restrictions with even block sizes zero through six and odd sizes one through seven:

```text
python research/coherence/check_even_odd_pfaffian_module.py
```

Artifacts:

- `check_even_odd_pfaffian_module.py`
- `even-odd-pfaffian-module.v1.json`
