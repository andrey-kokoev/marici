# Origin-Level Falsification and the Derived Ward--Brauer Dictionary

## Record

Date: 2026-08-13

Status: the naïve originwise strengthening of entry 54 is falsified exactly.
The physical/curve realization squares commute after summing the complete
five-vertex cubic-sector carrier, but not on the raw
\(\{0,1,2\}^{5}\) origin basis, not after summing either endpoint of a closed
edge, and not after summing both endpoints.  For both one-edge and two-edge
closure, every audited presentation requires transport across all five local
cubic-sector coordinates.

This does not undo entry 54.  It identifies the type of its missing lift: the
surface dictionary must be a **derived natural transformation** carrying
explicit Ward/V homotopies between cubic-sector origins.  It cannot be the
identity map on origin labels followed by ordinary augmentation.

Reproducible certificate:

```text
research/nima/check_two_open_pair_ward_naturality.rs
```

## The raw origin module

Each of the five Yang--Mills cubic vertices is decomposed into its three
metric/handle sectors.  Before summing the vertex tensor, the origin set is

\[
\Omega=\{0,1,2\}^{5},
\qquad |\Omega|=3^5=243.
\]

For a spanning-tree presentation with closure edge \(e\), let

\[
R_e(\omega)
=
\operatorname{Sew}^{\rm phys}_e
T^{\rm full}_{\omega}
-
\operatorname{Gl}^{\rm met}_e
T^{\rm red}_{\omega}
\]

be the polynomial-valued residual while the second edge pair remains open.
Entry 54 proves

\[
\sum_{\omega\in\Omega}R_e(\omega)=0.
\]

The new audit asks whether this equality is already supported on the two
vertices incident to \(e\).  For a set \(S\) of freely summed vertex-sector
coordinates, fix every coordinate outside \(S\) and test

\[
\sum_{\omega|_S}R_e(\omega)=0
\]

as an exact polynomial identity in the 48-variable Gram-free chart.

The same test is applied after both closures, using the union of the endpoints
of the two closure edges.

## Exact falsification

There are

\[
12\ \text{trees}
\times 2\ \text{references}
\times 2\ \text{first-closure choices}
=48
\]

partially sewn presentations.  Across their \(48\times243=11{,}664\) raw
origins:

- 9,471 have a nonzero patternwise residual;
- summing one closure endpoint leaves 6,903 nonzero fixed-environment
  defects out of 7,776 tests;
- summing both closure endpoints leaves 1,200 nonzero fixed-environment
  defects out of 1,296 tests;
- in all 48 presentations, the smallest coordinate set whose every
  fixed-environment residual vanishes has size five.

After both closures there are 24 tree/reference presentations.  Across their
\(24\times243=5{,}832\) raw origins:

- 4,491 have a nonzero patternwise residual;
- the complete closure-endpoint union fails in all 144 fixed environments;
- in all 24 presentations, the smallest closing coordinate set again has
  size five.

Thus neither of the candidate strict statements

\[
R_e(\omega)=0
\]

or

\[
\sum_{\omega|_{\partial e}}R_e(\omega)=0
\quad\text{for every fixed environment}
\]

is true.

## What exactly has been falsified

The audit rules out the **diagonal origin map** which sends a full cubic-sector
word to the reduced word with the same five singleton labels, even after the
ordinary endpoint-sector quotient.  It also rules out any proof that uses
only augmentation over the closure-incident vertex labels while treating the
other vertex origins as spectators.

It does not rule out an off-diagonal map that transports one origin to a
signed combination of neighboring origins.  Nor does it rule out a local
chain map once the local Ward/V relations are retained as one-cells.  Those
are now the only viable forms of origin-resolved strictification.

## The required derived carrier

Let the three sectors at one cubic vertex be the vertices of a filled
2-simplex:

\[
C_\bullet^{\rm cub}=C_\bullet(\Delta^2),
\qquad
d[i,j]=e_j-e_i,
\qquad
\epsilon(e_i)=1.
\]

For the marked handle, the minimal formal resolution is

\[
K_\bullet
=
\left(C_\bullet^{\rm cub}\right)^{\otimes5}.
\]

Because \(K_\bullet\) is an augmented contractible complex, the already-proved
total identity implies abstractly that each residual admits a one-chain

\[
H_e\in K_1\otimes\mathcal R,
\qquad
dH_e=R_e.
\]

But this abstract existence is not the desired theorem.  A freely adjoined
simplex would be as tautological as a formal cylinder.  The nontrivial task is
to realize:

1. each edge \([i,j]\) by the actual local cubic Ward/V identity changing the
   singleton sector at a specified vertex;
2. each coefficient by the resolved endpoint-extension or curve carrier;
3. every 2-simplex and product square by the coherence between two such
   transports;
4. the resulting chain map compatibly with either partial physical trace and
   with surface Cuts.

Only such a realized augmentation upgrades the polynomial equality to an
intrinsic carrier map.

## The non-tautological local generator is a moving Ward mark

There is a canonical candidate for the one-cells.  For the ordinary cubic
gluon vertex with outgoing momenta \(p+q+r=0\),

\[
V_{\mu\nu\rho}
=
\eta_{\mu\nu}(p-q)_\rho
+\eta_{\nu\rho}(q-r)_\mu
+\eta_{\rho\mu}(r-p)_\nu,
\]

direct contraction gives the off-shell Ward identity

\[
\boxed{
p^\mu V_{\mu\nu\rho}
=
P_{\nu\rho}(r)-P_{\nu\rho}(q),
\qquad
P_{\nu\rho}(k)=k^2\eta_{\nu\rho}-k_\nu k_\rho .}
\]

On the massless three-point locus this becomes

\[
p^\mu V_{\mu\nu\rho}
=q_\nu q_\rho-r_\nu r_\rho.
\]

A longitudinal mark entering one half-edge is therefore the signed boundary
of the two ways it can leave through the other half-edges.  The mark propagates
locally from vertex to vertex until it reaches a transverse external state or
closes around a circuit.  This explains why the residual has global support
in the *vertex-sector coordinates* without requiring a nonlocal physical
interaction.

It also replaces the formal simplex by a testable carrier.  Let
\(\mathsf W_\bullet(G)\) be generated by cubic-sector words together with a
marked oriented half-edge, with differential given by the displayed Ward
identity.  The actual task is to construct a comparison

\[
\mathsf W_\bullet(G)
\longrightarrow
\left(C_\bullet(\Delta^2)\right)^{\otimes V(G)}
\]

whose image of a moving mark is the endpoint-extension transport.  If this
comparison exists, the all-five-coordinate support measured above is the
expected footprint of a local mark traversing the connected marked-theta
network.  If it does not, the simplex filler remains formal bookkeeping.

## Revised Ward--Brauer target

The source of the dictionary is not merely

\[
\bigotimes_{e\in E}\langle M_e,L_e^+,L_e^-\rangle.
\]

It must also retain the cubic-sector resolution:

\[
\boxed{
\mathcal K_E
=
\left(C_\bullet(\Delta^2)\right)^{\otimes V(G)}
\otimes
\bigotimes_{e\in E}
\langle M_e,L_e^+,L_e^-\rangle .}
\]

The formal source must therefore be physically realized by the marked Ward
complex.  The desired surface dictionary is a derived transformation

\[
\Phi_E:
\mathsf W_\bullet(G)
\otimes
\bigotimes_{e\in E}\langle M_e,L_e^+,L_e^-\rangle
\longrightarrow
\mathsf{Cov}^{\rm res}(G;E)
\]

such that augmentation gives the entry-54 trace-strict representative and
each edge trace commutes with \(\Phi_E\) up to the specified one-chain
\(H_e\).  For two closures, the difference between the two composites is a
cycle which must be filled by a specified two-chain.  This is the first place
where genuine higher coherence, rather than final equality, is unavoidable.

## Relation to Nima's talk

The transcript of *Scattering Amplitudes and Dualities at Infinity* emphasizes
that the self-factorizing carrier precedes the function and that a separate
dictionary transports carrier factorization into amplitude factorization.
The present falsification is a concrete instance of that distinction:

- after valuation/augmentation, the physical and surface polynomials agree;
- on the raw carrier origins, the diagonal dictionary fails;
- the missing information is precisely the transport between origins.

Thus the correct new claim is not that the surface formula is termwise equal
to physical-projector sewing.  It is that the two may be related by a derived,
sewing-natural dictionary on a resolved carrier.

## Next executable test

Construct an integral one-chain \(H_e\) for each of the 48 partial
presentations using only nearest-neighbor changes of one cubic singleton.
Then impose three non-tautological restrictions:

1. every edge coefficient must be generated by the corresponding local
   three-gluon Ward/V relation;
2. the construction must be covariant under the order-three road rotation and
   independent of the null-reference choice up to an admitted boundary;
3. for the two closure orders, the induced one-cycle must be the boundary of a
   curve-resolved two-chain.

Failure of the first restriction means the formal simplex resolution is only
homological bookkeeping.  Failure of the third means entry 54 has no coherent
origin-level lift despite its exact polynomial naturality.

## Internal dependencies

- Entry 51: literal endpoint-extension origins and homotopy-sensitive curve
  labels.
- Entry 52: final symbolic physical/graphical identity.
- Entry 53: corrected Ward-quotient closure theorem.
- Entry 54: exact two-open-pair partial realization and closure stability.
- Source annotations: `research/sources/nima/talks/scattering-amplitudes-and-dualities-at-infinity/annotations.md`.
