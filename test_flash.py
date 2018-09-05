import caen_plu_py as plu
import ctypes as c_types

[ret,handle]=plu.CAEN_PLU_OpenDevice(0,'4',0,0)
#[ret,handle]=plu.CAEN_PLU_OpenDevice(1,'192.168.7.11',0,0)

if ret:
  raise Exception
  

#test flash
ret = 0
print("Testing flash....")
plu.CAEN_PLU_EnableFlashAccess(handle, plu.FPGA_MAIN)
[ret, data]=plu.CAEN_PLU_ReadFlashData(handle, plu.FPGA_MAIN, 0, 1)
print(hex(data))
plu.CAEN_PLU_DisableFlashAccess(handle, plu.FPGA_MAIN)

plu.CAEN_PLU_CloseDevice(handle)
