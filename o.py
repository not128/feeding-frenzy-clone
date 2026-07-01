import pybullet as p
import pybullet_data
import time
import keyboard as k
import math
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print("current_dir=" + currentdir)
parentdir = os.path.join(currentdir, "../gym")
# Connect to PyBullet GUI
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# Load ground plane and racecar
p.loadSDF(os.path.join(pybullet_data.getDataPath(), "stadium.sdf"))
plane = p.loadURDF('plane.urdf', globalScaling = 0.1)
slope_angle = math.radians(15)  # 15° slope
orientation = p.getQuaternionFromEuler([0, slope_angle, 0])

p.resetBasePositionAndOrientation(
    plane,
    [0, 0, 0],          # position
    orientation         # rotated orientation
)
cube = p.loadURDF("cube.urdf")
car = p.loadURDF("racecar/racecar.urdf", [0, 0, 0.2])
# l = p.loadURDF('husky/husky.urdf', [0,2,1])
new_position = [2, 0, 1]                # x, y, z
new_orientation = p.getQuaternionFromEuler([0, 0, 0])  # no rotation
p.resetBasePositionAndOrientation(cube, new_position, new_orientation)
# Enable gravity
p.setGravity(0, 0, -9.81)
p.changeDynamics(bodyUniqueId = cube,linkIndex = -1,mass = 3)

# Identify wheel joints (from racecar.urdf)
# 2,3,5,7 =  rl, rr, fl, fr
active_wheels = [2,3,5,7]
inactive_wheels = None
steering = [4, 6]
fspeed = p.addUserDebugParameter('forward speed', 1, 105, 50)
rspeed = p.addUserDebugParameter('reverse speed', -105, -1, -30)
torque = p.addUserDebugParameter('torque', 1, 99999, 100)
# try:
#     for w in active_wheels+inactive_wheels:
#         p.changeDynamics(car, w, lateralFriction = 1.5)
# except:
#     pass
def getJointandInfo(f):
    for i in range(p.getNumJoints(f)):
        info = p.getJointInfo(f, i)
        print(i, info[1].decode("utf-8"))
# getJointandInfo(l)
# Simulation loop
while 1:
    speed1 = p.readUserDebugParameter(fspeed)
    speed2 = p.readUserDebugParameter(rspeed)
    torque1 = p.readUserDebugParameter(torque)
    #husky
    # if k.is_pressed('up'):
    #     for w in [2,3,4,5]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = speed1, force = torque1)
    # elif k.is_pressed('down'):
    #     for w in [2,3,4,5]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = speed2, force = torque1)
    # else:
    #     for w in [2,3,4,5]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 0, force = 0)      
    # if k.is_pressed('left'):
    #     for w in [2,4]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 5, force = torque1)
    #     for w in [3,5]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 0, force = 0)
    # if k.is_pressed('right'):
    #     for w in [2,4]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 0, force = 0)   
    #     for w in [3,5]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 5, force = torque1)
    # pos, orn = p.getBasePositionAndOrientation(l)
    # roll, pitch, yaw = p.getEulerFromQuaternion(orn)

    # # Convert yaw (heading) to degrees
    # heading_deg = math.degrees(yaw)

    # # Camera parameters
    # distance = 2
    # pitch_cam = -20          # fixed downward tilt
    # yaw_cam = heading_deg-90    # follow car’s heading
    # target = pos

    # p.resetDebugVisualizerCamera(distance, yaw_cam, pitch_cam, target)        
    
    
    #r2d2
    
    # if k.is_pressed('down'):
    #     for w in [2,3,6,7]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = rspeed, force = 100)
    # elif k.is_pressed('up'):
    #     for w in [2,3,6,7]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = fspeed, force = 100)
    # elif k.is_pressed('left'):
    #     for w in [2,3]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = -25, force = 100)
    #     for w in [6,7]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 0, force = 100)
    # elif k.is_pressed('right'):
    #     for w in [2,3]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 0, force = 100)
    #     for w in [6,7]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = -25, force = 100) 
    # else:
    #     for w in [2,3,6,7]:
    #         p.setJointMotorControl2(l, w, p.VELOCITY_CONTROL, targetVelocity = 0, force = 0)
    # pos, orn = p.getBasePositionAndOrientation(l)
    # roll, pitch, yaw = p.getEulerFromQuaternion(orn)

    # # Convert yaw (heading) to degrees
    # heading_deg = math.degrees(yaw)

    # # Camera parameters
    # distance = 2
    # pitch_cam = -20          # fixed downward tilt
    # yaw_cam = heading_deg    # follow car’s heading
    # target = pos

    # p.resetDebugVisualizerCamera(distance, yaw_cam, pitch_cam, target)

    #car
    
    pos, orn = p.getBasePositionAndOrientation(car)
    roll, pitch, yaw = p.getEulerFromQuaternion(orn)

    # Convert yaw (heading) to degrees
    heading_deg = math.degrees(yaw)

    # Camera parameters
    distance = 2
    pitch_cam = -20          # fixed downward tilt
    yaw_cam = heading_deg-90    # follow car’s heading
    target = pos

    p.resetDebugVisualizerCamera(distance, yaw_cam, pitch_cam, target)
    
    if k.is_pressed('i'):
        new_orn = p.getQuaternionFromEuler([0,0,0])
        p.resetBasePositionAndOrientation(car, [0, 0, 0.2], new_orn)
    # Apply motor torque to wheels (drive forward)
    if k.is_pressed('up'):
        for wheel in active_wheels:
            p.setJointMotorControl2(
                bodyUniqueId=car,
                jointIndex=wheel,
                controlMode=p.VELOCITY_CONTROL,
                targetVelocity=speed1,     # wheel speed
                force=torque1     # max torque
            )
    elif k.is_pressed('down'):
        for wheel in active_wheels:
            p.setJointMotorControl2(
                bodyUniqueId=car,
                jointIndex=wheel,
                controlMode=p.VELOCITY_CONTROL,
                targetVelocity=speed2,     # wheel speed
                force=torque1    # max torque
            )
    else:
        for wheel in active_wheels:
            p.setJointMotorControl2(
                bodyUniqueId=car,
                jointIndex=wheel,
                controlMode=p.VELOCITY_CONTROL,
                targetVelocity=0,     # wheel speed
                force=0              # max torque
            )
    try:
        for wheel in inactive_wheels:
            p.setJointMotorControl2(bodyUniqueId = car, jointIndex = wheel, controlMode = p.VELOCITY_CONTROL, targetVelocity = 0, force = 0)
    except:
        pass

   
    
    # Steer the front wheels
    if k.is_pressed('right'):
        for steer in steering:
            p.setJointMotorControl2(
                bodyUniqueId=car,
                jointIndex=steer,
                controlMode=p.POSITION_CONTROL,
                targetPosition=-0.7    
            )
    elif k.is_pressed('left'):
        for steer in steering:
            p.setJointMotorControl2(
                bodyUniqueId=car,
                jointIndex=steer,
                controlMode=p.POSITION_CONTROL,
                targetPosition=0.7     
            )
    else:
        for steer in steering:
            p.setJointMotorControl2(
                bodyUniqueId=car,
                jointIndex=steer,
                controlMode=p.POSITION_CONTROL,
                targetPosition=0     
            )
        
    p.stepSimulation()
    time.sleep(1./240.)
