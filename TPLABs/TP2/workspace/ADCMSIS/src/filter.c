/*
===============================================================================
 Name        : filter.c
 Authors     : Israel Pavelek, Cesar Fuoco
 Version     : 1.0
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#include "filter.h"
#include <stdint.h>

int32_t fir_taps[FIR_TAP_NUM] = {0};
//Plantilla 1
float float_fir_taps[FIR_TAP_NUM] = {-0.05162433733236522,-0.007672519422928516,-0.00678880781242267,-0.004898142125166312,-0.0018130222403740636,0.0023430473577484546,0.007554643562306183,0.013839970332732366,0.02085058754485809,0.02841826251623787,0.0363856965421772,0.04440887725675523,0.052207713769222654,0.05945363169895248,0.06583915761165324,0.07108412576908336,0.07503778800290847,0.07746972104699341,0.078299568689035,0.07746972104699341,0.07503778800290847,0.07108412576908336,0.06583915761165324,0.05945363169895248,0.052207713769222654,0.04440887725675523,0.0363856965421772,0.02841826251623787,0.02085058754485809,0.013839970332732366,0.007554643562306183,0.0023430473577484546,-0.0018130222403740636,-0.004898142125166312,-0.00678880781242267,-0.007672519422928516,-0.05162433733236522};
//Plantilla2
//float float_fir_taps[FIR_TAP_NUM] = {-1952275.53,-7283316.43,-11851519.18,-4161036.74,23638153.12,57666421.52,62125827.60,13848072.28,-56693085.09,-79215776.40,-28628594.88,7124111.22,-101795610.12,-335053228.42,-429914842.67,-96426810.41,590432807.95,1088115179.35,870202891.76,102748886.29,-345198547.10,130123570.71,856029220.52,255279398.53,-2281042737.47,-4954360461.76,-4731830528.81,-654176455.84,4270649121.22,5588521800.10,2543634267.81,-64978982.15,3112375227.34,104683496590215.00,126352602475743.00,1864570856.89,-171698231408463.00,-286426240999588.00,-210806561906241.00,-1666147495.17,8985306187.56,66480647.49,-131262881431749.00,-2727195065.89,374501402822146.00,751254078907615.00,666434102817998.00,6009757146.14,-591923435900377.00,-723842578883738.00,-319005813176724.00,198859693.63,-330375876261921.00,-106154959725504.00,-120887051776905.00,-113577629172905.00,163164982815644.00,254821252425799.00,176789551990219.00,8896900560.41,-753259817189625.00,-3733153369.76,924689182760167.00,117490473030069.00,-268195835938045.00,-508184746211929.00,-427801318724926.00,-229541237110554.00,379661198059328.00,441143525339202.00,186093142362116.00,-273694288.68,192579079389455.00,588745520798072.00,641573083270842.00,326065639204522.00,-878196842050234.00,-131543680758608.00,-878827352727475.00,-228292847185695.00,379959710748514.00,125476054945159.00,-446649121938965.00,-259404029145641.00,134356086466662.00,248365459294635.00,205138127253060.00,455316270213645.00,-194059691198293.00,-223667088566061.00,-938813187703792.00,132674175.13,-113094444385248.00,-352052061717508.00,-399712045768695.00,-509639812652381.00,695856637537412.00,118451801827194.00,958203385545079.00,321633209789899.00,-109990205271541.00,732820672849811.00,-109990205271541.00,321633209789899.00,958203385545079.00,118451801827194.00,695856637537412.00,-509639812652381.00,-399712045768695.00,-352052061717508.00,-113094444385248.00,132674175.13,-938813187703792.00,-223667088566061.00,-194059691198293.00,455316270213645.00,205138127253060.00,248365459294635.00,134356086466662.00,-259404029145641.00,-446649121938965.00,125476054945159.00,379959710748514.00,-228292847185695.00,-878827352727475.00,-131543680758608.00,-878196842050234.00,326065639204522.00,641573083270842.00,588745520798072.00,192579079389455.00,-273694288.68,186093142362116.00,441143525339202.00,379661198059328.00,-229541237110554.00,-427801318724926.00,-508184746211929.00,-268195835938045.00,117490473030069.00,924689182760167.00,-3733153369.76,-753259817189625.00,8896900560.41,176789551990219.00,254821252425799.00,163164982815644.00,-113577629172905.00,-120887051776905.00,-106154959725504.00,-330375876261921.00,198859693.63,-319005813176724.00,-723842578883738.00,-591923435900377.00,6009757146.14,666434102817998.00,751254078907615.00,374501402822146.00,-2727195065.89,-131262881431749.00,66480647.49,8985306187.56,-1666147495.17,-210806561906241.00,-286426240999588.00,-171698231408463.00,1864570856.89,126352602475743.00,104683496590215.00,3112375227.34,-64978982.15,2543634267.81,5588521800.10,4270649121.22,-654176455.84,-4731830528.81,-4954360461.76,-2281042737.47,255279398.53,856029220.52,130123570.71,-345198547.10,102748886.29,870202891.76,1088115179.35,590432807.95,-96426810.41,-429914842.67,-335053228.42,-101795610.12,7124111.22,-28628594.88,-79215776.40,-56693085.09,13848072.28,62125827.60,57666421.52,23638153.12,-4161036.74,-11851519.18,-7283316.43,-1952275.53}
int32_t iir_taps[IIR_TAP_NUM] = {0};
float float_iir_taps[IIR_TAP_NUM] = {0.010419890902565022,0.020839781805130044,0.010419890902565022,1.0,-1.6911935001269052,0.7328730637371653};