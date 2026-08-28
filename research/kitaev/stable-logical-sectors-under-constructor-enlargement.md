# Stable logical sectors under constructor enlargement

## Question

Given authorized logical-stage maps

\[
f_{n,m}:H_n\longrightarrow H_m,
\qquad H_n=Z_n/R_n,
\]

which stage-\(n\) distinctions survive the directed constructor system, and when do probes faithfully observe those surviving distinctions?

A logical map exists only if the underlying enlargement preserves admissible states and sends \(R_n\) into \(R_m\). Identity and composition are required.

## Claim boundary

Define the eventual-death kernel

\[
D_n=\bigcup_{m\ge n}\ker f_{n,m}.
\]

For a filtered system of modules, two elements \(x,y\in H_n\) have the same colimit image exactly when \(x-y\in D_n\). Therefore

\[
H_n^{\mathrm{surv}}=H_n/D_n
\]

is the constructor-stable quotient of the stage-\(n\) logical sector.

Proof: equality in a filtered colimit is eventual equality. The colimit images of \(x\) and \(y\) agree exactly when a common later map kills \(x-y\).

Arbitrary stagewise probes do not define observations of this quotient. A class can be visible at one stage and killed at a later stage. To observe the stable sector, use a compatible probe cocone: maps

\[
p_n:H_n\longrightarrow O
\]

into one declared observation object satisfying

\[
p_m f_{n,m}=p_n.
\]

Compatibility implies \(D_n\subseteq\ker p_n\), so \(p_n\) factors uniquely through \(H_n/D_n\). For a family of compatible cocones \(p_n^\alpha\), define

\[
B_n=\bigcap_\alpha\ker p_n^\alpha.
\]

The family is jointly faithful on the constructor-stable quotient exactly when

\[
B_n=D_n.
\]

Without cocone compatibility, stagewise probe agreement is not a statement about the colimit.

For ordinary cellular subdivisions of a fixed torus, refinement maps are chain-homotopy equivalences and induce isomorphisms on

\[
H_1\simeq\mathbf F_2^2.
\]

Hence \(D_n=0\): neither noncontractible class dies under local subdivision. Local syndrome is blind to both classes, while two independent noncontractible loop probes give faithful coordinates.

Killing a torus class requires an enlargement that admits a filler for a formerly noncontractible loop, changes topology, changes coefficients, or imposes a nonlocal identification. That operation changes the constructor theory; it is not compilation inside the original local theory.

The cross-sector comparisons are typed as follows:

- Benincasa's rank-20 depth-transition kernel consists of certified one-step deaths. Its rank-1353 cokernel consists of new births. Neither fixes the colimit without later transition maps.
- Aspect's synthetic positive-degree cycle dies when a deeper authorized square supplies its boundary. The square is a finite death witness.
- Figueiredo's acyclic vectorlike stabilization is homologically invisible but spectrally active. This is blindness of the homology/anomaly lens, not equality in the richer chain-level constructor object.
- Grothendieck's primitive reciprocal pair is a boundary of the existing sewing cell, hence a constructor death inside that complex. Failure of separate scalar limits to select the seam is observational blindness unless a mixed-depth incidence is constructed.

This packet proves a filtered-colimit theorem conditional on typed transition maps and compatible probes. It does not prove that Benincasa's depth system stabilizes, that all Aspect net classes vanish in an unbounded semantic completion, or that any physical probe cocone is realizable.

## Disposition

The relevant equivalence is eventual constructor equivalence, not scalar equivalence. A readout certifies the stable logical sector only when it forms a compatible cocone and its joint kernel equals the eventual-death kernel.

The first falsifier is one of:

1. an enlargement fails to send repairs to repairs, so \(f_{n,m}\) is undefined;
2. composition fails, so there is no directed system;
3. a claimed death lacks a finite later-stage null witness;
4. a claimed stable class is killed by an authorized later filler;
5. a proposed stable probe violates \(p_m f_{n,m}=p_n\);
6. \(B_n/D_n\ne0\), exposing a surviving class invisible to every compatible probe;
7. a claimed local compilation kills a torus class only by changing the constructor theory.

The next finite audit must use at least three consecutive transitions and report kernels of composites, images, births, deaths, and probe-compatibility residuals. A one-step rank loss cannot establish eventual stabilization.
