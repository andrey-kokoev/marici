import {probePECoupledNRouting} from '../research/strominger/pe-coupled-n-routing.mjs';
console.log(JSON.stringify({sizes:[0,1,2,3].map(r=>probePECoupledNRouting(r).audit),largerAmbient:probePECoupledNRouting(3,3).audit,occupancyRemoved:probePECoupledNRouting(3,2,{occupied:false}).audit},null,2));
