# The certified twenty-point Xi Gram feature is a finite positive filler of the H134--H234 horn

## Lattice location

The relevant elementary cell has vertices

\[
V_1=(6,0,1,0),
\quad
V_2=(5,0,2,0),
\quad
V_3=(5,1,1,0),
\quad
V_4=(5,0,1,1).
\]

The metric residual belongs to the combined horn

\[
H_{134}\cup H_{234},
\]

whose common edge is

\[
V_3\to V_4.
\]

It is an interior filler, not an additional lattice vertex.

## Certified finite carrier

Let \(Z=\{z_1,\ldots,z_{20}\}\) be the point packet recorded in

`research/voevodsky/results/arb-certified-physical-xi-packet-ldl.json`.

Form the physical Xi de Branges matrix

\[
K_Z
=
[\mathcal D(z_j,z_k)]_{j,k=1}^{20}.
\]

Arb arithmetic certifies an \(LDL^*\) factorization

\[
K_Z=L_ZD_ZL_Z^*,
\qquad
D_Z>0.
\]

Define

\[
F_Z
=
D_Z^{1/2}L_Z^*.
\]

Then the checker certifies entrywise in complex ball arithmetic that

\[
K_Z=F_Z^*F_Z.
\]

Thus \(F_Z\) is an actual positive finite filler for the metric horn restricted to the observer packet \(Z\).

## Control role

On this finite packet:

- \(K_Z\) is the closed-loop storage residual;
- \(F_Z\) is its storage-output or defect feature;
- \(F_Z^*F_Z\) is the finite KYP certificate;
- the negative Krein--Langer feature has rank zero.

Consequently, the packetwise Douglas constructor accepts and returns a positive realization.

## Coherence strength

The twenty points were factored as one matrix. Hence the certificate includes all cross terms among:

1. the horizontal height-one packet;
2. the mixed-height packet;
3. the low-height packet;
4. pairs near the first four critical zeros.

It is stronger than twenty diagonal inequalities or five unrelated four-point certificates.

The construction persists on an independently varying product box of radius \(10^{-60}\) around all forty real coordinates. Larger coordinate boxes are separately certified for the original four-point packets.

## What has not been identified

The feature \(F_Z\) is obtained from the physical Gram matrix by certified \(LDL^*\). It has not been shown to equal the restriction of a source-defined universal feature on the theta, prime, or resolved-graph carrier.

In particular, the calculation does not provide:

1. naturality under adjoining arbitrary new observers;
2. a uniform lower bound as packet size grows;
3. a source formula for the transition maps between packet features;
4. vanishing of the global Krein--Langer denominator.

Unrelated Cholesky gauges would not provide these properties. The canonical packet embedding must instead be defined through the physical kernel sections themselves.

## Exact next gate

For nested packets \(Z\subset Z'\), the Gram identity gives a canonical isometry

\[
\operatorname{span}\{R_z:z\in Z\}
\longrightarrow
\operatorname{span}\{R_z:z\in Z'\},
\qquad
R_z\mapsto R_z.
\]

The next finite coherence calculation is to construct this isometry explicitly between certified factorizations and verify it in ball arithmetic. This removes the arbitrary \(LDL^*\) gauge at the finite level.

A directed limit over all packets would still require positivity for every packet, which is the universal theorem.

## Scope

The result is a rigorous finite positive filler at the existing horn location. It is not a new lattice coordinate and does not prove the global positive lift.
