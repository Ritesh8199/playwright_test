with open("/var/log/syslog", "r") as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
