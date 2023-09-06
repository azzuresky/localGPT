import subprocess

# Define the paths to your Python scripts
script1_path = 'run_localGPT_API-NGROK.py'
script2_path = 'localGPTUI/localGPTUI-NGROK.py'

# Run script1.py in a separate process
process1 = subprocess.Popen(['python', script1_path])

# Run script2.py in a separate process
process2 = subprocess.Popen(['python', script2_path])

# Wait for both processes to finish
process1.wait()
process2.wait()

print("Both scripts have finished running.")
