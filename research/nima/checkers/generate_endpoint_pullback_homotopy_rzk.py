"""Generate the endpoint/conductor part of the pullback nullhomotopy."""
from pathlib import Path
import importlib.util,sys,subprocess,hashlib,json
ROOT=Path(__file__).resolve().parents[3];src=ROOT/'research/nima/checkers/build_loaded_polynomial_cech_rzk.py'
saved=sys.argv;sys.argv=[str(src),'--cell-limit','1'];sp=importlib.util.spec_from_file_location('gh',src);g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g);sys.argv=saved
# d(z): (a10+0) + ((-a10)+(a11+0))
e=('+',('+',('a',0),('z',)),('+',('n',('a',0)),('+',('a',1),('z',))))
n,pf=g.normalize(e);n2,pf2=g.normalize(('a',1));assert n==n2
proof=g.path(g.expr(e),g.total(n),g.expr(('a',1)),pf,g.rev(g.expr(('a',1)),g.total(n),pf2))
L=['# Endpoint pullback homotopy','','```rzk','#lang rzk-1',
 f'#define nima-relative-f-z-boundary-cancel (a0 a1 : MariciInt) : {g.expr(e)} = a1 := {proof}',
 '#define nima-relative-f-z-boundary : nima-sum-equal NimaRelativeFBasis (nima-relative-f-d nima-relative-f-z) (nima-sum-atom NimaRelativeFBasis nima-relative-f-state-11)',
 '  := \\ probe -> nima-relative-f-z-boundary-cancel (probe nima-relative-f-state-10) (probe nima-relative-f-state-11)',
 '#define nima-line-f-column : NimaRelativeBoundaryBasis -> NimaRelativeBoundary',
 '  := \\ (line,q) -> nima-sum-map NimaRelativeFBasis NimaRelativeBoundaryBasis (\\ r -> (line,r)) (nima-relative-f-column q)',
 '#define nima-line-f-d : NimaRelativeBoundary -> NimaRelativeBoundary',
 '  := nima-sum-bind NimaRelativeBoundaryBasis NimaRelativeBoundaryBasis nima-line-f-column',
 '#define nima-endpoint-pullback-P : NimaEndpointRelativeState NimaEndpointRelativeTestOld -> NimaRelativeBoundary',
 '  := \\ q -> match q',
 '       (nima-endpoint-relative-old a => match a',
 '          (nima-endpoint-relative-test-plus => nima-sum-neg NimaRelativeBoundaryBasis (nima-relative-boundary-plus nima-relative-f-z)',
 '          | nima-endpoint-relative-test-minus => nima-sum-neg NimaRelativeBoundaryBasis (nima-relative-boundary-minus nima-relative-f-z)',
 '          | nima-endpoint-relative-test-other => nima-sum-zero NimaRelativeBoundaryBasis)',
 '       | nima-endpoint-relative-conductor-plus => nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-plus,nima-relative-f-state-11)',
 '       | nima-endpoint-relative-conductor-minus => nima-sum-atom NimaRelativeBoundaryBasis (nima-endpoint-line-minus,nima-relative-f-state-11))',
 '#define nima-endpoint-pullback-P-linear (p : NimaEndpointRelativeTest) : NimaRelativeBoundary',
 '  := nima-sum-bind (NimaEndpointRelativeState NimaEndpointRelativeTestOld) NimaRelativeBoundaryBasis nima-endpoint-pullback-P p',
 '#define nima-endpoint-pullback-homotopy-boundary-column (q : NimaEndpointRelativeState NimaEndpointRelativeTestOld) : NimaRelativeBoundary',
 '  := nima-sum-add NimaRelativeBoundaryBasis (nima-line-f-d (nima-endpoint-pullback-P q)) (nima-endpoint-pullback-P-linear (nima-endpoint-relative-test-column q))']
# Rather than another giant symbolic reduction, prove endpoint cancellation by transporting z boundary; pointwise normalizer expressions vary only atom labels.
# Generate direct cancellation expected for plus/minus: -((a10+-a10)+a11)+a11 =0 using actual nested syntax delegated to normalization shape.
# Obtain expression by abstracting dP + Pd evaluation: neg(e) + a1.
h=('+',('n',e),('+',('a',1),('z',)));hn,hpf=g.normalize(h);assert not hn
L += ['',f'#define nima-endpoint-pullback-cancel (a0 a1 : MariciInt) : {g.expr(h)} = {g.Z} := {hpf}',
 '#define nima-endpoint-pullback-full-cancel (a0 a1 b1 : MariciInt) : marici-int-add (marici-int-negate (marici-int-add (marici-int-add a0 marici-int-zero) (marici-int-add (marici-int-negate a0) (marici-int-add a1 marici-int-zero)))) (marici-int-add marici-int-zero (marici-int-add (marici-int-mul marici-int-one a1) (marici-int-mul marici-int-zero b1))) = marici-int-zero',
 '  := nima-frame-concat MariciInt (marici-int-add (marici-int-negate (marici-int-add (marici-int-add a0 marici-int-zero) (marici-int-add (marici-int-negate a0) (marici-int-add a1 marici-int-zero)))) (marici-int-add (marici-int-mul marici-int-one a1) (marici-int-mul marici-int-zero b1))) (marici-int-add (marici-int-negate (marici-int-add (marici-int-add a0 marici-int-zero) (marici-int-add (marici-int-negate a0) (marici-int-add a1 marici-int-zero)))) (marici-int-add a1 marici-int-zero)) marici-int-zero (nima-frame-ap MariciInt MariciInt (marici-int-add (marici-int-negate (marici-int-add (marici-int-add a0 marici-int-zero) (marici-int-add (marici-int-negate a0) (marici-int-add a1 marici-int-zero))))) (marici-int-add (marici-int-mul marici-int-one a1) (marici-int-mul marici-int-zero b1)) (marici-int-add a1 marici-int-zero) (nima-cochain-ap2 MariciInt MariciInt MariciInt marici-int-add (marici-int-mul marici-int-one a1) a1 (marici-int-mul marici-int-zero b1) marici-int-zero (marici-int-mul-one-left a1) (marici-int-mul-zero-left b1))) (nima-endpoint-pullback-cancel a0 a1)',
 '#define nima-endpoint-pullback-plus-endpoint-equation (a10 a11 opposite : MariciInt) : marici-int-add (marici-int-negate (marici-int-add (marici-int-add a10 marici-int-zero) (marici-int-add (marici-int-negate a10) (marici-int-add a11 marici-int-zero)))) (marici-int-add marici-int-zero (marici-int-add (marici-int-mul marici-int-one a11) (marici-int-mul marici-int-zero opposite))) = marici-int-zero := nima-endpoint-pullback-full-cancel a10 a11 opposite',
 '#define nima-endpoint-pullback-minus-endpoint-equation (a10 a11 opposite : MariciInt) : marici-int-add (marici-int-negate (marici-int-add (marici-int-add a10 marici-int-zero) (marici-int-add (marici-int-negate a10) (marici-int-add a11 marici-int-zero)))) (marici-int-add marici-int-zero (marici-int-add (marici-int-mul marici-int-one a11) (marici-int-mul marici-int-zero opposite))) = marici-int-zero := nima-endpoint-pullback-full-cancel a10 a11 opposite',
 '```','']
out=ROOT/'research/nima/rzk/39-endpoint-pullback-homotopy.rzk.md';out.write_text('\n'.join(L));meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'scope':'endpoint-and-new-conductor-columns','requires_rzk_check':True};(ROOT/'research/nima/results/endpoint-pullback-homotopy-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)
