c = get_config()
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.ip='*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:65e40360731f:316cbcc1284c826f9aa908bac71ca10ec65c5962'  # 第2步生成的sha1值
c.NotebookApp.port = 8888 # 端口号，设置一个没被占用的
