/* CAEN_PLU.i */
%module "caen_plu_py"

%include typemaps.i 					// Grab the standard typemap library

%include <windows.i> 
%include <stdint.i>
%include <exception.i>      
%include <attribute.i>
%include <cstring.i>
%cstring_bounded_output(char* sn, 1024);

%{
#define _CRT_SECURE_NO_WARNINGS
#include "CAEN_PLUlib.h"
%}

%apply int *OUTPUT {int*};
%apply uint32_t *OUTPUT {uint32_t *};

%include "CAEN_PLUlib.h"