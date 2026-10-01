# State-dependent mean return: laws and an insertion obstruction

## 1. Content fibre and complete presentations

Fix a finite live ID set I and endpoint assignment e. The scalar content fibre
is X_(I,e)=Q^I. Let F be a nonempty subset of I selected by a retained family.
Define the mean and absolute-target return by

    get_F(x) = sum_{i in F} x_i / |F|,
    put_F(x,y) = x + (y-get_F(x)) 1_F.

The latter is the unique least-Euclidean-change update attaining target y.
For any other admissible update u=delta*1_F+r on F, sum r_i=0 and
||u||^2=|F|*delta^2+||r||^2; changes outside F only add cost. This proves
minimality without a finite numerical search.

This is an ordinary well-behaved lens on fixed content:

    GetPut: put_F(x,get_F(x)) = x,
    PutGet: get_F(put_F(x,y)) = y,
    PutPut: put_F(put_F(x,y),z) = put_F(x,z).

Proof: the first shift is zero; the second mean is get_F(x)+y-get_F(x)=y;
and the two shifts telescope to z-get_F(x). Values outside F and residuals
x_i-get_F(x) inside F are unchanged. These are frame and residual laws.

For a bijective renaming pi:I->J, transporting the members and values gives

    pi_* put_F(x,y) = put_(pi F)(pi_* x,y).

Indeed summation and cardinality are preserved, as is 1_F. Thus complete
reindexing is a lens-compatible presentation change.

## 2. Versioned stores are not the same lens

Let S be the operational state: live records, versions, identity registry,
accepted event log and compensation stack. Projection c:S->X_(I,e) forgets
metadata. A successful version-scoped return implements the content law after
applying c. It does NOT generally satisfy these lens equations as equality in S.

In the current Store a successful zero shift still creates an event and advances
versions. Therefore full-store GetPut fails. Two absolute-target returns have
the same final content as the last return alone, but not the same event history.
Compensation likewise restores content, not old authority to edit it.

The right specification is a content lens with a separate partial, state-indexed
transaction interface. A request is admissible only for its current family and
descendant versions. Rejection leaves the store unchanged. Acceptance projects
to the requested content action and records a fresh transition. This is not yet
a dependent-type encoding or a machine-checked general theorem.

## 3. Insertion is not unqualified lens transport

Insert a fresh member j with value v into family F of size n. Write I_v for
that insertion and U_(F,delta) for a fixed increment on the old member IDs.
Then

    I_v U_(F,delta)(x) = U_(F,delta) I_v(x).

The right-hand action is still scoped to F, NOT to F union {j}. If its scope
is expanded to the current family, it shifts the inserted value too:

    U_(F union {j},delta) I_v(x) = I_(v+delta) U_(F,delta)(x).

Consequently insertion at fixed v cannot commute with an expanded-family
uniform shift unless delta=0.

There is a stronger obstruction. Even selecting a new absolute mean target
cannot make the expanded-family minimum-change return equal the desired
edit-then-insert result for nonzero delta. That result changes old members by
delta and the new member by zero, whereas a full-family return changes all
members by the same scalar. Equality forces that scalar to be both delta and
zero. Thus there is no target-selection trick that removes the discrepancy.

To cross a membership change, one must retain the original edit scope, explicitly
extend the edit's action to the new member, or reject/rebase the request. The
current transaction policy rejects its stale family snapshot. Dynamic readout
reconstruction remains coherent; it does not imply unqualified edit naturality.

## 4. Increment versus replacement

Fixed scoped increments U_(F,a) and U_(G,b) commute even if F and G overlap:
they add a*1_F+b*1_G. Absolute mean replacements generally do not commute,
because the first update changes the mean used to compute the second shift.

The Store accepts increments attached to snapshots. Although their underlying
fixed-scope additions commute, a stale snapshot is still rejected under its
optimistic policy. Algebraic commutation is not a concurrency permission.

## 5. Verification and structural consequence

    python research/nima/checkers/check_dependent_mean_return_laws.py

Exact finite regression:1701 GetPut/PutGet/PutPut cases, frame/residual and
renaming checks,81 insertion cases, overlapping increment/replacement controls,
and an actual Store zero-edit metadata control. The general fixed-fibre and
insertion statements above have algebraic proofs; the checker is not their
machine-checked dependent-type proof.

The synthesis now needs two distinct transports: presentation changes within a
fixed content fibre, and explicitly scoped edits between membership fibres.
Complete retained records make the first lossless. Edit scope and version policy
make the second meaningful, but do not canonically select how new members act.
