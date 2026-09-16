# Four-port pro-faithfulness does not yield the bounded C41 factorization

## Question

Does the complete four-port record satisfy the observability estimate needed to factor the complete spectral presentation through it and construct analytic \(C_{41}\)?

## Claim boundary

Not in the currently declared completed norm. Prior research proves pro-faithfulness but explicitly withholds a cutoff-independent lower bound. This gives algebraic uniqueness in the inverse-limit record, not a bounded analytic recovery map. A tail-coercive bulk augmentation supplies a sufficient repair on each half-line graph block, subject to a uniform global bound.

The desired factorization is

$$
C_{13}=R_{43}q_4,
$$

with \(R_{43}\) bounded. Since \(C_{13}\) is a conservative paired spectral presentation, bounded factorization requires an estimate of the form

$$
\|C_{13}h\|_{V_3}\le A\|q_4h\|_{V_4}.
$$

The retained four-port behavior theorem proves only

$$
\bigcap_N\ker q_{4,N}=0,
$$

or monicity of the full pro-record

$$
q_{4,\infty}:\mathsf{Obs}_S\longrightarrow\varprojlim_N V_{4,N}.
$$

It explicitly distinguishes this from uniform observability. Broad packets can have unit source norm while escaping every fixed finite probe depth. Therefore pro-faithfulness does not imply the displayed norm estimate and does not produce bounded \(R_{43}\).

## Algebraic consequence

If a source observer lies in the admitted analytic-uniqueness class, its full compatible four-port tower determines it uniquely. Thus a set-theoretic or pro-object recovery is unique on the image. Continuity in one completed Hilbert topology is not obtained.

## Sufficient analytic repair

Prior half-line analysis augments endpoint and derivative observation by a bounded bulk multiplier \(w\) satisfying

$$
|w(r)|\ge c>0
$$

for almost every \(r\ge R\). For

$$
Q_wh=(h',h(0),wh),
$$

it proves

$$
\|h\|_{H^1}^2
\le
M_{R,c}\|Q_wh\|^2,
\qquad
M_{R,c}=\max\{2R,R^2+1,c^{-2}\}.
$$

Hence an augmented fourth presentation

$$
q_4^{\mathrm{aug}}=(q_4,M_w)
$$

is bounded below on each declared half-line graph block. If the same \(R,c\) work uniformly across the semilocal direct sum and the paired spectral norm is bounded by that graph norm, then a bounded factorization \(R_{43}^{\mathrm{aug}}\) exists on \(\operatorname{im}q_4^{\mathrm{aug}}\), and

$$
C_{41}^{\mathrm{aug}}=C_{31}R_{43}^{\mathrm{aug}}
$$

is analytic.

## Disposition

The original complete four-port presentation gives pro-faithful uniqueness but not analytic \(C_{41}\). The first known sufficient route to analytic recovery is to add a source-derived tail-coercive bulk channel and prove uniformity of its lower margin across all semilocal blocks. Without that augmentation or another coercive estimate, bounded \(C_{41}\) remains unconstructed.