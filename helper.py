import os
import subprocess

class Helper:

    @staticmethod
    def clear():
        if os.name in ('nt', 'dos'):
            subprocess.call("cls")
        elif os.name in ('linux', 'osx', 'posix'):
            subprocess.call("clear")

    @staticmethod
    def new_line(n=1):
        print("\n"*n)

    @staticmethod
    def division(n=1):
        print("="*n)