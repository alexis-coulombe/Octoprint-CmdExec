# CmdExec

This plugin allows executing custom shell commands through the Octoprint's UI.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/alexis-coulombe/CmdExec/archive/master.zip

## Configuration

In the plugin's settings page, enter up to 4 commands you want to execute using the navbar buttons. You can also change the navbar icon if you want.

You can chain commands with the ```&&``` and write the result of a command to a file with ```>>```.
Here is an example to execute 3 commands: ```command1 && command2 && command3 >> log.txt```

You can also execute a script directly on your computer by writing the path to the script ```./path/to/script```

**The command execution is only allowed by admin users**
