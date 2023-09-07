import subprocess

# Define the paths to your Python scripts
script1_path = 'run_localGPT_API-TUNNEL.py'
script2_path = 'localGPTUI/localGPTUI-TUNNEL.py'

# Run script1.py in a separate process
process1 = subprocess.Popen(['python', script1_path])

# Run script2.py in a separate process
process2 = subprocess.Popen(['python', script2_path])

process3 = subprocess.Popen('lt --port 5111 --subdomain wyskgpt',shell=True)

process4 = subprocess.Popen('lt --port 5110 --subdomain wyskgptapi',shell=True)


# Wait for both processes to finish
process1.wait()
process2.wait()
process3.wait()
process4.wait()

print("All scripts have finished running.")
