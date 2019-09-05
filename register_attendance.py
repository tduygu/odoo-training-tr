from xmlrpc import client
# Variables required
server_url = 'http://localhost:8069'
db_name = 'odoo'
username = 'admin'
password = 'admin'
# No authenticate required
common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)
# Check Odoo Version
version = common.version()
print(version)
# Check user connection to database. Return user's ID
user_id = common.authenticate(db_name, username, password, {})
print(user_id)
res = models.execute_kw(db_name, user_id, password, 'hr.employee', 'register_attendance', ['1234'])
print(res)