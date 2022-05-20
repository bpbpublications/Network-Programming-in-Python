from ftplib import FTP, error_perm

def walk_dir(ftp, dirpath):
    original_dir = ftp.pwd()
    try:
        ftp.cwd(dirpath)
    except error_perm:
        return  # ignore non-directores and ones we cannot enter
    print(dirpath)
    names = sorted(ftp.nlst())
    for name in names:
        walk_dir(ftp, dirpath + '/' + name)
    ftp.cwd(original_dir)  # return to cwd of our caller

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login()
    walk_dir(ftp, '/pub/linux/kernel/Historic/old-versions')
    ftp.quit()

if __name__ == '__main__':
    main()