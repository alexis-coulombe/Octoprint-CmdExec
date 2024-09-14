$(function() {
    function CmdExecViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];
        self.loginState = parameters[1];

        self.executeCommand = function(index) {
            $.ajax({
                url: API_BASEURL + "plugin/cmdexec",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
                    command: "execute",
                    index: index+''
                }),
                contentType: "application/json; charset=UTF-8"
            })
        };
    }

    ADDITIONAL_VIEWMODELS.push([
        CmdExecViewModel,
        ["settingsViewModel", "loginStateViewModel"],
        ["#navbar_plugin_cmdexec"]
    ]);
});
