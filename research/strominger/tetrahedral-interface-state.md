# Internal interface states on a common tetrahedral carrier: new rival

## Source, task and nonpromotion

Operator: test an internal-state alternative, without added forces. Fresh source
is the verified128-center,256-edge periodic diamond network. Its four-coordinate
incidence, unwrapped six-loop and all earlier geometric counterexamples remain.
A/B now supplies only an orientation of incidence, NOT a physical P/N assignment.
This is explicitly a NEW rival to the rejected direct P/N=A/B transfer.

Specification: `inputs/tetrahedral-interface-state-v1.json`.
Reproduce:

    python research/strominger/checkers/check_tetrahedral_interface_state.py
    python research/aspect/scc/scc.py check tetrahedral-interface-state-v1 --verbose

Receipt: `results/tetrahedral-interface-state/verification.json`.

## The collective space is an incidence fiber, not a new spatial dimension

Orient every actual diamond edge from A to B. Let partial be the signed
center/edge incidence matrix. An interface state j has256 rational (or integer)
edge coefficients; its boundary is q=partial*j in128 center coordinates.

States compatible with the SAME boundary q form an affine space

    F(q)={j: partial*j=q},
    difference space ker(partial).

Connectedness gives boundary rank127 and cycle rank256-127=129. These dimensions
belong to this finite periodic graph, not a particle capacity or the homology of
ordinary3D space. No additional spatial axis is needed. Coefficients are signed
interface amplitudes/chains, not automatically particle occupancies or charges.

## An actual hidden distinction, not an appended charge counter

The retained unwrapped six-loop gives a nonzero signed edge state c with
partial*c=0 and squared norm6. The two alternating edge matchings m+ and m-
use three disjoint pairs each, occupy exactly the same six centers, and satisfy

    partial*m+ = partial*m-,
    m+ - m- = c.

The genuine interface reader eta(j)=c^T*j distinguishes them as+3 versus-3.
A center-only boundary reader cannot. This is real source-state information;
unlike the earlier exact-gradient counter it has nonzero circulation support.
It still does NOT identify an electron, neutron, proton or electric charge.

## A complete, executable retained-state constructor

Fix one canonical BFS spanning tree. Keep ALL q coordinates and the129 chord-edge
coefficients of j. Decode by subtracting their divergence and solving the127
tree-edge flows by leaf elimination. The packet has257 displayed coordinates
with one boundary-sum constraint, hence independent dimension256: all original
edge modes are retained, with no false increase in capacity.

The code checks decoder(encoder(j))=j on EVERY one of the256 source basis states.
No potentially expensive symbolic inverse or lossy quotient is used.

## Conservation is relative to a declared common operation

Test the common incidence operators

    H1=partial^T partial, H0=partial partial^T,
    U1=I-H1, U0=I-H0.

These are declared algebraic continuation maps, NOT forces, an energy law or a
physical time-step. They have no particle-specific weights. Boundary transport
commutes: partial U1=U0 partial. Chord packet coordinates update by subtracting
the corresponding component of partial^T q. Exact one- and two-application
commutation is verified on all256 original basis states.

For EACH of the129 independent fundamental cycles z,

    z^T U1 j=z^T j,

because partial*z=0. Thus the candidate internal readouts are genuinely conserved
by this specified operation. They are not merely labels assigned after decoding.
But there is an entire129-dimensional fiber, not just two states. All tested
integer multiples of c remain possible, and rational multiples are possible too.
Integer coefficients would be an additional domain choice, not a derivation of
physical charge quantization.

This is an explicit OPERATOR CHANGE from the old pyrochlore Laplacian:

    H1=8I-L_pyrochlore.

All256 basis actions verify that relation. The old operator sends c to8c; it
must not be described as preserving its amplitude under the same Euler update.

## Four strong controls limit the particle interpretation

1. The binary matching flip m+<->m- preserves endpoint exclusion, occupied centers
   and boundary data, but changes eta. Pairing compatibility alone therefore does
   not protect a P/N-like conserved label. Moreover U1 itself does not preserve
   the binary matching domain. Signed edge amplitudes and pair occupancy are
   different types; they cannot be silently interchanged.
2. A translated source inversion exchanges the two alternating matchings. They
   are not automatically two intrinsically different species. A marked reader
   distinguishes them, but its reference/symmetry behavior must be retained.
3. On the declared diamond channels, a single coordination star is a tree and
   has no nonzero circulation. Three corner-to-corner moves routed through the
   SAME central site make a geometric triangle whose refined source edge chain
   is ZERO. The genuine six-loop passes through different centers. Forgetting
   intermediate-center provenance would invent an apparent loop mode.
4. Higher incidence matters. Filling the six-loop with one2-cell is consistent
   with boundary-of-boundary zero, but adds c c^T to the full edge Hodge operator:
   it now sends c to6c. Separately, an actual tetrahedron with all six edges and
   four triangular faces has full edge Hodge operator4I6, hence no nonzero
   harmonic edge loop. Graph cycles alone are not protected holes of a solid
   tetrahedron. This says nothing against other kinds of local tetrahedral state.

No loops are asserted to involve six physical nucleons: they involve six
coordination centers of the source network. Likewise no selection of missing
faces or forbidden controls has been derived from physical particle data.

## DPC and disposition

Problem: can one common geometry support a reconstructible internal distinction
rather than P/N names tied to spatial colors? Bold candidate: actual interface
cycles provide boundary-invisible information and an incidence-conserved reader.
Rivals: lost information is fake; a zero-gradient ledger suffices; all pairing
controls conserve the label; isolated tetrahedral geometry uniquely selects two
states. Risk: full source reconstruction/composition, explicit matching flip,
unmarked exchange, fake-loop refinement and higher-cell completion.

Disposition: the internal-state fiber and faithful interface constructor EXIST.
A unique binary particle pair, protected physical charge and a selection of the
admitted controls do NOT follow. Earlier diamond/Garai transfer failures remain.

Next nonredundant test: classify minimal six-loop patterns modulo actual source
symmetries and compare relative/boundary-marked higher-cell conditions. Separate
true invariant distinctions from arbitrary orientation names; require a fixed
allowed-control set before calling any loop readout conserved physical identity.
This exploratory branch does not advance the unrelated unfinished flag-family
iteration or rewrite its current-net pointer.
