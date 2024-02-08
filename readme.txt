# WAF Build system test for MSVC (VS2022)

#Prepare
1) Install python for Windows (not the Microsoft App store version, use the python.org installer)
2) Download WAF from https://waf.io/
3) Rename the downloads WAF file (for example waf-2.0.26 to waf.py)
4) Put the "waf.py" file into the root of your prohect folder

Now, if you installed python and WAF as described above run with 

#Demo project
the structure looks like this:
E:\TEMP\TESTS\WAF_TESTS
├───include
└───src

#Compile and link - for all platforms and compilers (MSVC, CLANG, GCC)
waf.py configure
waf.py build

Run the test program by typing build/hello_word

That's it, have fun.


#If you want to remote compile on Windows with MSVC, it's possible.
Prequesites:
1) Install Cygwin and SSH
2) Connect to your Windows box where MSVC is installed and in Cygwin SSH Terminal type in cmd and hit enter
3) Run this command: E:\VS2022\Base\VC\Auxiliary\Build\vcvars64.bat
4) Now got to your waf_tests folder and type: run C:\Users\Dravion\AppData\Local\Programs\Python\Python312\python.exe waf.py configure 
and 
5) Now got to your waf_tests folder and type: run C:\Users\Dravion\AppData\Local\Programs\Python\Python312\python.exe waf.py build
   thats it, you c test program compiled with msvc is now available in folder build\hello_world.exe 
