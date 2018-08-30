import caen_plu_py

[ret,handle]=caen_plu_py.CAEN_PLU_OpenDevice(0,'4',0,0)
#[ret,handle]=caen_plu_py.CAEN_PLU_OpenDevice(1,'192.168.7.11',0,0)

if ret:
  raise Exception
  
print('Revision = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8200)[1]))
print('Year     = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B00)[1]*256+caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B04)[1]))
print('Month    = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B08)[1]))
print('Day      = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B0C)[1]))
print('Hour     = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B10)[1]))
print('Minutes  = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B14)[1]))
print('Seconds  = ' + hex(caen_plu_py.CAEN_PLU_ReadReg(handle, 0x8B18)[1]))

caen_plu_py.CAEN_PLU_CloseDevice(handle)
