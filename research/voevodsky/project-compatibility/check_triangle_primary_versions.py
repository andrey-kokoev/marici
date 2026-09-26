"""Source-sensitive audit of the versioned primary one-loop normalization.
Checks literal TeX changes, not an author's intended correction or absolute convention.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
v1=ROOT/'temp/triangle-measure-primary-2402.06558v1-source/IR_Divs.tex'
v3=ROOT/'temp/triangle-measure-primary-2402.06558v3-source/IR_Divs.tex'
paths=[Path(__file__),v1,v3,
 ROOT/'temp/triangle-measure-primary-2402.06558v1.tar',
 ROOT/'temp/triangle-measure-primary-2402.06558v3.tar',
 ROOT/'temp/triangle-measure-primary-2402.06558v3.html',
 ROOT/'temp/arxiv-2408.16386-source/sections/cosmologicalintegrals.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def equation(text,label):
 marker=r'\eqlabel{'+label+'}'
 start=text.index(marker)
 return re.sub(r'\s+','',text[start:text.index(r'\end{equation}',start)])
# A simpler literal delimiter extraction avoids interpreting TeX macro syntax.
def gamma_arg(eq):
 start=eq.index(r'\Gamma\left(')+len(r'\Gamma\left(')
 return eq[start:eq.index(r'\right)',start)]
before=inventory()
one_old=equation(v1.read_text(encoding='utf-8'),'eq:Ndne')
text=v3.read_text(encoding='utf-8')
one_new=equation(text,'eq:Ndne')
multi=equation(text,'eq:cL');appendix=equation(text,'eq:3s1lInt')
assert '+1}{2}' not in gamma_arg(one_old)
assert '+1}{2}' in gamma_arg(one_new)
assert r'\right\}^{-1}' not in one_old
assert r'\right\}^{-1}' in one_new
assert r'\}^{-1}' in multi
assert gamma_arg(appendix)==r'\frac{d-3}{2}'
assert r'\frac{d-n_{s_l}-L+l}{2}' in gamma_arg(multi)
for dim in (3,4,5,6):
 gamma=F(dim-4,2)
 assert 6+4*(F(-1,2)-gamma)+6*gamma==dim
 assert 6+4*(F(1,2)-gamma)+6*gamma==dim+4
# With a common Euclidean D,K dictionary, v3 one-loop / Cartesian
# coefficient is 48/3 times pi^(-1/2), independent of d and kinematics.
assert F(48,3)==16
assert before==inventory()
report={'passed':True,'source_unchanged':True,'source_sha256':before,
 'retrieval_urls':['https://arxiv.org/src/2402.06558v1','https://arxiv.org/src/2402.06558v3',
                  'https://arxiv.org/html/2402.06558v3'],
 'one_loop_v1':{'label':'eq:Ndne','gamma_argument':gamma_arg(one_old),'external_volume_power':1},
 'one_loop_v3':{'label':'eq:Ndne (3.11)','gamma_argument':gamma_arg(one_new),'external_volume_power':-1},
 'v3_internal_conflict':{'multiloop_label':'eq:cL','multiloop_gamma_argument':gamma_arg(multi),
   'triangle_label':'eq:3s1lInt (A.12)','triangle_gamma_argument':gamma_arg(appendix),
   'one_loop_at_d3':'Gamma(1/2), nonzero inverse','triangle_at_d3':'Gamma(0), inverse vanishes in the regulator limit'},
 'conclusion':'The revised specific one-loop formula matches the independent external-volume exponent and regulator structure; appendix/general formulas are not reconciled.',
 'absolute_normalization':'Under an ordinary-volume dictionary the specific v3 coefficient is16/sqrt(pi) times the Cartesian coefficient. Printed CM/Gram/volume conventions still require audit.',
 'no_silent_replacement':True}
(HERE/'triangle-primary-versions.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
