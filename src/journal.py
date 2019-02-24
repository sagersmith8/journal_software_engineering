import argparse
import os
import git
import re
from colorama import Fore, Style

journal_path = os.path.expanduser('~/.journal')
notes_path = os.path.join(journal_path, '.notes')
todo_path = os.path.join(journal_path, '.todo')
ticket_path = os.path.join(journal_path, '.ticket')
if not os.path.exists(journal_path):
    os.makedirs(journal_path)
    r = git.Repo.init(journal_path)
    readme_path = os.path.join(journal_path, 'README.md')
    open(readme_path, 'wb').close()
    r.index.add([readme_path])
    r.index.commit('initial commit')
if not os.path.exists(notes_path):
    r = git.Repo.init(notes_path)
    readme_path = os.path.join(notes_path, 'README.md')
    open(readme_path, 'wb').close()
    r.index.add([readme_path])
    r.index.commit('initial commit')
if not os.path.exists(todo_path):
    r = git.Repo.init(todo_path)
    readme_path = os.path.join(todo_path, 'README.md')
    open(readme_path, 'wb').close()
    r.index.add([readme_path])
    r.index.commit('initial commit')
if not os.path.exists(ticket_path):
    r = git.Repo.init(ticket_path)
    readme_path = os.path.join(ticket_path, 'README.md')
    open(readme_path, 'wb').close()
    r.index.add([readme_path])
    r.index.commit('initial commit')
journal = git.Repo(journal_path).git
ticket = git.Repo(ticket_path).git
notes = git.Repo(notes_path).git
todo = git.Repo(todo_path).git
journal_name_map = {
    journal: "JOURNAL",
    ticket: "TICKET",
    notes: "NOTES",
    todo: "TODO"
}


def journal_entry(entry):
    journal.commit('--allow-empty', '-m', entry)


def notes_entry(entry):
    journal_entry(entry)
    notes.commit('--allow-empty', '-m', entry)


def ticket_entry(entry):
    journal_entry(entry)
    ticket.commit('--allow-empty', '-m', entry)


def todo_entry(entry):
    journal_entry(entry)
    todo.commit('--allow-empty', '-m', entry)


def standup(repo, before, after):
    print('\t{}{}{}{}'.format(Style.BRIGHT, Fore.MAGENTA, journal_name_map[repo], Style.RESET_ALL))
    git_log_args = [
        '--pretty=format:"%s + %Cgreen[%cr]%Creset"',
        '--abbrev-commit'
    ]
    if before:
        git_log_args.append('--before="{}"'.format(before))
    if after:
        git_log_args.append('--since="{}"'.format(after))
    logs = repo.log(*git_log_args).split('\n')
    if logs == [u'']:
        print('{}{}{}'.format(
            Fore.RED, Style.BRIGHT, 'No logs found for specified time frame', Fore.RESET, Style.RESET_ALL)
        )
        return
    for log in logs:
        m = re.search("(.*) \+ (.*)", log)
        message, time = m.groups()
        print('{}*{} {}{}{} - {}{}{}'.format(
            Fore.RED, Fore.RESET,
            Fore.YELLOW, time, Fore.RESET,
            Fore.GREEN, message, Fore.RESET
        ))
    print


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='journal',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
        journal makes commits to repos in the following locations:
        \tjournal location: {}
        \tnotes location: {}
        \tticket location: {}
        \ttodo location: {}'''.format(journal_path, notes_path, ticket_path, todo_path),
        epilog='made by sage smith'
    )
    parser.add_argument('entry', nargs='?', type=str, help='entry to enter in journal')
    parser.add_argument('-t', '--ticket', action='store_true', help='specifies ticket journal')
    parser.add_argument('-d', '--do', action='store_true', help='specifies todo journal')
    parser.add_argument('-n', '--note', action='store_true', help='specifies note journal')
    parser.add_argument('-c', '--complete', action='store_true', help='makes a completed entry in journal')
    parser.add_argument('-s', '--standup', action='store_true', help='prints stand up')
    parser.add_argument('-j', '--journal', action='store_true', help='specifies entire journal')
    parser.add_argument('-b', '--before', type=str, help='specifies to grab standup logs before entered date')
    parser.add_argument('-a', '--after', type=str, help='specifies to grab standup logs after entered date')
    args = parser.parse_args()
    if args.standup:
        if args.ticket:
            standup(ticket, args.before, args.after)
        if args.do:
            standup(todo, args.before, args.after)
        if args.note:
            standup(notes, args.before, args.after)
        if not args.ticket and not args.do and not args.note or args.journal:
            standup(journal, args.before, args.after)
    else:
        if args.ticket:
            ticket_entry(args.entry)
        if args.do:
            todo_entry(args.entry)
        if args.note:
            notes_entry(args.entry)
        if not args.ticket and not args.do and not args.note or args.journal:
            journal_entry(args.entry)
