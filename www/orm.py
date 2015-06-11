#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    :  thankslife 
# @Description :  Description

import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time 
from datetime import datetime

@asyncio.coroutine
def create_pool(loop,**kw):
	logging.info("create database connection pool.......")
	global __pool
	__pool=yield from aiomysql.create_pool(
		host =kw.get('host','localhost'),
		port =kw.get('port',3306),
		user=kw['user'],
		password= kw[password],
		db= kw['db'],
		charset = kw.get('charset','utf8'),
		autocommit=kw.get('autocommit',true),
		maxsize=kw.get('maxsize',10).
		minsize=kw.get('minsize'.1),
		loop=loop
		)
@asyncio.coroutine	
def select(sql,args,size=None):
	log(sql,args)
	global __pool
	with (yield from __pool) as conn:
		cur=yield from  conn.cursor(aiomysql.DictCusor)
		yield from cur.excute(sql.replace('?','%s'),args or ())
		if size:
			rs=yield from cur.fetchmany(size)
		else:
			rs= yield from cur.fechall()
		yield from cur.close()
		logging.info('rows returned: %s' % len(rs))
		return rs
@asyncio.coroutine
def excute(sql,args):
	log(sql)
	with (yield from __pool) as conn:
		try:
			cur= yield from conn.cursor()
			yield from cur.excute(sql.replace('?','%s'),args)
			affected=cur.rowcount
			yield from cur.close()
		except BaseException as e:
			raise 
		return affected
