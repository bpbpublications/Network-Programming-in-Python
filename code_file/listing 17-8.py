from ftplib import FTP

def main():
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/academic/astronomy/')
    entries = []
    ftp.dir(entries.append)
    ftp.quit()

    print(len(entries), "entries:")
    for entry in entries:
        print(entry)

if __name__ == '__main__':
    main()