# Theta full-germ detector is not uniformly faithful on discrete labels

## Finite faithfulness versus closed range

Packet 181 proves that every finite family of distinct theta translates is
linearly independent.  That does not imply a cutoff-independent lower bound
when the coefficient module remembers exact integer labels.

The adjacent labels give an exact hostile sequence.

## Adjacent logarithmic packet

Put

\[
 q_n=\log n,
 \qquad
 d_n=q_{n+1}-q_n=\log(1+1/n)\longrightarrow0,
\]

and take the coefficient packet

\[
 c_n=e_{n+1}-e_n.
\]

Its seam germ is

\[
 F_n(t)=\Phi(t+q_{n+1})-\Phi(t+q_n).
\]

For every compact interval `[0,R]` and every derivative order `m`, the mean
value theorem gives

\[
 \sup_{0\le t\le R}|F_n^{(m)}(t)|
 \le d_n
 \sup_{q_n\le u\le q_{n+1}+R}|\Phi^{(m+1)}(u)|.
\]

The completed theta kernel and all its derivatives decay
super-exponentially on the positive ray. Therefore

\[
 \boxed{
 \sup_{0\le t\le R}|F_n^{(m)}(t)|\longrightarrow0}
\]

for every fixed `R,m`.

Thus `F_n` tends to zero in the standard compact-open `C^infinity` germ
topology, and likewise in every source germ topology for which positive
translations act strongly continuously and these seminorms are continuous.

## No lower frame bound against a discrete label norm

For any diagonal arithmetic norm

\[
 \|c\|_w^2=\sum_nw_n|c_n|^2
\]

with adjacent weights bounded below,

\[
 \|c_n\|_w^2=w_n+w_{n+1}\not\longrightarrow0.
\]

But its full germ tends to zero. Hence there is no constant `A>0` such that

\[
 A\|c\|_w^2
 \le
 \left\|\sum_kc_k\Phi(\,\cdot+\log k)\right\|_{\rm germ}^2
\]

uniformly over finite packets.

Equivalently, the full-germ synthesis is injective on the algebraic source
module but has nonclosed range relative to any such discrete coefficient
completion.

## Exact interpretation

The two conclusions are compatible:

\[
 \boxed{
 \text{finite germ faithfulness}
 \ne
 \text{completion-stable observability}.}
\]

The analytic germ sees nearby logarithmic shifts as nearby preparations. The
arithmetic source may still distinguish `n` and `n+1` through divisibility,
prime-power type, or Fock occupation.  Therefore neither topology can silently
replace the other.

The faithful completed carrier must be hybrid:

\[
 \mathcal H_{\rm full}
 =\mathcal H_{\rm germ}
 \oplus
 \mathcal H_{\rm discrete\ type},
\]

or a nontrivial extension carrying the same information.  The second port is
required only for source-authorized arithmetic constructors which fail to
descend continuously to the germ quotient.

## Consequence for a determinant--kernel bridge

Adding a silent discrete register does not solve RH. The scalar Tate readout
still factors through the analytic germ and can vanish while the discrete
component remains nonzero.  A genuine determinant--kernel theorem must couple
the type register into the source operator or boundary complex.  Otherwise it
only proves that the full state survives while its physical scalar projection
vanishes—the exact situation we are trying to explain.

The next construction must therefore answer:

\[
 \boxed{
 \text{Which source differential couples exact arithmetic type to the
 Poisson-seam germ?}}
\]

Positive Fock formation and the valuation/Adams operations are the available
source constructors; the coupling cannot be introduced merely to restore a
lower bound.

## Scope

This packet proves failure of uniform observability in compact-open smooth
germ topology and any compatible strongly translation-continuous topology.
It does not rule out a stronger source topology, but such a topology must
justify discontinuous arithmetic constructors explicitly.  It also does not
prove that the distinguished completed Tate state realizes the hostile
adjacent-difference sequence.
