# The smallest theta coherence cube stops at the absent parameter connection

## Source-instantiation audit

The relative cubical contract is frozen. The next question is not whether a synthetic cube can be made to commute, but whether the existing theta source records authorize every port of the smallest cutoff/parameter/reciprocal cube.

Take one finite labelled cutoff \(X\), one extension \(Y=X\sqcup\{p\}\) adding a prime or grade block, a parameter segment \(\gamma:s_0\to s_1\), and reciprocal reflection
\[
\rho(s)=1-\overline{s}
\]
in the full spectral plane. On a real normal slice this reduces to the earlier \(z\mapsto1-z\) model.

## Constructor inventory

### Cutoff edge: present at finite level

The finite labelled records authorize
\[
\iota_{X,Y}:V_X\longrightarrow V_Y
\]
by zero-padding the added labelled coordinate while preserving all old rates and incidences. They establish exact naturality for direct-sector constraints, reciprocal-sector constraints, equalizer formation, and endpoint-jet truncation.

Status: **present, finite only**.

This does not authorize the completed cutoff edge, since the source pushout record still withholds closed range and commutation with completion.

### Reciprocal edge: present on the Real-paired finite carrier

For a real source on the centered seam, the prime-orbit records authorize an antiunitary exchange
\[
J_X:\mathcal H^+_X(s)\longrightarrow\mathcal H^-_X(\rho(s))
\]
from conjugate shell returns and reciprocal prime weights. The record also establishes the seam as the isometric locus.

Status: **present on the declared finite Real carrier**.

Off the seam, the same formula is a reciprocal comparison but not an isometry. Low-grade completion additionally requires paired source counterterms, which remain withheld.

### Parameter edge: fiber family present, connection absent

The finite equalizer record gives matrices depending algebraically on \(z\):
\[
D_{+,X}(z),\qquad D_{-,X}(z),
\]
and proves rank statements pointwise. Pointwise dependence does not define an edge intertwiner
\[
G_{\gamma,X}:\mathcal F_X(s_0)\longrightarrow\mathcal F_X(s_1).
\]
No inspected source record supplies:

- a common source-authorized trivialization of the reduced carriers along \(\gamma\);
- a differentiable Riesz projection family on that carrier;
- a Kato connection or equivalent parallel-transport equation;
- endpoint comparison matrices satisfying the declared gauge law.

Status: **absent constructor**.

Therefore the contract stops before evaluating any cutoff/parameter or parameter/reciprocal face equation.

### Crossing wall factor: absent and not required on an admissible patch

No independent source constructor currently supplies a finite crossing complex and determinant clutching factor for this theta packet. It must not be inserted as identity. If \(\gamma\) is declared contour-admissible and avoids a crossing wall, the wall port is out of scope rather than unit-filled. If a crossing is claimed, the packet is incomplete until the wall factor is source-derived.

Status: **absent conditional port**.

## Contract packet result

The smallest source packet has the following outcome:

    verdict: incomplete
    first_absent_constructor: parameter_connection
    first_failed_degree: null
    equation_evaluation_started: false
    cutoff_edge: finite_source_authorized
    reciprocal_edge: finite_real_source_authorized
    parameter_edge: missing
    wall_factor: not_applicable_on_wall_free_patch | missing_if_crossing_claimed
    determinant_shadow: not_evaluated

This is not a failed degree-two coherence equation. A face residual cannot be formed until all four boundary transports exist. Assigning \(G_{\gamma,X}=I\) would confuse a fixed coordinate presentation with source-authorized continuation and would manufacture the desired square.

## Why the old finite cube is insufficient

The earlier equalizer cube proves that zero-padding commutes with pointwise sector matrices. It does not compare fibers at two distinct parameter values. Likewise, exact reciprocal conjugacy at each parameter does not prove that reciprocal transport commutes with continuation along a path.

The missing port is specifically a connection on the source-generated reduced theta carrier, not another scalar analytic formula.

## Minimal next theorem

On a contour-admissible parameter patch \(U\), construct a fixed source-generated carrier \(\mathcal H^{\mathrm{red}}_{X,U}\) and an analytic Fredholm pencil \(T_X(s)\) with norm-differentiable Riesz projections
\[
P_X(s)=\frac{1}{2\pi i}\int_\Gamma(z-T_X(s))^{-1}\,dz.
\]
Then define Kato transport by
\[
\dot G_{\gamma,X}(t)
=
[\dot P_X(t),P_X(t)]G_{\gamma,X}(t),
\qquad
G_{\gamma,X}(0)=I.
\]
The required source theorem must also prove naturality with finite cutoff inclusion and reciprocal exchange:
\[
\iota_{X,Y}G_{\gamma,X}
=
G_{\gamma,Y}\iota_{X,Y},
\]
and
\[
J_X(s_1)G_{\gamma,X}
=
G_{\rho\gamma,X}J_X(s_0).
\]

Only after these equations are typed and their operators exist may the finite contract compute face residuals.

## Hostile distinction

A synthetic \(\mathrm{GL}_2\) cube verifies contract semantics. It supplies no evidence that theta source data define \(G_{\gamma,X}\). Conversely, pointwise analyticity of matrix entries does not select a gauge-covariant connection. The source-instantiation result must remain **incomplete**, not “coherent by identity transport.”

## Research consequence

The obstruction tower has now reached its first concrete missing analytic constructor:

> construct the source-authorized parameter connection on the finite reduced theta/Riesz carrier and prove cutoff and reciprocal naturality.

This is earlier than the determinant-gerbe gate and earlier than any RH-strength spectral exclusion. It is the first port whose absence prevents the abstract coherence tower from touching the actual theta realization.
