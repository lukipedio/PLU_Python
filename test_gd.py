import caen_plu_py as plu
import ctypes as c_types
import time

[ret,handle]=plu.CAEN_PLU_OpenDevice(0,'4',0,0)
#[ret,handle]=plu.CAEN_PLU_OpenDevice(1,'192.168.7.11',0,0)

if ret:
  raise Exception
  
#test delays
plu.CAEN_PLU_InitGateAndDelayGenerators(handle)
  
plu.CAEN_PLU_WriteReg(handle, 0x1008, 1)
plu.CAEN_PLU_WriteReg(handle, 0x100C, 1)
print('Enable Monitor  Mode     = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x100C)[1]))
print('Enable Internal Trigger  = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x1008)[1]))

plu.CAEN_PLU_SetGateAndDelayGenerators(handle, 4,1,0)

time.sleep(1)

[ret, gate, delay, scale] = plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)
print(gate)
print(delay)
print(scale)

plu.CAEN_PLU_CloseDevice(handle)
