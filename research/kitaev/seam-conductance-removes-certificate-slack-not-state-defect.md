# Seam Conductance Removes Certificate Slack, Not State Defect

Fix an anchored weighted graph, a target vertex \(v\), and a state \(u\). Let

\[
R=R_{\mathrm{eff}}(a,v),
\qquad
E=\mathcal E_G(u),
\qquad
\delta=|u(v)-u(a)|^2.
\]

The resistance inequality gives \(\delta\le RE\). Add an authorized direct
seam edge from \(a\) to \(v\) with conductance \(t\ge0\). Then

\[
R_t=\frac{R}{1+tR},
\qquad
E_t=E+t\delta.
\]

Their certificate product obeys the exact identity

\[
R_tE_t
=
\delta+rac{RE-\delta}{1+tR}.
\]

Hence \(R_tE_t\) is nonincreasing in \(t\) and converges to the actual endpoint
defect \(\delta\). The improvement is strict exactly when the original
resistance inequality has slack. If \(u\) is the extremal harmonic voltage,
\(RE=\delta\), every seam conductance leaves the certificate product
unchanged.

## Seam pricing

If \(RE>1\) but \(\delta<1\), the strict unit certificate \(R_tE_t<1\)
requires

\[
t>rac{RE-1}{R(1-\delta)}.
\]

This is the minimal mathematical conductance threshold. It depends on the
actual endpoint defect as well as the original certificate. A source theorem
must supply or dominate both quantities before the seam can be priced.

If \(\delta\ge1\), no seam conductance can make this small-norm certificate
strict. In particular, when \(u(a)=1\) and \(u(v)=0\), \(\delta=1\): adding an
observation edge cannot repair the zero state.

## Exact fixtures on the three-vertex chain

For the harmonic voltage \(u=(1,3/4,1/2)\),

\[
R=2,
\quad E=1/8,
\quad\delta=1/4,
\]

so \(RE=\delta\) and the seam product remains \(1/4\) for every \(t\).

For the slack state \(u=(1,1,1/4)\),

\[
R=2,
\quad E=9/16,
\quad\delta=9/16,
\quad RE=9/8.
\]

The threshold is \(t>1/7\). At \(t=1/7\) the certificate is exactly one; above
it the small-norm unit test becomes strict.

## Authority and physical scope

The conductance \(t\) weights an observation/energy row. It is not a physical
actuator on \(u\). A source-authorized seam may sharpen the certificate, but it
does not change the endpoint value. Treating seam augmentation as state repair
would conflate observation geometry with actuation.

Likewise, optimizing \(t\) is legitimate only within a declared family of
source-authorized seam weights. A mathematically optimal unauthorized edge
does not prove the theta/Tate constructor theorem.

## Falsifiers

- Resistance decrease is reported as a change in the state.
- The seam energy contribution \(t\delta\) is omitted.
- A zero endpoint is claimed repairable by infinite seam conductance.
- Seam conductance is optimized outside the authorized source family.
- The threshold is priced from \(RE\) alone while \(\delta\) is unknown.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to determine whether seam augmentation genuinely improves
the full resistance-energy certificate after its added energy is counted.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The exact interpolation law shows seams remove certificate slack but
cannot alter the true defect, and yields a minimal authorized conductance
threshold.
