#coding=utf-8;
import os
import time
import commands
import datetime
# 定时备份网关plugins下的规则

plugins = ['divide','cache','rate_limiting']

def copy_plugins(curr_time,plugins_path,dst_path):
	cmd = 'cp -R %s %s'%(plugins_path,dst_path)
	if os.system(cmd)==0:
		print 'copy plugins success'
	else:
		print 'copy plugins failed'
	cmd = 'tar -zcf %s %s '%('gw_' + curr_time + '.tar.gz', dst_path + '/plugins')
	if os.system(cmd)==0:
		print 'tar success'


def check_md5(curr_time,plugins,plugins_path,dst_path):
	for name in plugins:
		cmd1 = 'md5sum %s'%(plugins_path + '/' + name +'/conf.json')
		cmd2 = 'md5sum %s'%(dst_path + '/plugins/' + name +'/conf.json')
		md5_str1= os.popen(cmd1).read().split()[0]
		md5_str2= os.popen(cmd2).read().split()[0]
		if cmp(md5_str1,md5_str2) != 0:
			print curr_time,'  the config changes in plugins',name  
		else:
			print 'nothing changes'


curr_time = time.strftime('%Y%m%d%H%M%S')
plugins_path ='/usr/local/mywork/gateway/orange/plugins'
dst_path='/usr/local/mywork/test'
check_md5(curr_time,plugins,plugins_path,dst_path)
copy_plugins(curr_time,plugins_path,dst_path)
