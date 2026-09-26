# A normalized contact-jet map retaining lower-grade data

## Fresh source constraints

Read ledger2158's contact matrix: its entries retain source-normalized spectator periods P_jk and products C_j C_k. Its moving kernel cannot be replaced by a source-constant vector. Combined with primary2401.05207 labels PD1/PD2/Oav, the extraction must preserve both component coefficients and normalization, not just the desired top contact term.

This note constructs the universal normalized perturbative coefficient interface. It does not yet substitute the actual wavefunction coefficients for all labelled contact sectors.

## Normalized coefficient construction

Let mu be a normalized reference Gaussian measure, independent of the formal contact coordinate nu in the declared chart. Write the unnormalized interaction factor

    W=1+lambda V(nu)+lambda^2 U(nu)+O(lambda^3),
    a(nu)=E_mu V(nu), b(nu)=E_mu U(nu),
    R=W/E_mu W.

Then

    R0=1,
    R1=V-a,
    R2=U-a V+a^2-b.

For a fixed physical insertion O, the normalized coefficient is E_mu(O Rn), with E_mu Rn=0 for n>0. This does not identify O with Rn or with an arbitrary polynomial sharing its moments.

For general orders the recursion is

    Rn=Wn-sum_(k=1..n) (E_mu Wk) R_(n-k).

This is the coefficient expansion of the primary normalized measure, not a choice of counterterm scheme. Formal normalization is meaningful order by order; positivity of a truncated signed coefficient is not required or asserted.

## First contact grade at second interaction order

Set V=V0+nu V1+..., U=U0+nu U1+..., and a_i=E V_i, b_i=E U_i. Then

    [nu]R1=V1-a1,
    [nu]R2=U1-b1-a0 V1-a1 V0+2a0 a1.

The desired second-order contact grade depends on V0 as well as V1. Keeping only graded V1,U1 and then normalizing loses the cross terms. This is not a claim that contact grading fails to commute with covariance differentiation when both are correctly applied to a fully retained normalized source. It is a counterexample to discarding lower-grade normalization data first.

Exact control: baseline X~N(0,1), O=X^2, V0=X^2, V1=X^4, U=0. The true lambda^2 nu coefficient is-18. Replacing V by V1 before applying normalization produces-36. All quantities are elementary Gaussian moments; the control is not the cosmological interaction itself.

## Score differentiation of the effective coefficient

When mu varies with covariance, Rn usually varies too. For a fixed O,

    D E_mu(O Rn)=E_mu(O Rn S)+E_mu(O D Rn),

where S is the centered score of the reference measure. The second term must not be omitted. At first order, for covariance-independent V,

    D R1=-E_mu(V S).

For O=V=X^2 at variance g, the normalized coefficient is2g^2 and its logarithmic derivative4g^2. Holding R1 artificially fixed gives5g^2; the required correction is-g^2. This explains precisely why folding normalization into an effective observable changes the differentiation rule.

## Typed norm obligation

If Rn is in L2(mu), it defines a bounded coefficient functional O -> E_mu(O Rn) on L2(mu), with bound ||Rn||_2. Uniform completion control requires bounds on the actual source coefficients and their scalar normalization moments. Neither formal jet recursion nor finite Gaussian examples supplies those bounds for an integrated cosmological sector.

The next source instantiation must retain the lower rectangular perturbative/contact jet, source spectator factors and momentum labels. If O or the reference measure also depends on the contact coordinate, their jets enter the same product rule. Do not assume independence outside ledger2219's generic chart.

## Decision and next task

The normalized contact interface now has an explicit executable recurrence and a tested noncommutation trap. The missing input is sharply localized: actual W_(n,m) and contact-sector assignments before contraction. Next instantiate the lowest source contact packet using those coefficients, rather than replacing it by the canonical Gaussian moment lift. The existing operator-lift handoff remains open; owner acknowledgment is not needed for continued local source inspection.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_normalized_contact_jet.py` checks the formal normalization identity through lambda^2, centered coefficients, the second-order contact control and the covariance-score correction. This is a normalized-interface proof with exact controls, not a completed physical contact calculation.
