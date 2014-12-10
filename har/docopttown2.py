#!/usr/bin/python

"""
Usage:
       docopttown2.py [options]... PATH

options:
       -#, --progress-bar
       -0, --http1.0
       -1, --tlsv1
       -2, --sslv2
       -3, --sslv3
       -4, --ipv4
       -6, --ipv6
       -a, --append
       -A, --user-agent <agent string>
       --anyauth
       -b, --cookie <name=data>
       -B, --use-ascii
       --basic
       -c, --cookie-jar <file name>
       -C, --continue-at <offset>
       --ciphers <list of ciphers>
       --compressed
       --connect-timeout <seconds>
       --create-dirs
       --crlf (FTP) Convert LF to CRLF in upload. Useful for MVS (OS/390).
       --crlfile <file>
       -d, --data <data>
       -D, --dump-header <file>
       --data-binary <data>
       --data-urlencode <data>
       --delegation LEVEL
       --digest
       --disable-eprt
       --disable-epsv
       -e, --referer <URL>
       -E, --cert <certificate[:password]>
       --engine <name>
       --environment
       --egd-file <file>
       --cert-type <type>
       --cacert <CA certificate>
       --capath <CA certificate directory>
       -f, --fail
       -F, --form <name=content>
       --ftp-account [data]
       --ftp-alternative-to-user <command>
       --ftp-create-dirs
       --ftp-method [method]
       --ftp-pasv
       --ftp-skip-pasv-ip
       --ftp-pret
       --ftp-ssl-ccc
       --ftp-ssl-ccc-mode [active/passive]
       --ftp-ssl-control
       --form-string <name=string>
       -g, --globoff
       -G, --get
       -H, --header <header>
       --hostpubmd5 <md5>
       --ignore-content-length
       -i, --include
       -I, --head
       --interface <name>
       -j, --junk-session-cookies
       -J, --remote-header-name
       -k, --insecure
       -K, --config <config file>
       --keepalive-time <seconds>
       --key <key>
       --key-type <type>
       --krb <level>
       -l, --list-only
       -L, --location
       --libcurl <file>
       --limit-rate <speed>
       --local-port <num>[-num]
       --location-trusted
       -m, --max-time <seconds>
       --mail-from <address>
       --max-filesize <bytes>
       --mail-rcpt <address>
       --max-redirs <num>
       -n, --netrc
       -N, --no-buffer
       --netrc-file
       --netrc-optional
       --negotiate
       --no-keepalive
       --no-sessionid
       --noproxy <no-proxy-list>
       --ntlm (HTTP) Enables  NTLM  authentication.  The  NTLM  authentication
       -o, --output <file>
       -O, --remote-name
       -p, --proxytunnel
       -P, --ftp-port <address>
       --pass <phrase>
       --post301
       --post302
       --proto <protocols>
       --proto-redir <protocols>
       --proxy-anyauth
       --proxy-basic
       --proxy-digest
       --proxy-negotiate
       --proxy-ntlm
       --proxy1.0 <proxyhost[:port]>
       --pubkey <key>
       -q     If  used  as the first parameter on the command line, the _c_u_r_l_r_c
       -Q, --quote <command>
       -r, --range <range>
       -R, --remote-time
       --random-file <file>
       --raw  When used, it disables all internal HTTP decoding of content  or
       --remote-name-all
       --resolve <host:port:address>
       --retry <num>
       --retry-delay <seconds>
       --retry-max-time <seconds>
       -s, --silent
       -S, --show-error
       --ssl  (FTP, POP3, IMAP, SMTP) Try to use SSL/TLS for  the  connection.
       --ssl-reqd
       --socks4 <host[:port]>
       --socks4a <host[:port]>
       --socks5-hostname <host[:port]>
       --socks5 <host[:port]>
       --socks5-gssapi-service <servicename>
       --socks5-gssapi-nec
       --stderr <file>
       -t, --telnet-option <OPT=val>
       -T, --upload-file <file>
       --tcp-nodelay
       --tftp-blksize <value>
       --tlsauthtype <authtype>
       --tlsuser <user>
       --tlspassword <password>
       --tr-encoding
       --trace <file>
       --trace-ascii <file>
       --trace-time
       -u, --user <user:password>
       -U, --proxy-user <user:password>
       --url <URL>
       -v, --verbose
       -w, --write-out <format>
       -x, --proxy <[protocol://][user@password]proxyhost[:port]>
       -X, --request <command>
       --xattr
       -y, --speed-time <time>
       -Y, --speed-limit <speed>
       -z, --time-cond <date expression>
       -h, --help
       -M, --manual
       -V, --version
"""

from docopt import docopt



if __name__ == '__main__':
    arguments = docopt(__doc__)

#    print(arguments)

    for arg,val in arguments.items():
        if not val:
            continue

        print arg, val
        if isinstance(val, (int, float, basestring, str)):
            print '{0}="{1}"'.format(arg, val)
            continue

        elif isinstance(val,list):
            print arg, 'LIST'
            for v in val:
                print '{0}="{1}"'.format(arg, v)
        


#    for a in arguments:
#        if arguments[a]:
#            print a, arguments[a]
#    for header in arguments['--header']:
#        print header

#    for k, v in arguments.items():
#        if v:
#            print k,v



