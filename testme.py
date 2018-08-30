import caen_plu_py as plu
import ctypes as c_types

[ret,handle]=plu.CAEN_PLU_OpenDevice(0,'4',0,0)
#[ret,handle]=plu.CAEN_PLU_OpenDevice(1,'192.168.7.11',0,0)

if ret:
  raise Exception
  
print('Revision = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8200)[1]))
print('Year     = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8B00)[1]*256+plu.CAEN_PLU_ReadReg(handle, 0x8B04)[1]))
print('Month    = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8B08)[1]))
print('Day      = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8B0C)[1]))
print('Hour     = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8B10)[1]))
print('Minutes  = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8B14)[1]))
print('Seconds  = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x8B18)[1]))

#test GetInfo()
binfo = plu.tBOARDInfo()
plu.CAEN_PLU_GetInfo(handle, binfo)

print(hex(binfo.c_code))
print(hex(binfo.r_code))

#test CAEN_PLU_USBEnumerate
print(plu.CAEN_PLU_USBEnumerate(plu.tUSBDevice())[1])

#test delays
plu.CAEN_PLU_InitGateAndDelayGenerators(handle)
print(plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)[1])
print(plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)[2])
print(plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)[3])

plu.CAEN_PLU_SetGateAndDelayGenerators(handle, 1,2,0)

plu.CAEN_PLU_InitGateAndDelayGenerators(handle)
print(plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)[1])
print(plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)[2])
print(plu.CAEN_PLU_GetGateAndDelayGenerator(handle, 0)[3])

#test flash
plu.CAEN_PLU_EnableFlashAccess(handle, plu.FPGA_MAIN)
plu.CAEN_PLU_DisableFlashAccess(handle, plu.FPGA_MAIN)

#test CAEN_PLU_GetSerialNumber
buffersize=100
[ret, sn] = plu.CAEN_PLU_GetSerialNumber(handle, buffersize)
print('Serial Number = ' + sn + ' ' + str(buffersize))

#test CAEN_PLU_ConnectionStatus
[ret, status] = plu.CAEN_PLU_ConnectionStatus(handle)
print(status)

plu.CAEN_PLU_WriteReg(handle, 0x1008, 1)
plu.CAEN_PLU_WriteReg(handle, 0x100C, 1)
print('Enable Monitor  = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x100C)[1]))
print('Enable Trigger  = ' + hex(plu.CAEN_PLU_ReadReg(handle, 0x1008)[1]))

#plu.CAEN_PLU_SetGateAndDelayGenerator(handle, 1, 1, 1, 40,0)
plu.CAEN_PLU_SetGateAndDelayGenerators(handle, 1,40,0)

plu.CAEN_PLU_CloseDevice(handle)
