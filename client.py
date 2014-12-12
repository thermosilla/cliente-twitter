#!/usr/bin/env python

import lib.twitterapi as tw
import models.twitter as dbtw
import argh


def read_tweets():
    pass

def save():
    pass

def create_tables():
    print(dbtw.main())


# Crea comandos
parser = argh.ArghParser()
parser.add_commands([read_tweets, save, create_tables])


if __name__ == '__main__':
    parser.dispatch()

