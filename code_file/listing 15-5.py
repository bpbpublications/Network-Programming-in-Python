import getpass, sys
from imapclient import IMAPClient

def main():
    if len(sys.argv) != 4:
        print('usage: %s hostname username foldername' % sys.argv[0])
        sys.exit(2)

    hostname, username, foldername = sys.argv[1:]
    c = IMAPClient(hostname, ssl=True)
    try:
        c.login(username, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
    else:
        select_dict = c.select_folder(foldername, readonly=True)
        for k, v in sorted(select_dict.items()):
            print('%s: %r' % (k, v))
    finally:
        c.logout()

if __name__ == '__main__':
    main()