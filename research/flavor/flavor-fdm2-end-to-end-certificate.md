# End-to-end FDM-2 selector certificate (WP101)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Factored experiment

The proposed experiment factors as

\[
\text{thermal source}
\to\text{vacuum branch}
\to\text{domain record}
\to\text{canonical light flavor state}
\to\text{moment samples}
\to\text{detector channel}
\to\text{deconvolved route weights}.
\]

The arrows have different jobs. The thermal source is the only candidate
selector. The branch record and moments separate contexts. Canonical matching
and detector inversion are readout maps. None of the latter inherit selector
authority merely by being faithful.

## Combined conditional error certificate

Let `gamma=min(gamma_o,gamma_e)>0` be the robust detector modal margin from
WP100. Let `epsilon_s` bound empirical modal sampling error, `epsilon_d`
detector-model/calibration error before inversion, `epsilon_c` canonical
matching or route-classification error, and `epsilon_r` reset/correlation
error. In the declared modal norm, triangle inequality gives

\[
\epsilon_{route}\le
{\epsilon_s+\epsilon_d\over\gamma}
+\epsilon_c+\epsilon_r.
\]

WP98 supplies a sufficient IID sample count for `epsilon_s`; WP100 supplies
the inverse factor. The other terms remain physically untyped. The bound is
therefore a conditional certificate, not an empirical instrument claim.

## Selector verdict

Within the authorized proposed model, the source operation is a **branchwise,
finite-threshold, conditional selector** of the proper physical16 attribute
`J != 0`. It is not a texture rigidifier. It does not select an absolute sign,
a CP-asymmetric unconditioned ensemble, the exact vacuum coordinate, or the
magnitude of `J`.

The contextual route family becomes jointly faithful under the first two
moments only if independent branch samples exist. A domain record defines a
relational experiment over its stabilizer groupoid. The measured-ten
projection remains unauthorized for uniqueness claims.

## First-failure rule and falsifiers

The first nonfaithful arrow is, in order:

1. thermal source, if transverse curvature never crosses;
2. domain channel, if no persistent branch record/reset exists;
3. canonical matching, if the finite mediator block is replaced by its bare
   Schur complement outside controlled mixing;
4. sampling context, if route weights fall below the declared resolution;
5. detector, if either robust modal margin is nonpositive.

The smallest exact end-to-end falsifier is `gamma=0`, which makes the claimed
finite readout bound undefined even when every earlier arrow is faithful.
The remaining physical-instrument gate is a single measured parameter bundle:
source-derived `V_eff(T)` and rates, domain lifetime/reset, canonical matching
errors, minimum route weight, detector calibration/drift, and their common
operating domain.

Verification: `uv run --with sympy python research/flavor/checkers/wp101_fdm2_end_to_end_certificate.py`.
