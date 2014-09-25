python-windows-service-experiment
=================================

Experiment codes for writing Windows Service with Python.


## required packages

Install required packages.

  * download and install `pywin32`
    - http://sourceforge.net/projects/pywin32/files/pywin32/
  * `pip install bottle`


## how to play it #1

Open a Command Prompt window as an administrator and run following commands.

    > python test_service.py install
    > net start TestService

Open web browser and access to `http://localhost:6809/hello`. A messaage `Hello!`
will be shown in your browser.

To remove TestService, run following commands.

    > net stop TestService
    > python test_service.py remove


## how to play it #2

This script can be converted to Windows EXE file with following command.

    > python setup.py py2exe

In `dist` folder, a file `test_service.exe` is created.

To install this file, open a Command Prompt window as an administrator
and run following commands.

    > cd dist
    > test_service -install
    > net start TestService

To remove TestServie, try following commands.

    > net stop TestService
    > test_service -remove


## changelog

  * first release
    * [new] TestService script and build script for py2exe.
