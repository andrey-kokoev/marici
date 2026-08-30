# Minimal Ward Index Has a Neutral RG Kernel

## Question

Can a physical positive comparison principle select the WP831 spectrum by
minimizing the Ward-current Gram

\[
S=\operatorname{Tr}Q^2?
\]

## Charged completion is rejected

For the primitive charge packet \((1,2,3)\),

\[
S=14.
\]

Every nonzero anomaly-neutral vectorlike pair \((r,-r)\) raises the pairing
by \(2r^2\). Therefore minimal Ward index genuinely excludes the charged
vectorlike family responsible for WP831's 14-to-16 threshold fiber. This is a
real partial selector, provided minimization of this physical pairing is
source-authorized.

## Neutral interacting completion

Add one neutral state:

\[
Q_4=\operatorname{diag}(1,2,3,0).
\]

Linear and cubic anomalies, primitive contrast, and Ward index remain
respectively 6, 36, 1, and 14. With

\[
D_4=
\begin{pmatrix}
0&1&0&1\\
1&1&1&0\\
0&1&2&1\\
1&0&1&3
\end{pmatrix},
\]

the neutral state mixes with the charged sector, \(D_4\) is nondegenerate,
and the common commutant of \(Q_4,D_4\) is scalar. Thus the neutral completion
also survives the WP833 irreducibility gate.

## RG-active null direction

Represent one allowed neutral interaction by the WP821 coefficient shift

\[
c=3+\eta^2,
\]

with the other normalized coefficients held at one. The interacting fixed
coordinate is

\[
x_*(\eta)=\frac1{2+\eta^2}.
\]

The packets \(\eta=0\) and \(\eta=1\) have identical Ward pairing but give

\[
x_*(0)=\frac12,
\qquad
x_*(1)=\frac13.
\]

Both local stability spectra are positive:

\[
\left\{\frac12,2\right\},
\qquad
\left\{\frac{7-\sqrt{13}}9,
\frac{7+\sqrt{13}}9\right\}.
\]

Hence the neutral direction can change magnitude and threshold flow without
leaving the minimal Ward-index class.

## First nonfaithful arrow

The pipeline fails at

\[
\text{full RG-active spectrum}
\longrightarrow
\text{Ward-current Gram}.
\]

The pairing is faithful on the charged-current coordinate but has a neutral
kernel. A current-correlator instrument can read the charged response; it does
not by itself detect which neutral RG constructor produced it.

## Claim boundary

The coefficient shift \(c=3+\eta^2\) is an exact declared hostile model. This
packet does not claim it as a loop calculation derived from the displayed
finite operator packet. Its role is to test whether Ward-index minimality has
authority over a neutral RG-active direction; it does not.

## Disposition

Progressive partial selector with a negative completion result. Minimal Ward
index excludes charged vectorlike additions but leaves neutral interacting
spectra, RG magnitude, thresholds, and physical readout unresolved.

The next source candidate must provide a positive functional faithful on every
RG-active sector, with its relative charged/neutral weights derived before the
desired portal is inspected.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp834_minimal_ward_index_neutral_rg_kernel.py
```
