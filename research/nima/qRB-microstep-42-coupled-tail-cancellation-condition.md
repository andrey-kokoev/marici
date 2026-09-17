# qRB microstep 42: coupled-tail cancellation condition

The hostile rank-one example shows that finite boundedness is insufficient. For a growing packet, write the cross-readout as

$$
T_P=T_P^{\rm common}+T_P^{\rm defect}.
$$

Uniformity requires the common coupled mode to cancel or be absorbed by the relative quotient before estimating the defect:

$$
\Pi_{\rm common}T_P\Pi_{\rm common}=0
$$

(or an equivalent source identity), followed by

$$
\sup_P
\|T_P^{\rm defect}\|_{\mathcal D_*\to\mathcal D_*^\vee}<\infty.
$$

Entrywise bounds cannot replace this condition: a rank-one common mode may have bounded entries but operator norm proportional to packet size.

Status: necessary structural condition isolated; its verification for the prime/prime′ source families remains open.
