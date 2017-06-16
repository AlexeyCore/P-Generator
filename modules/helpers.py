import subprocess as sp
import time


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
        time.sleep(5)
        output = sp.Popen(commands_line, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
        output.wait()
        return output.stdout.decode('utf-8')


def ask_question(question='', options=[]):
    if not options:
        return input('%s: ' % question)
    answer = input('%s (%s): ' % (question, '/'.join(options)))
    if answer in options:
        return answer
    return ask_question(question, options)
