import json
from textwrap import indent

import click
from crayons import yellow, cyan, white


with open('data.json', 'r') as f:
    data = json.load(f)

@click.command()
@click.argument('country')
@click.option('--themes', '-t',
              help='A comma separated list of themes you want to see')
def main(country, themes):
    info = data.get(country)

    print(yellow(f'{country}:', bold=True))
    for theme, values in info.items():
        theme = cyan(theme, always=True)
        print(indent(cyan(f'{theme}:'), '  '))
        if isinstance(values, dict):
            for key, value in values.items():
                print(indent(f'{white(key, bold=True)}: {value}', '    '))
        else:
            print(indent(values, '    '))


if __name__ == '__main__':
    main()
