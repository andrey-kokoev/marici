"""One-loop SM scale diagnostic for corrected matter-trace boundary.

Observable: MSbar s_W^2(MZ)=g'^2/(g'^2+g2^2), Q=T3+Y.
Boundary alphaY^-1=10*t, alpha2^-1=6*t at scale Lambda.
Inputs MZ=91.1876 GeV and illustrative alphaEM^-1(MZ)=127.95.
No thresholds, extra fields, higher loops, or fitted weak-angle target.
Writes no files. This is a conditional scale family, not a carrier prediction.
"""
import math
MZ=91.1876
A=127.95
bY=41/6
b2=-19/6

def run(scale):
    log_ratio=math.log(scale/MZ)/(2*math.pi)
    t=(A-(bY+b2)*log_ratio)/16
    y=10*t+bY*log_ratio
    w=6*t+b2*log_ratio
    assert t>0 and y>0 and w>0
    assert math.isclose(y+w,A,abs_tol=1e-12)
    angle=w/(y+w)
    # Eliminating normalization gives this direct scale dependence.
    assert math.isclose(angle, 3/8-(109/24)*log_ratio/A,abs_tol=1e-14)
    return t,y,w,angle

for scale in [MZ,1e3,1e10,1e13,1e16,1.22e19]:
    t,y,w,s=run(scale)
    print(f'Lambda={scale:.7g} GeV: t={t:.9f}, alphaY^-1={y:.9f}, alpha2^-1={w:.9f}, s_MSbar^2={s:.9f}')
print('All boundary and running identities passed. Boundary scale is an external input.')
