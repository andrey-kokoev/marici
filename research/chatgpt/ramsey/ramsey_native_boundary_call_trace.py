"""Trace actual native call boundaries without adding an exit policy. Contrast the quotient constructor with the explicit live receipt adapter, and separate handoff from completion."""
from pathlib import Path
import json,runpy,sys
D=Path(__file__).resolve().parent

def capture(fn,owner):
    calls=[]
    def observe(frame,event,arg):
        if event!='call' or frame.f_code.co_name not in ('execute','successor','compose_payloads'):return
        module=frame.f_globals.get('__name__');caller=frame.f_back
        if module not in ('check_seed_typed_execution','retained_path_successor') or Path(caller.f_code.co_filename).name!=owner:return
        calls.append((frame.f_code.co_name,list(frame.f_locals.get('word',()))))
    old=sys.getprofile();sys.setprofile(observe)
    try: result=fn()
    finally:sys.setprofile(old)
    return result,calls

def run():
    src='ramsey_row_quotient_constructor.py';q,constructor=capture(lambda:runpy.run_path(str(D/src)),src);assert len(q['final'])==1 and not constructor
    import ramsey_live_matching_receipt as live
    result,calls=capture(live.run,'ramsey_live_matching_receipt.py');assert len(calls)==24;observed=[]
    for i,row in enumerate(r for binding in result for r in binding['rows']):
        group=calls[3*i:3*i+3];assert all(k=='execute' for k,_ in group);a,b,s=[w for _,w in group];assert len(a)==len(b)==1 and not {'AB','BA'}.intersection(a+b) and {'AB','BA'}<=set(s) and a+b+s==row['receipt'];assert row['stops'][5]==(29,0);observed.append(dict(prefix=a+b,suffix=s,bit=row['bit']))
    return dict(constructor_calls=constructor,live_calls=len(calls),cases=observed)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_native_boundary_call_trace.json').write_text(json.dumps(out)+'\n')
