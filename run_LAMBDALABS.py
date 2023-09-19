import subprocess

# Define the paths to your Python scripts
script1_path = 'run_localGPT_API-LAMBDALABS.py'
script2_path = 'localGPTUI/localGPTUI-LAMBDALABS.py'

#export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32

# Run script1.py in a separate process
process1 = subprocess.Popen(['python', script1_path])

# Run script2.py in a separate process
process2 = subprocess.Popen(['python', script2_path])


# Wait for both processes to finish
process1.wait()
process2.wait()

print("All scripts have finished running.")
