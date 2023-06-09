$(function() {
    function CmdExecViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];

        self.executeCommand = function() {
            $.ajax({
                url: API_BASEURL + "plugin/cmdexec",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
                    command: "execute"
                }),
                contentType: "application/json; charset=UTF-8"
            })
        };
    }

    ADDITIONAL_VIEWMODELS.push([
        CmdExecViewModel,
        ["settingsViewModel"],
        ["#navbar_plugin_cmdexec"]
    ]);
});
