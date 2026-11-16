import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {bindCa46LocalPaths,planarFrameControl,studyDiagramFrameReturn} from '../examples/isotope-wiring/core/diagram-path-trial.mjs';
import {auditFrameReturn} from '../examples/isotope-wiring/core/frame-return.mjs';
const context=vm.createContext({}),html=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8');
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
const definition=JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().Ca46)),svg=context.IsotopeWiring.renderSVG(definition,{interactive:true,standalone:false});
test('binds all twenty PE occurrences and six current coherence contours',()=>{
 const b=bindCa46LocalPaths(definition,svg);assert.equal(b.topology.walks.length,26);assert.equal(b.counts.localPEWalks,20);assert.equal(b.counts.neutronWrapperWalks,6);assert.equal(b.counts.unboundVerticalDiagonals,10);
 assert.deepEqual(b.bindings.filter(x=>x.source.wrapper).map(x=>x.source.spans),[['s1','s2'],['s2','s3'],['s1','s2','s3'],['s3','s4'],['s2','s3','s4'],['s1','s2','s3','s4']]);
 assert(b.topology.edges.every(e=>e.transport===undefined));assert.equal(auditFrameReturn(b.topology).status,'unknown');
});
test('same current drawing supports both returning and nonreturning frame controls',()=>{
 const before=JSON.stringify(definition),r=studyDiagramFrameReturn(definition,svg);assert.equal(r.status,'unknown');assert.equal(r.planarControl.status,'verified');assert.equal(r.twistedControl.status,'refuted');assert.equal(r.twistedControl.walks.filter(w=>w.status==='refuted').length,1);assert.equal(JSON.stringify(definition),before);
});
test('missing drawing bindings are rejected, not silently skipped',()=>{
 assert.throws(()=>bindCa46LocalPaths({...definition,id:'Ca44'},svg));assert.throws(()=>bindCa46LocalPaths(definition,svg.replace('data-cell="s1-00" role="button"','data-cell="missing" role="button"')));
 assert.throws(()=>bindCa46LocalPaths(definition,svg.replace('space-frame trial-shell2-wrapper','removed-wrapper')));
});
test('declared candidate inverses are necessary even for the flat control',()=>{
 const t=planarFrameControl(bindCa46LocalPaths(definition,svg));t.edges=t.edges.filter(e=>e.id!==t.edges[0].reverse);assert.equal(auditFrameReturn(t).status,'refuted');
});
