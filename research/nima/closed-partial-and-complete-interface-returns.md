# Closed returns through partial and complete interfaces

## Partial request: constrained minimum change

A triangle-view increment dy requests a source change dx satisfying

    T2*dx=dy,
    d2_source*dx=0.

Among these changes choose the minimum of84*||dx||^2, the retained rectangle
metric. The combined constraint matrix has rank392:279 independent view
constraints on closed states plus113 source-closure constraints. Its nullspace
is the760-dimensional hidden closed-mode space.

The exact solver selects independent constraint rows C and solves

    (C*C^T)*p=rhs_selected,
    dx=C^T*p.

It then checks every original constraint. Consistency gives feasibility, and
membership in the row space gives orthogonality to every free hidden direction,
proving minimum cost. Inconsistent requests are rejected. The constant weight84
affects cost but not the minimizer.

The solver uses exact rational FLINT arithmetic. It also supplies a fallback
for live view reconstruction when floating-point multiplier proposals cannot
recover the required rational coefficients.

## Hidden content is preserved

For any other compatible update v,

    v=dx+k, with T2*k=0 and d2_source*k=0,
    cost(v)=cost(dx)+cost(k).

Thus the minimum partial return leaves the current orthogonal hidden component
unchanged. It does not set hidden records to zero. The checker verifies this
split on a request containing harmonic, visible internal and hidden internal
components.

For fixed topology and metric, let L be this right inverse on the admissible
view image. Absolute replacement is put(x,y)=x+L(y-T2*x). It satisfies the content
GetPut, PutGet and PutPut laws because T2*L is identity on that image and L is
linear. The executable tests include zero, doubled and successive requests.
Operational versions and histories still record the actual commits.

## Complete request: unique source change

Adding the760 selected source-cell readings to the triangle view gives a full-
rank interface on closed states. Exact elimination with the actual requested
values reconstructs its unique source increment. If those extra readings equal
the partial optimum's readings, the two returns agree. Otherwise they select
the additional hidden change and its exact cost.

The complete interface uses a labelled coordinate selection. Its induced cost
is84 times the squared norm of the decoded source increment; it is generally
not the unweighted norm of the interface readings.

## Compatibility is stronger than target closure

The checker constructs a closed target triangle chain outside the image of the
closed source space. Both return interfaces reject it. Being a valid target
cycle alone does not imply that this chosen comparison map can realize it.
The admissible readout domain is the actual source image.

## Versioned execution

The resulting source increment is decomposed into parent-class changes
(delta_hi=14*<Zi,dx>) and a zero-class closed internal change. It then uses the
existing live-store commit path, including version validation, full derived
rebuild, exact quotient/residual cost and retained events.

Tests commit a partial optimum, then its hidden completion to reach the complete
request with no further triangle-view change. A parent update invalidates an
older computed request. Compensation restores the earlier full source state
with fresh revisions.

## Structural result

Both interfaces now have executable read/return contracts on the same costed
closed state. Partial observation gives a760-dimensional response ambiguity;
minimum change resolves the update while preserving existing hidden content.
Complete observation resolves the state uniquely and exposes the corresponding
extra edit cost.

A next synthesis test can compare different presentation maps: identify which
requests describe the same source constraint, and verify that their induced
metrics give identical closed returns. Merely sharing a target homology class
is weaker than specifying the same cell-level request.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_closed_interface_returns.py

Exact constrained normal equations, compatible/incompatible partial targets,
complete decoding, zero/linear replacement checks, orthogonal hidden completion,
cost splitting, live commit, stale-request rejection and compensation. Shared
solver: checkers/exact_minimum_lift.py. The model retains its fixed topology and
serialized in-memory transaction scope.
