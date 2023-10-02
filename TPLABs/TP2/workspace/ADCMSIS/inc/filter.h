
/*
===============================================================================
 Name        : filter.h
 Author      : Israel Pavelek, Cesar Fuoco
 Version     : 1.0
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#ifndef LOWPASS_H_
#define LOWPASS_H_

#include <stdint.h>

#define FIR_TAP_NUM 37
#define IIR_TAP_NUM 6

#define SAMPLES_PER_BLOCK 1024

extern int32_t fir_taps[];
extern int32_t iir_taps[];
extern float float_fir_taps[];
extern float float_iir_taps[];


typedef enum{
	NO_PROCESAR,
	PROCESAR_A,
	PROCESAR_B,

}procesar_type_t;


#endif /* LOWPASS_H_ */
