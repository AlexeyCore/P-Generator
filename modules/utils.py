import subprocess as sp


def run_command(commands=['']):
    if len(commands):
        i = 0
        commands_line = ''
        for line in commands:
            if i > 0:
                commands_line += '; ' + line
            else:
                commands_line += line
            i += 1
        print (commands_line)
        output = sp.run(commands_line, stdout=sp.PIPE, shell=True)
        return output.stdout.decode('utf-8')
