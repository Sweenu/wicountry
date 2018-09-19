import json
from pprint import pprint

import click


with open('data.json', 'r') as f:
    data = json.load(f)

@click.command()
@click.argument('country')
@click.option('--themes', '-t',
              help='A comma separated list of themes you want to see')
def main(country, themes):
    info = data.get(country)
    pprint(info)


if __name__ == '__main__':
    main()
