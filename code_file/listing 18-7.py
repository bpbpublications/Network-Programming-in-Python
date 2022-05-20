import rpyc

def main():
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    fileobj = open('testfile.txt')
    linecount = proxy.root.line_counter(fileobj, noisy)
    print('The number of lines in the file was', linecount)

def noisy(string):
    print('Noisy:', repr(string))

if __name__ == '__main__':
    main()