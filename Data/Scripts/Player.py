import bge

#frequently Used Variables
cont = bge.logic.getCurrentScene()
objPlayer = cont.objects["player"]
groundSensor = cont.objects["groundSensor"]

def main():
    
    movement()
    

def movement():
    
    #frequently Used Variables Inside movement()
    keyboard = bge.logic.keyboard
    forwardSpeed = 0.08     #0.08
    backwardSpeed = 0.06    #0.06
    leftSpeed = 0.04        #0.04
    rightSpeed = 0.04       #0.04
    jumpHeight = 1          #1 meter
    
    #sensors
    onGround = groundSensor.sensors["onGround"]
    
    #actuators
    
    #property
    
    #keyboard Key Actions
    wKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]
    wKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.WKEY]
    aKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]
    aKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.AKEY]
    sKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]
    sKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.SKEY]
    dKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]
    dKeyJustUp = bge.logic.KX_INPUT_JUST_RELEASED == keyboard.events[bge.events.DKEY]
    shiftKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTSHIFTKEY]
    spaceKeyDown = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]
    spaceKeyJustDown = bge.logic.KX_INPUT_JUST_ACTIVATED == keyboard.events[bge.events.SPACEKEY]
    
    #jumping
    if spaceKeyJustDown and onGround.positive:
        objPlayer.applyForce((0,0,jumpHeight*250*objPlayer.mass),True)
            
    #movement
    
    #forward
    if wKeyDown and shiftKeyDown:
        objPlayer.applyMovement((0,forwardSpeed*2,0),True)
    elif wKeyDown:
        objPlayer.applyMovement((0,forwardSpeed,0),True)
    
    #backwards
    if sKeyDown and shiftKeyDown:
        objPlayer.applyMovement((0,-backwardSpeed*2,0),True)
    elif sKeyDown:
        objPlayer.applyMovement((0,-backwardSpeed,0),True)
    
    #left
    if aKeyDown and shiftKeyDown:
        objPlayer.applyRotation((0,0,leftSpeed*2),True)
    elif aKeyDown:
        objPlayer.applyRotation((0,0,leftSpeed),True)
    
    #right
    if dKeyDown and shiftKeyDown:
        objPlayer.applyRotation((0,0,-rightSpeed*2),True)
    elif dKeyDown:
        objPlayer.applyRotation((0,0,-rightSpeed),True)
    
    
    
