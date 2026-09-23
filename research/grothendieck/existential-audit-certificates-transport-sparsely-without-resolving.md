# Existential audit certificates transport sparsely without re-solving

## Result

A checked fine linear certificate whose objective ignores a retired audit can
be transported into a sparse combination of projected pair rows by algebra
alone. The weighted bound is preserved EXACTLY. For the supported joint LP
proof convention, the number of nonzero multipliers never increases.

The transformation does not build the complete projected dictionary and does
not call an optimizer. Reverse expansion is also algebraic. This supplies the
proof-transport component of the envelope program, not yet a complete compact
state representation closed under arbitrary repeated retirement.

## 1. Balanced certificate theorem

Let the expected fine inequalities be

    a_i dot y + c_i h <= b_i.

Suppose a nonnegative multiplier vector lambda satisfies

    sum_i lambda_i*c_i = 0.

Write P,N,Z for its ACTIVE positive, negative and zero h-coefficient rows,
and let p,n,z be their counts. The positive supplies and negative demands are

    s_i=lambda_i*c_i                 (i in P),
    t_j=lambda_j*(-c_j)              (j in N).

They have equal total mass. Match supplies to demands in index order, sending
min(remaining supply, remaining demand) at each step. Let gamma_ij be the
resulting nonnegative flows. Every step exhausts at least one active endpoint;
the final step exhausts both. Thus there are at most p+n-1 nonzero flows when
both sign families exist.

For each nonzero flow use the projected pair row

    (a_i/c_i-a_j/c_j) dot y <= b_i/c_i-b_j/c_j

with multiplier gamma_ij. Carry zero rows with multiplier lambda_i.
The marginal identities give

    sum_j gamma_ij/c_i = lambda_i,
    sum_i gamma_ij/(-c_j) = lambda_j.

Consequently expanding the projected proof recovers the ENTIRE original
multiplier vector, not merely its summed normal. The projected normal and
bound are exactly

    sum_i lambda_i*a_i,  sum_i lambda_i*b_i.

If k=p+n+z, the output uses at most k-1 terms when signed rows participate,
and exactly k zero-row terms otherwise. There is no search over all p*n pairs.

This is a transportation decomposition of a balanced nonnegative combination;
the construction is elementary, not a new general elimination theorem.

## 2. The owning joint solver's nonnegativity convention

The joint backend allows a dual combined normal >= the objective
componentwise, because all joint coordinates are nonnegative. An objective
ignoring h can therefore have an input certificate with excess retired
coefficient beta>=0, rather than exactly zero.

Before matching, add weight beta to the explicitly verified row

    -h <= 0.

This cancels the retired coefficient and changes neither the public normal
nor the bound. If beta>0, the correction adds at most one active row, and
signed matching then removes at least one term. Therefore the projected
proof has at most the ORIGINAL k nonzero multipliers.

The correction is permitted only when this exact zero-bound row belongs to
the verified context. It is not an arbitrary cancellation rule for shifted
coordinates or a row -h<=b with nonzero b. The normalized local-coordinate
families below use exactly balanced inputs and need no such assumption.

This is the existential analogue of the pinned bridge's correction step,
but the mechanism differs: an unfixed audit is eliminated by balancing
positive and negative coefficient mass, not by substituting a known value.

## 3. Optimality and inconsistency survive

For an optimality proof, project its admitted joint point and retain its
source witness as evidence of membership in the exact public projection.
The public objective has the same value, and the transported upper bound is
unchanged, proving the same optimum. Different witnesses need not be selected.

For a Farkas proof with combined normal >=0 and negative bound, the correction
and matching leave the public normal >=0 and preserve the negative bound.
This contradicts nonnegative public coordinates. For exact zero-normal rays,
the public normal remains exactly zero without a repair.

No solver exception supplies either proof. The input certificate is checked
against its expected source, schema, history and query before transport.

## 4. Reverse domain and composition

The reverse transformation accepts nonnegative combinations of the declared
projected zero rows and normalized positive/negative pair rows. Replace each
pair weight gamma by gamma/c_i on its positive fine row and -gamma/c_j on
its negative fine row. Merge repeated indices. The result has the same public
normal and bound and zero retired normal.

This accepts independently supplied projected combinations, not only the
syntax produced by the forward matcher. It introduces at most two fine
contributions per pair and one per zero row before aggregation. An arbitrary
compacted summary row requires its own checked derivation before this reverse
rule applies. Unrelated source-space formats and cut traces are not silently
coerced into this proof language.

Forward then reverse recovers the normalized input multipliers, including any
explicit nonnegativity repair. Reverse then forward need not recover the
same pair syntax. It can re-pair the same marginals much more sparsely.

The theorem can be applied successively when each next retired coordinate is
ignored by the retained objective and the appropriate row semantics remain
available. Proof support does not increase at each step. A control composes
three exact eliminations with support counts 32 -> 16 -> 8 -> 8, preserving
the final inequality -16*z<=85/8.

That is a certificate-composition statement. It does not bound the complete
projected state, coefficient bit growth or the storage of nested derivations.
Inlining old derivations and sharing a proof graph have different costs.

## 5. Sharp sparse transport on the quadratic projection family

Use the previously source-certified m=4 local box and evidence

    H >= 2a_i*x-a_i^2,
    H <= z-2a_j*y+a_j^2,
    a_i=(2i+1-n)/n.

Retiring H produces n^2 genuine evidence-pair facets. Assign weight one to
each upper-H row. Assign weights 1+1/(2n) to the first n-1 lower-H rows and
1-(n-1)/(2n) to the last. Both total masses equal n.

The transport emits exactly 2n-1 pair terms. This support bound is sharp for
recovering these specified marginals: no proper subset of the negative
weights has integer total, while every subset of positive weights does.
Thus a feasible bipartite support cannot have a proper balanced component;
it must be connected and have at least 2n-1 edges.

This is sharpness for transport of the GIVEN fine weights, not a claim that
no different fine proof or public proof can establish the same bound more
sparsely. The synthetic weighted combinations are valid bounds, not asserted
optimality certificates.

At n=256, 512 active fine weights become 511 projected terms despite 65,536
evidence-pair facets. The full raw dictionary also has box-related pairs and
zero rows; it is not materialized by the transport.

An independent reverse control starts with all 256 pair rows at n=16, each
weighted one. Reverse expansion followed by fresh matching yields only 16
pair terms with exactly the same combined inequality. It does not merely
undo the syntax of a prior forward run.

## 6. Verification and delivered artifacts

The producer first replays the existing independent audit-elimination
verifier. The upstream axis-query requests are checked against their frozen
expected direction list, in addition to the expected history and source.
It then transports:

- 12 checked joint optimum/inconsistency certificates;
- two explicit repair controls, one optimum and one contradiction;
- seven envelope families, n=2,3,4,8,16,64,256;
- one independently specified dense reverse proof;
- a three-elimination certificate chain.

The new independent verifier imports neither the transporter nor an optimizer.
It reconstructs each expected row context, validates statement digests,
checks every pair sign and flow marginal, verifies exact recovery of normalized
fine weights, and checks preserved bounds and projected witnesses. It also
checks the reverse and composed proofs independently.

Seven mutations are rejected: negative flow, omitted pair, reversed pair
signs, wrong retired position, omitted repair, wrong repair weight and a
wrong repair row. Verification refuses optimized Python execution.

Files:

- `checkers/audit_certificate_transport.py`
- `checkers/check_audit_certificate_transport.py`
- `checkers/verify_audit_certificate_transport.py`
- `results/audit-certificate-transport-contract.json`
- `results/audit-certificate-transport.json.gz`

Both reproduction commands are optimizer-free:

    python research/grothendieck/checkers/check_audit_certificate_transport.py
    python research/grothendieck/checkers/verify_audit_certificate_transport.py

This is fresh replay of existing source-relative certificates, not a fresh
upstream analytical source-admission proof. The result does not change the
owning API, authenticate observations or establish an actual source.

## 7. Resource and capability boundary

The matching phase uses O(k) rational arithmetic steps on active weights.
The implementation also scans/decodes the supplied row table; validation and
reconstruction of rows cost additional work. Reverse expansion currently
allocates a vector indexed by the supplied fine rows. Rational arithmetic
steps are not constant-time bit operations.

The output stores pair references and weights, not a complete boundary table.
Those references require the expected fine-row context or separately checked
row derivations. Nonzero multiplier counts do not measure the full statement,
source witness, provenance archive or certificate encoding. This result
therefore makes no total-storage-compression claim.

Most importantly, a sparse proof of ONE bound is not a presentation of the
possibility set. Treating its selected rows as the new state would repeat the
implication-only error: omitted projected constraints can admit false public
possibilities. State replacement still requires complete pair coverage or an
exact envelope membership/separation contract.

Public-only continuation preservation remains the scope of an exact projected
state. Sparse proof transport does not authorize re-exposure of a retired
audit or reconstruct discarded fine evidence.

## Synthesis

Quadratic projected geometry does not force quadratic transport of each
linear certificate. Balanced row mass gives a sparse algebraic bridge in both
directions, and the bridge composes at the level of proofs.

The remaining envelope target is now more focused: complete state-relative
membership/separation and controlled representation growth under successive
retirement and surviving-schema refinement. Its proof layer need not invoke
a fresh optimizer merely to translate a certificate already obtained.

Related notes:

- `audit-elimination-has-certified-savings-and-quadratic-projection-cost.md`
- `../voevodsky/pinned-source-certificates-project-back-without-resolving.md`
- `../voevodsky/certified-audit-elimination-needs-pair-coverage-not-just-valid-cuts.md`
- `../voevodsky/sufficient-state-is-relative-to-permitted-continuations.md`
