# The exchange stage is unique under the inherited port conditions

## Scope and assumptions

Keep the previously supplied port C and its positive Euclidean metrics fixed, with C C^T=I. The source is the prior memory lift in `comparison-update-dynamics-and-energy-normalization.md` and its bank extension in `four-packet-record-feedback.md`.

Require a linear isometry E satisfying:

1. Agreement is fixed: E(x,C^T x)=(x,C^T x).
2. With an empty bank, the exchanged carrier port is projected out: the carrier component of E(x,0) is zero.
3. Unread bank components are left untouched: E(0,k)=(0,k) for Ck=0.

The second requirement concerns the exchanged port, not arbitrary unmodeled transverse carrier coordinates. The third is stronger than information retention: a reversible rotation of the unread sector would retain information but would violate this particular unchanged-sector condition. It is an assumption inherited from the declared minimal exchange extension, not a consequence of WG alone.

## Uniqueness argument

Write E(x,0)=(0,t'). For any y, agreement-fixing and inner-product preservation give

    <t',C^T y> = <E(x,0),E(y,C^T y)> = <x,y>.

Therefore Ct'=x. The orthogonal splitting of the bank gives t'=C^T x+k with Ck=0. Isometry also gives ||t'||^2=||x||^2. Since C^T is isometric and the metric is positive,

    ||t'||^2 = ||x||^2 + ||k||^2,

so k=0. Thus E(x,0)=(0,C^T x) is forced, rather than supplied as a full output condition.

Linearity and agreement now imply

    E(0,C^T a)=E(a,C^T a)-E(a,0)=(a,0).

Finally decompose any bank t=C^T a+k, where a=Ct and Ck=0. The three established images force

    E(x,t)=(a,C^T x+k)
          =(Ct,C^T x+(I-C^T C)t).

This is precisely the existing positive exchange. There is no further linear freedom under the stated conditions. Its involution and conservation then follow; they need not be independent selection assumptions.

## Exact certificate for the current model

For the existing four-carrier/sixteen-record realization, the checker verifies C C^T=I and a twelve-dimensional unread kernel. Agreement vectors, empty-bank carrier vectors and unread-bank vectors span all twenty coordinates. Their prescribed images agree with the old exchange matrix. A nonredundant twenty-vector domain basis and its image basis are stored in the result.

This finite spanning certificate verifies the current rational matrix instance. The general implication from positivity and isometry to the empty-bank output is the algebraic proof above, not a new Agda theorem or an exhaustive search over matrices.

## Disposition

The positive sign is not merely preferred: the whole exchange stage is uniquely determined relative to these source port requirements. This is narrower than uniqueness of the complete back-reaction model. The two-edge adapter, coefficient metric, choice of rotations and schedule, physical status of the comparison records, and gravitational normalization remain unselected by this result.

In particular, the unread-sector condition should stay visible in subsequent work. Dropping it permits additional reversible dynamics there, which could become visible after the bank is mixed. No arbitrary such dynamics is adopted here.

## Follow-up: stronger agreement removes a separate assumption

`unread-record-selection.md` distinguishes pure-readable agreement from full-state agreement. If the inherited rule requires E(x,t)=(x,t) whenever Ct=x, unread-fixing follows immediately by taking x=0 and t in ker C. A reversible unread-sector negation preserves information but violates that full agreement condition. Thus unread-fixing need not be a separate assumption when the source agreement rule is stated in its full-state form.

## Verification

`python research/nima/checkers/check_record_exchange_uniqueness.py` passed with exact rational coisometry, orthogonality, rank, spanning and exchange checks. Result: `results/record-exchange-uniqueness.json`, including the complete basis certificate and source digests.

No existing update implementation was modified. No ledger entry, commit or publication is claimed.
