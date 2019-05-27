""" Small utility to select x number of elements from a configurable array of values """
import random
import click
import yaml


def loadConfig():
    with open('options.yaml', 'r') as f:
        return yaml.safe_load(f)


def saveConfig(config):
    with open("options.yaml", 'w') as stream:
        yaml.dump(config, stream)


def teamselect(team, number, nodup):
    conf = loadConfig()
    members = conf.get('Teams').get(team)
    alex = conf.get('Other').get('always-exclude')
    chosen = dict()

    while len(chosen) < number:
        newitem = random.choice(list(members.keys()))
        if newitem not in alex:
            if nodup:
                prev = conf.get('Other').get('previous-selection').keys()
                if newitem not in prev:
                    chosen[newitem] = members.get(newitem)
                    del members[newitem]

    click.echo(chosen)
    conf['Other']['previous-selection'] = chosen
    saveConfig(conf)

@click.command()
@click.argument('team')
@click.option('--number','-n', default=1, help='Number of team members to choose.')
@click.option('--nodup','-nd', is_flag=True, help='Exclude previousily selected team members.')
def cli(team, number, nodup):
    teamselect(team, number, nodup)

if __name__ == "__main__":
    teamselect('SHRL', 3, True)
