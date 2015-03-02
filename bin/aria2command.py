import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:6800/rpc')
s.aria2.addUri(['http://example.org/file'])

//s.aria2.addUri(['http://example.org/file', 'http://mirror/file'],dict(dir="/tmp"))
//s.aria2.addUri(['http://example.org/file'], {}, 0)