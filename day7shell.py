Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
<map object at 0x00000205FAB49648>
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
[3, 20, 35, 48, 63]
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
[3, 20, 35, 48]
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
[3, 20, 35, 48, 175]
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/day7script.py", line 3, in <module>
    c = list(filter(lambda x,y:x*y,a,b))
TypeError: filter expected 2 arguments, got 3
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
[3, 20, 35, 48, 175]
>>> a = [int(x) for x in input("").split(',')]
1,4,7,8,5,25,'codegnan'
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a = [int(x) for x in input("").split(',')]
  File "<pyshell#0>", line 1, in <listcomp>
    a = [int(x) for x in input("").split(',')]
ValueError: invalid literal for int() with base 10: "'codegnan'"
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
enter the values:4,5,7,8,9
<map object at 0x00000177F46C9548>
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
enter the values:4,0,8,7,9
{0, 4, 7, 8, 9}
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
enter the values:4,1,25,2.3,56
[4.0, 1.0, 25.0, 2.3, 56.0]
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
enter the values:25,22
25 22
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
enter the values:25,28
25,28
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
6750.0
>>> 
================= RESTART: C:/Users/Name/Desktop/day7script.py =================
51750.0
>>> help('modules')

Please wait a moment while I gather a list of all available modules...


Warning (from warnings module):
  File "C:\Users\Name\AppData\Local\Programs\Python\Python37\lib\site-packages\nltk\twitter\__init__.py", line 22
    "The twython library has not been installed. "
UserWarning: The twython library has not been installed. Some functionality from the twitter package will not be available.
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
29-6-2020           colorsys            itertools           socket
30-6-2020           commctrl            itsdangerous        socketserver
DAY3MTAA            compileall          jinja2              soupsieve
Day1Mta             concurrent          joblib              speech_recognition
PIL                 config              json                sqlite3
__future__          config_key          keyword             sqlparse
__main__            configdialog        kiwisolver          squeezer
_abc                configparser        lib2to3             sre_compile
_ast                contextlib          linecache           sre_constants
_asyncio            contextvars         locale              sre_parse
_bisect             copy                logging             ssl
_blake2             copyreg             lxml                sspi
_bootlocale         crispy_forms        lzma                sspicon
_bz2                crypt               macosx              stackviewer
_codecs             csv                 macpath             stat
_codecs_cn          ctypes              mailbox             statistics
_codecs_hk          curses              mailcap             statusbar
_codecs_iso2022     cv2                 mainmenu            string
_codecs_jp          cycler              markupsafe          stringprep
_codecs_kr          dataclasses         marshal             struct
_codecs_tw          datetime            math                subprocess
_collections        dateutil            matplotlib          sunau
_collections_abc    day1                message             symbol
_compat_pickle      day10mtaa           mimetypes           symtable
_compression        day14               mmap                sys
_contextvars        day14shell          mmapfile            sysconfig
_csv                day2                mmsystem            tabnanny
_ctypes             day2imp             modulefinder        tarfile
_ctypes_test        day2mta             moviepy             telnetlib
_datetime           day2mtashell        msilib              tempfile
_decimal            day3                msvcrt              test
_dummy_thread       day3mta             multicall           textview
_elementtree        day3mtashell        multiprocessing     textwrap
_functools          day3script          myspeech            this
_hashlib            day4                netbios             threading
_heapq              day4mta             netrc               threadpoolctl
_imp                day4mtaaa           nltk                time
_io                 day4script          nntplib             timeit
_json               day4shell           nt                  timer
_locale             day5                ntpath              tkinter
_lsprof             day5intro           ntsecuritycon       today
_lzma               day5mini            nturl2path          token
_markupbase         day5mtaa            numbers             tokenize
_md5                day5mtashell        numpy               tooltip
_msi                day5script          odbc                tqdm
_multibytecodec     day5shell           opcode              trace
_multiprocessing    day5todayshell      operator            traceback
_opcode             day6                optparse            tracemalloc
_operator           day6script          os                  tree
_osx_support        day6shelll          outwin              tty
_overlapped         day7mtaa            pandas              turtle
_pickle             day7mtashell        parenmatch          turtledemo
_portaudio          day7script          parser              types
_py_abc             day7shell           pathbrowser         typing
_pydecimal          day8mtaa            pathlib             undo
_pyio               day8mtaashell       pdb                 unicodedata
_queue              day9mtaa            percolator          unittest
_random             day9mtaashell       perfmon             urllib
_sha1               dayy3script         pickle              urllib3
_sha256             dbi                 pickletools         uu
_sha3               dbm                 pip                 uuid
_sha512             dde                 pipes               venv
_signal             debugger            pkg_resources       virtual assistant
_sitebuiltins       debugger_r          pkgutil             virtualenv
_socket             debugobj            platform            warnings
_sqlite3            debugobj_r          playsound           wave
_sre                decimal             plistlib            weakref
_ssl                decorator           poplib              webbrowser
_stat               defe                posixpath           werkzeug
_string             delegator           pprint              win2kras
_strptime           difflib             profile             win32api
_struct             dis                 proglog             win32clipboard
_symtable           distlib             pstats              win32com
_testbuffer         distutils           pty                 win32con
_testcapi           django              py_compile          win32console
_testconsole        doctest             pyaudio             win32cred
_testimportmultiple dummy_threading     pyclbr              win32crypt
_testmultiphase     dynoption           pydoc               win32cryptcon
_thread             easy_install        pydoc_data          win32event
_threading_local    editor              pyexpat             win32evtlog
_tkinter            email               pygame              win32evtlogutil
_tracemalloc        empdata             pylab               win32file
_warnings           employee            pyparse             win32gui
_weakref            encodings           pyparsing           win32gui_struct
_weakrefset         ensurepip           pyshell             win32help
_win32sysloader     enum                pythoncom           win32inet
_winapi             errno               pytz                win32inetcon
_winxptheme         faulthandler        pywin               win32job
abc                 filecmp             pywin32_bootstrap   win32lz
add1                fileinput           pywin32_testutil    win32net
addition            filelist            pywintypes          win32netcon
adodbapi            filelock            query               win32pdh
afxres              first               queue               win32pdhquery
aifc                flask               quopri              win32pdhutil
antigravity         fnmatch             random              win32pipe
app1                format              rasutil             win32print
appdirs             formatter           re                  win32process
argparse            fractions           redirector          win32profile
array               ftplib              regcheck            win32ras
asgiref             functools           regex               win32rcparser
ast                 gc                  regutil             win32security
asynchat            genericpath         replace             win32service
asyncio             getopt              reprlib             win32serviceutil
asyncore            getpass             requests            win32timezone
atexit              gettext             rlcompleter         win32trace
audioop             glob                rpc                 win32traceutil
autocomplete        greet               run                 win32transaction
autocomplete_w      grep                runpy               win32ts
autoexpand          gtts                runscript           win32ui
base64              gtts_token          saa                 win32uiole
bdb                 gzip                samp                win32verstamp
binascii            hashlib             sample              win32wnet
binhex              heapq               sas                 window
bisect              help                sched               winerror
browser             help_about          scipy               winioctlcon
bs4                 history             scrolledlist        winnt
builtins            hmac                seaborn             winperf
bz2                 html                search              winreg
cProfile            http                searchbase          winsound
calendar            hyperparser         searchengine        winxpgui
calltip             idle                secrets             winxptheme
calltip_w           idle_test           select              wsgiref
certifi             idlelib             selectors           xdrlib
cgi                 idna                servicemanager      xlrd
cgitb               imageio             setuptools          xml
chardet             imageio_ffmpeg      shelve              xmlrpc
chunk               imaplib             shlex               xxsubtype
click               imghdr              shutil              zipapp
cmath               imp                 sidebar             zipfile
cmd                 importlib           signal              zipimport
code                importlib_metadata  site                zipp
codecontext         inspect             six                 zlib
codecs              io                  sklearn             zoomheight
codeop              iomenu              smtpd               zzdummy
collections         ipaddress           smtplib             
colorizer           isapi               sndhdr              

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> 
===================== RESTART: C:/Users/Name/Desktop/greeet.py ====================
Hello everyone hope you are doing well and are safe
>>> 
===================== RESTART: C:/Users/Name/Desktop/greeet.py ====================
enter the Basic Salary:
===================== RESTART: C:/Users/Name/Desktop/greeet.py ====================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/greeet.py", line 1, in <module>
    import sassss
ModuleNotFoundError: No module named 'sassss'
>>> import datetime
>>> help('modules')

Please wait a moment while I gather a list of all available modules...


Warning (from warnings module):
  File "C:\Users\Name\AppData\Local\Programs\Python\Python37\lib\site-packages\nltk\twitter\__init__.py", line 22
    "The twython library has not been installed. "
UserWarning: The twython library has not been installed. Some functionality from the twitter package will not be available.
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
29-6-2020           colorsys            isapi               smtplib
30-6-2020           commctrl            itertools           sndhdr
DAY3MTAA            compileall          itsdangerous        socket
Day1Mta             concurrent          jinja2              socketserver
PIL                 config              joblib              soupsieve
__future__          config_key          json                speech_recognition
__main__            configdialog        keyword             sqlite3
_abc                configparser        kiwisolver          sqlparse
_ast                contextlib          lib2to3             squeezer
_asyncio            contextvars         linecache           sre_compile
_bisect             copy                locale              sre_constants
_blake2             copyreg             logging             sre_parse
_bootlocale         crispy_forms        lxml                ssl
_bz2                crypt               lzma                sspi
_codecs             csv                 macosx              sspicon
_codecs_cn          ctypes              macpath             stackviewer
_codecs_hk          curses              mailbox             stat
_codecs_iso2022     cv2                 mailcap             statistics
_codecs_jp          cycler              mainmenu            statusbar
_codecs_kr          dataclasses         markupsafe          string
_codecs_tw          datetime            marshal             stringprep
_collections        dateutil            math                struct
_collections_abc    day1                matplotlib          subprocess
_compat_pickle      day10mtaa           message             sunau
_compression        day14               mimetypes           symbol
_contextvars        day14shell          mmap                symtable
_csv                day2                mmapfile            sys
_ctypes             day2imp             mmsystem            sysconfig
_ctypes_test        day2mta             modulefinder        tabnanny
_datetime           day2mtashell        moviepy             tarfile
_decimal            day3                msilib              telnetlib
_dummy_thread       day3mta             msvcrt              tempfile
_elementtree        day3mtashell        multicall           test
_functools          day3script          multiprocessing     textview
_hashlib            day4                myspeech            textwrap
_heapq              day4mta             netbios             this
_imp                day4mtaaa           netrc               threading
_io                 day4script          nltk                threadpoolctl
_json               day4shell           nntplib             time
_locale             day5                nt                  timeit
_lsprof             day5intro           ntpath              timer
_lzma               day5mini            ntsecuritycon       tkinter
_markupbase         day5mtaa            nturl2path          today
_md5                day5mtashell        numbers             token
_msi                day5script          numpy               tokenize
_multibytecodec     day5shell           odbc                tooltip
_multiprocessing    day5todayshell      opcode              tqdm
_opcode             day6                operator            trace
_operator           day6script          optparse            traceback
_osx_support        day6shelll          os                  tracemalloc
_overlapped         day7mtaa            outwin              tree
_pickle             day7mtashell        pandas              tty
_portaudio          day7script          parenmatch          turtle
_py_abc             day7shell           parser              turtledemo
_pydecimal          day8mtaa            pathbrowser         types
_pyio               day8mtaashell       pathlib             typing
_queue              day9mtaa            pdb                 undo
_random             day9mtaashell       percolator          unicodedata
_sha1               dayy3script         perfmon             unittest
_sha256             dbi                 pickle              urllib
_sha3               dbm                 pickletools         urllib3
_sha512             dde                 pip                 uu
_signal             debugger            pipes               uuid
_sitebuiltins       debugger_r          pkg_resources       venv
_socket             debugobj            pkgutil             virtual assistant
_sqlite3            debugobj_r          platform            virtualenv
_sre                decimal             playsound           warnings
_ssl                decorator           plistlib            wave
_stat               defe                poplib              weakref
_string             delegator           posixpath           webbrowser
_strptime           difflib             pprint              werkzeug
_struct             dis                 profile             win2kras
_symtable           distlib             proglog             win32api
_testbuffer         distutils           pstats              win32clipboard
_testcapi           django              pty                 win32com
_testconsole        doctest             py_compile          win32con
_testimportmultiple dummy_threading     pyaudio             win32console
_testmultiphase     dynoption           pyclbr              win32cred
_thread             easy_install        pydoc               win32crypt
_threading_local    editor              pydoc_data          win32cryptcon
_tkinter            email               pyexpat             win32event
_tracemalloc        empdata             pygame              win32evtlog
_warnings           employee            pylab               win32evtlogutil
_weakref            encodings           pyparse             win32file
_weakrefset         ensurepip           pyparsing           win32gui
_win32sysloader     enum                pyshell             win32gui_struct
_winapi             errno               pythoncom           win32help
_winxptheme         faulthandler        pytz                win32inet
abc                 filecmp             pywin               win32inetcon
add1                fileinput           pywin32_bootstrap   win32job
addition            filelist            pywin32_testutil    win32lz
adodbapi            filelock            pywintypes          win32net
afxres              first               query               win32netcon
aifc                flask               queue               win32pdh
antigravity         fnmatch             quopri              win32pdhquery
app1                format              random              win32pdhutil
appdirs             formatter           rasutil             win32pipe
argparse            fractions           re                  win32print
array               ftplib              redirector          win32process
asgiref             functools           regcheck            win32profile
ast                 gc                  regex               win32ras
asynchat            genericpath         regutil             win32rcparser
asyncio             getopt              replace             win32security
asyncore            getpass             reprlib             win32service
atexit              gettext             requests            win32serviceutil
audioop             glob                rlcompleter         win32timezone
autocomplete        greeet              rpc                 win32trace
autocomplete_w      greet               run                 win32traceutil
autoexpand          grep                runpy               win32transaction
base64              gtts                runscript           win32ts
bdb                 gtts_token          saa                 win32ui
binascii            gzip                samp                win32uiole
binhex              hashlib             sample              win32verstamp
bisect              heapq               sas                 win32wnet
browser             help                sass                window
bs4                 help_about          sched               winerror
builtins            history             scipy               winioctlcon
bz2                 hmac                scrolledlist        winnt
cProfile            html                seaborn             winperf
calendar            http                search              winreg
calltip             hyperparser         searchbase          winsound
calltip_w           idle                searchengine        winxpgui
certifi             idle_test           secrets             winxptheme
cgi                 idlelib             select              wsgiref
cgitb               idna                selectors           xdrlib
chardet             imageio             servicemanager      xlrd
chunk               imageio_ffmpeg      setuptools          xml
click               imaplib             shelve              xmlrpc
cmath               imghdr              shlex               xxsubtype
cmd                 imp                 shutil              zipapp
code                importlib           sidebar             zipfile
codecontext         importlib_metadata  signal              zipimport
codecs              inspect             site                zipp
codeop              io                  six                 zlib
collections         iomenu              sklearn             zoomheight
colorizer           ipaddress           smtpd               zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> def display():
	print("This is Saketh from Codegnan")

	
>>> def show():
	print("Today is festivald day")

	
>>> print(__name__)
__main__
>>> display()
This is Saketh from Codegnan
>>> show()
Today is festivald day
>>> 2*3
6
>>> 2**3
8
>>> 
===================== RESTART: C:/Users/Name/Desktop/greeet.py ====================
Hello everyone hope you are doing well and are safe
>>> 
===================== RESTART: C:/Users/Name/Desktop/greeet.py ====================
>>> 
====================== RESTART: C:/Users/Name/Desktop/sass.py =====================
enter the salary:25000
Gross salary is 42500.00
Net Salary is 35750.00
>>> 
====================== RESTART: C:/Users/Name/Desktop/sass.py =====================
enter the salary:25000
Gross salary is 42500.00
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/sass.py", line 12, in <module>
    net = gross - pf(basic) - itax(gross)
NameError: name 'pf' is not defined
>>> 
====================== RESTART: C:/Users/Name/Desktop/sass.py =====================
enter the salary:25000
Gross salary is 42500.00
Net Salary is 35750.00
>>> 2+3
5
>>> 2*3
6
>>> 2-3
-1
>>> 2/
SyntaxError: invalid syntax
>>> 2/3
0.6666666666666666
>>> 2**3
8
>>> 2%3
2
>>> import math
>>> import math as m
>>> m.sqrt(5)
2.23606797749979
>>> m.pi
3.141592653589793
>>> m.e
2.718281828459045
>>> m.log(2)
0.6931471805599453
>>> m.log10(2)
0.3010299956639812
>>> from math import pi
>>> pi
3.141592653589793
>>> e
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> from math import *
>>> pi
3.141592653589793
>>> e
2.718281828459045
>>> log(2)
0.6931471805599453
>>> exp(1)
2.718281828459045
>>> import math as m
>>> m.ceil(2.0)
2
>>> m.ceil(2.1)
3
>>> round(2.1)
2
>>> round(2.5)
2
>>> round(2.6)
3
>>> m.floor(2.1)
2
>>> m.floor(2.9)
2
>>> m.trunc(2.5)
2
>>> m.trunc(2.9)
2
>>> m.fabs(-5.2)
5.2
>>> m.factorial(5)
120
>>> m.fmod(7,3)
1.0
>>> m.fmod(8,2)
0.0
>>> m.hypot(4,3)
5.0
>>> m.modf(4.5)
(0.5, 4.0)
>>> m.modf(4)
(0.0, 4.0)
>>> divmod(5,3)
(1, 2)
>>> #sys module will check for system specific path parameters
>>> import sys
>>> sys.path
['C:/Users/Name/Desktop', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32\\lib', 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\Pythonwin']
>>> for i in sys.path:
	print(i)

	
C:/Users/Name/Desktop
C:\Users\Name\AppData\Local\Programs\Python\Python37\Lib\idlelib
C:\Users\Name\AppData\Local\Programs\Python\Python37\python37.zip
C:\Users\Name\AppData\Local\Programs\Python\Python37\DLLs
C:\Users\Name\AppData\Local\Programs\Python\Python37\lib
C:\Users\Name\AppData\Local\Programs\Python\Python37
C:\Users\Name\AppData\Local\Programs\Python\Python37\lib\site-packages
C:\Users\Name\AppData\Local\Programs\Python\Python37\lib\site-packages\win32
C:\Users\Name\AppData\Local\Programs\Python\Python37\lib\site-packages\win32\lib
C:\Users\Name\AppData\Local\Programs\Python\Python37\lib\site-packages\Pythonwin
>>> sys.version
'3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)]'
>>> sys.version_info
sys.version_info(major=3, minor=7, micro=8, releaselevel='final', serial=0)
>>> sys.getallocatedblocks()
75800
>>> #displayhook
>>> 25+26
51
>>> x="Saketh"
>>> def display(x):
	print("Codegnan")
	print(x)

	
>>> x
'Saketh'
>>> display(x)
Codegnan
Saketh
>>> sys.displayhook = display
>>> x
Codegnan
Saketh
>>> 25+26
Codegnan
51
>>> 25*3
Codegnan
75
>>> 25*9
Codegnan
225
>>> [1,12,3]+[4,5,6]
Codegnan
[1, 12, 3, 4, 5, 6]
>>> 
================================== RESTART: Shell =================================
>>> 25+26
51
>>> #os Operating System interfaces
>>> import os
>>> os.path
<module 'ntpath' from 'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python37\\lib\\ntpath.py'>
>>> os.listdir()
['day4shell.py', 'day6shelll.py', 'DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'mtaexam.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> os.listdir('Doc')
['python378.chm']
>>> os.listdir('NEWS.txt')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    os.listdir('NEWS.txt')
NotADirectoryError: [WinError 267] The directory name is invalid: 'NEWS.txt'
>>> os.listdir('Lib')
['abc.py', 'aifc.py', 'antigravity.py', 'argparse.py', 'ast.py', 'asynchat.py', 'asyncio', 'asyncore.py', 'base64.py', 'bdb.py', 'binhex.py', 'bisect.py', 'bz2.py', 'calendar.py', 'cgi.py', 'cgitb.py', 'chunk.py', 'cmd.py', 'code.py', 'codecs.py', 'codeop.py', 'collections', 'colorsys.py', 'compileall.py', 'concurrent', 'configparser.py', 'contextlib.py', 'contextvars.py', 'copy.py', 'copyreg.py', 'cProfile.py', 'crypt.py', 'csv.py', 'ctypes', 'curses', 'dataclasses.py', 'datetime.py', 'dbm', 'decimal.py', 'difflib.py', 'dis.py', 'distutils', 'doctest.py', 'dummy_threading.py', 'email', 'encodings', 'ensurepip', 'enum.py', 'filecmp.py', 'fileinput.py', 'fnmatch.py', 'formatter.py', 'fractions.py', 'ftplib.py', 'functools.py', 'genericpath.py', 'getopt.py', 'getpass.py', 'gettext.py', 'glob.py', 'gzip.py', 'hashlib.py', 'heapq.py', 'hmac.py', 'html', 'http', 'idlelib', 'imaplib.py', 'imghdr.py', 'imp.py', 'importlib', 'inspect.py', 'io.py', 'ipaddress.py', 'json', 'keyword.py', 'lib2to3', 'linecache.py', 'locale.py', 'logging', 'lzma.py', 'macpath.py', 'mailbox.py', 'mailcap.py', 'mimetypes.py', 'modulefinder.py', 'msilib', 'multiprocessing', 'netrc.py', 'nntplib.py', 'ntpath.py', 'nturl2path.py', 'numbers.py', 'opcode.py', 'operator.py', 'optparse.py', 'os.py', 'pathlib.py', 'pdb.py', 'pickle.py', 'pickletools.py', 'pipes.py', 'pkgutil.py', 'platform.py', 'plistlib.py', 'poplib.py', 'posixpath.py', 'pprint.py', 'profile.py', 'pstats.py', 'pty.py', 'pyclbr.py', 'pydoc.py', 'pydoc_data', 'py_compile.py', 'queue.py', 'quopri.py', 'random.py', 're.py', 'reprlib.py', 'rlcompleter.py', 'runpy.py', 'sched.py', 'secrets.py', 'selectors.py', 'shelve.py', 'shlex.py', 'shutil.py', 'signal.py', 'site-packages', 'site.py', 'smtpd.py', 'smtplib.py', 'sndhdr.py', 'socket.py', 'socketserver.py', 'sqlite3', 'sre_compile.py', 'sre_constants.py', 'sre_parse.py', 'ssl.py', 'stat.py', 'statistics.py', 'string.py', 'stringprep.py', 'struct.py', 'subprocess.py', 'sunau.py', 'symbol.py', 'symtable.py', 'sysconfig.py', 'tabnanny.py', 'tarfile.py', 'telnetlib.py', 'tempfile.py', 'test', 'textwrap.py', 'this.py', 'threading.py', 'timeit.py', 'tkinter', 'token.py', 'tokenize.py', 'trace.py', 'traceback.py', 'tracemalloc.py', 'tty.py', 'turtle.py', 'turtledemo', 'types.py', 'typing.py', 'unittest', 'urllib', 'uu.py', 'uuid.py', 'venv', 'warnings.py', 'wave.py', 'weakref.py', 'webbrowser.py', 'wsgiref', 'xdrlib.py', 'xml', 'xmlrpc', 'zipapp.py', 'zipfile.py', '_bootlocale.py', '_collections_abc.py', '_compat_pickle.py', '_compression.py', '_dummy_thread.py', '_markupbase.py', '_osx_support.py', '_pydecimal.py', '_pyio.py', '_py_abc.py', '_sitebuiltins.py', '_strptime.py', '_threading_local.py', '_weakrefset.py', '__future__.py', '__phello__.foo.py', '__pycache__']
>>> os.remove("‪C:\Users\Name\Desktop\sat.txt")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 12-13: truncated \UXXXXXXXX escape
>>> os.remove("‪C:\\Users\\Name\\Desktop\\sat.txt")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    os.remove("‪C:\\Users\\Name\\Desktop\\sat.txt")
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: '\u202aC:\\Users\\Name\\Desktop\\sat.txt'
>>> 
================================== RESTART: Shell =================================
>>> import os
>>> os.remove("sat.txt")
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    os.remove("sat.txt")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'sat.txt'
>>> os.remove("C:\\Users\\Name\\Desktop\\sat.txt")
>>> os.rename("C:\\Users\\Name\\Desktop\\chat.txt
	  
SyntaxError: EOL while scanning string literal
>>> os.rename("C:\\Users\\Name\\Desktop\\chat.txt","C:\\Users\\Name\\Desktop\\saketh.txt")
>>> 