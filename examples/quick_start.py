# import api
import gira_homeserver_api as api

# create a client object
# XXX.XXX.XXX.XXX = ip of your gira homeserver
# 80 = port (probably not working with ssl)

client = api.Client("XXX.XXX.XXX.XXX", 80, "username", "password")

# function for listener
def onDeviceValue(deviceId, value):
    # print deviceId and value
    print(deviceId, value)

# add event listener for all devices
client.onDeviceValue(onDeviceValue)

# Make sure you put all commands that are supposed to get called after connect() in this listener
def onClientReady(sessionToken):
    # get value from device by id
    # Sometimes this does not work - In that case it returns -1
    deviceId = 101
    deviceValue = client.getDeviceValue(deviceId)
    print(deviceValue) # returns -1 if device is not reachable

    # control a device

    # devices with type 1 are things like lights. They can mostly only take 0 or 1 as value. However blinds are still type 1.
    # devices with type 20 are devices that can take a real number. Things like garages
    deviceType = 1

    # device id is unique
    # you can figure it out by using the device and the onDeviceValue listener
    deviceId = 101

    # Since deviceType is 1 we can only use 0 and 1 as a value.
    # In this case we toggle a light on
    value = 1

    # excutes the command by providing all 3 values
    client.setDeviceValue(deviceType, deviceId, value)

# Add listener
client.onClientReady(onClientReady)

# connect to server
client.connect()
