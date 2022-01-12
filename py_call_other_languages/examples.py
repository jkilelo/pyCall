import json
from src import Java


# Calling JAVA class from Python
# Step 1: Instantiate all required variables

java_exe_path = (
    '"C:/Program Files/Java/jdk-17.0.1/bin/java.exe"'  # Path to the java executable
)
# Path to the directory that contains the package/class
java_class_directory_bin_path = f'"C:/Users/xxx\OneDrive\Desktop\java_dev\scratch_pad/bin"' # make sure to change this to the path to the directory that contains the package/class
java_package_name = "java2python"  # Package name
java_class_name = "HelloWorld"  # Class name that you want to call
java_class_args = (
    "arg1 arg2 arg3 ..."  # Arguments to be passed to the java class, separated by space
)


# I love json since it makes the code more readable and well structured.
# If your params are not in json format, no worries - just proceed to step 2.
params_to_json = json.dumps(
    {
        "java_exe_path": java_exe_path,
        "java_class_directory_bin_path": java_class_directory_bin_path,
        "java_package_name": java_package_name,
        "java_class_name": java_class_name,
        "java_class_args": java_class_args,
    }
)
# load the json into a python dictionary
params_to_python = json.loads(params_to_json)

# Step 2: Call the function
# If your params are in json format, you can call the class like this:
# Uncomment the following line to call the class
# result = Java.CallJavaClass(**params_to_python).execute()
# print(result)

# If your params are not in json format, you can call the class:
result = Java.CallJavaClass(
    java_exe_path,
    java_class_directory_bin_path,
    java_package_name,
    java_class_name,
    java_class_args,
).execute()

# Uncomment the following line to print the result
print(result)
