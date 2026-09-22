# Vacuum attachment readouts are direct, but residual readouts need stronger tail priors

## Result

The two independent relative attachment readouts from Voevodsky's vacuum-probe theorem have different stability properties in the specified acquisition protocol.

- The vacuum evaluation is a directly acquired unit coordinate: it is Lipschitz with constant one in its scalar error norm.
- The original residual attachment evaluation is NOT uniformly recoverable under the polynomial actual-letter moment priors that suffice for Holder recovery of the actual-letter source norm. This remains false after adding a uniform unweighted path-norm bound.
- A positive background moment in the PATH norm restores conditional residual-readout recovery, with a logarithmic modulus and an unavoidable squared-log-log factor for the full two-coefficient residual functional.
- At a fixed packet, certified intervals can establish independence of the two attachment readouts using a positive determinant margin.

These are statements about scalar witness evaluations and their derived nonvanishing certificates, not a proposed norm on Ext. The adjacent pushout into the whole enlarged kernel still vanishes, exactly as in the owning theorem.

## 1. Specify the source family and the target readouts

Use the translated two-feature cubic source family from `translated-cubic-reconstruction-is-compact-and-requires-quantitative-tail-priors.md`. At each background A also allow the forgotten product k_A on the same three prescribed diamonds. Write

`x_A=sum_j a_(A,j)v_(A,j)+b_A k_A`.

The source coefficients have unweighted path norm

`p(x_A)=32 sum_j|a_(A,j)|+8|b_A|`.

Keep the 270 private feature readings z_(A,j)=E_(A,j)a_(A,j), and acquire the extra vacuum coordinate u_A=b_A. These are distinct labelled outputs. The all-vacuum coordinate annihilates the two-feature source space.

Normalize the residual attachment only by its fixed physical factor w^2, where w=w_seam, and define

`t_A=lambda_(r,A)(x_A)/w^2
   =sigma_0(A)a_(A,0)+sigma_x(A)a_(A,x)`.

Here

`sigma_0=[mu(A_2)-mu(A_1)][mu(B_2)-mu(B_1)]/18`,

`sigma_x=-(mu(A_1)-L)(mu(B_2)-L)/18`,

at y=3, with A_1=[A,2A], A_2=[2A,6A], B_1=[6A,30A], B_2=[30A,210A] in arithmetic-endpoint notation. No background-dependent renormalization is inserted into the target readout.

The target is the labelled pair (u_A,t_A), with sums of absolute scalar errors. Under the path-moment prior below these sequences are summable. The statements of nonuniformity already hold on finite sources, where summability presents no issue.

## 2. A source-reconstruction guarantee does not automatically control t

Consider x_A=v_(A,0), with coefficient one, and let A tend to infinity through admitted backgrounds. Each is a genuine finite source in both source domains, with p(x_A)=32.

The completed-theta estimates give

`Q_1(x_A)/w ~ const A^15(log A)^2 exp(-37pi A^2)`.

Thus A^eta Q_1(x_A)/w tends to zero for every fixed polynomial moment order eta. The acquired private data also tend to zero; their sole nonzero feature reading is E_(A,0), of Gaussian smallness. The vacuum reading is zero.

Nevertheless

`t_A -> log(2)log(5)/18 >0`.

Compare each x_A to zero and take the midpoint of their data. The required noise radius tends to zero while the residual-readout ambiguity stays bounded away from zero. Therefore no recovery error modulus tending to zero exists on this family under an actual-letter background-moment bound, even when a uniform path bound of 32 is also imposed.

All these finite sources satisfy the individual common-path membership requirements. What fails is endpoint tightness in that stronger norm, not existence of a source or frame consistency. This is why the earlier Holder estimate for Q_1 error cannot be used to certify the residual attachment evaluation.

## 3. Vacuum readout stability is direct

For full labelled vacuum scalar data, ||u_measured-u||_1<=epsilon_v is already the readout error bound. No source inverse, tiny-amplitude division or arithmetic feature calibration enters this statement.

If only backgrounds A<=H are acquired, a declared prior sum_A A^eta p(x_A)<=M bounds the unmeasured vacuum tail by

`sum_(A>H)|u_A|<=M/(8H^eta)`.

The unit coordinate still has to be acquired. Neither frame coherence nor feature reconstruction manufactures this additional record data.

## 4. A uniform bound for residual-readout amplification

On a fixed background, the exact norm of t as a functional of the selected raw scalar data is

`c_t(A)=max(|sigma_0|/E_0, |sigma_x|/E_x)`.

This can be much smaller than the full source-coefficient inverse, but is still severely ill-conditioned.

The interval means satisfy 0<mu_F<=log(upper endpoint), and L>0. The positive adjacent-window ordering gives

`|sigma_0|,|sigma_x| <=D(1+log A)^2`,

`D=(1+log 6)(1+log 210)/18 <1`.

The existing residual lower bound is

`K_a>=k_0(1+log a)a^(11/2)exp(-pi a^2)`,

`k_0=pi(1-exp(-1))/8`,

and E_0=K_A K_(6A)/5, E_x=K_A K_(10A)/5. The logarithmic factors cancel in these upper inverse estimates. Since k_0^2*6^(11/2)*2^11>5, we obtain the explicit bound

`c_t(A)<=exp(101pi A^2)` for A>=2.

Moreover the actual boundary asymptotics give

`c_t(A) ~[5/(18pi^2*10^(11/2))] A^(-11)exp(101pi A^2)`.

The crossed coefficient controls this asymptotic. In particular the obstruction is not an artifact of the coarse upper bound.

## 5. Conditional recovery under a stronger tail prior

Now impose the genuinely stronger endpoint-tightness condition

`sum_A A^eta p(x_A)<=M`, with eta>0.

Reconstruct the residual readout only on A<=H using the exact E and sigma constants. With total scalar feature noise at most epsilon, its error obeys

`sum_A |t_hat_A-t_A|
 <=exp(101pi H^2)epsilon
   +(M/32)(1+log H)^2 H^(-eta)`

provided H>=2 and H>=exp(2/eta-1). The latter condition makes (1+log A)^2/A^eta decreasing beyond H. The tail bound uses |t_A|<=(1+log A)^2 p(x_A)/32.

Putting c=101pi and H=sqrt(log(M/epsilon)/(2c)), when this meets the stated cutoff conditions, gives

`error <=sqrt(M epsilon)
        +(M/32)(1+log H)^2[2c/log(M/epsilon)]^(eta/2)`.

Thus the asymptotic conditional modulus has order

`M [log log(M/epsilon)]^2 [log(M/epsilon)]^(-eta/2)`.

Vacuum error may be added separately; its finite-cutoff term is M/(8H^eta), without the squared-log-log loss or inverse amplification.

All implementation and calibration errors must enter the effective scalar error bound before applying these estimates. They are not supplied by the abstract reconstruction formula.

## 6. The residual rate has a matching obstruction

Take a single crossed source at background A with coefficient M/(32A^eta). It saturates the path-moment budget. Its residual target has magnitude asymptotic to a positive constant times

`M A^(-eta)(log A)^2`.

Its observed scalar data are Gaussian small, with log(M/data magnitude) asymptotic to 101pi A^2. Midpoint data with half this magnitude as noise cannot distinguish it from zero. Every estimator has residual error at least half the target separation on one of the two sources.

This gives the same logarithmic order, including the squared-log-log factor, along admitted backgrounds. Stronger priors or different measurements can change the problem; rearranging the same data cannot remove this obstruction.

## 7. A finite robust independence certificate

At A=2, use the two verified product witnesses k and v_0. The exact evaluation matrix for the vacuum and normalized residual readouts is

`[[1,0],[0,d]]`, where `d=sigma_0(2)>0`.

Fresh complete-theta interval integration proves d>1/25. If acquired and calibrated intervals for the TRUE matrix entries imply

`|m_11|>=0.99`, `|m_22|>=0.03`,

`|m_12|<=0.01`, `|m_21|<=0.01`,

then every matrix in those intervals satisfies

`|det M|>=0.99*0.03-0.01^2=37/1250>0`.

This is a conditional acquisition certificate, not a claim that those measurements have been performed. Entry intervals must include all errors, not merely enclose noisy nominal values.

The owning finite-roof argument says that a vanishing linear combination of the scalar attachment classes would vanish on both these product witnesses. The determinant certificate excludes such a combination. Therefore it robustly certifies the same independence established algebraically by Voevodsky, when the source witnesses and acquisition intervals are justified.

No topology or norm on the entire Ext group is introduced. Nor does this revive the adjacent pushout into the whole observer kernel: the information still resides in the two independent relative boundary classes described in `../voevodsky/the-vacuum-probe-adds-a-relative-attachment-but-not-a-surviving-adjacent-pushout.md`.

## Consequence

Attachment nonvanishing, source reconstruction and robust attachment readout are distinct assertions. For this protocol the vacuum readout is directly stable, while the normalized residual readout requires a stronger tail prior than actual-letter source recovery alone.

The constructive bridge is therefore: justified product witnesses, correctly typed relative classes, and certified scalar intervals with a nonzero witness-matrix margin. Frame coherence preserves their meaning but cannot supply the missing analytical error bounds.

## Verification

`uv run --with python-flint --with sympy python research/nima/checkers/check_attachment_readout_stability.py`

Artifact: `research/nima/results/attachment-readout-stability.json`.

The checker certifies the actual positive residual witness, the uniform scalar bounds and the exact determinant margin. Infinite counterexamples and matching conditional rates use the completed-theta asymptotics and midpoint-noise arguments above.
