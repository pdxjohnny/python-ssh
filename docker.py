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
        "wget -qO- https://get.docker.com/ > /tmp/docker_install.sh",
        "sed -i \"s/sh_c='sudo -E sh -c\'/sh_c='sh -c\'/g\" /tmp/docker_install.sh",
        SUDO + "chmod 700 /tmp/docker_install.sh",
        SUDO + "/tmp/docker_install.sh",
        SUDO + "usermod -aG docker {}".format(USERNAME),
        SUDO + "service docker restart"
    ]
    ssh.run_all(command, **kwargs)

def status(**kwargs):
    command = [
        "service docker status",
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
