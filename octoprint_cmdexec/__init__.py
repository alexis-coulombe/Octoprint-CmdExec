# coding=utf-8

import octoprint.plugin
from flask import make_response
from . import cli
import subprocess

from octoprint.access.permissions import Permissions

class CmdExecPlugin(octoprint.plugin.StartupPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.SimpleApiPlugin):

    def __init__(self):
        self._icons = self.get_icons()
        self._displayModes = self.get_display_modes()

    def get_settings_defaults(self):
        return dict(
            displayMode="list",
            command="",
            icon="f120",
            tooltip="Execute the first command",
            command1="",
            icon1="f120",
            tooltip1="Execute the second command",
            command2="",
            icon2="f120",
            tooltip2="Execute the third command",
            command3="",
            icon3="f120",
            tooltip3="Execute the fourth command",
        )

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False),
        ]

    def get_api_commands(self):
        return dict(
            execute=[]
        )

    def get_icons(self):
        return [
            'f019', 'f093', 'f095',
            'f0e0', 'e2ca', 'f030',
            'f03d', 'f0f3', 'f0e7',
            'f021', 'f02f', 'f121',
            'f1eb', 'f011', 'f0eb',
            'f120', 'f52b', 'f52a',
            'f188', 'f624', 'f04b'
        ]

    def get_display_modes(self):
        return [
            'list',
            'dropdown'
        ]

    def get_template_vars(self):
        return {
            'icons': self._icons,
            'displayModes': self._displayModes,

            'displayMode': self._settings.get(['displayMode']),
            'command': self._settings.get(['command']),
            'icon': self._settings.get(['icon']),
            'tooltip': self._settings.get(['tooltip']),
            'command1': self._settings.get(['command1']),
            'icon1': self._settings.get(['icon1']),
            'tooltip1': self._settings.get(['tooltip1']),
            'command2': self._settings.get(['command2']),
            'icon2': self._settings.get(['icon2']),
            'tooltip2': self._settings.get(['tooltip2']),
            'command3': self._settings.get(['command3']),
            'icon3': self._settings.get(['icon3']),
            'tooltip3': self._settings.get(['tooltip3']),
        }

    def execute(self, index):
        if index == '0':
            subprocess.Popen(self._settings.get(["command"]), shell=True)
        elif index == '1':
            subprocess.Popen(self._settings.get(["command1"]), shell=True)
        elif index == '2':
            subprocess.Popen(self._settings.get(["command2"]), shell=True)
        elif index == '3':
            subprocess.Popen(self._settings.get(["command3"]), shell=True)

    def on_api_command(self, command, data):
        if not Permissions.ADMIN.can():
            return make_response("Insufficient rights", 403)

        if command == "execute":
            self.execute(data['index'])
        pass

    def get_assets(self):
        return {
            "js": ["js/cmdexec.js"],
            "css": ["css/cmdexec.css"]
        }

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

    def on_after_startup(self):
        command = self._settings.get(["command"])

    def get_update_information(self):
        return dict(
            cmdexec=dict(
                displayName="CMD Exec",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="Chargnn",
                repo="Octoprint-CmdExec",
                current=self._plugin_version,

                # update method: pip w/ dependency links
                pip="https://github.com/Chargnn/Octoprint-CmdExec/archive/refs/tags/{target_version}.zip"
            )
        )

__plugin_name__ = "CMD Exec"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = CmdExecPlugin()
__plugin__hook__ = {
        "octoprint.cli.commands": cli.commands
}
