import code

from basescript import BaseScript

from .diskdict import DiskDict


class DiskDictCommand(BaseScript):
    DESC = 'DiskDict command-line tool'

    def interact(self):
        fpath = self.args.fpath

        interact = DiskDict(fpath=fpath, log=self.log)

        namespace = dict(dd=interact)
        code.interact("DiskDict Console", local=namespace)

    def define_subcommands(self, subcommands):
        super(DiskDictCommand, self).define_subcommands(subcommands)

        interact_cmd = subcommands.add_parser('interact',
                                              help='DiskDict Console')
        interact_cmd.set_defaults(func=self.interact)
        interact_cmd.add_argument('fpath',
                                  help='Input file which is used to store disk dictionary.\
                        eg: /tmp/disk.dict')


def main():
    DiskDictCommand().start()


if __name__ == '__main__':
    main()
