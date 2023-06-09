# coding=utf-8

import octoprint.plugin
import flask
from . import cli
import subprocess

__plugin_pythoncompat__ = ">=3.7,<4"

class CmdExecPlugin(octoprint.plugin.StartupPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.SimpleApiPlugin):
    def get_settings_defaults(self):
        return dict(
            command=""
        )

    def get_template_configs(self):
        return [
            #dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_api_commands(self):
        return dict(
            execute=[]
        )

    def execute(self):
        subprocess.run([self._settings.get(["command"])], shell=True)

    def on_api_command(self, command, data):
        if command == "execute":
            self.execute()

    def get_assets(self):
        return {
            "js": ["js/cmdexec.js"]
        }

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

    def on_after_startup(self):
        command = self._settings.get(["command"])

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = CmdExecPlugin()

    global __plugin_hooks__
    __plugin__hook__ = {
        "octoprint.cli.commands": cli.commands
    }

