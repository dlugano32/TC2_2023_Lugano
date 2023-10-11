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
float float_fir_taps[FIR_TAP_NUM] = {	-0.057398970908269474,
										-0.004999788910768728,
										-0.004004529351799197,
										-0.002219521369345348,
										 0.000505258700698784,
										 0.004087986997725539,
										 0.008502809193304270,
										 0.013630725644450595,
										 0.019381081919970597,
										 0.025581803520127439,
										 0.032084786125957172,
										 0.038673097364851951,
										 0.045162729747569894,
										 0.051318844919700235,
										 0.056955774120560465,
										 0.061857002901818330,
										 0.065872395112153689,
										 0.068838069779585065,
										 0.070669780009158453,
										 0.071280505215630993,
										 0.070669780009158453,
										 0.068838069779585065,
										 0.065872395112153689,
										 0.061857002901818330,
										 0.056955774120560465,
										 0.051318844919700235,
										 0.045162729747569894,
										 0.038673097364851951,
										 0.032084786125957172,
										 0.025581803520127438,
										 0.019381081919970598,
										 0.013630725644450595,
										 0.008502809193304270,
										 0.004087986997725539,
										 0.000505258700698784,
										-0.002219521369345348,
										-0.004004529351799197,
										-0.004999788910768728,
										-0.057398970908269474};

////Plantilla2
//float float_fir_taps[FIR_TAP_NUM] = {
//														-0.000163773823403122,
//														 0.003210980170084704,
//														 0.009197191531208930,
//														 0.012267991335825297,
//														 0.007055607909213318,
//														-0.005433488515563998,
//														-0.016640194970777043,
//														-0.017456693948339371,
//														-0.008063307636007272,
//														-0.000234560620256806,
//														-0.006995766191640451,
//														-0.027092264783830658,
//														-0.039827559888669470,
//														-0.019480518214305888,
//														 0.039267846526197643,
//														 0.107089532843489530,
//														 0.133965500115171610,
//														 0.085649171142886324
//														-0.024772800403268767,
//														-0.137964881062733302,
//														 0.814349175770745060,
//														-0.137964881062733302,
//														-0.024772800403268767,
//														 0.085649171142886324,
//														 0.133965500115171610,
//														 0.107089532843489529,
//														 0.039267846526197643,
//														-0.019480518214305888,
//														-0.039827559888669470,
//														-0.027092264783830658,
//														-0.006995766191640451,
//														-0.000234560620256806,
//														-0.008063307636007272,
//														-0.017456693948339371,
//														-0.016640194970777043,
//														-0.005433488515563998,
//														 0.007055607909213318,
//														 0.012267991335825297,
//														 0.009197191531208930,
//														 0.003210980170084704,
//														-0.000163773823403129};

int32_t iir_taps[IIR_TAP_NUM] = {0};
float float_iir_taps[IIR_TAP_NUM] = {	0.0243291191293037,0.0486582382586074,0.0243291191293037,   1,-1.7861009996060575,0.8834174761232725,
										0.0219634728361699,0.0439269456723398,0.0219634728361699,   1,-1.6124291462839451,0.7002830376286249,
										0.0204421556472663,0.0408843112945326,0.0204421556472663,   1,-1.5007429755937021,0.5825115981827674,
										0.0197035413515773,0.0394070827031546,0.0197035413515773,   1,-1.4465182531595728,0.5253324185658821};
