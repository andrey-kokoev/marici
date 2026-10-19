# History6 endpoint/boundary iteration 8 — actual decorated target residue square

Freshly read the radial source checker/receipt and current work-net (pins v34). The target blowup is now constructed using the actual CZ inverse, not by adding a fitted tangent direction.

For six active external vectors, Ctilde=N*inverse(Z_support) reconstructs the source row space from the normalized target N. Normalize Ctilde at its active columns (1,2). Its bottom entries give b5,b6,b7,b8; the successive negative top/bottom slopes give b1,b2,b3,b4. At each positive external fixture, all eight symbolic source parameters are recovered identically, not just a numerical boundary point.

Let Ui(Y)=bi be these rational inverse coordinates. Blow up the target center U2=U3=0 using the chart

    U3=T, U2=R*T,
    target order (b1,T,R,b4,b5,b6,b7,b8).

R is exceptional direction data, not an ordinary ratio defined at the blowdown center. The inverse-coordinate transition determinant is -1/b3, while the radial source-forward determinant is -T. Their composition has identity Jacobian and extends as a regular decorated map. Rational arcs with T=tau and R=R0+tau reconstruct exactly at both external fixtures. This is an actual target modification; cancellation of T in the lifted inverse does not define R at an undecorated ordinary target point.

## Degree-preserving decorated boundary extraction

On the decorated target the full map has rank eight and T=0 boundary rank seven. Source exceptional residue then pushforward equals decorated top pushforward then residue. The target/source surviving order is (b1,R,b4,b5,b6,b7,b8), with split seven-dlog coefficients 1/(1+R) and R/(1+R). In ordinary coordinates on this **specified target chart**, the densities are:

- K0=1/7759752, B22=1/2586584;
- K0=1/95611230, B22=1/19122246.

The two pieces recombine to the transported exceptional form. Orientation reversal gives retained nonzero defects. These densities use inverse-source coordinates on the decorated target, not the earlier row-major ordinary target chart or common-corner generator.

The complementary target chart is

    S=U2=R*T, V=U3/U2=1/R.

Its eight-log transition determinant is -1. The transformed top form sign is +1, deletion of S has parity -1, and dlog R=-dlog V supplies the exceptional seven-form transition sign. Both fixture K0 densities agree after conversion back to the R reference. No compensating coefficient was chosen from a residual.

## Preserved blowdown obstruction and continuation

The ordinary blowdown still has full radial germ rank seven and exceptional boundary rank six. Its seven-form residue remains unavailable, not zero. The decorated map does not manufacture a physical supercomponent boundary extraction or global BCFW/weighted comparison. It is explicitly a map to a different target that retains the direction.

Next executable continuation: audit the two directional endpoints R=0 and R=infinity and the added R=-1 pole in both decorated target charts, including deletion/transition signs and matching to the retained ordered source diagnostics. Separately determine a source-authorized boundary-supercomponent object that can retain this additional direction; do not collapse the decorated degree-seven map onto the ordinary degree-six image.

Evidence: `checkers/check_history6_target_blowup.py`, `results/history6_target_blowup.json`. All scientific node verdicts unchanged; successor pins v35 and structural net/SCC validation are distinct from these inverse-arc/transition/residue tests. Nonredundant executable continuation remains.
