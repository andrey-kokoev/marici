# The physical half twist removes seven fourth-order source-jet directions

The source-generated object must be constructed by differentiating raw
labelled rational forms before quotient reduction.  With that correction, the
rank profile through covariant jet order five is

\[
\begin{array}{c|rrrrrr}
\gamma & J_{\le0}&J_{\le1}&J_{\le2}&J_{\le3}&J_{\le4}&J_{\le5}\\
\hline
5 &1&3&9&19&26&26\\
-\tfrac12&1&3&9&19&19&19.
\end{array}
\]

The generic source becomes cyclic at order four.  Physical specialization
removes exactly the seven fourth-order directions that would complete the
rank-26 quotient, and no direction returns at order five.

This reproduces over \(\mathbf F_{32003}\) and \(\mathbf F_{32009}\) at
\(K\)-pole depths three and four.  The physical profile through order four
also agrees at depth two over \(\mathbf F_{32003}\).  At depth four both
primes retain the same nineteen source words and the same seven-plane support
pattern through order five.

## What changed

The earlier frozen-point Krylov algorithm reported rank 25 because it reduced
after every derivative and then treated the reduced coefficients as constants.
The corrected algorithm instead retains exact polynomial dependence on all
three external parameters, applies every derivative to the raw labelled form,
and reduces only the completed jet.

Therefore the old codimension-one line is not repaired.  It is replaced by a
source-derived finite-cutoff jet defect of dimension

\[
\boxed{26-19=7.}
\]

The number seven is derived from differential source transport, not fitted
from a quotient or selected complement.  However, only its dimension is
currently intrinsic.  No splitting of the seven-dimensional quotient and no
physical/Leray interpretation has been chosen.

This calculation supersedes the differential interpretations of Entries 887
and 892.  Those entries explicitly iterate matrices in a frozen source
presentation; they remain finite-fiber linear algebra, but they do not prove
that rank 26 is the smallest family-level horizontal source object.  The
raw-before-reduction family calculation instead supplies the rank-19
horizontal candidate.

The equality \(26-19=7=\dim T_7\) is not an identification.  The new
seven-dimensional object is a quotient/annihilator of the marked rank-26
presentation, while \(T_7\) is the absolute algebraic kernel inside
\(M_9\).  Finite-to-one is not one-to-one: only a source-normalized
localization/Gysin comparison defined on a faithful quotient can relate these
objects.  Until that map is constructed, the dimension match has no
theorem-level content.

## Scope

This is a replicated finite-field, finite-cutoff, finite-jet result at the
frozen generic external point.  It does not yet prove:

- a characteristic-zero rank-19 differential submodule;
- stability at higher pole depth, cutoff, point, or jet order;
- cyclic-chart descent of the rank-19 subspace;
- identification of the seven-dimensional quotient with marked residues,
  Leray periods, Tate/Kummer data, or a physical readout.

The next admissible test is to compute the annihilator seven-plane without a
primal splitting, transport it through the cyclic charts, and test whether it
is preserved by the source-derived connection.

## First cyclic descent result

The annihilator seven-plane has a stable reduced support pattern at both
primes.  Each of its seven basis rows contains the same six coordinates

\[
b^4,b^5,b^6,b^7,ab^4,ab^5
\]

and one distinct pivot among

\[
ab^6,a^2b^3,a^2b^4,a^2b^5,a^4,a^4b,a^5.
\]

An independent G31 raw-jet construction reproduces the rank profile
\(1,3,9,19,19,19\).  Under the exact G12-to-G31 quotient transition,
contragredient transport of the G12 annihilator has rank seven, and its joint
rank with the independently computed G31 annihilator remains seven:

\[
\boxed{
T^{-\vee}\operatorname{Ann}(J_{G12})
=
\operatorname{Ann}(J_{G31}).
}
\]

This equality replicates over both primes.  It establishes one genuine cyclic
descent square for the finite-cutoff seven-plane; it does not yet establish
order-three closure across all three residue charts or horizontality over an
open parameter locus.

The full quotient wiring was then tested on the genuine cyclic orbit

\[
G12(2,3,4)\to G23(4,2,3)\to G31(3,4,2)\to G12(2,3,4).
\]

All three transition matrices have rank 26 and their ordered product is the
identity matrix, with zero entrywise defect, over both primes.  Thus the
finite quotient itself carries an exact order-three cyclic chart action.  The
remaining distinction is that the seven-plane has been independently checked
on the two reflection targets, while its restriction around every leg of this
specific cyclic orbit has not yet been independently rebuilt.

## Open-locus frame and horizontal-closure evidence

The physical G12 construction was rebuilt at the additional generic external
points \((3,5,7)\) and \((5,7,11)\), over both primes.  Every run gives the
same cumulative ranks

\[
1,3,9,19,19
\]

through order four, the same seven-row annihilator pivot/support pattern, and
the same 19 source-labelled frame words.  Besides the source itself, the frame
contains two first-order words, all six symmetric order-two multi-indices, and
all ten symmetric order-three multi-indices.  None of the 81 ordered
fourth derivatives adds a direction.

Consequently the sampled frame satisfies

\[
\nabla_i J_{\le3}\subseteq J_{\le3}
\]

at every tested point: derivatives of the lower generators are later jet
generators, and every derivative of an order-three generator is an order-four
jet already in the rank-19 span.  This is replicated finite-open-locus
evidence for a horizontal rank-19 subbundle.  It remains short of a symbolic
open-set theorem because the common frame minor and the closure coefficients
have not yet been reconstructed as rational functions.

## Exact evidence

- `research/nima/checkers/check_rank26_physical_source_covariant_jet_census.py`
- `research/nima/results/rank26_generic_source_covariant_jet_census_k3_p32003.json`
- `research/nima/results/rank26_generic_source_covariant_jet_census_k3_p32009.json`
- `research/nima/results/rank26_physical_source_covariant_jet_census_k3_p32003.json`
- `research/nima/results/rank26_physical_source_covariant_jet_census_k3_p32009.json`
- `research/nima/checkers/check_rank26_physical_source_second_covariant_jet.py`
- `research/nima/checkers/check_rank26_physical_jet_seven_plane_chart_transport.py`
- its two prime-indexed result packets.
- `research/nima/checkers/check_rank26_cyclic_chart_order_three_closure.py`
- its two prime-indexed result packets.
- epistemic graph event
  `ev-000000002349-a6161454-27f8-4617-9d36-ed7b19c9c5af`.
- cyclic descent event
  `ev-000000002356-0eb0f605-1c79-4b17-8ca2-78e24c432ad3`.
- cyclic order-three quotient event
  `ev-000000002361-533d1976-7fb3-48fe-825d-787f236c43d3`.
- open-locus frame event
  `ev-000000002362-9b614a57-27fa-4634-89ec-4fd0b3c655b5`.
