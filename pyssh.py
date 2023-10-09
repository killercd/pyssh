import fire
import paramiko



def r_output(stdout, stderr, line_read=False):
    if not line_read:
        output = stdout.read().decode('utf-8')
        if output:
            return output, True
        else:
            return stderr.read().decode('utf-8'), False
    else:
        while True:
            line = stdout.readline().decode('utf-8')
            if not line:
                break
            print(line)

def run(host,
        user,
        passsword,
        command,
        line_output=False
        ):
    """
    run specific command on a remote computer
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, username=user, password=passsword)
    stdin, stdout, stderr = ssh_client.exec_command(command)

    if not line_output:
        output, status = r_output(stdout, stderr)
        print(output)
    else:
        r_output(stdout, stderr, line_output)

    ssh_client.close()

def upload(host,
            user,
            passsword,
            local_file,
            remote_file):

    """
    upload a file to a specific folder
    """
    ssh_client = paramiko.Transport((host, 22))
    ssh_client.connect(username=user, password=passsword)
    local_file=local_file.replace("//","/")
    remote_file=remote_file.replace("//","/")
    sftp = paramiko.SFTPClient.from_transport(ssh_client)
    sftp.put(local_file, remote_file)
    sftp.close()
    ssh_client.close()

def download(host,
            user,
            passsword,
            remote_file,
            local_file):
    """
    download a file to a specific folder
    """
    ssh_client = paramiko.Transport((host, 22))
    ssh_client.connect(username=user, password=passsword)
    sftp = paramiko.SFTPClient.from_transport(ssh_client)
    sftp.get(remote_file, local_file)
    sftp.close()
    ssh_client.close()

if __name__ == '__main__':
      fire.Fire({
        'run': run,
        'upload': upload,
        'download': download
  })
