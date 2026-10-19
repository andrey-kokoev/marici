# Concrete identity-bearing port equations

## Packet and geometry

A port packet contains `(complex identity, q, history)`, with q three rational
configuration coordinates. Identity is a discrete boundary-supplied label, not
the constant1 or an extra real coordinate. Three such presentations implement
the operator's3+9 bookkeeping: three identity slots plus nine configuration
coordinates. Agreement leaves one identity and three independent coordinates.

The checker imports the CURRENT viewer `carrier.mjs` through Node, loading the
actual P=C0/M0/C1[M1], N=M0/C1/M1[C2], E=M1/C1/C2[M2] bodies. All calculations
thereafter use checked exact rational coordinates. The viewer is not modified.

For each vertex v choose the first containing ordered tetrahedron. Let F_v be
the3×3 matrix whose columns are the edges from v to that tetrahedron's other
three vertices, in its declared order. Every F_v is invertible. Define

    decoded configuration displacement: delta_v = F_v q_v,
    edge equation: F_v q_v = F_u q_u,
    link matrix: T_(v<-u) = inverse(F_v) F_u,
    identity_v = identity_u.

A world-space position corresponding to that packet is p_v+delta_v. Thus the
same decoded displacement can be carried from the input C0 to the output C2.
Local coordinates change, while the identity and complete path history travel
with the packet. Each link preserves the induced metric F_v^T F_v.

This is an explicitly declared FLAT GEOMETRIC CONNECTION. It is not a derivation
of the earlier native coefficient operators or physical dynamics. Wireframe
edges are admitted as geometric port-links here; they are not promoted to native
primitive commands. The original repeated-C1 source walk is tested separately.

## The three incoming paths and actual matrices

The P/N shared face supplies three two-edge geometric C0-to-C2 paths:

    C0 -> M0 -> C2
    C0 -> C1 -> C2
    C0 -> M1 -> C2.

Decode their intermediate presentations to the C0 configuration frame:

    R_M0 q_M0 = R_C1 q_C1 = R_M1 q_M1 = q_in,
    identity_M0 = identity_C1 = identity_M1 = identity_in.

The matrices derived from the actual tetrahedron edge frames are:

    R_M0 = [-1 -1 -1;  0  1  0;  0  0  1]
    R_C1 = [ 0  1  0; -1 -1 -1;  0  0  1]
    R_M1 = [ 0  1  0;  0  0  1; -1 -1 -1].

Consequently the incoming coordinate equations are

    [R_M0  -R_C1     0  ] [q_M0]   [0]
    [  0    R_C1  -R_M1] [q_C1] = [0].
                           [q_M1]

This6×9 system has rank6, leaving three free coordinate components. Identity
agreement is checked independently on the actual labels.

## Output at C2

For the same identity, the output configuration is

    q_out = S q_in,

    S = inverse(F_C2) F_C0
      = (1/3) [ 1 -2 -2;
               -2  1 -2;
               -2 -2  1].

S is a boundary-frame conversion, not a claimed native particle operation.
The three short paths and all31 simple geometric C0-to-C2 paths give exactly
this matrix. Their histories remain distinct. The original source history
C0/M0/C1/M1/C1/C2 yields the same boundary configuration, retaining both C1
occurrences rather than deduplicating its history.

## No silent averaging of incompatible packets

Let E stack the three inverse R matrices and D=(1/3)[R_M0 R_C1 R_M1]. Then

    D E = I3,
    Pi = E D,  Pi^2 = Pi,
    r = (I9-Pi) q,
    q = E D q + r.

The decoder is lossless on compatible incoming presentations. All six transverse
coordinate directions remain in r for arbitrary inputs. A nonzero r rejects
recombination; it is not discarded to manufacture agreement. Mismatched identity
labels also reject recombination, even with identical coordinate values.

## Full network and the second attachment

| Network | Coordinate variables | Edge equations | Rank | Free coordinates |
|---|---:|---:|---:|---:|
| P/N/E, six geometric vertices |18|36|15|3|
| P/N/E/E2, seven geometric vertices |21|45|18|3|

Fixing the three input coordinates at C0 gives a unique solution at every port
in both networks. The same one complex identity is carried throughout.

E2 is the geometric attachment M2/C1/C2[M3], with
M3=(-83/27,13/27,-77/27), obtained by reflecting M1 across M2/C1/C2. It is regular
and has disjoint interiors from the existing bodies; no original point or port
frame moves. All59 simple geometric paths in the enlarged graph give the same
boundary matrix. This is an admitted geometric attachment, not an established
independent electron excitation.

### General result: this law cannot give an occupancy restriction

Writing B for the connected graph's incidence matrix, the system is

    A = (B tensor I3) blockdiag(F_v).

Since all frames are invertible, rank(A)=3(n-1) for n vertices. It always leaves
three free configuration coordinates. Adding another consistently framed carrier
therefore cannot produce a one-electron exclusion under THIS law. Boundary
identity transport and frame compatibility are constructed; an additional
source-supported interaction/occupancy constraint has not been supplied.

A common rigid configuration shift is another compatible state. No restoring
force, energy minimum, binding or physical stability is inferred from these
frame relations.

## Verification

    python research/strominger/checkers/check_identity_bearing_port_equations_v1.py

27 exact groups pass. They include actual geometry/frame construction, inverse
and metric checks, three-cut ranks, complete residual recovery, all-path transport,
identity/history retention, incompatible identity and coordinate controls,
nonmonomial frame changes, a corrupted-link loop obstruction, and both attachment
networks. The complete matrices, numerical example, solutions and source hashes
are in `results/identity-bearing-port-equations-v1.json`.

Prospective specification: `contracts/identity-bearing-port-equations-v1.json`.
The first execution encountered a syntax typo and the second a Windows subprocess
encoding error; both were corrected without changing the mathematical gates.
No browser, shared fixture, native producer, SCC registration or conjecture-net
status was changed.
