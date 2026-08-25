# Oriented-flux selector audit (WP142)

Owner: `marici.Figueiredo`.

## Bounded question

Can a source-fixed CP-odd flux bias remove WP141's orientation degeneracy
while preserving a normalizable preparation law and selecting a
detector-accessible sector?

Pre-objective process report: excitement `9/10`, confidence `8/10` that a
stable bias selects orientation but cannot favor arbitrarily large accessible
flux, expected information gain `9/10`. Confounds are the linear bias and
one-dimensional flux lattice. These reports are non-evidential.

After minimizing WP140's modulus at `a=1`, the sector energy is `2|n|`.
Introduce the oriented source

\[
E_h(n)=2|n|-hn.
\]

The term `-hn` is odd under flux reversal and requires a physical orientation
or pseudoscalar background. It changes the source groupoid; it does not reveal
an absolute sign already measurable by the unoriented experiment.

On the full integer lattice, a finite-temperature partition sum is normalizable
iff

\[
|h|<2.
\]

For `h=1`, the frozen sectors `{-4,-1,1,4}` have exact energies

\[
E(-4)=12,\quad E(-1)=3,\quad E(1)=1,\quad E(4)=4.
\]

The zero-temperature source now selects the unique oriented sector `n=1`.
This is the first genuine sector-orientation selector in the flux branch,
conditional on the CP-odd boundary.

It does not close the detector gate. WP140 gives the selected sector threshold
`1`, above reach `3/4`. More generally, every stable positive bias has positive
tail slope `2-h`; its ground state is the smallest positive flux. A linear
bias strong enough to favor increasingly large positive flux requires `h>2`,
where `E_h(n)` is unbounded below and the full sector ensemble is not
normalizable. The exact hostile value `h=3` exhibits this failure.

Thus orientation selection and accessible-scale selection are independent.
Choosing an unstable or lattice-truncated bias solely to select `n=4` would be
target-fitted detector engineering.

Classification: **conditional oriented-sector selector; selected threshold
inaccessible in the stable linear-bias class**. The source coefficient `h`
and its pseudoscalar/oriented boundary remain physically unvalidated, and no
topological or collider instrument is established.

The smallest stability falsifier is `h=3`, for which the positive-flux energy
falls without bound. The smallest accessibility falsifier is the stable
selected sector `n=1`, whose threshold exceeds the declared reach. A lawful
repair requires a source-derived nonlinear sector energy with a stable
interior minimum at an accessible flux—not a bias fitted after detector
inspection.

Post-objective process report: excitement `9/10`, confidence `10/10`, realized
information gain `10/10`. Raw delta: the sign pair is split by energy `2`; one
unique sector is selected; its threshold remains inaccessible; the
detector-favoring linear bias is rejected by non-normalizability; twelve of
twelve checks pass. These reports are non-evidential.
