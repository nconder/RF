from rflib import *

d = RfCat()
d.setFreq(315005000)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(4800)

print "Starting"
d.RFxmit("\xb8\xb8\xb8\xb8\xb8\x00\x00\x00"*10)
print "Transmission COmplete"
