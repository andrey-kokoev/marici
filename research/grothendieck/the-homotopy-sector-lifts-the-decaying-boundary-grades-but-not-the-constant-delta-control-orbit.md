# The Homotopy Sector Lifts the Decaying Boundary Grades but Not the Constant–Delta Control Orbit

## Regularity of the third sector

For the theta forcing `f`, the outgoing resolvents preserve rapid decay on the
positive scale chart.  Therefore

\[
K_z=R_{-z}R_zf
\]

has the same superexponential tail class as `f`.  The face equations

\[
(D+z)K_z=x_+,
\qquad
(D-z)K_z=x_-
\]

also place `K_z` one graph rung above the unilateral tails: for smooth theta
forcing it has the value and flux traces needed by both faces.

Consequently the following grades lift to the homotopy sector:

- primitive prime sampling;
- prime-square sampling;
- connected prime-power sampling;
- seam value and flux traces.

Their continuity follows from the same superexponential sample majorants used
for `f`; applying either resolvent changes polynomial prefactors but not the
decisive `exp(-c exp(2q))` decay.  The face identities hold before evaluation,
so applying any one of these typed currents preserves its grade.

## Failure of the archimedean control orbit

The five-component archimedean Fourier cell contains the pair

\[
1\longleftrightarrow\delta_0.
\]

Neither member belongs to the common outgoing `L2` resolvent state domain:

- the constant function has infinite half-line `L2` norm;
- `delta_0` is a boundary distribution rather than an `L2` state;
- regularizations of `delta_0` have diverging `L2` norm;
- their resolvent images depend on a choice of half-plane and boundary
  prescription, so there is no common off-seam graph lift.

Therefore the entire archimedean five-cell cannot be copied into the `K`
sector as an ordinary state packet.  Doing so would again identify boundary
controls with bulk states.

## Correction to the nested architecture

The outer three-sector structure is exact, and the decaying arithmetic and
seam subpacket lifts across all three sectors.  But the literal replication
of every inner control cell in

`3(3+2+1)+2+1`

is too strong if the inner `+1` is interpreted as the constant–delta
archimedean control orbit.

The source-faithful interpretation is:

1. three bulk packets carrying theta, arithmetic sampling, and seam traces;
2. two directed resolvent faces from the homotopy packet;
3. one external archimedean/augmentation control correspondence shared by all
   three.

The final `+1` is global precisely because it cannot be internalized into the
three bulk graph domains.

If each inner `+1` instead denotes an abstract mate cell rather than the
physical control orbit, the numerical expression remains possible, but those
three mates must be constructed separately and may not be populated by
copies of `1` and `delta_0`.

## Exact next gate

Construct the external control correspondence

\[
\mathcal A
\longrightarrow
P_+\times P_K\times P_-
\]

at the rigged level, where `A` carries the constant–delta Fourier orbit and
the other three packets carry their bulk graph domains.  Then test whether its
three incidence maps make the two resolvent-face squares commute.

The smallest falsifier is already identified: any proposed `K`-sector state
norm assigning finite ordinary `L2` norm to both `1` and `delta_0` is not the
source graph norm.

## Result

The third sector lifts every decaying arithmetic grade and the seam trace
packet, but not the constant–delta control orbit.  The global control cell is
forced to remain an external rigged correspondence.  The architecture works
only when “three copies” means three bulk packets sharing one nonduplicated
control port, not three identical Hilbert blocks.

