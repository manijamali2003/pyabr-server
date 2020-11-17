import shutil, sys, os, control, git

packname = 'pyabr'

## Get the latest version of Pyabr ##
cs = control.read_record('cs','etc/distro')

## Git ##
git.Git('pack/').clone(cs) # Git source code package # Helped from stockoverflow