import argparse
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent',type=int)
foo_parser = argparser.ArgumentParser(parents=[parent_parser])
foot_parser.add_argument('foo')
foo_parser.parser_args('--parent','2','XXX')
bar_parser = argparse.Argument(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parser_args(['--bar','YYY'])

