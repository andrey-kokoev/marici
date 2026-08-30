# Exclusion plus valuation degree renormalizes to the square current

## Bounded question

What exact source object remains when each primitive-exclusion boundary port
is coupled to its own valuation-number operator before global aggregation?

## Local valuation oscillator

For a fixed prime \(p\), let

\[
N_pe_n=v_p(n)e_n.
\]

Using the multiplication isometry \(T_p\),

\[
N_p=\sum_{k\geq1}T_p^kT_p^{*k}
=\sum_{k\geq1}P_{p^k\mid n}.
\]

The primitive boundary projection is

\[
E_p=I-T_pT_p^*=P_{p\nmid n}.
\]

On a label of valuation \(r\), the operator \(E_p+N_p\) has eigenvalue one
when \(r=0\) and eigenvalue \(r\) when \(r\geq1\). Therefore

\[
E_p+N_p\geq I.
\]

Each prime port is individually gapped when its boundary and degree channels
are retained together.

## Finite-cutoff renormalized sum

For a finite prime set \(S\), subtract the universal identity contribution
from the primitive boundary channel and add logarithmic valuation degree:

\[
Q_{2,S}
=\sum_{p\in S}(\log p)(E_p-I+N_p).
\]

Since \(E_p-I=-P_{p\mid n}\),

\[
Q_{2,S}
=\sum_{p\in S}(\log p)(N_p-P_{p\mid n}).
\]

Using the incidence expansion of \(N_p\), this becomes

\[
Q_{2,S}
=\sum_{p\in S}\sum_{k\geq2}(\log p)P_{p^k\mid n}.
\]

Thus the renormalized primitive-boundary-plus-degree balance is exactly the
square-and-higher prime-power current.

## Arithmetic eigenvalue

Once \(S\) contains every prime divisor of \(n\),

\[
Q_2e_n
=\left(\sum_{p\mid n}(v_p(n)-1)\log p\right)e_n.
\]

Equivalently,

\[
Q_2e_n
=\log\left(\frac{n}{\operatorname{rad}(n)}\right)e_n.
\]

The kernel is precisely the squarefree label sector, including the vacuum.

## Interpretation

The primitive divergence, valuation degree, and square current are not three
unrelated corrections. They form one exact filtration step: primitive boundary
plus valuation degree, after removal of the universal cutoff line, equals the
square-and-higher current.

This explains why deleting the primitive current and then appending a square
counterterm is unsafe: the square channel is the typed remainder of their
relative balance.

## RH boundary

The resulting operator is positive but not faithful. Every squarefree packet
lies in its kernel. Hence this identity does not orient scalar zeros.

Iterating the same subtraction moves from depth \(k\) to depth \(k+1\), which
reconstructs the entire valuation filtration. That hierarchy explains the
regularization anatomy but, without a zero-state boundary law linking all
depths, remains arithmetic provenance rather than zero confinement.

## Next gate

Derive whether the doubled Green boundary current performs this filtration
step dynamically: the primitive endpoint term should combine with
logarithmic degree to leave the square current with exactly the displayed
coefficient. Any coefficient mismatch at \(p^2\) is the smallest falsifier.
