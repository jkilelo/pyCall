import subprocess
import sys


'''
Author: Jeffrey Kilelo
License: MIT
'''
class CallJavaClass:
    '''
    This class calls java class from python. 
    Command line arguments are passed as string, separated by space. 
    Communication between python and java is done via stdin and stdout.
    :param: java_exe_path: path to java executable
    :param: java_class_directory_bin_path: bin path to the java directory that contains the package/class
    :param: java_package_name: java package name
    :param: java_class_name: name of java class you want to call
    :param: java_class_args: arguments to be passed to java class, separated by space
    :return: output of java class
    '''
    def __init__(self, java_exe_path: str, java_class_directory_bin_path: str,
                 java_package_name: str, java_class_name: str,
                 java_class_args: str):
        self.java_exe_path = java_exe_path
        self.java_class_directory_bin_path = java_class_directory_bin_path
        self.java_package_name = java_package_name
        self.java_class_name = java_class_name
        self.java_class_args = java_class_args

    def execute(self) -> str:
        cmd = f'{self.java_exe_path} --enable-preview -XX:+ShowCodeDetailsInExceptionMessages -cp {self.java_class_directory_bin_path} {self.java_package_name}.{self.java_class_name} {self.java_class_args}'
        p = subprocess.Popen(cmd,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            return err.decode('utf-8')
        return out.decode('utf-8')

if __name__ == '__main__':
    CallJavaClass(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]).execute()
    