# Source-sewn contour factorization revision

## Question

Does the source define boundary-side maps for each physical `C6` occurrence, or only a canonical contour after sewing the occurrences?

## Claim boundary

The source equation frozen in `cyclic_q_assembly_certificate.md` writes the three-site scalar integral as six displayed terms, each with coefficient `+1`, one common measure, and the same oriented chain `Gamma`. Cyclic relabelling preserves that orientation because the three-variable wedge undergoes an even cycle.

Thus a graph-level physical chain exists for the sewn scalar combination

\[
S(I)=\sum_{ij\in\{12,23,31\}}\sum_{a=1}^{2}I_{ij}^{(a)}.
\]

It does not follow that `Gamma` induces a unique boundary side or physical period for every summand. The occurrence-resolved no-go certificate proves the opposite at the frozen three-site corner:

- four source-admissible regulator hierarchies give currents `2,0,0,-2`;
- endpoint exact terms have nonzero polar jets without a chosen relative trivialization;
- specialization and regulator limits fail to commute occurrence by occurrence;
- hierarchy dependence cancels only in the unsplit source combination.

Therefore the earlier demand for six individually canonical contour-side maps was too strong. The source-defined operation is a sewing codiagonal from occurrence-resolved meromorphic/endpoint-jet data to one physical relative period.

## Revised conjecture

Amplitude and cosmological-wavefunction factorization descend to the shared Carrier only after quotienting occurrence-level regulator and endpoint-trivialization ambiguity by source sewing. The comparison should have the form

\[
\mathcal D_q^{\rm occ}
\longrightarrow
\mathcal D_q^{\rm sewn}
\longrightarrow
\mathcal W_C,
\]

not an edgewise map from every occurrence directly to a physical Carrier wall.

The first arrow must preserve the all-`+1` source coefficients, common orientation, cyclic action, endpoint-jet cancellation, and the unsplit relative class. The second arrow may then be tested for residue/factorization compatibility.

## Strongest falsification attempt

If an occurrence-level physical contour map existed, changing an allowed regulator hierarchy would leave each normalized residue invariant. The exact chamber census changes the current from `2` to `0` or `-2`; hence such a map is not source-canonical. This does not refute the sewn conjecture because the source assigns the boundary value only to the unsplit combination, where the spurious dependence cancels.

## First unresolved square

The next square is whether physical residue commutes with sewing:

\[
\operatorname{Res}\circ S
\stackrel{?}{=}
S_{\partial}\circ\bigoplus\operatorname{Res}_{\rm occ}.
\]

Both sides require the source normalization and relative-chain boundary prescription. A proof must show cancellation of regulator hierarchy and endpoint subtraction before identifying the result with a lower-graph amplitude or wavefunction coefficient.

## Acceptance test

For one physical divisor:

1. retain all occurrence-resolved rational forms and endpoint jets;
2. apply the six source coefficients and common orientation;
3. compute the sewn residue under at least two admissible regulator hierarchies;
4. verify hierarchy and endpoint-subtraction independence of the sewn result;
5. compare it with the independently normalized lower-graph source object;
6. keep a single-occurrence residue as a deliberate failure.

## Disposition

The physical chain is neither absent nor occurrence-wise canonical. It is canonical after source sewing. The factorization programme must move from incidence-level `F_div` to a sewn residue comparison; individual-residue normalization is retained only as intermediate meromorphic and endpoint-jet data.

## Evidence

- `research/benincasa/cyclic_q_assembly_certificate.md`
- `research/benincasa/occurrence-resolved-physical-period-no-go.md`
- `research/benincasa/iterated-cut-regulator-chambers.json`
