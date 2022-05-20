from ftplib import FTP

def main():
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/academic/astronomy/')
    entries = ftp.nlst()
    ftp.quit()

    print(len(entries), "entries:")
    for entry in sorted(entries):
        print(entry)

if __name__ == '__main__':
    main()