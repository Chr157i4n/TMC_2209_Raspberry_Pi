from src.TMC_2209.TMC_2209_StepperDriver import *
import time


print("---")
print("SCRIPT START")
print("---")





#-----------------------------------------------------------------------
# initiate the TMC_2209 class
# use your pins for pin_en, pin_step, pin_dir here
#-----------------------------------------------------------------------
tmc = TMC_2209(21, 16, 20)





#-----------------------------------------------------------------------
# set the loglevel of the libary (currently only printed)
# set whether the movement should be relative or absolute
# both optional
#-----------------------------------------------------------------------
tmc.setLoglevel(Loglevel.debug)
tmc.setMovementAbsRel(MovementAbsRel.absolute)





#-----------------------------------------------------------------------
# these functions change settings in the TMC register
#-----------------------------------------------------------------------
tmc.setDirection_reg(False)
tmc.setCurrent(300)
tmc.setInterpolation(True)
tmc.setSpreadCycle(False)
tmc.setMicrosteppingResolution(2)
tmc.setInternalRSense(False)


print("---\n---")





#-----------------------------------------------------------------------
# these functions read and print the current settings in the TMC register
#-----------------------------------------------------------------------
tmc.readIOIN()
tmc.readCHOPCONF()
tmc.readDRVSTATUS()
tmc.readGCONF()

print("---\n---")





#-----------------------------------------------------------------------
# set the Accerleration and maximal Speed
#-----------------------------------------------------------------------
tmc.setAcceleration(2000)
tmc.setMaxSpeed(500)





#-----------------------------------------------------------------------
# activate the motor current output
#-----------------------------------------------------------------------
tmc.setMotorEnabled(True)





#-----------------------------------------------------------------------
# set a callback function for the stallguard interrupt based detection
# 1. param: pin connected to the tmc DIAG output
# 2. param: is the threshold StallGuard
# 3. param: is the callback function (threaded)
# 4. param (optional): min speed threshold (in steptime measured  in  clock  cycles)
#-----------------------------------------------------------------------
def my_callback(channel):  
    print("StallGuard!")
    tmc.stop()

tmc.setStallguard_Callback(26, 50, my_callback) # after this function call, StallGuard is active



finishedsuccessfully = tmc.runToPositionSteps(4000, MovementAbsRel.relative)        #uses STEP/DIR to move the motor
# finishedsuccessfully = tmc.setVActual_rpm(30, revolutions=10)                     #uses VActual Register to  move the motor


if(finishedsuccessfully == True):
    print("Movement finished successfully")
else:
    print("Movement was not completed")





#-----------------------------------------------------------------------
# homing
# 1. param: DIAG pin
# 2. param: maximum number of revolutions. Can be negative for inverse direction
# 3. param(optional): StallGuard detection threshold
#-----------------------------------------------------------------------
#tmc.doHoming(26, 1, 50)





#-----------------------------------------------------------------------
# deactivate the motor current output
#-----------------------------------------------------------------------
tmc.setMotorEnabled(False)

print("---\n---")





#-----------------------------------------------------------------------
# deinitiate the TMC_2209 class
#-----------------------------------------------------------------------
del tmc

print("---")
print("SCRIPT FINISHED")
print("---")
