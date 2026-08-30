# Connected four-point constructor task

Work package: WP559  
Owner: marici.Figueiredo

## Question

Can WP133's formal four-point port be derived from a declared source operation
rather than fitted after inspecting the isospectral rival?

## Frozen task grammar

On the bounded two-adjoint hostile sector, freeze one canonically normalized
real source coordinate \(\varphi\) with local action term

\[
V(\varphi)={m^2\over2}\varphi^2+{\lambda\over4}\varphi^4.
\]

The source operations are fixed before choosing the rival values:

\[
\Gamma^{(2)}(0)=\left.{d^2V\over d\varphi^2}\right|_{\varphi=0}=m^2,
\qquad
\Gamma^{(4)}(0)=\left.{d^4V\over d\varphi^4}\right|_{\varphi=0}=6\lambda.
\]

Thus equal \(m^2\) makes two constructors isospectral at tree level, while a
nonzero difference in \(\lambda\) is detected by the connected amputated
four-point vertex. The operation is derived from the same action grammar for
every constructor; it is not one bespoke observable per rival.

## Exact bounded separation

Freeze the hostile values \(\lambda=0\) and \(\lambda=1\). Their two-point
responses agree exactly and their normalized four-point responses are zero and
one. Appending this source-derived row to WP133's three two-point rows raises
the four-constructor response rank from three to four and kills its
one-dimensional kernel.

The task is constructor-sensitive because it probes an interaction derivative
that the two-point functor erases. It does not reconstruct a constructor from
`physical16`; it defines a new multipoint source experiment.

## Executability boundary

Algebraic source authorization is not executable control. A physical task
would require:

- preparation or production of the relevant adjoint/flavon excitations;
- four external channels with calibrated kinematics and normalization;
- amputation or an equivalent scattering observable;
- finite widths, mixing, thresholds, backgrounds, and detector response;
- a covariance-bearing likelihood over a source class frozen before data.

None is present. In the decoupled or inaccessible branch, the constructor
task has no physical support even though the action derivative exists.

## Selector status

The four-point task can identify the bounded isospectral pair if instrumented.
It does not remove either constructor from the admissible source family and
does not select \(g_Ff/v\). Identification and selection remain independent.

The smallest exact falsifier is the hostile pair with common \(m^2\) and
\(\lambda=0,1\): the Hessian agrees while the fourth derivative differs by
six.

## Status

WP559 supplies a source-derived constructor-sensitive operation and exact
finite-family separation theorem. Its physical instrument is absent.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp559_connected_four_point_constructor_task.py

The generated result is
research/flavor/results/wp559_connected_four_point_constructor_task.json.
