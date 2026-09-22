# Witness or finite separator for dominated tail carriers

## Frozen class

Index possible tail atoms by integers n>N. Retain:

1. a fixed support S, and finite atom bounds 0<=x_n<=b_n;
2. prefix bounds sum_{N<n<=j}x_n<=U_j;
3. interval bounds sum_{i<n<=j}x_n<=C_{ij}, for N<=i<j;
4. U_j nonnegative and nondecreasing, and C_{ij} nonnegative and
   nondecreasing in j for each fixed i;
5. an objective F(x)=sum k_n x_n with a PROVED uniform absolute tail bound
   sup_admitted sum_{n>m}|k_n|x_n<=epsilon_m, epsilon_m -> 0.

Missing interval restrictions may be represented by redundant finite bounds.
Support and all finite data are effectively accessible; numerical coefficients
must have certified approximations. There are no lower-mass requirements,
hidden historical guards, or unclosed strict inequalities in this class.

The finite implementation below uses rational data. For real analytic kernels,
finite rational coefficient enclosures contribute a separately bounded error.
This note does not assert a practical enumeration size for the actual tail.

## Result: the structural DPC becomes a theorem under these hypotheses

Let A be this carrier and v=inf_A F. Its product topology is inherited from
prod [0,b_n]. Support restrictions and each finite-sum inequality are closed.
Hence A is compact; it is nonempty because zero is admitted. Uniform absolute
tail control makes F a uniform limit of continuous finite-coordinate sums.
Therefore F is continuous and attains its minimum on A.

This resolves the approximation uncertainty: within this class, an admitted
sequence approaching a relaxed optimum cannot evade all admitted optimizers.
A convergent subnet (or diagonal subsequence in this countable product) has
an admitted limit with the same objective value. Approximate extremal
realizability and actual value-realizability coincide.

Let P_m be the finite LP through m, retaining all prefix and interval bounds
with endpoints through m, support restrictions and atom caps. Every global
member restricts to P_m. Conversely, every member of P_m extends by zero to
A: a later interval ending at j>m has the same mass as its truncation at m,
and C_{i,m}<=C_{i,j}; future prefixes are handled by U_m<=U_j. Intervals
starting at or after m have zero mass. This is an explicit joint-admission
constructor, not equality of local summaries.

Writing v_m=min P_m F_m, we consequently have

    v_m - epsilon_m <= v <= v_m.

The upper bound has a finite, zero-extended primal witness. The lower bound
has a finite LP dual certificate plus the uniform tail estimate. In particular
v_m decreases to v, but v_m-epsilon_m need not increase monotonically.

For a relaxation R containing A with infimum r, exactly one of the following
holds:

- v=r: an actual member of A realizes the relaxed value;
- v>r: some finite m satisfies v_m-epsilon_m>r, and a finite dual separates.

Equivalently, if no finite lower certificate exceeds r, then v<=r, hence
v=r. A strict gap cannot hide solely at infinity under the uniform tail bound.
For computable real data, any strictly positive gap absorbs sufficiently
small rational coefficient errors and a sufficiently narrow enclosure of r.

There is NO claim that equality has a finite recognizer, or that this is a
uniform algorithm deciding which case holds in finite time. Strict separation
is eventually certifiable; equality may require a separate structural proof.

## Exact finite primal/dual packet

For rational finite constraints Ax<=b, x>=0 and objective c.x, retain

    primal x>=0, Ax<=b;
    dual y>=0, A^T y>=-c;
    c.x = -b.y.

These equations independently verify finite optimality. Then -b.y-epsilon_m
is a full-tail lower certificate; zero-extension of x is a full-tail feasible
witness. No trust in the optimization routine is needed to check the packet.
An optimizer may be used to find the packet, not to authorize its result.

The executable controls use k_n=-2^-n, b_n=1, and uniform tail error 2^-m.
The unrestricted relaxed optimum is -1. Even-only support changes it to
-1/3. A third control retains all support but bounds every interval of length
j-i by ceil((j-i)/2); its optimum is -2/3. Odd-only unit mass attains it,
and the adjacent-pair bounds supply a matching infinite geometric dual.
Thus both support and genuinely relational local capacity have strict-gap
controls. Exact primal/dual packets at m=2,4,8,16 are replayed independently.
This verifies the construction and strict-gap/equality controls; it does not
replace the general proof by finite sampling.

## Why the hypotheses matter

Uniform tail control is essential, not a technical decoration. Let x_n>=0,
sum x_n<=1, and F(x)=-sum (1-1/n)x_n. This carrier is compact in the product
topology and satisfies bounded atoms and closed prefix constraints. Unit
mass at n tends in objective to -1, but no admitted measure attains -1:

    1+F(x)=1-sum x_n + sum x_n/n > 0.

The zero measure also has positive slack. Here the uniform absolute tail
supremum is 1 for every cutoff. Approximate realizability does NOT imply
attainment without the dominated-tail hypothesis.

Right-endpoint monotonicity, or an alternative explicit extension theorem,
is essential to the finite primal constructor. If the interval capacity is
C_(0,1)=1 but C_(0,2)=0, the finite mass x_1=1 passes the first cutoff but its
zero extension fails the second. General compatibility relations need not
admit the particular truncation/extension maps proved in this note.

## Relation to our actual results

- The single-valley construction supplied a compatible extremizer directly.
- Atom caps supplied a finite strict separator via the two-sided local cut.
- The wheel supplied a different, globally admitted below-threshold witness.

These are three instances of objective-relative realizability, not conflicting
claims about whether compatibility always matters.

The actual arithmetic relaxations have finite atom caps and closed constraints.
A dominating Chebyshev prefix bound and exponential kernel suffix supply
uniform absolute tail control. For example, if cumulative mass <=D x^q and
|k_n|<=C n^-p with p>q, partial summation gives the sufficient uniform bound

    sum_{n>m}|k_n|x_n <= C D p/(p-q) m^(q-p).

The constants and starting cutoff must be certified. The existing signed
kernel is a constant times n^-7/2 after log n>=64. This establishes eventual
domination, not a computationally cheap integer-level cutoff. The present
experiment does not construct a new actual-prime separating packet.

## Why this is the synthesis, and its boundary

The decisive closure is admission plus objective continuity. It is stronger
than matching local observations, and different from coherence of how a
relation is presented. Regrouping preserves packets only when it preserves
this full admitted carrier; transposing a compatibility query is not itself
an LP dual or permission to execute the source backward.

The theorem explains when a genuinely infinite obstruction has a finite
witness of separation. It uses standard compactness, uniform convergence
and LP duality; its contribution here is to identify and check the precise
hypotheses connecting the lane's examples. No universal new duality theorem
or finite bound on necessary certificate size is claimed.

## Reproduction

    uv run --with sympy python research/grothendieck/checkers/construct_tail_witness_separator.py
    python research/grothendieck/checkers/verify_tail_witness_separator.py

The second command uses exact Fraction arithmetic, not the LP solver.
Artifact: `results/tail-witness-separator.json`.
