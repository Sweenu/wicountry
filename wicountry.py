from textwrap import indent, fill

import click
import yaml
from crayons import yellow, cyan, white


initial_indent = 2 * ' '
second_indent = initial_indent + 4 * ' '

with open('data.yml', 'r') as f:
    data = yaml.load(f)

@click.command()
@click.argument('country')
@click.option('--themes', '-t',
              help='A comma separated list of themes you want to see')
def main(country, themes):
    country = country.capitalize()
    info = data.get(country)
    
    # remove the unused themes from `info`
    if themes is not None:
        themes = themes.split(',')
        for theme in list(info.keys()):
            if theme not in map(str.capitalize, themes):
                info.pop(theme)

    print(yellow(f'{country}:', bold=True))
    for theme, values in info.items():
        theme = cyan(theme, always=True)
        print(indent(cyan(f'{theme}:'), initial_indent))

        if isinstance(values, dict):
            for key, value in values.items():
                print(indent(f'{white(key, bold=True)}: {value}', second_indent))
            print('')
        else:
            for line in values.split('\n'):
                print(indent(fill(line), second_indent))


if __name__ == '__main__':
    main()
