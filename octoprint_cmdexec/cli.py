# coding=utf-8

def commands(cli_group, pass_octoprint_ctx, *args, **kwargs):
    from octoprint.cli.client import create_client, client_options

    def _api_command(command, apikey, host, port, httpuser, httppass, https, prefix):
        client = create_client(settings=cli_group.settings,
                               apikey=apikey,
                               host=host,
                               port=port,
                               httpuser=httpuser,
                               httppass=httpass,
                               https=https,
                               prefix=prefix)

        r = client.post_command("plugin/cmdexec", command)
        try:
            r.raise_for_status()
        except:
            click.echo("HTTP Error, got {}".format(e))
            sys.exit(1)

        return r

    @client_options
    @click.command("execute")
    def execute_command(apikey, host, port, httpuser, httppass, https, prefix):
        r = api_command("execute", apikey, host, port, httpuser, httppass, https, prefix)

        if r.status_code in [200, 204]:
            click.echo("ok")

    return [execute_command]
