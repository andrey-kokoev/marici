---
authors:
  - marici.Nima
date: 2026-08-18
---
# 675 — The Physical Wall Cocycle Preserves the Rank-One Exceptional Quotient

## Hard-to-vary claim

Away from the signed-energy conductor letters, all six reduced-tangency
residues of the physical wall cocycle are nonzero.  Weighting the exceptional
syzygy evaluation by these physical residues therefore preserves Entry
672's two-dimensional kernel and rank-one quotient.

## Physical residues at reduced tangencies

On a shared wall \(q_i=0\), Entry 673 gives

\[
\sqrt{K_E}|_{q_i=0}=\pm h_i.
\]

The physical wall component has the form

\[
\rho_i
\sim
\frac{N_i(t)\,dt}
{h_i(t)D_i(t)},
\]

where \(N_i\) is the restricted unsplit occurrence numerator and \(D_i\)
is the product of the remaining four marked denominators, including the two
occurrence marks.

At a simple root \(r\) of \(h_i\), its reduced-tangency residue is

\[
\operatorname{Res}_{t=r}\rho_i
\sim
\frac{N_i(r)}{h_i'(r)D_i(r)}.
\]

The exact checker tests the three required coprimalities:

\[
\gcd(h_i,h_i')=1,
\qquad
\gcd(h_i,N_i)=1,
\qquad
\gcd(h_i,D_i)=1.
\]

Across fifty generic exact fibers, all six residues are nonzero.  The
excluded fibers are precisely signed-energy degenerations where a remaining
marked denominator meets a tangency root; these belong to the already known
wall-conductor support and are not generic counterexamples.

## Kernel comparison

Let

\[
E_{\rm exc}:\operatorname{Der}^{(7)}(-\log D)
\longrightarrow\mathbb K^6
\]

be the reduced exceptional evaluation from Entry 672, and let
\(R_{\rho}\) be diagonal multiplication by the six physical tangency
residues, with orientation signs retained.  Generically every diagonal
entry is nonzero, so \(R_\rho\) is invertible.  Therefore

\[
\boxed{
\ker(R_\rho E_{\rm exc})=ker E_{\rm exc},
}
\]

and hence

\[
\boxed{
\dim\ker(R_\rho E_{\rm exc})=2,
\qquad
\operatorname{rank}(R_\rho E_{\rm exc})=1.
}
\]

This conclusion is independent of residue normalization and orientation
signs because those only rescale the six nonzero coordinates.

## Consequence

The rank-one exceptional quotient is not merely an ambient weighted
singularity detector.  The canonical physical wall cocycle occupies all of
its reduced tangency coordinates and preserves exactly the same quotient
line.  Thus we now have a source-derived physical pairing with the line:

\[
\boxed{
\text{minimal source syzygies}
\xrightarrow{E_{\rm exc}}
\text{weighted tangency data}
\xrightarrow{\rho_{\rm phys}}
\text{rank-one physical quotient}.
}
\]

Entry 674 still excludes identifying this line with the Källén collision
line by diagonal support.  The new result establishes physical occupancy,
not \(\mathcal Q\)-provenance or a canonical lift into \(\mathcal T_7\).

## Updated frontier

Extend the six-residue pairing across the signed-energy conductor letters.
Compute its logarithmic/nearby-cycle limit and determine whether the generic
rank-one quotient remains locally free, acquires torsion, or merges with the
known conductor blocks.  Only after this extension is the line a global
coefficient candidate.

## Evidence

- `research/benincasa/physical_shared_wall_reduced_factors.py`;
- Entries 648, 668, and 672--674.

## Outcome contract

~~~json
{
  "claim": "The physical wall cocycle vanishes on enough reduced tangency points to change or annihilate the exceptional rank-one quotient generically.",
  "status": "falsified",
  "generic_exact_fibers": 50,
  "reduced_tangency_residues_per_fiber": 6,
  "all_generic_physical_tangency_residues_nonzero": true,
  "physical_weighting_invertible": true,
  "physical_exceptional_kernel_dimension": 2,
  "physical_exceptional_rank": 1,
  "Kallen_line_identified": false,
  "next_experiment": "Extend the rank-one physical exceptional pairing across signed-energy conductor letters."
}
~~~
