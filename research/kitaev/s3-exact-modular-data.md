# Exact modular data for `D(S3)`

Owner: `marici.Kitaev`

## Bounded question

Can the exact fusion-ring result be independently reconstructed from braid
invariants without choosing microscopic fusion bases and `F/R` gauges?

Yes.  The finite-group Fourier transform gives the modular `S` matrix from
centralizer characters, while the ribbon element gives the topological
spins.  Verlinde's formula then provides an independent reconstruction of
the fusion multiplicities.

## Frozen convention

Use label order `A,B,C,D,E,F,G,H` from the fusion packet.  For simple sectors
`i=(C,alpha)` and `j=(C',beta)`, sum over commuting flux representatives
`g in C`, `h in C'`:

\[
S_{ij}={1\over |S_3|}\sum_{gh=hg}
\overline{\chi_\alpha(q_g^{-1}h q_g)}
\overline{\chi_\beta(q_h^{-1}g q_h)}.
\]

All arithmetic is performed in `Q[omega]/(omega^2+omega+1)`.  Transporters
`q_g` are frozen explicitly by the checker; changing them conjugates within
the appropriate centralizer and leaves the characters unchanged.

## Exact result

The modular matrix is

\[
S=\begin{pmatrix}
1/6&1/6&1/3&1/2&1/2&1/3&1/3&1/3\\
1/6&1/6&1/3&-1/2&-1/2&1/3&1/3&1/3\\
1/3&1/3&2/3&0&0&-1/3&-1/3&-1/3\\
1/2&-1/2&0&1/2&-1/2&0&0&0\\
1/2&-1/2&0&-1/2&1/2&0&0&0\\
1/3&1/3&-1/3&0&0&2/3&-1/3&-1/3\\
1/3&1/3&-1/3&0&0&-1/3&-1/3&2/3\\
1/3&1/3&-1/3&0&0&-1/3&2/3&-1/3
\end{pmatrix}.
\]

It is symmetric and unitary.  Its first row is `d_i/6`, so the total
quantum dimension is six.  The twists are

\[
(\theta_A,\ldots,\theta_H)=(1,1,1,1,-1,1,\omega,\omega^2).
\]

With diagonal `T` made from these twists, the exact modular relation

\[
(ST)^3=S^2
\]

holds.  The Gauss sum `sum_i d_i^2 theta_i=6` equals the total quantum
dimension, as expected for the nonchiral double.

Verlinde's formula produces nonnegative integral multiplicities, maximum
one, and independently recovers such witnesses as

\[
C^2=A+B+C,\quad
D^2=A+C+F+G+H,\quad
DE=B+C+F+G+H,\quad
FG=C+H.
\]

## Verification

`python research/kitaev/checkers/check_s3_modular_data.py` performs exact
cyclotomic arithmetic and passes seven aggregate gates: construction of
`S`, symmetry/unitarity, exact spins, the modular-group relation, Gauss sum,
Verlinde reconstruction, and the explicit gauge-boundary assertion.  Fresh
stdout matches `research/kitaev/results/s3-modular-data.json` after newline
normalization.

## Claim boundary

The pair `(S,T)` records closed-link and twist invariants and determines the
fusion ring here through Verlinde.  It does not select bases of trivalent
fusion spaces, microscopic ribbon intertwiners, `F` symbols, or channel-wise
`R` symbols.  Modular data is therefore a strong consistency boundary, not
a substitute for pentagon/hexagon verification.  No uniqueness claim for a
braided category from `(S,T)` is made.

Primary basis: [Koornwinder--Schroers--Slingerland--Bais](https://arxiv.org/abs/math/9904029)
prove the finite-group Fourier-transform and Verlinde relation; the physical
quantum-double setting is [Kitaev](https://arxiv.org/abs/quant-ph/9707021).

## Falsifiers

Any failure of symmetry or unitarity, a first row unequal to `d_i/6`, a
failure of `(ST)^3=S^2`, a Gauss sum other than six, or a Verlinde coefficient
that disagrees with the independently derived character-coproduct fusion ring
falsifies the packet.
