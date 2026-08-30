# Spin(5) Anomaly-Completion Beta Fiber

## Question

Does anomaly cancellation uniquely determine the additional matter needed for
the full simple-parent fixed-point calculation opened by WP877--WP878?

## Frozen portal multiplets

Use left-handed conventions and normalize the Spin(5) indices by

\[
T(5)=1,
\qquad
T(4)=\frac12.
\]

For each of three families, the minimal portal Yukawa packet contains

\[
4_{-1/2}\oplus5_{+1}.
\]

The vector charge is the charge of the left-handed conjugate of the
right-handed WP736 mediator. Per family, this packet has anomaly coordinates

\[
\begin{aligned}
A_{Spin(5)^2Y}&=\frac34,\\
A_{\mathrm{grav}^2Y}&=3,\\
A_{Y^3}&=\frac92.
\end{aligned}
\]

The three-family packet also contains three Spin(5) spinors, so its global
spinor parity is odd before completion.

## Completion A: conjugate packet

Per family add

\[
4_{+1/2}\oplus5_{-1}.
\]

Its anomaly vector is

\[
\left(-\frac34,-3,-\frac92\right),
\]

and its Spin(5) Dynkin-index sum is \(3/2\). Across three families the total
number of spinors becomes six, so the global parity obstruction also cancels.
This is the smallest representation-by-representation conjugate completion.

## Completion B: chiral packet

An inequivalent half-integer-lattice completion exists. Per family add

\[
4_{-3/2}\oplus1_0\oplus1_{+1}\oplus1_{+2}.
\]

Its mixed anomaly is

\[
\frac12\left(-\frac32\right)=-\frac34.
\]

Its Abelian anomalies are

\[
4\left(-\frac32\right)+(0+1+2)=-3,
\]

and

\[
4\left(-\frac32\right)^3+(0^3+1^3+2^3)
=-\frac92.
\]

It therefore cancels exactly the same local and global anomaly packet. Its
Spin(5) Dynkin-index sum is only \(1/2\) per family.

## Exact beta-coefficient split

Include the shared portal fermions, one complex spinor Higgs, and the two real
fundamental breaking fields required by WP877. With
\(C_2(Spin(5))=3\), the one-loop coefficient is

\[
b_0=
\frac{11}{3}C_2(G)
-\frac23\sum_{\rm Weyl}T(R_f)
-\frac13\sum_{\rm complex}T(R_s).
\]

The two real vectors count as one complex vector. The scalar subtraction is
therefore \(1/2\). The two completions give

\[
b_0^{A}=\frac92,
\qquad
b_0^{B}=\frac{13}{2}.
\]

Both are asymptotically free at one loop, but they differ by

\[
b_0^{B}-b_0^{A}=2.
\]

Consequently anomaly cancellation does not define one beta system or one
common-coupling magnitude. It supplies a fiber of ultraviolet constructors
whose RG data differ before Yukawa and two-loop terms are considered.

## Why minimality does not close the fiber

Completion A uses fewer multiplets and admits representation-paired mass
terms. Completion B is chiral and requires a separate mass-generation
mechanism. These are useful physical distinctions, but “fewest multiplets”
and “immediately massable” are not consequences of anomaly cancellation.
Promoting either to selection authority requires a declared source principle
and then its own threshold consequences.

Adding arbitrary vectorlike pairs produces an even larger kernel, but the
displayed hostile does not rely on that trivial enlargement. The two
completions already differ in their chiral charge grammar.

## Disposition

Negative uniqueness theorem. The sequential simple parent fixes the ordered
dimensionless portal operator \(H\), but local anomalies and global spinor
parity do not uniquely fix the matter packet that controls the common
coefficient \(g\). Therefore no single “complete Spin(5) fixed point” is yet
source-authorized.

The next admissible source principle must select between these completions
before beta functions are solved. Candidate selectors include a literal
higher-dimensional zero-mode index, a parent representation that contains
exactly one completion, or a locality/normalizability theorem that derives
the chiral spectrum and its mass operators. Minimal field count chosen after
examining the beta function is excluded.

## Claim boundary

This packet proves nonuniqueness of anomaly-compatible matter and the exact
one-loop Spin(5) coefficient split. It does not derive either completion's
full Yukawa grammar, two-loop fixed points, global basin, finite thresholds,
or physical instrument. High-charge singlets in completion B may face further
phenomenological exclusions; those exclusions are additional probes, not
anomaly identities.

## Smallest exact falsifier

The per-family packets

\[
4_{+1/2}\oplus5_{-1}
\quad\text{and}\quad
4_{-3/2}\oplus1_0\oplus1_{+1}\oplus1_{+2}
\]

cancel the same portal anomaly vector while changing the three-family Spin(5)
fermion index by \(3\), hence changing \(b_0\) by \(2\).

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp879_spin5_anomaly_completion_beta_fiber.py
~~~

