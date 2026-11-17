import assert from 'node:assert/strict';

export function selectBrowserMatrix(manifest,args=[]) {
 assert.equal(manifest.schema,'marici.isotope-wiring-browser-matrix.v1');
 assert.deepEqual(manifest.engines,['chromium','firefox','webkit']);
 assert(Array.isArray(manifest.cases)&&manifest.cases.length>0,'Empty browser matrix');
 const ids=manifest.cases.map(c=>c.id);
 assert.equal(new Set(manifest.cases.map(c=>c.script)).size,ids.length,'Duplicate browser script');
 assert.equal(new Set(ids).size,ids.length,'Duplicate browser case');
 for(const c of manifest.cases)assert(/^[a-z0-9-]+$/.test(c.id)&&/^test-[a-z0-9-]+\.mjs$/.test(c.script)&&c.scope,'Unsafe or incomplete browser case');
 const engines=[],cases=[];
 for(const arg of args){
  if(arg.startsWith('--case=')){
   const id=arg.slice(7);assert(ids.includes(id),'Unknown browser case: '+id);cases.push(id);
  }else{assert(manifest.engines.includes(arg),'Unknown browser engine/argument: '+arg);engines.push(arg);}
 }
 return {engines:engines.length?[...new Set(engines)]:[...manifest.engines],cases:cases.length?manifest.cases.filter(c=>cases.includes(c.id)):[...manifest.cases]};
}

export function browserMatrixResult(manifest,selection,runs,sourceUnchanged) {
 if(!sourceUnchanged)return 'invalidated';
 const key=(engine,id)=>engine+':'+id;
 const expected=new Set(selection.engines.flatMap(e=>selection.cases.map(c=>key(e,c.id))));
 const seen=new Set();
 for(const run of runs){
  const id=key(run.engine,run.case);
  if(!expected.has(id)||seen.has(id)||run.status!=='passed')return 'failed';
  seen.add(id);
 }
 if(seen.size!==expected.size)return 'failed';
 const full=selection.engines.length===manifest.engines.length&&manifest.engines.every(e=>selection.engines.includes(e))&&selection.cases.length===manifest.cases.length&&manifest.cases.every(c=>selection.cases.some(s=>s.id===c.id));
 return full?'passed':'partial_pass';
}
