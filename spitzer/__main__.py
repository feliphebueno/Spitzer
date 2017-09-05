import getopt
import sys
import os
import django

sys.path.insert(0, os.path.realpath('.'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spitzer.settings")

django.setup()

from spitzer import __version__
from spitzer.lib.main import Main


def main():
    try:
        opts, args = getopt.getopt(sys.argv[2:], "hv", ["help", "version"])

        for o, a in opts:
            if o in ("-V", "--version"):
                version()
                sys.exit()
            if o in ("-V", "--version"):
                version()
                sys.exit()
            elif o in ("-h", "--help"):
                usage()
                sys.exit()
            else:
                assert False, "unhandled option"

        command = sys.argv[1]
        if command not in ('migrate', 'migrations', 'make_migrations', 'create', 'install', 'rollback'):
            raise getopt.GetoptError("Unrecognized command {0}".format(command))
    except IndexError:
        usage()
        sys.exit(1)
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    working_dir = sys.argv[0]

    Main(command, working_dir).run()


def usage():
    print("python spitzer comand [args]")


def version():
    print(__version__)

if __name__ == "__main__":
    main()