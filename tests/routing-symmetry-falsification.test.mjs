import test from 'node:test';import assert from 'node:assert/strict';
import {enumerateThreefoldPortMatchings} from '../research/strominger/routing-symmetry-falsification.mjs';
import {probePECoupledNRouting} from '../research/strominger/pe-coupled-n-routing.mjs';
test('C3 symmetry alone allows 27 local reversible matchings, not just three',()=>{
 assert.deepEqual(enumerateThreefoldPortMatchings(),{totalReversibleMatchings:10395,threefoldMatchings:27,withCompanionStrandsFixed:3,nontrivialWithCompanionFixed:2});
});
test('all four nontrivial distinguished-triplet handedness choices retain 126 pairs',()=>{
 for(const routingPolicy of['cyclic','reverse','vacancy-reversed','occupied-reversed']){const a=probePECoupledNRouting(3,2,{routingPolicy}).audit;assert.equal(a.dualResponsePairs,126);assert.equal(a.closedLoops,0);assert.equal(a.coupledNCells,248);assert.equal(a.dualityVerified,true);assert.equal(a.threefoldSymmetryVerified,true);}
});
test('same triggers plus companion-triplet response falsify symmetry-forced 126',()=>{
 for(const[routingPolicy,loops]of[['both-triplets',128],['equator-reversed',144]]){const p=probePECoupledNRouting(3,2,{routingPolicy}),a=p.audit;assert.equal(a.coupledNCells,248);assert.equal(a.changedOpenChannels,396);assert.equal(a.dualResponsePairs,198);assert.equal(a.closedLoops,loops);assert.equal(a.dualityVerified,true);assert.equal(a.threefoldSymmetryVerified,true);assert.equal(a.branchingJunctions,0);assert.equal(a.localizedNeutronCount,null);
 const ids=p.paths.flatMap(path=>path.passes.map(p=>p.id));assert.equal(ids.length,a.localPasses);assert.equal(new Set(ids).size,ids.length);for(const path of p.paths.filter(p=>p.closed))assert.deepEqual(path.points[0],path.points.at(-1));
 const outer=probePECoupledNRouting(3,3,{routingPolicy}).audit;assert.equal(outer.dualResponsePairs,198);assert.equal(outer.closedLoops,loops);
 const empty=probePECoupledNRouting(3,2,{routingPolicy,occupied:false}).audit;assert.equal(empty.changedOpenChannels,0);assert.equal(empty.closedLoops,0);}
});
test('trigger freedom gives another counterexample; symmetry-breaking control is rejected',()=>{
 const a=probePECoupledNRouting(3,2,{routingPolicy:'vacancy-only'}).audit;assert.equal(a.dualResponsePairs,60);assert.equal(a.coupledNCells,80);assert.equal(a.dualityVerified,true);assert.equal(a.threefoldSymmetryVerified,true);
 assert.throws(()=>probePECoupledNRouting(3,2,{routingPolicy:'both-triplets-odd'}),/broke P\/E geometric duality/);
});
