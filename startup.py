# This is the main python file

# upon boot, this will attempt to connect to the mqtt server
# will control other scripts via environment variables
# ie. armed=1 for on. armed=0 for off
# will send status update to mqtt server 
# Will announce if triggered
# ie. triggered=1 for yes. triggered=0 for no