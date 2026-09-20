# Adjacent-prime transport requires the signed ratio window

## Question

Can two ordered prime seam attachments be compared by a two-port permutation, or does source interval composition force an additional comparison coordinate?

## Source operation and type

For `L_p<L_q`, the order `(p,q)` cuts the total interval at `L_p`, while `(q,p)` cuts it at `L_q`. Their common refinement has three typed pieces:

\[
I_1=[0,L_p),\qquad
I_2=[L_p,L_q),\qquad
I_3=[L_q,L_p+L_q).
\]

The middle piece has signed length

\[
L_q-L_p=\log(q/p).
\]

It is a comparison stratum, not an integer-labelled source state.

## Transport matrices

On common-refinement coordinates `(x,y,z)`, the two ordered two-port readouts are

\[
P_{pq}(x,y,z)=(x,y+z),
\]

\[
P_{qp}(x,y,z)=(x+y,z).
\]

Both have the same total scalar window:

\[
x+y+z.
\]

Scalar endpoint agreement therefore does not construct transport between the ordered packets.

## Finite falsifier

Take the signed ratio-window state

\[
h=(0,1,-1).
\]

Then

\[
P_{pq}h=(0,0),
\qquad
P_{qp}h=(1,-1).
\]

If a two-port map `M` satisfied `P_qp=M P_pq`, every vector in `ker P_pq` would lie in `ker P_qp`. The displayed state disproves that inclusion. Hence no two-port permutation or linear adapter can implement the adjacent swap.

The exact checker also verifies that both ordered packets retain the same total interval readout. The residual is therefore specifically the signed ratio window, not a mismatch of total support.

## Claim boundary

The minimal adjacent-prime transport object is the three-piece common refinement with its signed middle coordinate. This is a finite-cutoff source-typed obstruction theorem.

It does not establish:

- braid coherence for three primes;
- determinant-line transport of the ratio window;
- compatibility with the order-three anomaly;
- completion over all prime words.

## Disposition

The two-port transport rival is falsified. Any endpoint–Euler clutching cell must retain the ratio-window coherencer before scalar summation or determinant formation.

Verification:

- `research/nima/checkers/check_adjacent_prime_ratio_window_transport.py`
- `research/nima/results/adjacent-prime-ratio-window-transport.json`
