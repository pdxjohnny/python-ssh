import sys
import threading

import ssh

USERNAME = "username"
PASSWORD = "password"
THREADS = True
PRINT_HOST = True
SUDO = "echo \"{}\" | sudo -SHE ".format(PASSWORD)
HOSTS = [
    {
        "host":"example2.com",
        "username":"server_username",
        "password":"server_password"
    },
    {
        "host":"example3.com",
        "username":"server_username",
        "password":"server_password"
    }
]

def install(**kwargs):
    command = [
        SUDO + "apt-get install -y apache2"
    ]
    ssh.run_all(command, **kwargs)

def configure(**kwargs):
    pass
    # ssh.put_all("./000-default.conf", "000-default.conf", **kwargs)
    # command = [
    #     SUDO + "cp ~/000-default.con, /etc/apache2/sites-available/000-default.conf",
    #     SUDO + "rm ~/000-default.conf",
    #     SUDO + "service apache2 restart"
    # ]
    # ssh.run_all(command, **kwargs)

def status(**kwargs):
    command = [
        SUDO + "service apache2 status"
    ]
    ssh.run_all(command, **kwargs)

def main():
    ssh.connect_all(HOSTS)
    for function_name in sys.argv:
        try:
            function = getattr(sys.modules[__name__], function_name)
            function(print_host=PRINT_HOST, threads=THREADS)
        except Exception as error:
            pass
    ssh.close_all()

if __name__ == '__main__':
    main()
