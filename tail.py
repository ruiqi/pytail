from time import sleep

def follow(file_path, sleep_time=10):
    f = open(file_path)

    #seek to the end
    #f.seek(0, 2)

    while True:
        lines = f.readlines()
        print lines
        if not lines:
            sleep(sleep_time)
            continue
        for line in lines:
            print 'yield'
            yield line

if __name__ == '__main__':
    for line in follow('test.txt', 1):
        print line
