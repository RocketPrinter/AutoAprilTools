import sys
import os
import cv2
import subprocess
import colorama
colorama.init()
aprilToolsPath = "D:\Blender\AprilTools\AprilTools.exe"

# Path hadling
if len(sys.argv)!=2:
    print("python AutoAprilTools <video path>")
    sys.exit()

videoPath = sys.argv[1]
workingDir= os.path.dirname(videoPath) + "\sequence_" + os.path.basename(videoPath)

for i in range(len(workingDir)-1,0,-1):
    if workingDir[i]==".":
        workingDir = workingDir[0:i-1]
        break
try:
    os.mkdir(workingDir)
except:
    print ("Creation of the directory %s failed!" % workingDir)
    sys.exit()

logFile = open(file= workingDir + "\AprilTools.log", mode='w')
logFile.write("[-----AprilTools Log-----]")

print ("")
print ("AprilTools path:" +  aprilToolsPath)
print ("Video Path:"+ videoPath)
print ("Output Directory:" +workingDir)
print ("")

# video splitting
video = cv2.VideoCapture(videoPath)
currentframe = 0
while 1:
    ret, frame=video.read()
    if ret:
        path = workingDir +"\\"
        if int(currentframe/1000)==0: path+="0"
        if int(currentframe/100) ==0: path+="0"
        if int(currentframe/10)  ==0: path+="0"
        path+= str(currentframe) + ".png"
        print ("Creating "+path)
        
        try:
            cv2.imwrite(path,frame)
        except:
            print ("Failed to write frame "+currentframe+" !")
            sys.exit(0)
        
        currentframe+=1
    else:
        break

# Estimate focal length
command = aprilToolsPath+" --path \""  + workingDir + "\" --estimate-focal-length"
print ("Getting focal length...")

process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout

i=output.find("Best guess:")
while (output[i]<"0" or output[i]>"9") and output[i]!="-": i+=1
j=i
while output[j]!=" ": j+=1

focalLength= float (output[i:j-1])
print ("Focal Length is " + str(focalLength) + " px.")

logFile.writelines(output)

if focalLength==-1:
    print (colorama.Fore.RED+"INVALIID FOCAL LENGTH")
    sys.exit()
    
# AprilTools solve
command = aprilToolsPath+" --path \""  + workingDir + "\" --focal-length-pixels " + str(focalLength) + " --tag-size 145"
print ("Solving camera position...")

process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout
logFile.writelines(output)
logFile.close()

print ("Done!")
# Profit! 