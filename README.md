# teamselect

## WOT
Quick util to randomly pick n number of users from a team. 

## WHY
I needed a way to randomly pick team members for tasks. Works with multiple teams

## HOW

### Setup
Clone repo locally

`virtualenv -p python3 venv`

Setup Venv

`source venv/bin/activate`

Install/get requirements

`pip install .`

### Config
Move options.yaml.default to options.yaml, Add team members in the format Name: email

### Usage
Usage: teamselect [OPTIONS] TEAM

Options:
  -n, --number INTEGER  Number of team members to choose.
 
  -nd, --nodup          Exclude previousily selected team members.
  
  -s, --safe            Run without saving previously selected users.
  
  --help                Show this message and exit.
  
## WHO
?

## TODO
Handle some errors 
  
