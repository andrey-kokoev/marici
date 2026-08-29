# The valuation carrier makes Volterra prime diagonality tautological before pushforward

## Label tensor factor

Let \(\mathcal L\) be the source valuation carrier with orthonormal basis

\[
e_{p,k},
\qquad p\text{ prime},\quad k\ge1.
\]

The analytic history fiber at label \((p,k)\) is \(\mathcal E_{p,k}\), and the labelled source object is the Hilbert direct sum

\[
\mathscr E
=
\bigoplus_{p,k}
e_{p,k}\otimes\mathcal E_{p,k}.
\]

The projection

\[
P_{p,k}
=
|e_{p,k}\rangle\langle e_{p,k}|\otimes I
\]

is a source carrier idempotent, not a Fourier--Bohr projection reconstructed from scalar characters.

## Labelled Volterra constructor

Define the history constructor fiberwise:

\[
\mathbf H_+
=
\bigoplus_{p,k}
I_{e_{p,k}}\otimes H_{+,p,k}.
\]

Then, by construction,

\[
P_{q,\ell}\mathbf H_+P_{p,k}
=
0
\qquad
((q,\ell)\ne(p,k)),
\]

and

\[
[P_{p,k},\mathbf H_+]=0.
\]

Reflection, even/odd history splitting, completion, and transported Mellin metrics also act inside the analytic factor and therefore commute with every label idempotent.

Prime diagonality is thus an exact constructor theorem before any scalar observation or prime pushforward.

## Adams grade map

The Adams edge changes grade inside one prime fiber:

\[
A_r:
e_{p,k}\otimes f
\longmapsto
e_{p,rk}\otimes A_{r,p,k}f.
\]

It obeys the typed covariance

\[
A_rP_{p,k}
=
P_{p,rk}A_r.
\]

This allows grade change while forbidding prime change. For \(p\ne q\),

\[
P_{q,rk}A_rP_{p,k}=0.
\]

Hence the earlier twisted Mellin equivariance is a scalar shadow of a simpler carrier law.

## Assembly consequence

For a finite source packet

\[
x=\sum_{p,k}e_{p,k}\otimes x_{p,k},
\]

the history energy is a sum of fiber energies with no cross-prime term unless a later constructor explicitly couples label factors. Ordinary Volterra propagation does not do so.

The absence of primitive \(pq\) flux and the absence of analytic cross-prime history are now distinct:

- the first is arithmetic typing of the Adams/Fock constructor;
- the second follows from label-diagonal history;
- a later authorized global Green interaction may still couple completed outputs after labels have been retained.

## Authority boundary

This theorem is source-authorized only if the valuation/Fock carrier is admitted before analytic realization. If labels are erased and later reconstructed from Mellin frequencies, invariant-mean authority returns as an unresolved condition.

The safest constructor order is therefore

\[
\text{valuation-labelled source}
\to
\text{fiberwise completion and history}
\to
\text{typed mixed block}
\to
\text{prime pushforward}.
\]

## Next gate

Prime diagonality is closed before pushforward. The next unresolved theorem is faithfulness of prime pushforward on the two-dimensional reciprocal even-odd incidence system. It must retain both the constant-wall and oriented-jump ports; scalar Euler readout alone cannot do so.
