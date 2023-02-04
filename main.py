from utils.loader import config

import asyncio
from asyncio import exceptions
import datetime

from utils import gw, cr, db, vd, logger, plate
from entities import User, Interview

from pyrogram import Client, filters
from pyrogram.enums import ChatAction

import pyromod
from pyromod import listen
from pyromod.helpers import ikb

if __name__ == '__main__':
    logger.info("app started")
    plugins = dict(root="plugins")
    Client(config.name,
           workdir=config.workdir,
           session_string=config.session,
           plugins=plugins
           ).run()
