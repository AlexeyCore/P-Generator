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
        try:
            output = sp.Popen(commands_line, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            output.wait()
            return output.communicate()[0].decode('utf-8')
        except:
            return None


def ask_question(question='', options=[]):
    if not options:
        return input('\033[94m%s: \033[0m' % question)
    answer = input('\033[94m%s (%s): \033[0m' % (question, '/'.join(options)))
    if answer in options:
        return answer
    return ask_question(question, options)
