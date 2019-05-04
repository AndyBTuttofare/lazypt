import pyperclip
import yaml
from .pathmanager import path_finder


class RevShell(object):

    def __init__(self, lang, host, port):
        self._lang = lang
        self._host = host
        self._port = port
        self._msg = '\n[+] Reverse shell code copied to the clipboard!'
        self._data = RevShell.get_data(RevShell, 'yaml/revshell.yaml')

    def get_code(self):
        for d in self._data:
            for k, v in d.items():
                if self._lang == k:
                    return d[self._lang]['code']

        return "[-] --lang not found in YAML file."

    def _format_code(self):
        try:
            code = self.get_code().format(self._host, self._port)
            pyperclip.copy(code)
            return self._msg
        except:
            code = self.get_code() % (self._host, self._port)
            pyperclip.copy(code)
            return self._msg

    def get_data(self, dbfile):
        script_path = path_finder()
        with open(script_path + dbfile) as f:
            return yaml.safe_load(f)

    def get_langs(self, dbfile):
        data = RevShell.get_data(RevShell, dbfile)
        langs = []
        for d in data:
            for k, v in d.items():
                langs.append(k)
        return langs

    def __str__(self):
        return self._format_code()


class ShellFile(object):

    def __init__(self, lang, filename):
        self._lang = lang
        self._filename = filename
        self._data = RevShell.get_data(RevShell, 'yaml/shellfile.yaml')
        self._make = self._make_file()

    def _get_code(self):
        for d in self._data:
            for k, v in d.items():
                if self._lang == k:
                    return d[self._lang]['code']

        return "[-] --lang not found in YAML file."
    
    def _make_file(self):
        filename = self._filename + '.' + self._lang
        try:
            f = open(filename, 'w+')
            shell = self._get_code()
            f.write(shell)
            f.close()
            return '[+] File %s created' % filename
        except FileNotFoundError as identifier:
            return str(identifier)

    def __str__(self):
        return self._make


class OpenSSL(object):

    def __init__(self, action):
        self.action = action
        self.data = RevShell.get_data(RevShell, 'yaml/openssl.yaml')
        self._msg = '\n[+] Openssl code copied to the clipboard!'

    def get_data(self, node):
        for d in self.data:
            for k,v in d.items():
                if k == self.action:
                    pyperclip.copy(v[node])
                    return self._msg
                    # return v[node]
    
    def get_all_info(self):
        infos = []
        temp = {}
        i = 1

        for d in self.data:
            temp['ossl' + str(i)] = d['ossl' + str(i)]['info']
            infos.append(temp)
            temp = {}
            i += 1
                    
        return infos
