import psycopg2
import os

class ReversePickupDataCompute():
	def __init__(self, srcDB, dstDB):
		self.srcDB = {}
		self.srcDB['db'] = srcDB['db'];
		self.srcDB['username'] = srcDB['username'];
		self.srcDB['password'] = srcDB['password'];
		self.srcDB['host'] = srcDB['host'];
		self.srcDB['port'] = srcDB['port'];

		self.dstDB = {}
		self.dstDB['db'] = dstDB['db'];
		self.dstDB['username'] = dstDB['username'];
		self.dstDB['password'] = dstDB['password'];
		self.dstDB['host'] = dstDB['host'];
		self.dstDB['port'] = dstDB['port'];

		self.dstConn = psycopg2.connect(database=self.dstDB['db'], user=self.dstDB['username'], password=self.dstDB['password'], host=self.dstDB['host'], port=self.dstDB['port'])
		self.dstCursor = self.dstConn.cursor()
		psqlCmd = '''PGPASSWORD=\'{d[password]}\' psql -h {d[host]} -d {d[db]} -U {d[username]} -p {d[port]} -c "{{query}}" '''
		self.srcPsqlCmd = psqlCmd.format(d=srcDB)
		self.dstPsqlCmd = psqlCmd.format(d=dstDB)

	def executeShellCmd(self, query, psqlCmd = None):
		status = None
		if psqlCmd:
			status = os.system(psqlCmd.format(query=query))
		else:
			status = os.system(query)
		if status != 0:
			raise ValueError('Error in executing query: ', query)

	def excecuteQuery(self, query):
		self.dstCursor.execute(query)

	def commitTransaction(self):
		self.dstConn.commit()

	def computeMetrics(self, deleteTmpTableQuery, srcCopyQuery, dstTmpTableCopyQuery, dstInsertQuery):
		self.executeShellCmd(deleteTmpTableQuery, self.dstPsqlCmd)
		copySrcCmd = self.srcPsqlCmd.format(query=srcCopyQuery)
		copyDstCmd = self.dstPsqlCmd.format(query=dstTmpTableCopyQuery)
		self.executeShellCmd(copySrcCmd + '|' + copyDstCmd)
		self.excecuteQuery(dstInsertQuery)
		self.commitTransaction()

	def closeConnection(self):
		self.dstCursor.close()
		self.dstConn.close()