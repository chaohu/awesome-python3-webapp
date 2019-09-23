#!/usr/bin/en python3
#-*-coding:utf-8-*-

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get,post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
	users = await User.findAll()
	logging.info(str(users))
	return {
		'__template__': 'test.html',
		'users': users
	}
