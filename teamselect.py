""" Small utility to select x number of elements from a configurable array of values """

import click

def loadConfig():
    pass


def teamselect():
    pass

@click.command()
@click.argument('team')
@click.option('--number','-n', default=1, help='Number of team members to choose.')
@click.option('--nodup','-nd', is_flag=True, help='Exclude previousily selected team members.')

def cli(team, number, nodup):
    pass

if __name__ == "__main__":
    teamselect()
