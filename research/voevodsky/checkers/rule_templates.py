"""Hand-declared full runtime templates; fail closed on missing rule.

x/y are removed agents; integers are fresh allocation ordinals (zero based).
Port lists are sets semantically; edge ordering/orientation is irrelevant.
"""
TEMPLATES={}
def rule(key,nodes,edges):
 TEMPLATES[key]=(tuple((k,tuple(sorted(ps.split()))) for k,ps in nodes),tuple(sorted(tuple(sorted(e.split('--'))) for e in edges.split())))
rule('GS--DONE',[('FUEL','p s u r o c')],'x.f--0.p x.b--0.u x.s--0.s x.r--0.r x.o--0.o x.c--0.c')
rule('GA--DONE',[('ABc','p a r c')],'x.s--0.a x.b--0.p x.r--0.r x.c--0.c')
rule('GU--DONE',[('ULc','p a r c')],'x.s--0.p x.b--0.a x.r--0.r x.c--0.c')
rule('GM--DONE',[('COPY','p a b'),('QB','p a r c')],'x.s--0.p x.r--0.a 0.b--1.a x.b--1.p x.o--1.r x.c--1.c')
rule('GC--DONE',[('COPY','p a b'),('QB','p a r c'),('WAIT','p b s r t f o c')],'x.s--0.p 0.a--2.s 0.b--1.a x.b--1.p 1.r--2.b 1.c--2.p x.r--2.r x.t--2.t x.f--2.f x.o--2.o x.c--2.c')
rule('WAIT--DONE',[('PICK','p s r t f o c')],'x.b--0.p x.s--0.s x.r--0.r x.t--0.t x.f--0.f x.o--0.o x.c--0.c')
for head,selected,rejected in [('TRUE','t','f'),('FALSE','f','t')]:
 rule('PICK--'+head,[('ABc','p a r c'),('EA','p r'),('JOIN','p a c'),(head,'p')],f'x.{selected}--0.p x.s--0.a x.r--0.r 0.c--2.p x.{rejected}--1.p 1.r--2.a x.c--2.c x.o--3.p')
rule('JOIN--DONE',[('JOINR','p c')],'x.a--0.p x.c--0.c')
rule('JOINR--DONE',[('DONE','p')],'x.c--0.p')

from remaining_rule_templates import install
install(rule)

def check_template(types,names,edges,new,*,before):
 key='--'.join(n.split('_')[0] for n in names)
 if key not in TEMPLATES:raise ValueError('uncovered rule: '+key)
 fresh=sorted(new,key=lambda item:int(item[0].rsplit('_',1)[1]))
 mapping={names[0]:'x',names[1]:'y'}
 for slot,(n,ps) in enumerate(fresh):
  if int(n.rsplit('_',1)[1])!=before+slot+1:raise ValueError('noncontiguous allocation')
  mapping[n]=str(slot)
 def port(p):
  n,s=p.split('.');return mapping[n]+'.'+s
 actual=(tuple((n.split('_')[0],tuple(sorted(ps))) for n,ps in fresh),tuple(sorted(tuple(sorted((port(a),port(b)))) for a,b in edges)))
 if actual!=TEMPLATES[key]:raise ValueError('rule template mismatch: '+key)
 return key
