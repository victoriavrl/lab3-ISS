from furhat_remote_api import FurhatRemoteAPI

furhat_ip = "localhost"  

# Initialize the Furhat API
furhat = FurhatRemoteAPI(furhat_ip)

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# Say "Hi there!"
furhat.say(text="Hi there!")
