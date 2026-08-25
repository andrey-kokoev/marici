# Production–acceptance kernel in source `P_det`

Owner: `marici.Figueiredo`.

## Pipeline audit

WP237 supplies a source-derived dimuon portal, and WP235 supplies a calibrated
dimuon detector. The intervening physical map is

\[
N_i=\mathcal L\,\sigma_i(M_i,\theta_i)\,
\operatorname{BR}_i\,A_i\,\varepsilon_i.
\]

Writing the portal residue explicitly, the response contains the product
`residue * production * branching * acceptance * efficiency`. A spectral fit
to `N_i` cannot assign that product uniquely to the microscopic residue unless
the other factors are independently calibrated.

## Smallest exact kernel

Hold luminosity, production, branching, efficiency, mass, width, and detector
shape fixed. Then

\[
(r,A)=\left(\frac1{100},\frac12\right),\qquad
(r',A')=\left(\frac1{200},1\right)
\]

give the same accepted yield because both have `r A = 1/200`. They are
different source/detector-interface packets, not weak-basis presentations.

Thus a rank-four line-shape Jacobian written in effective-yield coordinates
would identify yields, not portal residues. Granting microscopic source
authority at that stage would be a quotient error.

## Physical calibration route

CERN Open Data record 718 is the validated 2010 CMS Drell–Yan AODSIM source
corresponding to the collision era used by WP235. It contains two million
events in 57 files totaling 198,875,911,585 bytes. It can calibrate Standard
Model dimuon acceptance, but it is not a WP237 trace-adjoint portal signal
sample. The portal source still needs generated signal samples across the
predeclared mass/residue support, processed through the same reconstruction
and selection.

## Disposition

The first remaining nonfaithful arrow is now localized:

\[
\text{portal source residue}
\longrightarrow
\boxed{\text{produced and accepted event yield}}
\longrightarrow
\text{calibrated mass record}.
\]

WP235 and WP237 cannot be composed across this box without an acceptance
constructor. The smallest next artifact is a reproducible portal-signal event
generator plus detector/selection response, not another fitted line shape.

## Exact checker

- Checker: `checkers/wp238_production_acceptance_kernel.py`
- Result: `results/wp238_production_acceptance_kernel.json`

## Calibration

- Pre excitement/confidence/expected information gain: `9/9/9`.
- Post excitement/confidence/realized information gain: `9/10/10`.
- Eliminated: effective-yield rank as authority for microscopic residue rank.
- Opened: an explicit CMS AODSIM acceptance route and a portal-signal
  generation requirement.

## Report to `marici.Nima`

- Domain: WP237 trace-adjoint portal packets composed with WP235 CMS records.
- Faithful coordinate: microscopic residue plus independently calibrated
  production, branching, acceptance, and efficiency—not effective yield alone.
- Probe family: dimuon line shapes after a common reconstruction/selection.
- Contextual partition: multiplicative fibers of constant accepted yield.
- Classification: nonfaithful production–acceptance arrow.
- Smallest falsifier: `(1/100,1/2)` versus `(1/200,1)`.
- Remaining instrument gate: portal-signal Monte Carlo or control data that
  calibrate production and acceptance independently of the desired residue.
