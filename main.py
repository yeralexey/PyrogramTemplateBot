from utils.loader import config

import uvloop

import asyncio
from asyncio import exceptions
import datetime

from utils import gw, cr, db, vd, logger, plate, kb
from entities import User, Interview
from pyrogram import Client, filters
from pyrogram.enums import ChatAction

if __name__ == '__main__':
    logger.info("app started")
    plugins = dict(root="plugins")
    uvloop.install()
    Client(config.name,
           workdir=config.workdir,
           session_string=config.session,
           plugins=plugins
           ).run()
