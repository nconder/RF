from rflib import *

print "Start RF Jamming"
d = RfCat()
d.setMdmModulation(MOD_ASK_OOK)
d.setFreq(315005000)
d.setMdmSyncMode(0)
d.setMdmDRate(4800)
d.setMdmChanSpc(24000)
d.setModeIDLE()
d.setPower(100)
d.makePktFLEN(0)


print "Starting"
d.setModeTX() #start Transmission
raw_input("Unplug to stop jamming")
print 'done'
d.setModeIDLE() # this puts the YardStick in IDEL mode to stop jamming
