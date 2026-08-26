# Two-loop gauge fixed-point gate

## Question and admitted domain

WP464 asks whether the already declared `SU(3)_F` gauge dynamics can select the
dimensionless coupling `g_F`, and hence remove one of WP458's source freedoms.
The bounded spectrum is six Dirac fundamentals and three real adjoint scalars.
Yukawa contributions to the gauge beta function are excluded from this packet;
thresholds are also excluded, so all listed fields are active in one common
mass-independent scheme.

For real scalars and Dirac fermions the two-loop gauge-only coefficients are

\[
b_0={11\over3}C_A-{4\over3}S_2(F)-{1\over6}S_2(S),
\]

\[
b_1={34\over3}C_A^2-
\left(4C_2(F)+{20\over3}C_A\right)S_2(F)-
\left(2C_2(S)+{1\over3}C_A\right)S_2(S).
\]

Here `S_2(F)=6/2=3`, `S_2(S)=3*3=9`, `C_A=C_2(S)=3`, and
`C_2(F)=4/3`. Thus

\[
b_0={11\over2},\qquad b_1=-37.
\]

The gauge-only two-loop truncation therefore has the formal nonzero root

\[
g_*^2={88\pi^2\over37},\qquad
\alpha_*={g_*^2\over4\pi}={22\pi\over37}.
\]

## Exact hostile gate

WP449 derived, on its open-channel leading-width domain,

\[
{\Gamma_r\over M_r}={g_F^2\over4\pi}.
\]

At the formal root this becomes `22*pi/37`, which is greater than one. Hence
the root is outside both weak-coupling control and the narrow-pole regime used
by the admitted pole, width, and production packets. It cannot be composed
with those packets as a source-derived selector.

This is stronger than saying that the two-loop polynomial has no root: it has
one, but the first nonfaithful arrow is perturbative truncation at a coupling
where the predicted width is already broader than the mass. The root neither
selects an admissible `physical16` lens nor yields an experimentally typed pole
readout.

## Classification and falsifier

- Operation: gauge-only two-loop RG truncation.
- Quotient: it is weak-basis invariant and therefore descends to the faithful
  quotient as a law-level flow.
- Selector status: neither an admitted selector nor a rigidifier; its formal
  root lies outside the declared response domain.
- Smallest exact falsifier: `Gamma/M = 22*pi/37 > 1` at the proposed root.
- Remaining gate: a nonperturbative or controlled gauge-Yukawa construction
  must produce a fixed coupling inside a separately validated pole/instrument
  domain and survive thresholds and the full fitted ensemble.

