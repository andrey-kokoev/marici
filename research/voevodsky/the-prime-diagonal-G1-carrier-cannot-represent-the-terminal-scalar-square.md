# The prime-diagonal G1 carrier cannot represent the terminal scalar square

## Local positive form

The retained G1 carrier preserves source prime idempotents and has

\[
G=\bigoplus_pG_p,
\qquad
G(P_px,P_qy)=0
\quad(p\neq q).
\]

This exact diagonality is essential to the accepted local construction.

## Terminal scalar polarization

The later evaluator has the form

\[
\varepsilon((z_p)_p)=\sum_pz_p.
\]

Its square is

\[
|\varepsilon(z)|^2
=
\sum_p|z_p|^2
+
\sum_{p\neq q}\overline{z_p}z_q.
\]

The second sum consists of cross-prime terms absent from the retained G1 norm.

Already for two real prime coordinates,

\[
\|(x,y)\|_{\oplus}^2=x^2+y^2,
\]

whereas

\[
|\varepsilon(x,y)|^2=(x+y)^2.
\]

At \((1,1)\), these values are two and four; at \((1,-1)\), they are two and zero.

Therefore the terminal scalar square is neither equal to nor determined positively by the prime-diagonal G1 form.

## Consequence for the common-carrier programme

The strict primitive/square carrier genuinely forces local Schwarz positivity within each labelled prime fibre. But it cannot simply be summed and then claimed to represent the global scalar-polarized Weil observer.

Doing so would require moving \(\varepsilon\) before polarization, exactly the construction order rejected by the G1.4 audit.

The missing form-preserving map

\[
L(q^*p)=\langle\iota(q),\iota(p)\rangle
\]

therefore needs a new source-authorized cross-prime coupling object. It cannot be obtained from the existing orthogonal direct sum alone.

## Exact next gate

A candidate global carrier must provide a kernel \(C_{pq}\) satisfying

\[
G_{m global}(x,y)
=
\sum_pG_p(x_p,y_p)
+
\sum_{p\neq q}C_{pq}(x_p,y_q),
\]

while preserving:

- source labels through construction;
- positive definiteness of the full block kernel;
- the terminal evaluator's exact polarization;
- cutoff naturality and completion;
- the coupled endpoint–gamma–prime identity.

No such cross-prime coherencer is currently constructed.

## Verification

```text
python research/voevodsky/checkers/check_prime_diagonal_carrier_terminal_square_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_prime_diagonal_carrier_terminal_square_no_go.py`
- `research/voevodsky/results/prime_diagonal_carrier_terminal_square_no_go.json`
