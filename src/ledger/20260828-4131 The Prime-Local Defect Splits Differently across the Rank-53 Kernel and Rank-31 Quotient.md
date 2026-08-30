# 4131 — The Prime-Local Defect Splits Differently across the Rank-53 Kernel and Rank-31 Quotient

## Claim

Reduce the canonical good-prime sequence

\[
0\longrightarrow K_{53}
\longrightarrow F_{84}
\longrightarrow L_{31}
\longrightarrow0
\]

at the exceptional primes \(2,3,5\).

The dimensions become:

| \(p\) | \(\dim F_p\) | \(\dim L_p\) | \(\dim K_p\) |
|---:|---:|---:|---:|
| generic tested | 84 | 31 | 53 |
| 2 | 143 | 90 | 53 |
| 3 | 250 | 167 | 83 |
| 5 | 209 | 133 | 76 |

Hence the excess decomposes as:

| \(p\) | Lower excess | Kernel excess | Total |
|---:|---:|---:|---:|
| 2 | 59 | 0 | 59 |
| 3 | 136 | 30 | 166 |
| 5 | 102 | 23 | 125 |

## Derivation

The lower projection uses 2,158 active lower columns. Its ranks are

\[
2068, 1991, 2025
\]

at \(p=2,3,5\), giving lower quotient dimensions

\[
90, 167, 133.
\]

Subtracting these from the full quotient dimensions gives the relative-kernel dimensions.

## Interpretation

The arithmetic obstruction is layered.

At \(p=2\), the rank-53 relative barcode kernel remains unchanged. The entire defect lies in the lower projected quotient.

At \(p=3\) and \(p=5\), the lower quotient still carries most of the defect, but the relative kernel also enlarges:

\[
K_{53}\rightsquigarrow K_{83}
\quad(p=3),
\]

\[
K_{53}\rightsquigarrow K_{76}
\quad(p=5).
\]

Thus no single undifferentiated torsion label describes the integral lift. The primes act on different layers of the exact sequence.

## Qualification

These are exact modular dimensions and exact-sequence differences. Calling the excesses complete Smith multiplicities remains conditional on proving the characteristic-zero rank is exactly 2,194.

## Next falsifier

Perform prime-power lifting separately on:

- \(L\) at \(p=2,3,5\);
- \(K\) at \(p=3,5\).

The \(p=2\) kernel requires no higher audit unless a prime-power connecting morphism reintroduces it.

## Durable artifact

`research/benincasa/results/interaction-net-integral-residual-prime-local-sequence.json`

Sequence claim: `seqclaim-4c7668fafa5f5ba7386a19eb`.
