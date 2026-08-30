# Theta logarithmic moment tower observes finite packets, but prime transport preserves their divisor

## Status

Exact finite-packet theorem. Iterating logarithmic scale degree produces a
complete moment observer on every finite labelled packet. Nevertheless prime
transport acts on these moments by triangular translation and preserves the
first nonzero moment.

Equivalently, prime multiplication changes the associated exponential
polynomial only by a nonvanishing factor. It preserves zero order and leading
residue. The logarithmic tower supplies observability of cancellation, not a
mechanism that removes or orients it.

## Moment observer

On the finite arithmetic module let

\[
Le_n=(\log n)e_n,
\qquad
\varepsilon(e_n)=1.
\]

For a finite packet

\[
v=\sum_{j=1}^r a_je_{n_j},
\]

with distinct labels (n_j), define its logarithmic moments

\[
\mu_k(v)=\varepsilon L^kv
=\sum_{j=1}^r a_j(\log n_j)^k.
\]

The first (r) moments form the Vandermonde system

\[
\begin{pmatrix}
\mu_0\\
\mu_1\\
\vdots\\
\mu_{r-1}
\end{pmatrix}
=
\begin{pmatrix}
1&1&\cdots&1\\
\log n_1&\log n_2&\cdots&\log n_r\\
\vdots&\vdots&&\vdots\\
(\log n_1)^{r-1}&(\log n_2)^{r-1}&\cdots&(\log n_r)^{r-1}
\end{pmatrix}
\begin{pmatrix}
a_1\\a_2\\\vdots\\a_r
\end{pmatrix}.
\]

Its determinant is

\[
\prod_{i<j}(\log n_j-\log n_i),
\]

which is nonzero. Hence

\[
\mu_0(v)=\cdots=\mu_{r-1}(v)=0
\]

forces (v=0). The moment tower is a complete finite-packet observer.

## Prime transport is triangular on moments

For (T_pe_n=e_{pn}), the commutator identity gives

\[
LT_p=T_p(L+(\log p)I).
\]

Therefore

\[
L^kT_p=T_p(L+(\log p)I)^k
\]

and, since \(\varepsilon T_p=\varepsilon\),

\[
\mu_k(T_pv)
=
\sum_{j=0}^k
\binom{k}{j}
(\log p)^{k-j}\mu_j(v).
\]

The transport matrix on the moment vector is upper triangular with diagonal
entries one.

If

\[
\mu_0(v)=\cdots=\mu_{d-1}(v)=0,
\qquad
\mu_d(v)\neq0,
\]

then

\[
\mu_j(T_pv)=0
\quad (j<d),
\qquad
\mu_d(T_pv)=\mu_d(v).
\]

Prime transport preserves both the cancellation order and its leading
logarithmic residue.

## Exponential-polynomial form

Package the moments into

\[
F_v(z)=\varepsilon e^{zL}v
=\sum_{j=1}^r a_jn_j^z.
\]

Then

\[
F_v^{(k)}(0)=\mu_k(v).
\]

Prime transport satisfies

\[
F_{T_pv}(z)=p^zF_v(z).
\]

Since (p^z) is an entire nonvanishing unit, it cannot create, remove, or move
the divisor of (F_v). At (z=0) it preserves the zero multiplicity and the
first nonzero Taylor coefficient.

This is the divisor-level version of the augmentation-ideal no-go.

## Reciprocal parity

On a rationally enlarged label module, reciprocal reflection sends

\[
e_n\longmapsto e_{1/n}.
\]

It reverses logarithmic degree:

\[
L\longmapsto-L.
\]

Consequently

\[
\mu_k\longmapsto(-1)^k\mu_k.
\]

The first nonzero moment therefore carries an exact reflection parity. But
parity is not positivity: even residues retain their sign, and odd residues
reverse without selecting which orientation is admissible.

## Finite examples

For the two-label cancellation packet

\[
v=e_m-e_n,
\]

we have

\[
\mu_0(v)=0,
\qquad
\mu_1(v)=\log(m/n)\neq0.
\]

Every prime transport preserves this leading residue.

For three distinct labels, coefficients can be chosen so that

\[
\mu_0(v)=\mu_1(v)=0,
\qquad
\mu_2(v)\neq0.
\]

Prime transport again preserves the first nonzero moment. Higher cancellation
order therefore does not evade the theorem.

## Completion obstruction

Finite observability does not imply observability after completion. A completed
nonzero packet might have all logarithmic moments zero if:

- the augmentation or powers of (L) fail to extend;
- finite packets converge to a flat vector in the projective moment topology;
- the infinite label sum permits moment indeterminacy;
- a boundary-at-infinity functional survives outside every algebraic moment.

Grothendieck's beyond-all-orders band result makes the last possibility
structurally live. The completion must therefore retain a nonperturbative
boundary observable in addition to the entire algebraic moment tower.

## Consequence

The labelled constructor architecture now has a precise division:

- augmentation detects scalar cancellation;
- logarithmic moments determine every finite packet;
- prime transport preserves the divisor filtration;
- reciprocal reflection supplies parity but not orientation;
- only a modular completion current outside ordinary transport can change or
  constrain the divisor.

Any proposal that uses only prime multiplication, its powers, and logarithmic
moments can classify a zero packet but cannot eliminate it. The next RH-bearing
operation must act nontrivially on the divisor filtration while remaining
source-derived and failing on hostile even sources.
