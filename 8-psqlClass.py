import psycopg2


def convertToListOfDict(rows, cols):
	req = []
	for row in rows:
		req_object = {}
		for i in range(len(row)):
			req_object[cols[i]] = row[i]
		req.append(req_object)
	return req


class psql():
	def __init__(self):
		self.uri = "dbname='' user='' host='' password=''"
		self.con_psql = psycopg2.connect(self.uri)
		self.con_psql.autocommit = True
		self.cur = self.con_psql.cursor()
	def update_query(self, query, parameter=None):
		try:
			self.cur.execute("BEGIN;")
			if parameter != None:
				self.cur.execute(query, parameter)
			else:
				self.cur.execute(query)
			self.cur.execute("COMMIT;")
			return True
		except Exception as e:
			self.cur.execute("ROLLBACK;")
			raise e

	def execute_query_with_fetch(self, query, parameter=None):
		try:
			if parameter != None:
				self.cur.execute(query, parameter)
			else:
				self.cur.execute(query)
			col = [desc[0] for desc in self.cur.description]
			data = self.cur.fetchall()
			return convertToListOfDict(data, col)
		except Exception as e:
			raise e

psqlObject = psql()