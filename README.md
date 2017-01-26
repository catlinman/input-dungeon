
# Input Dungeon #

Input Dungeon is a command line dungeon crawler game project. It requires the Python interpreter version 3.4+ and is not platform specific.

### Setup ###

Before running Input Dungeon you will have to make sure that the required dependencies have been met. As of now (1/26/2017) the only dependency is *curses* which should natively ship with Unix systems.

This however is not the case on Windows systems and requires a little bit of extra work to get running. Thanks to some good people *curses* is now also available for Windows' CPython distribution. You can find the converted binaries on [this page](http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses). To install *curses* all you will need to do is to download one of the wheel files from the given page - in this case either the *cp34win32* or *cp34amd64* version - and to install the wheel using *pip* with the following syntax:

	$ pip install [Path to your wheel file]

If at any point the page goes down your best bet is to contact me for the binaries or hope that there is a working version of curses in your Python version. Either way you will need to do some work to get it running.

Once you have fulfilled the requirements all you need to do is to execute *game.py* with Python as you normally would.

	$ python game.py [Optional arguments]

## License ##

This repository is released under the MIT license. For more information please refer to [LICENSE](https://github.com/catlinman/input-dungeon/blob/master/LICENSE)
