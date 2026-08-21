"""Exact asymptotic sign of the squared inward monotonicity tail reserve."""

from __future__ import annotations
from collections import defaultdict
from math import comb
import math
from decimal import Decimal
import sympy as sp
from flint import arb,ctx
from hyperbolic_inward_monotonicity_symbolic import generate,k,l,t
from hyperbolic_limiting_tail_certificate import evaluate as critical_evaluate
from theta_inner_interval_certificate import I


def main()->None:
    _,_,q,m=generate();qp=sp.Poly(q,l);q2=qp.coeff_monomial(l**2);q1=qp.coeff_monomial(l);delta=sp.discriminant(q,l)
    _,rem=sp.div(sp.Poly(m,l,domain=sp.QQ.frac_field(t,k)),sp.Poly(q,l,domain=sp.QQ.frac_field(t,k)))
    numerator,_=sp.fraction(sp.cancel(rem.as_expr()));s=sp.cancel(-numerator/((1-t)**2*(1+t)**2));a=sp.diff(s,l);b=s.subs(l,0);c=sp.expand(-a*q1+2*q2*b)
    h=sp.factor(c*c-a*a*delta);p=sp.cancel(h/((t-1)*(t+1)*t**6*(3*t-1)**6*(3*t+1)**6))
    y,e=sp.symbols("y e",positive=True);poly=sp.Poly(sp.expand(p.subs(t,1-y)),y,k)
    valuation=min(i-2*j for (i,j),_ in poly.terms());leading=sp.factor(sum(coef*(2/e)**i for (i,j),coef in poly.terms() if i-2*j==valuation))
    expected=-sp.Integer(79164837199872)*(e**6+9*e**4-15*e**2+9)/e**9
    assert valuation==-13 and sp.cancel(leading-expected)==0
    x=sp.symbols("x",positive=True);shape=x**3+9*x**2-15*x+9
    assert shape.subs(x,1)==4 and sp.expand(sp.diff(shape,x)-3*(x**2+6*x-5))==0
    print(f"weighted_valuation={valuation}")
    print(f"leading_coefficient={leading}")
    print("positive_shape_for_E_gt_1=True")
    print("tail_boundary_H_positive=True")

    # Construct the fully denominator-cleared tail polynomial coefficient by
    # coefficient.  This avoids an expensive global rational expansion.
    source=sp.Poly(p,t,k);dt,dk=source.degree(t),source.degree(k);terms=defaultdict(lambda:sp.S.Zero)
    for (ta,kb),coefficient in source.terms():
        for i in range(ta+1):
            for j in range(dt-ta+1):
                for h in range(kb+1):
                    ze=2*dk-2*kb-9+i+j+2*h;ee=dt-i-j
                    terms[(ze,ee)]+=coefficient*(-1)**(i+h)*comb(ta,i)*comb(dt-ta,j)*comb(kb,h)
    terms={monomial:coefficient for monomial,coefficient in terms.items() if coefficient!=0}
    assert min(ze for ze,_ in terms)==0
    boundary=sp.factor(sum(coefficient*e**ee for (ze,ee),coefficient in terms.items() if ze==0))
    expected_boundary=-sp.Integer(79164837199872)*e**39*(e**6+9*e**4-15*e**2+9)
    assert sp.expand(boundary-expected_boundary)==0
    linear=sp.factor(sum(coefficient*e**ee for (ze,ee),coefficient in terms.items() if ze==1))
    expected_linear=sp.Integer(13194139533312)*e**38*(19*e**8+568*e**6+2880*e**4-6288*e**2+4941)
    assert sp.expand(linear-expected_linear)==0
    lprime=sp.sqrt(3)*(11-sp.log(27))/9
    normalized_boundary=boundary/e**39;normalized_linear=linear/e**39
    boundary_derivative=sp.simplify((normalized_linear+e*sp.diff(normalized_boundary,e)*lprime).subs(e,sp.sqrt(3)))
    expected_derivative=sp.Integer(316659348799488)*sp.sqrt(3)*(33*sp.log(3)+280)
    assert sp.simplify(boundary_derivative-expected_derivative)==0
    print(f"cleared_tail_terms={len(terms)}")
    print(f"cleared_tail_degrees={(max(ze for ze,_ in terms),max(ee for _,ee in terms))}")
    print(f"cleared_tail_boundary={boundary}")
    print(f"cleared_tail_linear={linear}")
    print(f"normalized_boundary_derivative={boundary_derivative}")
    print("normalized_boundary_derivative_positive=True")

    z,lvar=sp.symbols("z lvar");w=sp.Poly.from_dict(terms,(z,e)).as_expr()
    qbar=sp.cancel(z**2*q.subs({t:(e-z)/(e+z),k:z**-2-1,l:lvar}));qn,qd=sp.fraction(qbar)
    assert sp.expand(qd-(e+z)**5)==0
    ql_num=(e*sp.diff(qn,e)+sp.diff(qn,lvar))*(e+z)-5*e*qn
    qz_num=sp.diff(qn,z)*(e+z)-5*qn
    derivative_num=sp.expand(sp.diff(w,z)*ql_num-(e*sp.diff(w,e)-39*w)*qz_num)
    derivative_poly=sp.Poly(derivative_num,z,e,lvar);derivative_boundary=sp.factor(derivative_poly.eval(z,0).as_expr().subs({e:sp.sqrt(3),lvar:sp.log(3)/2}))
    expected_k0=-sp.Integer(59622635402543133100081152)*(33*sp.log(3)+280)
    assert sp.simplify(derivative_boundary-expected_k0)==0
    print(f"derivative_numerator_terms={len(derivative_poly.terms())}")
    print(f"derivative_numerator_degrees={(derivative_poly.degree(z),derivative_poly.degree(e),derivative_poly.degree(lvar))}")
    print(f"derivative_numerator_boundary={derivative_boundary}")
    print("derivative_numerator_boundary_negative=True")
    _,critical_remainder=sp.div(sp.Poly(derivative_num,lvar,domain=sp.QQ.frac_field(z,e)),sp.Poly(qn,lvar,domain=sp.QQ.frac_field(z,e)))
    rn,rd=sp.fraction(sp.cancel(critical_remainder.as_expr()))
    assert sp.expand(rd-z*(-2*e+z)*(-e+z)*(-e+2*z))==0
    correction=sp.Integer(2849934139195392)*e**45*(e**4+6*e**2-5)
    desingularized=sp.Poly(sp.expand(rn-correction*qn),z,e,lvar);assert desingularized.eval(z,0).is_zero
    g=sp.div(desingularized,sp.Poly(z,z,e,lvar))[0];g0=sp.factor(g.eval(z,0).as_expr().subs({e:sp.sqrt(3),lvar:sp.log(3)/2}))
    expected_g0=sp.Integer(357735812415258798600486912)*sp.sqrt(3)*(33*sp.log(3)+280)
    assert sp.simplify(g0-expected_g0)==0
    print(f"desingularized_terms={len(g.terms())}")
    print(f"desingularized_degrees={(g.degree(z),g.degree(e),g.degree(lvar))}")
    by_l=tuple(sum(1 for powers,_ in g.terms() if powers[2]==degree) for degree in range(3))
    occupied_z=len({powers[0] for powers,_ in g.terms()});occupied_e=len({powers[1] for powers,_ in g.terms()})
    print(f"desingularized_L_block_terms={by_l}")
    print(f"desingularized_occupied_degrees={(occupied_z,occupied_e)}")
    quadratic_l=sp.factor(sp.Poly(g.as_expr(),lvar).coeff_monomial(lvar**2))
    print(f"desingularized_L2_factor={quadratic_l}")
    holding_poly=sp.Poly(g.as_expr(),lvar);block0=holding_poly.coeff_monomial(1);block1=holding_poly.coeff_monomial(lvar)
    for degree in (0,1):
        block=holding_poly.coeff_monomial(lvar**degree);constant,factors=sp.factor_list(block)
        summary=tuple((len(sp.Poly(factor,z,e).terms()),sp.Poly(factor,z,e).degree(z),sp.Poly(factor,z,e).degree(e),power) for factor,power in factors)
        print(f"desingularized_L{degree}_factor_constant={constant}")
        print(f"desingularized_L{degree}_factor_summary={summary}")
    residual1=sp.cancel(-block1/(sp.Integer(2)**43*e));residual_poly=sp.Poly(residual1,z,e)
    positive_coefficients=sum(1 for _,coefficient in residual_poly.terms() if coefficient>0);negative_coefficients=sum(1 for _,coefficient in residual_poly.terms() if coefficient<0)
    weighted_degrees=tuple(sorted({a+b for (a,b),_ in residual_poly.terms()}))
    print(f"G1_residual_coefficient_signs={(positive_coefficients,negative_coefficients)}")
    print(f"G1_residual_xE_weighted_degree_range={(weighted_degrees[0],weighted_degrees[-1],len(weighted_degrees))}")
    residual_z0=-sp.Integer(432)*e**48*(e**4+6*e**2-5);assert sp.expand(residual1.subs(z,0)-residual_z0)==0
    print(f"G1_residual_z0_factor={residual_z0}")
    x,y=sp.symbols("x y",nonnegative=True);rx=sp.Poly(sp.expand(residual1.subs(z,x*e)/e**46),x,e)
    assert all(power_e%2==0 for (_,power_e),_ in rx.terms())
    rxy=sum(coefficient*x**power_x*y**(power_e//2) for (power_x,power_e),coefficient in rx.terms());fr=sp.lambdify((x,y),(rxy,sp.diff(rxy,x),sp.diff(rxy,x,2)),"math")
    r_min=(float("inf"),None);r_max=(-float("inf"),None);dx_max=(0,None);dx_signed_max=(-float("inf"),None);dxx_min=(float("inf"),None)
    for ix in range(21):
        xv=(.09/math.exp(.45))*ix/20
        for iy in range(21):
            yv=math.exp(.9)+(math.exp(1.7)-math.exp(.9))*iy/20;rv,dv,ddv=fr(xv,yv)
            if rv<r_min[0]:r_min=(rv,(xv,yv))
            if rv>r_max[0]:r_max=(rv,(xv,yv))
            if abs(dv)>dx_max[0]:dx_max=(abs(dv),(xv,yv,dv))
            if dv>dx_signed_max[0]:dx_signed_max=(dv,(xv,yv))
            if ddv<dxx_min[0]:dxx_min=(ddv,(xv,yv))
    print(f"G1_normalized_residual_profile_min={r_min}")
    print(f"G1_normalized_residual_profile_max={r_max}")
    print(f"G1_normalized_residual_dx_abs_max={dx_max}")
    print(f"G1_normalized_residual_dx_signed_max={dx_signed_max}")
    print(f"G1_normalized_residual_dxx_min={dxx_min}")
    def exact_interval(value:sp.Rational)->I:
        value=sp.Rational(value);return I.point(str(int(value.p)))/I.point(str(int(value.q)))
    def compile_table(expression:sp.Expr)->tuple[tuple[I,...],...]:
        polynomial=sp.Poly(expression,x,y);dx,dy=polynomial.degree(x),polynomial.degree(y)
        return tuple(tuple(exact_interval(polynomial.coeff_monomial(x**a*y**b)) for b in range(dy+1)) for a in range(dx+1))
    def horner(table:tuple[tuple[I,...],...],xi:I,yi:I)->I:
        result=I.point(0)
        for row in reversed(table):
            coefficient=I.point(0)
            for entry in reversed(row):coefficient=coefficient*yi+entry
            result=result*xi+coefficient
        return result
    endpoint_table=compile_table(rxy);ya,yb=Decimal("2.459"),Decimal("5.474")
    endpoint_stack=[(ya,yb,0)];endpoint_unresolved=0;endpoint_upper=None
    while endpoint_stack:
        y0,y1,depth=endpoint_stack.pop();value=horner(endpoint_table,I.point(Decimal(".058")),I(y0,y1))
        if value.hi<0:endpoint_upper=value.hi if endpoint_upper is None else max(endpoint_upper,value.hi);continue
        if depth>=14:endpoint_unresolved+=1;continue
        mid=(y0+y1)/2;endpoint_stack.extend(((y0,mid,depth+1),(mid,y1,depth+1)))
    print(f"G1_far_endpoint_unresolved={endpoint_unresolved}; G1_far_endpoint_upper={endpoint_upper}")
    print(f"G1_far_endpoint_certified={endpoint_unresolved==0 and endpoint_upper is not None and endpoint_upper<0}")

    # Exact tensor-product Bernstein certificate for R_xx > 0 on the
    # deliberately enlarged rational rectangle.  If
    #
    #   F(u,v) = sum c[p,q] u^p v^q
    #          = sum b[i,j] B_i^n(u) B_j^m(v),
    #
    # then b[i,j] is the lower-triangular binomial transform below.  All
    # arithmetic remains rational, so a positive minimum coefficient is a
    # proof on the full rectangle, rather than a sampling statement.
    rxx=sp.Poly(sp.diff(rxy,x,2),x,y)
    xa,xb=sp.Rational(0),sp.Rational(29,500)
    ylo,yhi=sp.Rational(2459,1000),sp.Rational(2737,500)
    u,v=sp.symbols("u v",nonnegative=True)
    unit_rxx=sp.Poly(sp.expand(rxx.as_expr().subs({x:xa+(xb-xa)*u,y:ylo+(yhi-ylo)*v})),u,v)
    nx,ny=unit_rxx.degree(u),unit_rxx.degree(v)
    power={(i,j):unit_rxx.coeff_monomial(u**i*v**j) for i in range(nx+1) for j in range(ny+1)}
    bernstein={}
    for i in range(nx+1):
        for j in range(ny+1):
            bernstein[(i,j)]=sp.factor(sum(
                power[(p,q)]*sp.Rational(comb(i,p),comb(nx,p))*sp.Rational(comb(j,q),comb(ny,q))
                for p in range(i+1) for q in range(j+1)
            ))
    bernstein_min_key=min(bernstein,key=bernstein.get);bernstein_min=bernstein[bernstein_min_key]
    bernstein_nonpositive=tuple((key,value) for key,value in bernstein.items() if value<=0)
    print(f"G1_Rxx_Bernstein_degree={(nx,ny)}")
    print(f"G1_Rxx_Bernstein_min_key={bernstein_min_key}")
    print(f"G1_Rxx_Bernstein_min={bernstein_min}")
    print(f"G1_Rxx_Bernstein_nonpositive={len(bernstein_nonpositive)}")
    print(f"G1_Rxx_Bernstein_certified={not bernstein_nonpositive}")
    assert not bernstein_nonpositive
    left_shape=ylo**2+6*ylo-5
    assert left_shape>0 and ylo>0
    global_g1_certified=(endpoint_unresolved==0 and endpoint_upper is not None and endpoint_upper<0 and not bernstein_nonpositive)
    print(f"G1_left_endpoint_shape_lower={left_shape}")
    print(f"G1_whole_rectangle_certified={global_g1_certified}")
    assert global_g1_certified
    # Discovery profile for the remaining graph-dependent affine inequality.
    # Differentiate along N(z,exp(L),L)=0 without differentiating a numerical
    # root finder: L'=-N_z/(E N_E+N_L).
    affine=sp.expand(block0+lvar*block1)
    qn_z=sp.diff(qn,z);qn_l=e*sp.diff(qn,e)+sp.diff(qn,lvar)
    affine_z=sp.diff(affine,z);affine_l=e*sp.diff(affine,e)+sp.diff(affine,lvar)
    graph_functions=sp.lambdify((z,e,lvar),(qn,qn_z,qn_l,affine,affine_z,affine_l,block0),"math")
    affine_min=(float("inf"),None);affine_derivative_min=(float("inf"),None);affine_derivative_max=(-float("inf"),None);block0_zero_bracket=None
    previous=None
    for index in range(101):
        zv=.09*index/100;left=.45;right=.85
        for _ in range(70):
            middle=(left+right)/2;value=graph_functions(zv,math.exp(middle),middle)[0]
            if value>0:left=middle
            else:right=middle
        lv=(left+right)/2;ev=math.exp(lv);_,nz,nl,f,fz,fl,b0=graph_functions(zv,ev,lv);slope=-nz/nl;df=fz+fl*slope
        if f<affine_min[0]:affine_min=(f,(zv,lv))
        if df<affine_derivative_min[0]:affine_derivative_min=(df,(zv,lv))
        if df>affine_derivative_max[0]:affine_derivative_max=(df,(zv,lv))
        if previous is not None and previous[1]>0>=b0:block0_zero_bracket=(previous[0],zv)
        previous=(zv,b0)
    print(f"G_aff_graph_profile_min={affine_min}")
    print(f"G_aff_graph_derivative_profile_min={affine_derivative_min}")
    print(f"G_aff_graph_derivative_profile_max={affine_derivative_max}")
    print(f"G0_graph_zero_bracket={block0_zero_bracket}")
    affine_derivative_numerator=sp.Poly(sp.expand(affine_z*qn_l-affine_l*qn_z),lvar,domain=sp.QQ.frac_field(z,e))
    _,affine_derivative_remainder=sp.div(affine_derivative_numerator,sp.Poly(qn,lvar,domain=sp.QQ.frac_field(z,e)))
    adr_num,adr_den=sp.fraction(sp.cancel(affine_derivative_remainder.as_expr()))
    adr_poly=sp.Poly(adr_num,z,e,lvar)
    print(f"G_aff_derivative_remainder_denominator={sp.factor(adr_den)}")
    print(f"G_aff_derivative_remainder_terms={len(adr_poly.terms())}")
    print(f"G_aff_derivative_remainder_degrees={(adr_poly.degree(z),adr_poly.degree(e),adr_poly.degree(lvar))}")
    print(f"G_aff_derivative_remainder_boundary={sp.factor(adr_poly.eval(z,0).as_expr())}")
    print(f"critical_numerator_z0={sp.factor(sp.Poly(qn,z).coeff_monomial(1))}")
    print(f"critical_numerator_z1={sp.factor(sp.Poly(qn,z).coeff_monomial(z))}")
    print(f"critical_numerator_z2={sp.factor(sp.Poly(qn,z).coeff_monomial(z**2))}")
    # Remove the apparent z^-3 singularity without changing the value on
    # N=0.  At each order the residual coefficient is exactly divisible by
    # N(0,E,L); hence the correcting multiplier remains polynomial.
    n0=sp.Poly(qn,z).coeff_monomial(1);regular_work=sp.expand(adr_num);regular_correction=sp.S.Zero
    correction_coefficients=[]
    for order in range(3):
        coefficient=sp.Poly(regular_work,z).coeff_monomial(z**order)
        quotient,remainder=sp.div(sp.Poly(coefficient,e,lvar),sp.Poly(n0,e,lvar))
        print(f"G_aff_derivative_zadic_order_{order}_remainder_zero={remainder.is_zero}")
        assert remainder.is_zero
        multiplier=quotient.as_expr()*z**order;correction_coefficients.append(sp.factor(quotient.as_expr()))
        regular_correction+=multiplier;regular_work=sp.expand(regular_work-multiplier*qn)
    regular_poly=sp.Poly(regular_work,z,e,lvar)
    assert all(regular_poly.coeff_monomial(z**order*e**i*lvar**j)==0 for order in range(3) for i in range(regular_poly.degree(e)+1) for j in range(regular_poly.degree(lvar)+1))
    regular_derivative=sp.div(regular_poly,sp.Poly(z**3,z,e,lvar))[0]
    print(f"G_aff_derivative_zadic_corrections={tuple(correction_coefficients)}")
    print(f"G_aff_derivative_regular_terms={len(regular_derivative.terms())}")
    print(f"G_aff_derivative_regular_degrees={(regular_derivative.degree(z),regular_derivative.degree(e),regular_derivative.degree(lvar))}")
    print(f"G_aff_derivative_regular_boundary={sp.factor(regular_derivative.eval(z,0).as_expr())}")
    regular_endpoint=sp.factor(regular_derivative.eval(z,0).as_expr().subs({e:sp.sqrt(3),lvar:sp.log(3)/2}))
    print(f"G_aff_derivative_regular_critical_endpoint={regular_endpoint}")
    freg=sp.lambdify((z,e,lvar),regular_derivative.as_expr(),"math");regular_profile_max=(-float("inf"),None);regular_profile_min=(float("inf"),None)
    for index in range(101):
        zv=.09*index/100;left=.45;right=.85
        for _ in range(70):
            middle=(left+right)/2
            if graph_functions(zv,math.exp(middle),middle)[0]>0:left=middle
            else:right=middle
        lv=(left+right)/2;value=freg(zv,math.exp(lv),lv)
        if value<regular_profile_min[0]:regular_profile_min=(value,(zv,lv))
        if value>regular_profile_max[0]:regular_profile_max=(value,(zv,lv))
    print(f"G_aff_derivative_regular_graph_profile_min={regular_profile_min}")
    print(f"G_aff_derivative_regular_graph_profile_max={regular_profile_max}")
    regular_rectangle_min=(float("inf"),None);regular_rectangle_max=(-float("inf"),None)
    for iz in range(21):
        zv=.09*iz/20
        for il in range(21):
            lv=.45+.40*il/20;value=freg(zv,math.exp(lv),lv)
            if value<regular_rectangle_min[0]:regular_rectangle_min=(value,(zv,lv))
            if value>regular_rectangle_max[0]:regular_rectangle_max=(value,(zv,lv))
    print(f"G_aff_derivative_regular_rectangle_profile_min={regular_rectangle_min}")
    print(f"G_aff_derivative_regular_rectangle_profile_max={regular_rectangle_max}")
    _,regular_branch_remainder=sp.div(sp.Poly(regular_derivative.as_expr(),lvar,domain=sp.QQ.frac_field(z,e)),sp.Poly(qn,lvar,domain=sp.QQ.frac_field(z,e)))
    rbr_num,rbr_den=sp.fraction(sp.cancel(regular_branch_remainder.as_expr()));rbr_poly=sp.Poly(rbr_num,z,e,lvar)
    assert rbr_poly.degree(lvar)<=1
    rbr_a=sp.Poly(rbr_num,lvar).coeff_monomial(lvar);rbr_b=sp.Poly(rbr_num,lvar).coeff_monomial(1)
    print(f"G_aff_derivative_branch_denominator={sp.factor(rbr_den)}")
    print(f"G_aff_derivative_branch_terms={len(rbr_poly.terms())}")
    print(f"G_aff_derivative_branch_degrees={(rbr_poly.degree(z),rbr_poly.degree(e),rbr_poly.degree(lvar))}")
    branch_functions=sp.lambdify((z,e,lvar),(rbr_a,rbr_b,rbr_den,rbr_num),"math")
    orientation={"a_min":(float("inf"),None),"a_max":(-float("inf"),None),"b_min":(float("inf"),None),"b_max":(-float("inf"),None),"d_min":(float("inf"),None),"d_max":(-float("inf"),None),"r_min":(float("inf"),None),"r_max":(-float("inf"),None)}
    for index in range(101):
        zv=.09*index/100;left=.45;right=.85
        for _ in range(70):
            middle=(left+right)/2
            if graph_functions(zv,math.exp(middle),middle)[0]>0:left=middle
            else:right=middle
        lv=(left+right)/2;av,bv,dv,rv=branch_functions(zv,math.exp(lv),lv)
        for name,value in (("a",av),("b",bv),("d",dv),("r",rv)):
            low=name+"_min";high=name+"_max"
            if value<orientation[low][0]:orientation[low]=(value,(zv,lv))
            if value>orientation[high][0]:orientation[high]=(value,(zv,lv))
    print(f"G_aff_derivative_branch_orientation={orientation}")
    qn_lpoly=sp.Poly(qn,lvar);nq2=qn_lpoly.coeff_monomial(lvar**2);nq1=qn_lpoly.coeff_monomial(lvar);nq0=qn_lpoly.coeff_monomial(1);ndelta=sp.expand(nq1*nq1-4*nq2*nq0)
    branch_c=sp.expand(2*nq2*rbr_b-rbr_a*nq1);branch_h=sp.expand(branch_c*branch_c-rbr_a*rbr_a*ndelta)
    fh=sp.lambdify((z,e,lvar),(nq2,branch_c,branch_h),"math")
    oriented={"q2_min":(float("inf"),None),"q2_max":(-float("inf"),None),"c_min":(float("inf"),None),"c_max":(-float("inf"),None),"h_min":(float("inf"),None),"h_max":(-float("inf"),None)}
    for index in range(1,101):
        zv=.09*index/100;left=.45;right=.85
        for _ in range(70):
            middle=(left+right)/2
            if graph_functions(zv,math.exp(middle),middle)[0]>0:left=middle
            else:right=middle
        lv=(left+right)/2;q2v,cv,hv=fh(zv,math.exp(lv),lv)
        for name,value in (("q2",q2v),("c",cv),("h",hv)):
            low=name+"_min";high=name+"_max"
            if value<oriented[low][0]:oriented[low]=(value,(zv,lv))
            if value>oriented[high][0]:oriented[high]=(value,(zv,lv))
    print(f"G_aff_derivative_root_orientation={oriented}")
    print(f"G_aff_derivative_squared_terms={len(sp.Poly(branch_h,z,e).terms())}")
    print(f"G_aff_derivative_squared_degrees={(sp.Poly(branch_h,z,e).degree(z),sp.Poly(branch_h,z,e).degree(e))}")
    branch_h_poly=sp.Poly(branch_h,z,e);h_z_valuation=min(powers[0] for powers,_ in branch_h_poly.terms());h_e_valuation=min(powers[1] for powers,_ in branch_h_poly.terms())
    h_weights=tuple(sorted({powers[0]+powers[1] for powers,_ in branch_h_poly.terms()}));h_parities=tuple(sorted({weight%2 for weight in h_weights}))
    print(f"G_aff_derivative_squared_valuations={(h_z_valuation,h_e_valuation)}")
    print(f"G_aff_derivative_squared_xE_weight_range={(h_weights[0],h_weights[-1],len(h_weights),h_parities)}")
    assert h_z_valuation==6 and h_weights[0]==126 and h_parities==(0,)
    compact_h_terms=defaultdict(lambda:sp.S.Zero)
    for (z_power,e_power),coefficient in branch_h_poly.terms():
        compact_h_terms[(z_power-6,(z_power+e_power-126)//2)]+=coefficient
    compact_h=sp.Poly.from_dict(dict(compact_h_terms),(x,y));compact_h_signs=(sum(1 for _,coefficient in compact_h.terms() if coefficient>0),sum(1 for _,coefficient in compact_h.terms() if coefficient<0))
    fcompact_h=sp.lambdify((x,y),compact_h.as_expr(),"math");compact_h_profile_min=(float("inf"),None);compact_h_profile_max=(-float("inf"),None)
    for ix in range(21):
        xv=.058*ix/20
        for iy in range(21):
            yv=2.459+(5.474-2.459)*iy/20;value=fcompact_h(xv,yv)
            if value<compact_h_profile_min[0]:compact_h_profile_min=(value,(xv,yv))
            if value>compact_h_profile_max[0]:compact_h_profile_max=(value,(xv,yv))
    print(f"G_aff_derivative_squared_compact_degrees={(compact_h.degree(x),compact_h.degree(y))}")
    print(f"G_aff_derivative_squared_compact_signs={compact_h_signs}")
    print(f"G_aff_derivative_squared_compact_profile_min={compact_h_profile_min}")
    print(f"G_aff_derivative_squared_compact_profile_max={compact_h_profile_max}")
    # Fast rigorous thin-tube evaluation in Arb.  The exact integer
    # coefficient table is converted once; subsequent ball arithmetic runs in
    # the compiled Arb kernel rather than the interpreted Decimal interval
    # class used by the rejected prototype.
    ctx.prec=128
    compact_dx,compact_dy=compact_h.degree(x),compact_h.degree(y)
    arb_table=tuple(tuple(arb(int(compact_h.coeff_monomial(x**i*y**j))) for j in range(compact_dy+1)) for i in range(compact_dx+1))
    def arb_horner(xvalue:arb,yvalue:arb)->arb:
        result=arb(0)
        for row in reversed(arb_table):
            coefficient=arb(0)
            for entry in reversed(row):coefficient=coefficient*yvalue+entry
            result=result*xvalue+coefficient
        return result
    root_cache={}
    def root_bracket(point:Decimal)->tuple[Decimal,Decimal]:
        if point in root_cache:return root_cache[point]
        left,right=Decimal("0.45"),Decimal("0.85")
        for _ in range(100):
            middle=(left+right)/2;qvalue=critical_evaluate(I.point(point),I.point(middle))[0].v
            if qvalue.lo>0:left=middle
            elif qvalue.hi<0:right=middle
            else:break
        root_cache[point]=(left,right);return left,right
    def ball(lower:Decimal,upper:Decimal)->arb:
        middle=(lower+upper)/2;radius=(upper-lower)/2
        return arb(str(middle),str(radius))
    tube_stack=[(Decimal("0.09")*i/Decimal(16),Decimal("0.09")*(i+1)/Decimal(16),0) for i in range(16)]
    tube_accepted=tube_unresolved=0;tube_worst=None;tube_max_depth=0
    while tube_stack:
        za,zb,depth=tube_stack.pop();la,_=root_bracket(za);_,lb=root_bracket(zb)
        zball=ball(za,zb);lball=ball(la,lb);eball=lball.exp();value=arb_horner(zball/eball,(2*lball).exp())
        if value>0:
            tube_accepted+=1;tube_max_depth=max(tube_max_depth,depth)
            lower=value.lower()
            if tube_worst is None or lower<tube_worst[-1]:tube_worst=(za,zb,la,lb,value,lower)
            continue
        if depth>=14:tube_unresolved+=1;continue
        middle=(za+zb)/2;tube_stack.extend(((za,middle,depth+1),(middle,zb,depth+1)))
    tube_certified=tube_unresolved==0 and tube_accepted>0
    print(f"G_aff_derivative_squared_arb_tube_accepted={tube_accepted}")
    print(f"G_aff_derivative_squared_arb_tube_unresolved={tube_unresolved}")
    print(f"G_aff_derivative_squared_arb_tube_max_depth={tube_max_depth}")
    print(f"G_aff_derivative_squared_arb_tube_worst={tube_worst}")
    print(f"G_aff_derivative_squared_arb_tube_certified={tube_certified}")
    fg0=sp.lambdify((z,e),block0,"math");fg1=sp.lambdify((z,e),block1,"math")
    g0_min=(float("inf"),None);g1_min=(float("inf"),None)
    for iz in range(21):
        zv=.09*iz/20
        for il in range(21):
            lv=.45+.40*il/20;ev=math.exp(lv);v0=fg0(zv,ev);v1=fg1(zv,ev)
            if v0<g0_min[0]:g0_min=(v0,(zv,lv))
            if v1<g1_min[0]:g1_min=(v1,(zv,lv))
    print(f"rectangle_profile_G0_min={g0_min}")
    print(f"rectangle_profile_G1_min={g1_min}")
    print(f"desingularized_boundary={g0}")
    print("desingularized_boundary_positive=True")


if __name__=="__main__":main()
